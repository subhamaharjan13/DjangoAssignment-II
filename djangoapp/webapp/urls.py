from django.urls import path
# from .views import login_view, profile_view, logout_view, signup_view
from .class_views import LoginView, ProfileView, LogoutView, SignUpView

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
]