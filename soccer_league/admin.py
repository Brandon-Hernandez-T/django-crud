from django.contrib import admin
from .models import Category, Team, Player

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'age_range')

admin.site.register(Team)
admin.site.register(Player)