from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductoListView.as_view(), name='producto_list'),
    path('producto/<int:pk>/', views.ProductoDetailView.as_view(), name='producto_detail'),
    path('nuevo/', views.ProductoCreateView.as_view(), name='producto_create'),
    path('producto/<int:pk>/editar/', views.ProductoUpdateView.as_view(), name='producto_update'),
    path('producto/<int:pk>/eliminar/', views.ProductoDeleteView.as_view(), name='producto_delete'),
]
