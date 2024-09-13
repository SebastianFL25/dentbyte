#django utils
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
#models
from django.views.generic import DetailView,FormView,UpdateView
from .models import CustomUser
#exceptions
from django.db.utils import IntegrityError
#forms
from users.forms import SignupForm,CustomUserForm


# class UserDetailView(LoginRequiredMixin,DetailView):
#     template_name='users/detail.html'
#     queryset= CustomUser.objects.all()
#     slug_field='username'
#     slug_url_kwarg= 'username'
#     context_object_name='user'
    
#     def get_context_data(self, **kwargs):
#         """Add user's posts to context."""
#         context = super().get_context_data(**kwargs)
#         user = self.get_object()
#         context['posts'] = Post.objects.filter(user=user).order_by('-create')
#         return context

class UserSignupFormView(FormView):
    template_name='users/signup.html'
    form_class= SignupForm
    success_url= reverse_lazy('users:login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

# class UserUpdateView(LoginRequiredMixin,UpdateView):
    
#     template_name = 'users/update.html'
#     model=CustomUser
#     fields=['website','biography','phone_number','picture']

#     def get_object(self): 
#         return self.request.user.profile
    
#     def get_success_url(self):
#         username=self.object.user.username
#         return reverse('users:detail',kwargs={'username':username})

class LoginView(LoginView):
    template_name='users/login.html'  
    
class LogoutView(LoginRequiredMixin,LogoutView):
    pass
