
from django.contrib import admin
from django.urls import path

from Tutor import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page (login)
    path('about/', views.about, name='about'),  # About page
    path('contact/', views.contact, name='contact'),  # Contact page
    path('details/', views.details, name='details'),  # Course details page
    path('courses/', views.courses, name='courses'),  # Courses page
    path('events/', views.events, name='events'),  # Events page
    path('trainers/', views.trainers, name='trainers'),  # Trainers page
    path('starter/', views.starter, name='starter'),  # Starter page
    path('checkout/', views.checkout, name='checkout'),  # Checkout page
    path('display/', views.view, name='display'),  # Display all checkouts
    path('delete/<int:id>/', views.delete, name='delete_checkout'),  # Delete checkout by ID
    path('edit/<int:id>/', views.edit, name='edit_checkout'),  # Edit checkout by ID
    path('update/<int:id>/', views.update, name='update_checkout'),  # Update checkout by ID
    path('register/', views.register, name='register'),  # Register new member
    path('login/', views.login, name='login'),
    path('uploadimage/', views.upload_image, name='upload'),
    path('showimage/', views.show_image, name='image'),
    path('imagedelete/<int:id>', views.imagedelete),
    path('view-event/<int:event_id>/', views.view_event, name='view_event'),

]
