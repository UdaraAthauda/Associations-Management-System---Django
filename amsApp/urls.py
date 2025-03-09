from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=""),
    path('home', views.home, name="home"),
    path('register', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),

    # association details display url
    path('associationDetails/<int:pk>/', views.associationDetails, name="associationDetails"),

    # membership request url
    path('membershipRequest/<int:pk>/', views.membershipRequest, name="membershipRequest"),

    # membership display url
    path('memberships', views.memberships, name="memberships"),

    # accosiation servises display url
    path('services/<int:pk>/', views.services, name="services"),

    # association service request url
    path('serviceRequest/<int:pk>/', views.serviceRequest, name="serviceRequest"),
]
