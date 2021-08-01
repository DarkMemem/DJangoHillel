from django.views.generic import CreateView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy, reverse

from .forms import AccountRegistrationForm, AccountUpdateForm


class AccountRegistrationView(CreateView):
    model = User
    form_class = AccountRegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/registration.html'


class AccountLoginView(LoginView):
    template_name = 'accounts/login.html'

    def get_redirect_url(self):
        param_next = self.request.GET.get('next')
        if param_next:
            return param_next

        return reverse('index')


class AccountLogoutView(LogoutView):
    template_name = 'accounts/logout.html'


class AccountUpdateView(UpdateView):
    model = User
    template_name = 'accounts/profile_update.html'
    success_url = reverse_lazy('index')
    form_class = AccountUpdateForm

    def get_object(self, queryset=None):
        return self.request.user
