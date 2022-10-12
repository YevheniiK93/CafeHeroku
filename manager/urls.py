from django.urls import path
from .views import reservation_list, reservation_update

app_name = 'manager'

urlpatterns = [
    path('reservations/', reservation_list, name='reservation_list'),
    path('reservations/update/<int:pk>/', reservation_update, name='reservation_close'),

]
