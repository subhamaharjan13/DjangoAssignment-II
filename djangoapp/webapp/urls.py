from django.urls import path
# from .views import login_view, profile_view, logout_view, signup_view
from django.conf import settings
from django.conf.urls.static import static
from .class_views import LoginView, ProfileView, LogoutView, SignUpView
from .func_views import image_view, success

app_name = 'webapp'
urlpatterns = [
    # path('login/', login_view),
    # path('profile/', profile_view),
    # path('logout/', logout_view),
    # path('signup/', signup_view),
    path('log-in/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('profile-pic/', image_view),
    path('success', success)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
