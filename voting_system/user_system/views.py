from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import reverse

# Create your views here.
def log_voter_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))

def add_user(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)

        if form.is_valid():
            new_user = form.save()
            authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('main:index'))
    
    context = {'form' : form}
    return render(request, 'user_system/add_user.html', context)
