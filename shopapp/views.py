import datetime
from dateutil import parser
from rest_framework import status
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination
from .serializer import (Color_serializer,Brand_serializer,
                         Model_serializer, Order_serializer,Model_order_serializer)
from .models import (Car_color, Car_brand, Car_model, Order)
from .utils import (get_object,data_validator)


def index(request):
    return HttpResponse("index page")


class Color_list(APIView):
    """
    API для вывода ВСЕХ цветов, и создание нового ЦВЕТА (GET/POST).
    """
    permission_classes = [AllowAny]
    def get(self, request): 
        serializer = Color_serializer(Car_color.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Color_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Color_detail(APIView):
    """
    API для GET/PUT/DELETE конкретного ЦВЕТА.
    """
    def get(self, request, pk, format=None):
        serializer = Color_serializer(get_object(Car_color,pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = Color_serializer(get_object(Car_color,pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        get_object(Car_color,pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Brand_list(APIView):
    """
    API для вывода ВСЕХ брендов, и создание нового БРЕНДА (GET/POST).
    """
    permission_classes = [AllowAny]
    def get(self, request): 
        serializer = Brand_serializer(Car_brand.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Brand_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Brand_detail(APIView):
    """
    API для GET/PUT/DELETE конкретного БРЕНДА.
    """
    def get(self, request, pk, format=None):
        serializer = Brand_serializer(get_object(Car_brand,pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = Brand_serializer(get_object(Car_brand,pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        get_object(Car_brand,pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Model_list(APIView):
    """
    API для вывода ВСЕХ брендов, и создание новой модели машины (GET/POST).
    """
    permission_classes = [AllowAny]
    def get(self, request): 
        serializer = Model_serializer(Car_model.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = Model_order_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Model_detail(APIView):
    """
    API для GET/PUT/DELETE конкретного БРЕНДА машины.
    """
    def get(self, request, pk, format=None):
        serializer = Model_serializer(get_object(Car_model,pk))
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        serializer = Model_order_serializer(get_object(Car_model,pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        get_object(Car_model,pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class Order_list(APIView):
    """
    API для вывода ВСЕХ брендов, и создание новой БРЕНДА машины (GET/POST).
    """
    permission_classes = [AllowAny]
    def get(self, request): 
        serializer = Order_serializer(Order.objects.all(), many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        target_data = {"amount":int, 
                       "ordered_model":int, 
                       "ordered_color":int
        }
        #валидация данных
        validation = data_validator(request,target_data)
        if not validation["is_valid"]:
            return Response(validation["error_fields"])
        validated_data = validation["parsed_data"]
        
        #получение данных
        amount = validated_data["amount"]
        ordered_model = Car_model.objects.filter(pk=validated_data["ordered_model"]).first()
        if not ordered_model: 
            return Response("указаный order_model не найден")
        ordered_color = Car_color.objects.filter(pk=validated_data["ordered_color"]).first()
        if not ordered_color: 
            return Response("указаный ordered_color не найден")

        #валидация/получение времени (формат "2022-10-11 22:42:17")
        try:
            created = parser.parse(request.POST.get("created"))
        except:
            created = datetime.datetime.now()
        
        ordered_brand = ordered_model.brand
        new_order = Order(amount=amount, ordered_brand=ordered_brand, ordered_model=ordered_model,
                          ordered_color=ordered_color,created=created)
        new_order.save()
        serializer = Order_serializer(new_order)
        return Response(serializer.data)


class Order_detail(APIView):
    """
    API для GET/PUT/DELETE конкретного БРЕНДА машины.
    """
    def get(self, request, pk, format=None):
        serializer = Order_serializer(get_object(Order,pk))
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        get_object(Order,pk).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        updated = False
        order_obj = get_object(Order,pk)
        target_data = {"amount":int, 
                       "ordered_model":int, 
                       "ordered_color":int
        }
        #валидация данных
        validation = data_validator(request,target_data)
        parsed_data = validation["parsed_data"]
        message_error = ""
        if parsed_data:
            if parsed_data.get("amount"):
                order_obj.amount = int(parsed_data["amount"])
                updated=True

            if parsed_data.get("ordered_model"):
                try:
                    ordered_model_obj = Car_model.objects.get(pk = int(parsed_data["ordered_model"]))
                    order_obj.ordered_brand = ordered_model_obj.brand
                    order_obj.ordered_model = ordered_model_obj
                    updated=True
                except:
                    message_error += "ошибка в ordered_model; "
                    
            if parsed_data.get("ordered_color"):
                try:
                    order_obj.ordered_color =  Car_color.objects.get(pk = int(parsed_data["ordered_color"]))
                    updated=True
                except:
                    message_error += "ошибка в ordered_color; "
        
        if request.POST.get("created"):
            try:
                created = parser.parse(request.POST.get("created"))
                order_obj.created = created
                updated=True
            except:
                created = order_obj.created
                
        if updated:
            order_obj.save()
            serializer = Order_serializer(order_obj)
            result =  serializer.data
            result["info_updated"] = updated
            result["info_message_error"] = validation["error_fields"]
            result["info_not_found_objects"] = message_error
            return Response(result)
        else:
            return Response(f"'не заполнено поле: amount', 'не заполнено поле: ordered_model',\
'не заполнено поле: ordered_color', 'не заполнено поле: created (формат 2022-10-11 22:42:17)';  {message_error}")




class Order_list_modified(APIView,PageNumberPagination):
    """
    Доп.задание, API для вывода заказов с:
    1) Пагинация и вывод по 10 обьектов на странице.
    2) Сортировка заказов по количеству (amount).
    3) Фильтрация заказов по бренду (audi, bmw, lada).
    """
    permission_classes = [AllowAny]
    page_size = 10
    def get(self, request): 
        #сортировка по полю amount
        sort_amount = False
        if str(request.GET.get("sort")) == "amount":
            sort_amount = True
        # фильтрация по brand
        brand_filter = False
        if str(request.GET.get("filter_brand")):
            brand_filter = True
        # если и сортировка и фильтрация
        if sort_amount and brand_filter:
            try:
                brand_ob = Car_brand.objects.get(pk=int(request.GET.get("filter_brand")))
                queryset = Order.objects.filter(ordered_brand=brand_ob).order_by("-amount")
            except:
                queryset = Order.objects.all().order_by("-amount")
        #если сортировка, без фильтрации
        elif (sort_amount) and (not brand_filter):
            queryset = Order.objects.all().order_by("-amount")
        #если фильтрация по бренду, без сортировки
        elif (not sort_amount) and (brand_filter):
            try:
                brand_ob = Car_brand.objects.get(pk=int(request.GET.get("filter_brand")))
                queryset = Order.objects.filter(ordered_brand=brand_ob)
            except:
                queryset = Order.objects.all().order_by("-pk")
        #если ни сортировки, ни фильтрации
        else:
            queryset = Order.objects.all().order_by("-pk")
        results = self.paginate_queryset(queryset, request, view=self)
        serializer = Order_serializer(results, many=True)
        return self.get_paginated_response(serializer.data)


class Color_amount(APIView):
    """
    Список цветов с указанием количества заказанных авто 
    каждого цвета (атрибуты элементов: цвет, количество)
    """
    def get(self, request): 
        all_colors = Car_color.objects.all()
        result = []
        for color in all_colors:
            color_orders = len(Order.objects.filter(ordered_color = color))
            result.append({"color":color.title,"amount":color_orders})
        return Response(result)

class Brand_amount(APIView):
    """
    Список марок с указанием количества заказанных авто 
    каждой марки (атрибуты элементов: марка, количество).
    """
    def get(self, request): 
        all_brands = Car_brand.objects.all()
        result = []
        for brand in all_brands:
            brand_orders = len(Order.objects.filter(ordered_brand = brand))
            result.append({"brand":brand.title,"amount":brand_orders})
        return Response(result)
