from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from accounts.forms import SignupForm
from .models import Profile, Product, CartItem
from .forms import ProfileForm

def mainpage(request):
    return render(request, 'pages/mainpage.html')

def login_view(request):
    return render(request, 'pages/login.html')

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
    return render(request, 'pages/signup.html', {'form': form})

@login_required
def mypage_view(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()  # 폼 데이터 저장
            return redirect("pages:mypage")  # 수정 후 마이페이지로 리다이렉트
    else:
        form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'pages/mypage.html', context)

def help_view(request):
    return render(request, 'pages/help.html')

def products_view(request):
    products = Product.objects.all()
    return render(request, 'pages/products.html', {'products':products})

@login_required
def order_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)

    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        # 주문 처리 로직 추가 (예: 결제 처리)
        cart_items.delete()  # 주문 후 장바구니 비우기
        return redirect('pages:mainpage')  # 주문 완료 후 메인 페이지로 리다이렉트
    return render(request, 'pages/order.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'user_profile': user_profile,
    })

def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    return render(request, 'pages/cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1  # 수량 증가
        cart_item.save()
    return redirect('pages:products')  # 제품 목록으로 리다이렉트

@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()  # 장바구니에서 아이템 삭제
    return redirect('pages:cart')  # 장바구니 페이지로 리다이렉트

