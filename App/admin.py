from django.contrib import admin
from .models import Users, Notes
# Register your models here.
@admin.register(Users)
class UserModelAdmin(admin.ModelAdmin):
    list_display=['id','name','email']


@admin.register(Notes)
class NotesAdmin(admin.ModelAdmin):
    list_display=['id','title','description','time','date']
