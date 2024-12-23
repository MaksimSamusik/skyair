from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from . import forms
from .forms import ProfileUpdateForm, UserUpdateForm
from .models import *
from django.core.mail import send_mail


class LoginUser(LoginView):
    form_class = forms.LoginUserForm
    template_name = 'scamclothes/password/login.html'
    success_url = reverse_lazy('main')
    context_object_name = 'Вход'


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('main'))


class RegisterUser(CreateView):
    form_class = forms.RegisterUserForm
    template_name = 'scamclothes/password/register.html'
    success_url = reverse_lazy('login')
    context_object_data = 'Регистрация'


def flight(request):
    posts = Planes.objects.all()
    return render(request, 'scamclothes/pages/flights.html', {'posts': posts, 'title': "Рейсы"})


def main(request):
    return render(request, 'scamclothes/pages/main.html', {'title': "SkyAir"})


def flight_post(request, slug):
    post = get_object_or_404(Planes, slug=slug)
    title = post.city1 + '-' + post.city2
    return render(request, 'scamclothes/pages/flight_post.html', {'post': post, 'title': title})


def search_flights(request):
    city1 = request.GET.get('city1')
    city2 = request.GET.get('city2')
    if city1 and city2:
        flights = Planes.objects.filter(city1__icontains=city1, city2__icontains=city2)
        title = city1 + '-' + city2
    else:
        flights = Planes.objects.all()
        title = 'Не найдено'
    return render(request, 'scamclothes/pages/search_results.html', {'posts': flights, 'title': title})


def profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            print('Ваш профиль обновлен')
            return redirect('profile')  # Перенаправляем на страницу профиля

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'title': 'Профиль'
    }

    return render(request, 'scamclothes/pages/profile.html', context)


def about(request):
    return render(request, 'scamclothes/pages/about.html', {'title': 'О нас'})


def get_user_bucket(user):
    bucket, created = Bucket.objects.get_or_create(user=user)
    return bucket


def add_to_bucket(request, flight_id):
    if request.method == "POST":
        flight = get_object_or_404(Planes, id=flight_id)
        quantity = int(request.POST.get("quantity", 1))

        # Получаем корзину пользователя
        bucket = get_user_bucket(request.user)

        # Проверяем, есть ли уже этот рейс в корзине
        bucket_item, created = BucketItem.objects.get_or_create(bucket=bucket, plane=flight)

        if not created:
            # Если элемент уже в корзине, обновляем количество
            bucket_item.quantity += quantity
        else:
            # Если новый элемент, устанавливаем количество
            bucket_item.quantity = quantity

        bucket_item.save()

        # Переходим на страницу корзины после добавления
        return view_bucket(request)

    # Если запрос не POST, можно вернуть ошибку или перенаправить
    return render(request, "error.html", {"message": "Invalid request"})


def view_bucket(request):
    bucket = get_user_bucket(request.user)
    bucket_items = BucketItem.objects.filter(bucket=bucket)

    items = []
    for item in bucket_items:
        items.append({
            "flight_id": item.plane.id,
            "city1": item.plane.city1,
            "city2": item.plane.city2,
            "start_price": item.plane.start_price,
            "quantity": item.quantity,
        })

    return render(request, "scamclothes/pages/bucket.html", {"cart_items": items, 'title': 'Корзина'})


def checkout(request):
    bucket = get_user_bucket(request.user)
    bucket_items = BucketItem.objects.filter(bucket=bucket)

    items = []
    final_price = 0

    for item in bucket_items:
        items.append({
            "flight_id": item.plane.id,
            "city1": item.plane.city1,
            "city2": item.plane.city2,
            "departure_date": item.plane.departure_date,
            "arrival_date": item.plane.arrival_date,
            "start_price": item.plane.start_price,
            "quantity": item.quantity,
        })
        final_price += item.plane.start_price * item.quantity

    return render(request, "scamclothes/pages/checkout.html", {"items": items, 'final_price': final_price,
                                                               'title': 'Оплата'})


def remove_from_bucket(request, flight_id):
    if request.method == 'POST':
        BucketItem.objects.filter(plane_id=flight_id).delete()
    return redirect('view_bucket')


def pay(request, user_id):
    user = get_object_or_404(User, id=user_id)
    print(user.email)
    send_mail(
        'Оплата рейса',
        '''Здравствуйте! Благодарим вас за выбор наших услуг.
        
Ваш заказ успешно добавлен . Для его оплаты свяжитесь с менеджером в телеграм: @SCAAAMSHIT.
                
Если у вас возникли вопросы, наша служба поддержки всегда готова помочь.
                
Спасибо за ваш выбор!''',
        'djangotesting1@yandex.ru',
        [user.email],
    )
    return render(request, "scamclothes/pages/pay.html", {'title': 'Перейдите на почту'})

