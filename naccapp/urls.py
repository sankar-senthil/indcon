from django.urls import path
from . import views 
urlpatterns = [
    path('',views.dashboard, name='dash-board'),
    path('result-page',views.result_page, name='result-page'),
]