from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import TemplateView, CreateView
from accounts.forms import ProfileForm, CreateUserForm, CustomUserChangeForm
from accounts.models import Profile
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings

def index(request):
  return render(request, 'index.html')

User = get_user_model()

class ProfileView(LoginRequiredMixin, TemplateView):
  template_name = 'accounts/profile.html'

profile = ProfileView.as_view()

# @login_required
# def profile_edit(request):
#   try:
#     profile = request.user.profile
#   except Profile.DoesNotExist:
#     profile = None
  
#   if request.method == 'POST':
#     form = ProfileForm(request.POST, request.FILES, instance=profile)
#     if form.is_valid():
#       profile = form.save(commit=False)
#       profile.user = request.user
#       profile.save()
#       return redirect('profile')
#   else:
#     form = ProfileForm(instance=profile)
#   return render(request, 'accounts/profile_form.html', {
#     'form' : form,
#   })

@login_required
def update(request):
  if request.method == 'POST':
    user_change_form = CustomUserChangeForm(request.POST, instance=request.user)
    if user_change_form.is_valid():
        user_change_form.save()
        return redirect('/accounts/profile', request.user.username)
  else:
    user_change_form = CustomUserChangeForm(instance = request.user)
    return render(request, 'accounts/update.html', {
                          'user_change_form':user_change_form
                          })


signup = CreateView.as_view(
  model = User,
  form_class = CreateUserForm,
  success_url = settings.LOGIN_URL,
  template_name = 'accounts/signup.html',

)
