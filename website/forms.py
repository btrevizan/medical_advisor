import datetime
from django import forms
from .models import Doctor, Patient


class AppointmentForm(forms.Form):
    doctor = forms.IntegerField()       # doctor_id
    patient = forms.IntegerField()      # patient_id
    datetime = forms.DateTimeField()

    def clean(self):
        cleaned_data = super().clean()
        doctor_id = cleaned_data.get('doctor')
        patient_id = cleaned_data.get('patient')

        if not Doctor.objects.filter(pk=doctor_id).exists():
            self.add_error['doctor'] = 'Médico não existe.'

        if not Patient.objects.filter(pk=patient_id).exists():
            self.add_error['patient'] = 'Paciente não existe.'


class SearchDoctorForm(forms.Form):
    DEFAULT_ATTRS = {'class': 'form-control form-control-lg'}
    DATE_FORMAT = '%d/%m/%y %H:%M'

    DEFAULT_ATTRS.update({'placeholder': 'Especialidade'})
    speciality = forms.CharField(max_length=25,
                                 widget=forms.TextInput(attrs=DEFAULT_ATTRS))

    DEFAULT_ATTRS.update({'placeholder': 'De'})
    startdt = forms.DateTimeField(initial=datetime.datetime.now().strftime(DATE_FORMAT),
                                  input_formats=[DATE_FORMAT],
                                  widget=forms.TextInput(attrs=DEFAULT_ATTRS))

    DEFAULT_ATTRS.update({'placeholder': 'Até'})
    enddt = forms.DateTimeField(initial=datetime.datetime.now().strftime(DATE_FORMAT),
                                input_formats=[DATE_FORMAT],
                                widget=forms.TextInput(attrs=DEFAULT_ATTRS))

    DEFAULT_ATTRS.update({'placeholder': 'Cidade'})
    city = forms.CharField(max_length=40,
                           widget=forms.TextInput(attrs=DEFAULT_ATTRS))

    DEFAULT_ATTRS.update({'placeholder': 'Bairro'})
    neighborhood = forms.CharField(max_length=40,
                                   required=False,
                                   widget=forms.TextInput(attrs=DEFAULT_ATTRS))
