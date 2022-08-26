from django.forms import ModelForm, ClearableFileInput
from .models import Archivos
class CustomClearableFieldInput(ClearableFileInput):
    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class FormArchivos(ModelForm):
    class Meta:
        model = Archivos
        fields = ('nombre', 'archivo', 'comentario', 'archivoExp')
        widgets = {
            'archivo': CustomClearableFieldInput
        }