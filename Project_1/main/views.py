from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm, UserRegisterForm
from django.views.generic.edit import FormView
from django.contrib import messages


def index(request):
    tasks = Task.objects.order_by('-id')    # .all  ,  .order_by('-id')[:1]
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def login(request):
    return render(request, 'main/login.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Акк готов, {username}')
            return redirect('home')
    else:
        form = UserRegisterForm
    return render(request, 'main/register.html', {'form': form})


def profile(request):
    return render(request, 'main/profile.html')


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():  # проверка данных на корректность ввода
            form.save()  # сохранение данных (переменная form)
            return redirect('home')  # переносим пользователья на страницу home
        else:
            error = 'Форма заполнена не корректно'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)


