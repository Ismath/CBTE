from django.urls import path
from django.contrib import admin
from . import views
from .views import CartItemViews, ProductProvider, ProductApi, ConsumptionApi, AnnouncemetAPI
from django.contrib.auth import views as auth_views
urlpatterns = [
    #path(r'^login/$', auth_views.login, {'template_name': 'login_page.html'}),
    #path('',views.hi, name='home-page' ),
    path('home', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    #path('login_page', views.login, name='login_page'),
    path('my_form', views.my_form, name='my_form'),
    path(r'api/t_user', views.t_userApi),
    path(r'api/t_user/update', CartItemViews.as_view()),
    path(r'api/t_user/update/<int:id>', CartItemViews.as_view()),

    path(r'api/productProvider', views.t_product_providerApi),
    path(r'api/productProvider', ProductProvider.as_view()),
    path(r'api/productProvider/<int:id>', ProductProvider.as_view()),
    
    path(r'api/products', views.t_productsApi),
    path(r'api/productProvider', ProductApi.as_view()),
    path(r'api/productProvider/<int:id>', ProductApi.as_view()),

    path(r'api/products', views.t_consumptionsApi),
    path(r'api/productProvider', ConsumptionApi.as_view()),
    path(r'api/productProvider/<int:id>', ConsumptionApi.as_view()),

    path(r'api/announcements', views.t_announcementsApi),
    path(r'api/announcements', AnnouncemetAPI.as_view()),
    path(r'api/announcements/<int:id>', AnnouncemetAPI.as_view()),

    path('', views.users, name='users'),
    path('signup', views.my_form, name='signup'),
    #path('',views.login_page, name = 'signup')







]