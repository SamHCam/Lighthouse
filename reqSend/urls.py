from django.urls import path

from . import views

app_name = 'reqSend'
urlpatterns = [
    
    path('', views.IndexView.as_view(), name='IndexView'),
    path('<int:pk>/', views.DetailView.as_view(), name='DetailView'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='ResultsView'),
    path('<int:question_id>/amount/', views.amount, name='amount'),
]