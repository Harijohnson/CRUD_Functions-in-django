from django.shortcuts import render,redirect
from userForm.models import user
from userForm.forms import userForm
# Create your views here.


def index(request):
    contex={}
    user_data = user.objects.all()
    context = {'user_data':user_data}
    form = userForm()
    context['form'] = form
    if request.method == 'POST':
        if 'submit' in request.POST :
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            my_user = user.objects.create(username=username,email=email,password=password)
            # my_user = userForm(request.POST)
            my_user.save()
    return render(request,'index.html',context=context)

def enter(request):
    # context={}
    # form = userForm()
    # context['form'] = form
    # if request.user.is_authenticated:

    # return render(request,'enter.html',context=context)
    contex={}
    # user_data = user.objects.all()
    # context = {'user_data':user_data}
    # form = userForm()
    # context['form'] = form
    if request.method == 'POST':
        # if 'submit' in request.POST :
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        my_user = user.objects.create(username=username,email=email,password=password)
        # my_user = userForm(request.POST)
        my_user.save()
        print('saved')
    else:
        print('bad connection')
    context={}
    return render(request,'enter.html',context=context)

def exit(request):
    context={}
    return render(request,'exit.html',context=context)

