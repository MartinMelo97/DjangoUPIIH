from django import forms
from .models import Tool

class ToolForm(forms.ModelForm):
    name = forms.CharField(label='Nombre', required=True)
    serial_number = forms.CharField(label='Número de serie', required=True)
    model = forms.CharField(label='Modelo', required=True)
    has_been_in_mainteance = forms.BooleanField(label='¿Ha tenido mantenimiento?', required=False)
    mainteance_date = forms.DateField(
        label='Fecha de mantenimiento',
        widget=forms.SelectDateWidget(years=range(2010, 2022))
    )
    is_in_maintain = forms.BooleanField(label='¿Está en mantenimiento?', required=False)
    specifications = forms.CharField(label='Características', widget=forms.Textarea, required=False)
    has_tracker = forms.BooleanField(label='¿Cuenta con rastreador?', required=False)
    tracker_id = forms.CharField(label='Id del rastreador', required=False)
    class Meta:
        model = Tool
        fields = ('name', 'serial_number', 'model', 'has_been_in_mainteance',
            'mainteance_date', 'is_in_maintain', 'specifications',
            'has_tracker', 'tracker_id'
        )