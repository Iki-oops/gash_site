from django.contrib import admin

from .models import Tag, Course, CourseTag

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'hex_color',)
    search_fields = ('name', 'hex_color',)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'description', 'created_at', 'updated_at')
    search_fields = ('name', 'description')
    empty_value_display = '--пусто--'


@admin.register(CourseTag)
class CourseTagAdmin(admin.ModelAdmin):
    list_display = ('pk', 'tag', 'course',)
    search_fields = ('tag', 'course',)
