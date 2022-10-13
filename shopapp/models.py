from django.db import models
import django

class Time_Stamped_Mixin(models.Model):
    """
    Абстрактный класс для присваивания к моделям двух полей с датами
    """
    created = models.DateTimeField('обьект создан', auto_now_add=True)
    modified = models.DateTimeField('обьект изменен', auto_now=True)
    class Meta:
        abstract = True


class Car_brand(Time_Stamped_Mixin):
    """
    Бренд автомобиля (audi, bmw, lada).
    """
    title = models.CharField("Название бренда",max_length = 150)

    def __str__(self):
        return self.title


class Car_model(Time_Stamped_Mixin):
    """
    Марка(модель) автомобиля (TT, a6, q7, kalina).
    """
    brand = models.ForeignKey(Car_brand, verbose_name="Бренд модели", on_delete=models.CASCADE)
    title = models.CharField("Название модели",max_length = 150)

    def __str__(self):
        return self.title


class Car_color(Time_Stamped_Mixin):
    """
    Цвет машины (зеленый, фиолетовый).
    """
    title = models.CharField("Название цвета",max_length = 50)

    def __str__(self):
        return self.title


class Order(models.Model):
    """
    Сфрормированый заказа пользователя.
    """
    amount = models.IntegerField()
    ordered_brand = models.ForeignKey(Car_brand, verbose_name='Бренд машины', on_delete=models.SET_NULL, null=True)
    ordered_model = models.ForeignKey(Car_model, verbose_name='Модель машины', on_delete=models.SET_NULL,blank=False, null=True)
    ordered_color = models.ForeignKey(Car_color, verbose_name='Выбранный цвет', on_delete=models.SET_NULL,blank=False, null=True)
    created = models.DateTimeField('заказ создан', default=django.utils.timezone.now)
    modified = models.DateTimeField('заказ изменен', auto_now=True)
    