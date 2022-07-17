from django.contrib import admin
from api.models import Movies, Director
# Register your models here.


class MoviesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'year')
    list_display_links = ('id', 'title', 'year')


class DirectorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname')
    list_display_links = ('name', 'surname')


admin.site.register(Movies, MoviesAdmin)
admin.site.register(Director, DirectorAdmin)
