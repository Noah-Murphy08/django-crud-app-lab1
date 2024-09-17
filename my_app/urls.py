from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('pets/', views.pet_index, name='pet_index'),
    path('pets/<int:pet_id>/', views.pet_detail, name='pet_detail'),
    path('pets/create/', views.PetCreate.as_view(), name='pet_create'),
    path('pets/<int:pk>/update/', views.PetUpdate.as_view(), name='pet_update'),
    path('pets/<int:pk>/delete/', views.PetDelete.as_view(), name='pet_delete'),
    path('pets/<int:pet_id>/add-feeding/', views.add_feeding, name='add_feeding'),
    path('toys/create/', views.ToyCreate.as_view(), name='toy_create'),
    path('toys/<int:pk>/', views.ToyDetail.as_view(), name='toy_detail'),
    path('toys/', views.ToyList.as_view(), name='toy_index'),
    path('toys/<int:pk>/update/', views.ToyUpdate.as_view(), name='toy_update'),
    path('toys/<int:pk>/delete/', views.ToyDelete.as_view(), name='toy_delete'),
    path('pets/<int:pet_id>/associate-toy/<int:toy_id>/', views.associate_toy, name='associate_toy'),
    path('pets/<int:pet_id>/remove-toy/<int:toy_id>/', views.remove_toy, name='remove_toy'),
    path('accounts/signup/', views.signup, name='signup')
]
