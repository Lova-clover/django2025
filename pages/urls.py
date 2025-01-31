from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import add_to_cart, remove_from_cart

app_name = 'pages'
urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('help/', views.help_view, name='help'),
    path('products/', views.products_view, name='products'),
    path('order/', views.order_view, name='order'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),




]