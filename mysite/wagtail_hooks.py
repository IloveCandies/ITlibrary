from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register 

from .models import UploadFileModel


class DocumentAdmin(ModelAdmin):
    model = UploadFileModel 
    menu_label = "Предложенное"  
    add_to_settings_menu = False 
    exclude_from_explorer = False 
    list_display = ('description','file')
    search_fields = ('description',)


modeladmin_register(DocumentAdmin)