from django.contrib import admin
from .models import About
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
@admin.register(About)
class AboutAdmin(SummernoteModelAdmin): # instead of using django admin.ModelAdmin

    summernote_fields = ('content',) # tells AboutAdmin which fields will be summernote_fields
