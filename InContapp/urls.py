from django.urls import path
from .views import Incont


urlpatterns = [
    path('',Incont.indecont, name='indeconthome'),
]