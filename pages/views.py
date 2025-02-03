from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from accounts.forms import SignupForm
from .models import Profile, Product, CartItem, Inquiry, Order
from .forms import ProfileForm, ProductForm

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
            profile = form.save(commit=False)  # 폼 데이터 저장 (commit=False로 수정)
            profile.save()  # 프로필 정보 저장
            return redirect("pages:mypage")  # 수정 후 마이페이지로 리다이렉트
    else:
        form = ProfileForm(instance=profile)

    context = {
        'profile': profile,
        'form': form
    }
    return render(request, 'pages/mypage.html', context)

@login_required
def products_view(request):
    products = Product.objects.filter(quantity__gt=0)  # 기본적으로 재고가 있는 상품만 가져오기

    # 검색 조건 처리
    region = request.GET.get('region')  # 지역
    product_name = request.GET.get('product')  # 상품명

    if region:
        products = products.filter(region=region)  # 지역으로 필터링
    if product_name:
        products = products.filter(name__icontains=product_name)  # 상품명으로 필터링

    profile = Profile.objects.get(user=request.user)
    return render(request, 'pages/products.html', {
        'products': products,
        'profile': profile,
    })



@login_required
def order_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price() for item in cart_items)
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        for item in cart_items:
            # 주문 저장
            Order.objects.create(
                user=request.user,
                product=item.product.name,  # 제품 이름
                quantity=item.quantity,  # 주문 수량
                total_price=item.total_price(),  # 총 가격
                status='주문 접수'  # 기본 상태
            )

            # 재고 차감
            product = item.product
            product.quantity -= item.quantity
            product.save()

        cart_items.delete()  # 주문 후 장바구니 비우기
        messages.success(request, '주문이 완료되었습니다!')  # 성공 메시지 추가
        return redirect('pages:order_status')  # 주문 상태 페이지로 리다이렉트

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
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))  # 수량을 POST에서 가져옴, 기본값 1

    cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += quantity  # 기존 제품에 수량 추가
        cart_item.save()
    else:
        cart_item.quantity = quantity  # 새로운 장바구니 항목에 수량 설정
        cart_item.save()

    return redirect('pages:products')  # 제품 목록으로 리다이렉트


@login_required
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id, user=request.user)
    cart_item.delete()  # 장바구니에서 아이템 삭제
    return redirect('pages:cart')  # 장바구니 페이지로 리다이렉트


@login_required
def add_product_view(request):
    if request.method == 'POST':
        # 폼으로부터 데이터 가져오기
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']
        region = request.POST['region']

        # 상품 생성 및 저장
        Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity,
            region=region,
        )

        return redirect('pages:products')  # 상품 목록 페이지로 리다이렉트

    return render(request, 'pages/add_product.html')  # GET 요청시 상품 추가 페이지 렌더링
@login_required
def inquiry_list_view(request):
    inquiries = Inquiry.objects.filter(user=request.user)  # 로그인한 사용자의 문의만 가져오기
    return render(request, 'pages/inquiry_list.html', {'inquiries': inquiries})

@login_required
def create_inquiry(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        Inquiry.objects.create(user=request.user, name=name, email=email, message=message)  # 사용자 지정
        messages.success(request, '문의가 등록되었습니다.')
        return redirect('pages:inquiry_list')  # 문의 목록으로 리다이렉트
    return render(request, 'pages/create_inquiry.html')

@login_required
def edit_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(Inquiry, id=inquiry_id)
    if inquiry.user != request.user:  # 사용자 확인
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('pages:inquiry_list')

    if request.method == 'POST':
        inquiry.name = request.POST['name']
        inquiry.email = request.POST['email']
        inquiry.message = request.POST['message']
        inquiry.save()
        messages.success(request, '문의가 수정되었습니다.')
        return redirect('pages:inquiry_list')
    return render(request, 'pages/edit_inquiry.html', {'inquiry': inquiry})

@login_required
def delete_inquiry(request, inquiry_id):
    inquiry = get_object_or_404(Inquiry, id=inquiry_id)
    if inquiry.user != request.user:  # 사용자 확인
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('pages:inquiry_list')

    inquiry.delete()
    messages.success(request, '문의가 삭제되었습니다.')
    return redirect('pages:inquiry_list')

def order_status(request):
    if request.user.is_authenticated:
        orders = Order.objects.filter(user=request.user).order_by('-order_date')
    else:
        orders = []

    return render(request, 'pages/order_status.html', {'orders': orders})


