from django.db import models

# Create your models here.
class Poroda(models.Model):
    vid = models.CharField(max_length=20, verbose_name='Вид')
    poroda = models.CharField(max_length=20, verbose_name='Порода')

    def __str__(self):
        return self.vid

class Disease(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    VIBOR = (('начальная','начальная'),('разгар','разгар'),('исход','исход'),('хроническая','хроническая'))
    stage = models.CharField(max_length=20,choices=VIBOR, verbose_name='Стадия')

    def __str__(self):
        return self.name

class Medicine(models.Model):
    name = models.CharField(max_length=20, verbose_name='Название')
    dosa = models.IntegerField(verbose_name='Дозировка')
    period = models.IntegerField(verbose_name='Срок приёма')

    def __str__(self):
        return self.name

class Klient(models.Model):
    name = models.CharField(max_length=20, verbose_name='Кличка')
    age = models.IntegerField(verbose_name='Возраст')
    poroda = models.ForeignKey(Poroda, on_delete=models.SET_DEFAULT, default=1, verbose_name='Порода')
    disease = models.ForeignKey(Disease, on_delete=models.SET_DEFAULT, default=1, verbose_name='Заболевание')
    medicine = models.ManyToManyField(Medicine, verbose_name='Лекарство')

    def __str__(self):
        return self.name