from django.contrib import admin
from .models import UploadFormModel

class UploadFromAdmin(admin.ModelAdmin):
    class Meta:
        model = UploadFormModel

admin.site.register(UploadFormModel, UploadFromAdmin)
    
