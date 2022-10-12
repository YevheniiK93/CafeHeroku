from django.shortcuts import render, redirect
from .models import Category, Dish, Gallery, Events, Whuus, MyCarousel, Chefs, Emotions
from .forms import UserReservationsForm


def main_page_view(request):
    if request.method == 'POST':
        user_reservation = UserReservationsForm(request.POST)
        if user_reservation.is_valid():
            user_reservation.save()
            return redirect('/')
    categories = Category.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    special_dishes = Dish.objects.filter(is_visible=True).filter(is_special=True)
    gallery = Gallery.objects.filter(is_visible=True)
    user_reservation = UserReservationsForm()
    events = Events.objects.filter(is_visible=True)
    whuus = Whuus.objects.all()
    carousel = MyCarousel.objects.filter(carousel_access=True)
    chefs = Chefs.objects.all()
    emotions = Emotions.objects.all()

    return render(request, 'main_page.html', context={
        'categories': categories,
        'dishes': dishes,
        'special_dishes': special_dishes,
        'gallery': gallery,
        'form_reservation': user_reservation,
        'events': events,
        'whuus': whuus,
        'carousel': carousel,
        'chefs': chefs,
        'emotions': emotions,

    })
