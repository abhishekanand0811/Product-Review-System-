from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.http import JsonResponse
from django.views.decorators.http import require_POST

from .models import User, Product, Review
# from .forms import UserRegistrationForm, ReviewForm

def home_view(request):
    """Home page view"""
    featured_products = Product.objects.all()[:6]
    recent_reviews = Review.objects.select_related('user', 'product').all()[:5]
    
    context = {
        'featured_products': featured_products,
        'recent_reviews': recent_reviews,
    }
    return render(request, 'home.html', context)

def products_view(request):
    """Products listing view"""
    products = Product.objects.all()
    
    # Search functionality
    search_query = request.GET.get('search')
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )
    
    
    paginator = Paginator(products, 9)  # 9 products in a page
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)
    
    return render(request, 'products.html', {'products': products})

def product_detail_view(request, product_id):
    """Product detail view"""
    product = get_object_or_404(Product, id=product_id)
    reviews = product.reviews.select_related('user').all()
    
    # Check if current user has already reviewed this product
    user_review = None
    if request.user.is_authenticated:
        try:
            user_review = Review.objects.get(product=product, user=request.user)
        except Review.DoesNotExist:
            pass
    
    context = {
        'product': product,
        'reviews': reviews,
        'user_review': user_review,
    }
    return render(request, 'product_detail.html', context)

@login_required
@require_POST
def submit_review_view(request, product_id):
    """Submit a review for a product"""
    product = get_object_or_404(Product, id=product_id)
    
    # Check if user is regular user
    if request.user.role != 'regular':
        messages.error(request, 'Only regular users can submit reviews.')
        return redirect('product_detail', product_id=product_id)
    
    # Check if user already reviewed this product
    if Review.objects.filter(product=product, user=request.user).exists():
        messages.error(request, 'You have already reviewed this product.')
        return redirect('product_detail', product_id=product_id)
    
    rating = request.POST.get('rating')
    comment = request.POST.get('comment')
    
    if rating and comment:
        try:
            rating = int(rating)
            if 1 <= rating <= 5:
                Review.objects.create(
                    product=product,
                    user=request.user,
                    rating=rating,
                    comment=comment
                )
                messages.success(request, 'Your review has been submitted successfully!')
            else:
                messages.error(request, 'Rating must be between 1 and 5.')
        except ValueError:
            messages.error(request, 'Invalid rating value.')
    else:
        messages.error(request, 'Please provide both rating and comment.')
    
    return redirect('product_detail', product_id=product_id)

def register_view(request):
    """User registration view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        if password1 != password2:
            messages.error(request, 'Passwords do not match.')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists.')
            return render(request, 'auth/register.html')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists.')
            return render(request, 'auth/register.html')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password1,
                role='regular'
            )
            messages.success(request, 'Registration successful! You can now login.')
            return redirect('login')
        except Exception as e:
            messages.error(request, 'Registration failed. Please try again.')
    
    return render(request, 'auth/register.html')

def login_view(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'auth/login.html')

@login_required
def profile_view(request):
    """User profile view"""
    user_reviews = Review.objects.filter(user=request.user).select_related('product')
    
    context = {
        'user_reviews': user_reviews,
    }
    return render(request, 'profile.html', context)
