from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True)
    address = models.CharField(max_length=255, blank=True)
    role = models.CharField(max_length=10, choices=[('USER', '유저'), ('FARMER', '농부')], default='USER')
    produce_info = models.TextField(blank=True)
    crop = models.TextField(blank=True)

    def __str__(self):
        return self.user.username

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(default="설명 없음")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    region = models.CharField(max_length=100, default='Unknown')

    def __str__(self):
        return self.name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.product.price * self.quantity

class Inquiry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 작성한 사용자
    name = models.CharField(max_length=100)  # 사용자의 이름
    email = models.EmailField()                # 사용자의 이메일
    message = models.TextField()               # 문의 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일자
    updated_at = models.DateTimeField(auto_now=True)      # 수정일자

    def __str__(self):
        return f'{self.name}의 문의'

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, default='주문 접수')

    def __str__(self):
        return f"{self.product} - {self.user.username} ({self.status})"



