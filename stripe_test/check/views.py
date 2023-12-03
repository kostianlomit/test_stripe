import os

from django.http import JsonResponse
from django.shortcuts import render, redirect
import stripe

from .models import Item
from ..stripe_test.settings import SECRET_KEY_API


def get_checkout_session_id(request, id):
    # Получение выбранного товара по id
    item = Item.objects.get(id=id)
    stripe.api_key = SECRET_KEY_API
    # Создание сеанса checkout с помощью Stripe
    session = stripe.checkout.Session.create(
        line_items=[{
            'price_data': {
                "currency": "rub",
                'product_data': {"name": item.name},
                'unit_amount': item.price,
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url='http://localhost:8000/success',
        cancel_url='http://localhost:8000/cancel',
    )

    return JsonResponse({'session_id': session.id})


# Получение информации о выбранном Item по его id
def get_item(request, id):
    item = Item.objects.get(id=id)
    context = {
        'item': item,
    }
    return render(request, 'checkout.html', context)

