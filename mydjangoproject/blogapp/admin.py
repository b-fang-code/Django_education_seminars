from django.contrib import admin
from .models import Author


# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email', 'birthday')
    list_filter = ('name',)
    search_fields = ('name',)
    fields = ('name', 'surname', 'email', 'bio', 'birthday')
    readonly_fields = ('birthday',)


admin.site.register(Author, AuthorAdmin)
