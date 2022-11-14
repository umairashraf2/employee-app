from app import views
from django.urls import path

urlpatterns = [
    path('', views.Home, name="home"),
    path('add', views.Add, name="add"),
    path('edit', views.Edit, name="edit"),
    path('update/<str:id>', views.Update, name="update"),
    path('delete/<str:id>', views.Delete, name="delete"),
    path('search', views.Search, name="search"),
    path("login", views.loginUser, name='login'),
    path("logout", views.logoutUser, name='logout'),
]