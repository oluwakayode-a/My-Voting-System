from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Aspirant, Position, Vote
from .forms import AddAspirant, VotingForm
from next_prev import next_in_order, prev_in_order
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def add_aspirant(request):
    # data = {'name' : 'Hug', 'post' : Position.objects.get(post='PRO').id}
    if request.method == 'POST':
        form = AddAspirant(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            post = form.cleaned_data['post']
            aspirant = Aspirant.objects.create(name=name, post=post)
            aspirant.save()
    else:
        form = AddAspirant(request.POST or None)
    
    return render(request, 'main/add_aspirant.html', {'form' : form})

def asp_post(request):
    all_posts = Position.objects.all()
    return render(request, 'main/asp_post.html', {'all_posts' : all_posts })

@login_required
def vote(request, slug):
    post = Position.objects.get(slug=slug)

    aspirants = Aspirant.objects.filter(post=post)

    if request.method == 'POST':
        if not post.user_can_vote(request.user):
            messages.error(request, 'You have already voted.')
            return HttpResponseRedirect(reverse("main:vote", args=(slug,)))
        form = VotingForm(request.POST, request=request)
        if form.is_valid():
            name = form.cleaned_data['aspirants']
            _asp = Aspirant.objects.get(name=name, post=post)
            new_vote = Vote.objects.create(user=request.user, post=post, aspirant=_asp)
            new_vote.save()

            messages.success(request, "Voted!")
            return HttpResponseRedirect(post.get_absolute_url())

             
    else:
        form = VotingForm(request=request)

    context = {
        'aspirants' : aspirants,
        'post' : post,
        'form' : form,
        }

    return render(request, 'main/vote.html', context)

def log_voter_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('main:index'))
    




