from django import forms
from django.utils import timezone
import datetime


class SearchTeamForm(forms.Form):
    team_name = forms.CharField(
        label='Название команды',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'placeholder': 'Введите название команды...',
            'class': 'form-control'
        })
    )

    start_date = forms.DateTimeField(
        label='Начальная дата',
        required=True,
        input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        })
    )

    end_date = forms.DateTimeField(
        label='Конечная дата',
        required=True,
        input_formats=['%Y-%m-%dT%H:%M', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d'],
        widget=forms.DateTimeInput(attrs={
            'type': 'datetime-local',
            'class': 'form-control'
        })
    )

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if start_date > end_date:
                raise forms.ValidationError(
                    "Начальная дата не может быть позже конечной"
                )

            if end_date > timezone.now():
                raise forms.ValidationError(
                    "Конечная дата не может быть в будущем"
                )

        return cleaned_data

    def get_default_start_date(self):
        return timezone.now() - datetime.timedelta(days=7)

    def get_default_end_date(self):
        return timezone.now()


class ContestSearchForm(forms.Form):
    team_slug = forms.CharField(
        label='Название команды',
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control form-control-lg',
            'placeholder': 'Введите название команды',
            'id': 'team_slug'
        })
    )
