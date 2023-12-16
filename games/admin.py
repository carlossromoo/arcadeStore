from django.contrib import admin

from .models import Games,Review

class ReviewInLine(admin.TabularInline):
    model = Review

class GamesAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInLine,
    ]
    list_display = ('title','author','price',)

admin.site.register(Games, GamesAdmin)
# Register your models here.
