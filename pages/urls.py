from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import (add_to_cart, remove_from_cart,
                    inquiry_list_view, create_inquiry,
                    edit_inquiry, delete_inquiry, order_status)

app_name = 'pages'
urlpatterns = [
    path('', views.mainpage, name="mainpage"),
    path('login/', auth_views.LoginView.as_view(template_name='pages/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup, name='signup'),
    path('mypage/', views.mypage_view, name='mypage'),
    path('products/', views.products_view, name='products'),
    path('order/', views.order_view, name='order'),
    path('cart/', views.cart_view, name='cart'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('remove_from_cart/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('add_product/', views.add_product_view, name='add_product'),  # 상품 추가 URL
    path('inquiry/', inquiry_list_view, name='inquiry_list'),  # 문의 목록
    path('inquiry/create/', create_inquiry, name='create_inquiry'),  # 문의 생성
    path('inquiry/edit/<int:inquiry_id>/', edit_inquiry, name='edit_inquiry'),  # 문의 수정
    path('inquiry/delete/<int:inquiry_id>/', delete_inquiry, name='delete_inquiry'),  # 문의 삭제
    path('order_status/', order_status, name='order_status'),

]