from django.urls import path
from .import views

urlpatterns = [
    path('say_hello/',views.sample, name="say nothing"),
    path('members/',views.members, name = "members"),
    path('members/details/<int:id>',views.details, name="details"),
    path('home/',views.home_page, name='home page')
]