from django.shortcuts import redirect
from django.contrib.auth import logout

class RestrictAdminMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.user.is_authenticated:
            if not request.user.is_superuser:
                logout(request)
                return redirect('login')
        return self.get_response(request)
