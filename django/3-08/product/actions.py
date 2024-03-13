import csv

from django.contrib import admin
from django.http import HttpResponse


@admin.action(description="선택된 상품을 CSV로 내보내기")
def export_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = "attachment; filename=export.csv"
    writer = csv.writer(response, quoting=csv.QUOTE_MINIMAL)
    model = queryset.model
    field_names = [field.name for field in model._meta.fields]
    response.write(",".join(field_names) + "\n")
    for obj in queryset:
        row = [str(getattr(obj, field)) for field in field_names]
        writer.writerow(row)
    return response
