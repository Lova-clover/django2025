from django.contrib import admin
from .models import Inquiry, Order

admin.site.register(Inquiry)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', 'quantity', 'total_price', 'order_date', 'status')  # 표시할 필드
    list_filter = ('status',)  # 필터링 옵션
    search_fields = ('product',)  # 검색 옵션

admin.site.register(Order, OrderAdmin)  # Order 모델 등록