# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class RestaurantBlogReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    published_date = models.DateField(blank=True, null=True)
    blog_url = models.CharField(max_length=255, blank=True, null=True)
    restaurant = models.ForeignKey('Restaurants', models.DO_NOTHING, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.id}: {self.title}"
    
    class Meta:
        managed = False
        db_table = 'restaurant_blog_reviews'
        verbose_name = "레스토랑 블로그 리뷰"
        verbose_name_plural = "레스토랑 블로그 리뷰s"




class Restaurants(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    area_name = models.CharField(max_length=100, blank=True, null=True)
    kakao_place_id = models.CharField(max_length=100, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cuisine_type = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    tags = models.TextField(blank=True, null=True)
    menu = models.JSONField(blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    keyword = models.TextField(blank=True, null=True)
    rating_count = models.IntegerField(blank=True, null=True)
    business_hour = models.CharField(max_length=100, blank=True, null=True)
    latitude = models.CharField(max_length=20, blank=True, null=True)
    longitude = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.id}: {self.name}"
    
    class Meta:
        managed = False
        db_table = 'restaurants'
        verbose_name = "레스토랑"
        verbose_name_plural = "레스토랑s"
