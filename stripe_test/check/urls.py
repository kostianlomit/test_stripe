from django.urls import path

from .views import *

urlpatterns = [
    path('buy/<int:id>/', get_checkout_session_id),
    path('item/<int:id>/', get_item, name='checkout'),
]