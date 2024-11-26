from .models import Car, Driver, Owner, Contacts
from django.forms import ModelForm, TextInput, DateInput
from django import forms
from .models import Cars


class CarsForm(forms.Form):
    class Meta:
        model = Cars
        fields = ['ID_MARK', 'firmAuto', 'modelAuto']

    ID_MARK = forms.ModelChoiceField(
        queryset=Cars.objects.values('ID_MARK').distinct(),
        label='ID',
        empty_label="Выберите ID",
        to_field_name='ID',
        widget=forms.Select(attrs={'class': 'carIn'})
    )

    firmAuto = forms.ModelChoiceField(
        queryset=Cars.objects.values('Марка').distinct(),
        label='Марка',
        empty_label="Выберите марку",
        to_field_name='Марка',
        widget=forms.Select(attrs={'class': 'carIn'})
    )

    modelAuto = forms.ModelChoiceField(
        queryset=Cars.objects.values('Модель').distinct(),  # Сначала пустой список моделей
        label='Модель',
        empty_label="Выберите модель",
        to_field_name='Модель',
        widget = forms.Select(attrs={'class': 'carIn'})
    )

class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['numberAuto', 'firmAuto', 'modelAuto', 'dateCreate',
                  'powerEngine', 'seriesNumberSTS', 'dateGiveDoc', 'numberVIN']

        widgets = {
            "numberAuto": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'A 000 AA 00',
                'id': 'numberAuto'
            }),
            "firmAuto": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Марка'
            }),
            "modelAuto": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Модель'
            }),
            "dateCreate": forms.Select(attrs={
                'class': 'carIn',
                'type': 'text',
                'placeholder': 'Год выпуска',
                'maxlength': 4
            }),
            "powerEngine": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Мощность двигателя'
            }),
            "seriesNumberSTS": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Серия и номер CТС'
            }),
            "dateGiveDoc": DateInput(attrs={
                'class': 'carIn datepicker',
                'placeholder': 'Дата выдачи документа',
                'maxlength': 10
            }),
            "numberVIN": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'VIN номер'
            }),
        }

    def __init__(self, *args, **kwargs):
        super(CarForm, self).__init__(*args, **kwargs)
        YEAR_CHOICES = [(str(year), str(year)) for year in range(2024, 1971, -1)]
        YEAR_CHOICES.insert(0, ('', 'Год выпуска'))
        self.fields['dateCreate'] = forms.ChoiceField(choices=YEAR_CHOICES, widget=forms.Select(attrs={'class': 'carIn'}))

class DriverForm(ModelForm):
    class Meta:
        model = Driver
        fields = ['fioDriver', 'bithDateDriver', 'seriesNumberLicence', 'dateOfStartDrive']

        widgets = {
            "fioDriver": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'ФИО'
            }),
            "bithDateDriver": DateInput(attrs={
                'class': 'carIn datepicker',
                'placeholder': 'Дата рождения',
                'maxlength': 10
            }),
            "seriesNumberLicence": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Серия и номер прав'
            }),
            "dateOfStartDrive": DateInput(attrs={
                'class': 'carIn datepicker',
                'placeholder': 'Дата начала стажа категории B',
                'maxlength': 10
            }),
        }

class OwnerForm(ModelForm):
    class Meta:
        model = Owner
        fields = ['fioOwner', 'bithDateOwner', 'seriesNumberPassport', 'dateGivePassport', 'adreesReg',
                  'numberAppart', 'fioCearAuto']

        widgets = {
            "fioOwner": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'ФИО'
            }),
            "bithDateOwner": DateInput(attrs={
                'class': 'carIn datepicker',
                'placeholder': 'Дата рождения',
                'maxlength': 10
            }),
            "seriesNumberPassport": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Серия и номер паспорта'
            }),
            "dateGivePassport": DateInput(attrs={
                'class': 'carIn datepicker',
                'placeholder': 'Дата выдачи паспорта',
                'maxlength': 10

            }),
            "adreesReg": TextInput(attrs={
                'class': 'carIn',
                'id': 'address-input',
                'placeholder': 'Адрес регистрации'
            }),
            "numberAppart": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Номер квартиры'
            }),
            "fioCearAuto": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Кто страхует транспортное средство?'
            })
        }

class ContactsForm(ModelForm):
    class Meta:
        model = Contacts
        fields = ['email', 'numberPhone']

        widgets = {
            "email": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Email'
            }),
            "numberPhone": TextInput(attrs={
                'class': 'carIn',
                'placeholder': 'Номер телефона'
            })
        }