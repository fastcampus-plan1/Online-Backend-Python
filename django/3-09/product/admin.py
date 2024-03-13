import csv

from django import forms
from django.contrib import admin
from django.http import HttpResponse, QueryDict
from django.urls import path, reverse
from django.shortcuts import render, redirect

from .models import Product


def export_as_csv(queryset, fields):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=export.csv"
    writer = csv.writer(response, quoting=csv.QUOTE_MINIMAL)
    response.write(",".join(fields) + "\n")
    for obj in queryset:
        row = [str(getattr(obj, field)) for field in fields]
        writer.writerow(row)
    return response


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "price", "created_at", "updated_at"]
    fields = ["name", "price", "description", "tags"]
    search_fields = ["name"]
    actions = ["select_exported_fields"]

    def get_urls(self):
        urls = super().get_urls()
        urls = [
            path(
                "select-exported-fields/",
                self.select_exported_fields,
                name="select_exported_fields",
            ),
        ] + urls
        return urls

    @admin.action(description="선택된 상품을 CSV로 내보내기")
    def select_exported_fields(self, request, queryset=None):
        class SelectExportedFieldsForm(forms.Form):
            fields = forms.MultipleChoiceField(
                choices=[
                    (field.name, field.verbose_name) for field in Product._meta.fields
                ]
            )

        if queryset:
            selected = queryset.values_list("id", flat=True)
            params = QueryDict(mutable=True)
            params.setlist("id", selected)
            return redirect(
                f"{reverse('admin:select_exported_fields')}?{params.urlencode()}"
            )
        else:
            queryset = Product.objects.filter(id__in=request.GET.getlist("id"))
            form = SelectExportedFieldsForm(request.POST or None)
            if request.method == "POST" and form.is_valid():
                fields = form.cleaned_data["fields"]
                return export_as_csv(queryset, fields)
            else:
                return render(
                    request,
                    "admin/select_exported_fields.html",
                    {
                        "opts": self.model._meta,
                        "form": form,
                        "has_permission": request.user.has_perm("product.view_product"),
                    },
                )
