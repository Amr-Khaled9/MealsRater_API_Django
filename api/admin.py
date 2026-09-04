from django.contrib import admin

from api.models import Meal, Rating

# Register your models here.

class RatingAdmin(admin.ModelAdmin):
    list_display = ('meal', 'user', 'stars', 'comment', 'created_at', 'updated_at')
    list_filter = ('meal', 'user', 'stars')
    search_fields = ('meal__name', 'user__username', 'comment')

class MealAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at', "name" , 'description')
    search_fields = ('name', 'description')

admin.site.register(Meal, MealAdmin)
admin.site.register(Rating, RatingAdmin)