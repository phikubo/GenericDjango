from django.urls import path

from . import views

app_name='appli'
urlpatterns = [
    path('', views.IndexView.as_view(),name='index'),
    path('<int:pk>/',views.DetallesView.as_view(),name='detalles'),
    path('<int:pk>/resultados/', views.ResultadosView.as_view(), name='resultados'),
    path('<int:id_pregunta>/votar/', views.votar, name='votar'),
]   