from django import forms
from .models import CycleTracker, ActionPlanner, Reminder, Preparation, Interview

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
        
class ReminderForm(forms.ModelForm):
    date= forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            ), required=False
        )
    def __init__(self, *args, **kwargs):
        super(ReminderForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'narrow-select'
    class Meta:
        model = Reminder
        fields = '__all__'
        
class PreparationForm(forms.ModelForm):
    date= forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            ), required=False
        )
    def __init__(self, *args, **kwargs):
        super(PreparationForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'narrow-select'
    class Meta:
        model = Preparation
        fields = '__all__'
        
class InterviewForm(forms.ModelForm):
    date= forms.DateField(
            widget=forms.TextInput(
                attrs={'type': 'date'}
            ), required=False
        )
    def __init__(self, *args, **kwargs):
        super(InterviewForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'narrow-select'
    class Meta:
        model = Interview
        fields = '__all__'