
from django.shortcuts import render
from .forms import SignForm ,UserForm ,ProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.shortcuts import render,redirect
from django.urls import reverse
from .models import Profile

# Create your views here.

def signup(request):
    if request.method=='POST':
        form = SignForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')

    else :
        form = SignForm()

    return render(request,'registration/signup.html',{'form':form})


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    context = {'profile':profile}

    return render(request,'accounts/profile.html',context)

@login_required
def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        userform=UserForm(request.POST,instance=request.user)
        profileForm = ProfileForm(request.POST,request.FILES,instance=profile)
        if userform.is_valid():
            userform.save()
            profileForm = profileForm.save(commit=False)
            profileForm.user = request.user
            profileForm.save()
            return redirect(reverse('accounts:profile'))

    else :
        userform=UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)
        context = {'userform':userform,'profileform':profileform}

    return render(request,'accounts/edit_profile.html',context)

