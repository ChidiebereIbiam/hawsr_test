from django.urls import path
from . import views 

urlpatterns = [
    path('', views.health_check.as_view()),
    path('user/', views.UserAPI.as_view()),
    path('worker/', views.WorkerAPI.as_view()),
    path('company/', views.CompanyAPI.as_view()),
    path('building/', views.BuildingAPI.as_view()),
    path('office/', views.OfficeAPI.as_view()),
    path('user-office/', views.UserOfficeAPI.as_view())
]
