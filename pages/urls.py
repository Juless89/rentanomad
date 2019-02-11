from django.urls import path, include
from .views import *

urlpatterns = [
    path('', WordpressPageView.as_view()),
    path('django/', DjangoPageView.as_view()),
]
