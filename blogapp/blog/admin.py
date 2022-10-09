from django.contrib import admin
from .models import Blog ,Catagory
from django.utils.safestring import mark_safe
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("title","is_active","is_home","selected_catagories",)
    list_editable = ("is_active","is_home",)
    search_fields = ("title","description",)
    readonly_fields = ("slug",)
    list_filter = ("catagories",)
    
    def selected_catagories(self,obj):
        html = "<ul>"
        for catagory in obj.catagories.all():
            
            html += "<li>" +  catagory.name + "</li> "
        
        html += "</ul>"
        return mark_safe(html)
        
admin.site.register(Blog,BlogAdmin)

admin.site.register(Catagory)