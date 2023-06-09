from django.urls import path,include
from .views import *

urlpatterns = []

from customer.views import *

urlpatterns += [

    path('log-in-customer',LoginCustomerView.as_view()),

]