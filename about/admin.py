from django.contrib import admin
from .models import About, CollaborateRequest
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
@admin.register(About)
# instead of using django admin.ModelAdmin
class AboutAdmin(SummernoteModelAdmin):
    """
    This class is used to customise the admin panel view for the About model.
    """
    # tells AboutAdmin which fields will be summernote_fields
    summernote_fields = ('content',)
# Note: admin.ModelAdmin is the standard way of registering
#       our model with the admin panel. We do it differently
#       above because we are supplying Summernote fields.
#       If you want to customise the admin panel view in your
#       own projects, then inherit from admin.ModelAdmin like
#       we do below.


@admin.register(CollaborateRequest)
class CollaborateRequestAdmin(admin.ModelAdmin):
    """
    This class is used to customise the admin panel view for the CollaborateRequest model.
    """

    list_display = ('message', 'read',)
