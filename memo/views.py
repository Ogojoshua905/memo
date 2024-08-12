from django.shortcuts import render, redirect, get_list_or_404
from django.contrib import messages
from django.contrib.auth.models import User, auth
from .forms import MemoForm
from .models import Memo

# Create your views here.
def home(request):
    redirect('message')
    if request.method == 'POST':
        print(request.POST, request.FILES)
        form = MemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = MemoForm()

    memos = Memo.objects.all()
    return render(request, 'index.html', {'memo_data': memos})

def message_func(request):
    return render(request, 'message.html')

def detail_func(request):
    filter_memo = get_list_or_404(Memo, pk=pk)
    return render(request, 'details.html', {'memo_data': filter_memo})
# def register(request):
#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # Redirect to a login page or wherever you want after registration
#     else:
#         form = UserCreationForm()

    # return render(request, "register.html", {'form': form})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email Already In Used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already In Use')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password Not the Same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    