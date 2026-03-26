from django.shortcuts import render, redirect
from .models import ReachOut, Variety   # ✅ include Variety here
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseForbidden


def home(request):
    success = False
    varieties = Variety.objects.all()  # ✅ Fetch all varieties from DB

    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        message = request.POST.get('message')

        if username and email and phone and address and message:
            ReachOut.objects.create(
                username=username,
                email=email,
                password=password,
                phone=phone,
                address=address,
                message=message
            )
            return redirect('/?success=true')

    if request.GET.get('success') == 'true':
        success = True

    return render(request, "home/home.html", {
        'success': success,
        'varieties': varieties  # ✅ Pass varieties to template
    })
def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")

        # Validation
        if not username or not email or not password1 or not password2:
            messages.error(request, "All fields are required.")
            return redirect('register')

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

        # Check if username or email already exist
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        # ✅ Create user
        user = User.objects.create_user(username=username, email=email, password=password1)
        user.save()

        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'home/register.html')


# LOGIN VIEW
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('home')
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'home/login.html')



# LOGOUT VIEW
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')

def admin_redirect(request):
    if not request.user.is_superuser:
        return redirect('home')  # Redirect normal users to homepage
    return redirect('/admin/')  # Only allow superuser to access admin
