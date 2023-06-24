from django.urls import path

from orders.views import (CancelTemplateView, OrderCreateView, OrderDetailView,
                          OrderListView, SuccessTemplateView)

app_name = 'orders'

urlpatterns = [
    path('order-create/', OrderCreateView.as_view(), name='order-create'),
    path('order-success/', SuccessTemplateView.as_view(), name='order_success'),
    path('order-canceled/', CancelTemplateView.as_view(), name='order_canceled'),
    path('', OrderListView.as_view(), name='orders_list'),  # .../orders/
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order'),
]
