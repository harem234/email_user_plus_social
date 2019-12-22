from django.views.decorators.http import require_http_methods
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordChangeDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm


# @method_decorator(require_http_methods(["POST", ]), name='dispatch')
class PostLogoutView(views.LogoutView):
    """only with Post request user can log out,
    this add more security."""
    next_page = reverse_lazy('logout_post')

    @method_decorator(require_http_methods(["POST", ]))
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

    # model object
    # context_object_name = 'signup_model'
    #
    # context_form_name = 'signup_form'


class CustomLoginView(LoginView):
    template_name = 'registration/password_change_form.html'
    extra_context = {'next': reverse_lazy('FLEX:index')}


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch', )
class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('password_change_done')


@method_decorator(login_required(login_url=reverse_lazy('login')), name='dispatch', )
class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
