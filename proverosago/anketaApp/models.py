from django.core.exceptions import ValidationError
from django.db import models


def validate_popular_mark(value):
    if value not in [0, 1]:
        raise ValidationError('Value must be 0 or 1.')
# Create your models here.
class Cars(models.Model):
    ID_MARK = models.TextField()
    Марка = models.TextField()
    Марка_кириллица = models.TextField()
    Популярная_марка = models.PositiveSmallIntegerField(validators=[validate_popular_mark])  # tinyint(1)
    Страна = models.TextField()
    MODEL_ID = models.TextField()
    Модель = models.TextField()
    Модель_кириллица = models.TextField()
    Класс = models.TextField()
    Год_от = models.BigIntegerField()  # bigint
    Год_до = models.FloatField()  # double

    class Meta:
        db_table = 'cars'  # Укажите имя существующей таблицы


class Car(models.Model):
    numberAuto = models.CharField('Номер автомобиля', max_length=12)
    firmAuto = models.CharField('Марка', max_length=50)
    modelAuto = models.CharField('Модель', max_length=50)
    dateCreate = models.CharField('Год выпуска', max_length=4)
    powerEngine = models.CharField('Мощность двигателя', max_length=50)
    seriesNumberSTS = models.CharField('Серия и номер СТС', max_length=10)
    dateGiveDoc = models.DateField('Дата выдачи документа')
    numberVIN = models.CharField('VIN номер', max_length=50)

    def __str__(self):
        return self.numberAuto

class Driver(models.Model):
    fioDriver = models.CharField('ФИО', max_length=50)
    bithDateDriver = models.DateField('Дата рождения')
    seriesNumberLicence = models.CharField('Серия и номер прав', max_length=50)
    dateOfStartDrive = models.DateField('Дата начала стажа категории B')

    def __str__(self):
        return self.fioDriver

class Owner(models.Model):
    fioOwner = models.CharField('ФИО', max_length=50)
    bithDateOwner = models.DateField('Дата рождения')
    seriesNumberPassport = models.CharField('Серия и номер паспорта', max_length=50)
    dateGivePassport = models.DateField('Дата выдачи паспорта')
    adreesReg = models.CharField('Адрес регистрации', max_length=100)
    numberAppart = models.CharField('Номер крвартиры', max_length=10)
    fioCearAuto = models.CharField('Кто страхует транспортное средство?', max_length=50)

    def __str__(self):
        return self.fioOwner

class Contacts(models.Model):
    email = models.CharField('Email', max_length=50)
    numberPhone = models.CharField('Номер телефона', max_length=50)

    def __str__(self):
        return self.numberPhone
