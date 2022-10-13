from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    #API цвета
    path("color_list/", views.Color_list.as_view()),
    path("color_detail/<int:pk>/", views.Color_detail.as_view()),
    #API брендов
    path("brand_list/", views.Brand_list.as_view()),
    path("brand_detail/<int:pk>/", views.Brand_detail.as_view()),
    #API модели
    path("model_list/", views.Model_list.as_view()),
    path("model_detail/<int:pk>/", views.Model_detail.as_view()),
    #API заказы
    path("order_list/", views.Order_list.as_view()),
    path("order_detail/<int:pk>/", views.Order_detail.as_view()),
    
    #Доп задание
    # 1) Пагинация/сортировка/фильтрация заказов
    path("order_list_mod/", views.Order_list_modified.as_view()),
    # 2) цвета и кол-во заказаных машин
    path("color_amount/", views.Color_amount.as_view()),
    path("brand_amount/", views.Brand_amount.as_view()),
]