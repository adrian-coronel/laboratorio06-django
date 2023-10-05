from django.urls import path
from . import views

urlpatterns = [
  path('productos', views.index, name='index'),
  path('productos/create', views.create, name='create'),
  path('productos/<int:id>/', views.show, name='show'),
  path('productos/create/store', views.store, name='store'),
  path('productos/<int:id>/edit', views.edit, name='edit'),
  path('productos/<int:id>/update', views.update, name='update'),
]