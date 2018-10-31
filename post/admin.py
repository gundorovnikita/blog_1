from django.contrib import admin
from .models import *
from django_summernote.admin import SummernoteModelAdmin
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
        summernote_fields = '__all__'
# Register your models here.
admin.site.register(GdsModel, SomeModelAdmin)
admin.site.register(Category)
