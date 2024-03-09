from django.urls import path

from users.views import Login, Register, UpdateProfile, logout_user

urlpatterns = [
    path('update_profile/', UpdateProfile.as_view(), name='update_profile'),
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout_user/', logout_user, name='logout_user')
]
