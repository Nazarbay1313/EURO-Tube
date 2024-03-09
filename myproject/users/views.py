from django.contrib.auth import get_user_model, login, logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from myapp.utils import DataMixin
from users.forms import LoginForm, RegisterForm, UpdateProfileForm

# Create your views here.


class UpdateProfile(DataMixin, UpdateView):
    form_class = UpdateProfileForm
    template_name = 'users/update_profile.html'
    model = get_user_model()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UpdateProfile, self).get_context_data()
        c_def = self.get_user_context(title='Редактирование профиля')
        return dict(list(c_def.items())+list(context.items()))

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy('home')


class Register(DataMixin, CreateView):
    form_class = RegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Register, self).get_context_data()
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(c_def.items())+list(context.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class Login(DataMixin, LoginView):
    form_class = LoginForm
    template_name = 'users/login.html'

    def get_success_url(self):
        return reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Login, self).get_context_data()
        c_def = self.get_user_context(title='Вход')
        return dict(list(c_def.items())+list(context.items()))


def logout_user(request):
    logout(request)
    return redirect('home')
