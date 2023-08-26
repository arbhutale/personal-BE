from django.urls import re_path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from api.bank_account.views import BankAccountViewSet
from api.credit_card.views import CreditCardViewSet
router = DefaultRouter()
router.register(r'bank-accounts', BankAccountViewSet)
router.register(r'credit-cards', CreditCardViewSet)

urlpatterns = [
    re_path(r'^authenticate/$', obtain_auth_token),
    path('', include(router.urls)),
]