from rest_framework import serializers
from .models import (Car_color, Car_brand, Car_model, Order)

class Color_serializer(serializers.ModelSerializer):
    """
    Сериалайзер для цветов
    """
    class Meta:
        model = Car_color
        exclude = ["created", "modified"]


class Brand_serializer(serializers.ModelSerializer):
    """
    Сериалайзер для брендов с моделями
    """
    models_of_brand = serializers.SerializerMethodField()
    class Meta:
        model = Car_brand
        exclude = ["created", "modified"]
    
    def get_models_of_brand(self, obj):
        models = Car_model.objects.filter(brand=obj.pk)
        models_list = [({"title":i.title, "pk": i.pk}) for i in models]
        return models_list
        

class Brand_model_serializer(serializers.ModelSerializer):
    """
    доп сериалайзер для брендов с моделями используется как дополнительное поле
    """
    class Meta:
        model = Car_brand
        exclude = ["created", "modified"]


class Model_serializer(serializers.ModelSerializer):
    """
    Сериалайзер для Моделей машинн
    """
    brand = Brand_model_serializer()
    class Meta:
        model = Car_model
        exclude = ["created", "modified"]

class Model_order_serializer(serializers.ModelSerializer):
    """
    доп Сериалайзер для Моделей машинн ДЛЯ ЗАКАЗА
    """
    class Meta:
        model = Car_model
        exclude = ["created", "modified"]


class Order_serializer(serializers.ModelSerializer):
    """
    Сериалайзер для ЗАКАЗОВ
    """
    ordered_brand = Brand_model_serializer()
    ordered_model = Model_order_serializer()
    ordered_color = Color_serializer()
    class Meta:
        model = Order
        fields = ["pk","amount", "ordered_brand","ordered_model","ordered_color", "created"]
