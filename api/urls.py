from django.urls import path
from .views import UserView, UserLanguageView, OrderView
urlpatterns = [
    path('user-data', UserView.as_view(), name='user'),
    path('user-language', UserLanguageView.as_view(), name='user-language'),
    path('order', OrderView.as_view(), name='order'),
]
