from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .class_views import LoginView, ProfileView, LogoutView, SignUpView
from .func_views import image_view

app_name = 'webapp'
urlpatterns = [
    path('log-in/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('profile-pic/', image_view),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
