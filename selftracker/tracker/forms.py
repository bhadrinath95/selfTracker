from django import forms
from .models import CycleTracker, ActionPlanner

class GenerateCycleForm(forms.ModelForm):
    date= forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            ), required=False
        )
    def __init__(self, *args, **kwargs):
        super(GenerateCycleForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'narrow-select'
    class Meta:
        model = CycleTracker
        fields = '__all__'
        
class ActionPlannerForm(forms.ModelForm):
    date= forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            ), required=False
        )
    def __init__(self, *args, **kwargs):
        super(ActionPlannerForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'narrow-select'
    class Meta:
        model = ActionPlanner
        fields = '__all__'