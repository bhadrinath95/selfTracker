from django import forms
from .models import CycleTracker

class GenerateCycleForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(GenerateCycleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'narrow-select'
    class Meta:
        model = CycleTracker
        fields = '__all__'