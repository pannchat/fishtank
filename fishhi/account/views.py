from django.shortcuts import render, redirect,get_object_or_404
from django.conf import settings
from .forms import SingupForm
from django.contrib.auth.models import User		#유저관리를 위해 import해주기
from django.contrib import auth	
from tankManage.models import Feed
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
import datetime
from django.utils.dateformat import DateFormat

@login_required(login_url='/signin')
def my_profile(request):
    who = get_object_or_404(User, username=request.user)
    feeds = Feed.objects.all()
    feed_list = feeds.filter(username=who)
    today = datetime.date.today()
    dday = (today - feed_list[0].start)
    for el in feed_list:
        el.dday = dday.days
    print(feed_list[0].dday)
    context = {'feed_list':feed_list}
    return render(request, "my_profile.html",context )

def profile(request,pk):
    who = get_object_or_404(User, username=pk)
    user_list = User.objects.all()
    user = user_list.get(username=who)
    print(user.email)
    feeds = Feed.objects.all()
    feed_list = feeds.filter(username=who)
    #  

    # photos = user.Feed.filter(public=True)[:20]
    # context = {"profile_user": user, "photos": photos}
    return render(request, "profile.html",{'feeds':feed_list, 'user':user})

def signup(request):
    if request.method == "POST":
        form = SingupForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('index')
    else:
        form = SingupForm()
    return render(request, 'signup.html', {
        'form': form,
    })

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'signin.html')

def signout(request):

    auth.logout(request)

    return render(request, 'signin.html')