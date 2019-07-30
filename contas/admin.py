from django.contrib import admin
from contas import models

# Register your models here.
admin.site.register(models.Pessoa)
admin.site.register(models.Conta)

# # Register your models here.
# @admin.register(models.Person)
# class PersonAdmin(admin.ModelAdmin):
#     date_hierarchy = 'created_at'
#     list_display = ('first_name', 'last_name')
#     list_filter = (
#         ('created_at'),
#         ('active',  admin.BooleanFieldListFilter)
#     )
#     search_fields = ('first_name', 'last_name')

# # admin.site.register(models.Person)
# admin.site.register(models.Idea)
