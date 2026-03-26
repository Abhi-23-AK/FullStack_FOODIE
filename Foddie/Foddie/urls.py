
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from django.contrib.auth import logout

# ✅ Function to control admin access
def admin_redirect(request):
    if not request.user.is_superuser:
        logout(request)
        return redirect('login')  # normal users go to login
    return admin.site.urls(request)  # superuser can access admin

urlpatterns = [
    path('', include('home.urls')),  # home app URLs

    # ✅ Override admin access
    path('admin/', admin.site.urls),  # keep normal admin route
]

# ✅ Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
