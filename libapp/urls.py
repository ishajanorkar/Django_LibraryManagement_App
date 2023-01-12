from django.contrib import admin #By Default
from django.urls import path
from libapp import views

urlpatterns = [
    path('index',views.index),

    path('',views.index, name="index_page"),

    path('about',views.about, name="about_page"),

    path('borrow',views.borrow, name="borrow_page"),

    path('udash',views.udash, name="udash_page"),

    path('singUp',views.user_singUp, name="singUp_page"),

    path('Login',views.user_Login, name="Login_page"),

    path('edit/<rid>',views.edit),

    path('delete/<rid>',views.delete),

    path('catfilter/<catopt>',views.catfilter),

    path('authfilter/<authopt>',views.authfilter),

    path('djangoform',views.djangoform),

    path ('logout',views.user_logout, name='logout_page'),
]