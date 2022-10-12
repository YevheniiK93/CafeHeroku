from django.shortcuts import render, redirect
from .models import UserReservations
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.groups.filter(name='manager').exists())
def reservation_list(request):
    lst = UserReservations.objects.filter(is_processed=False)
    return render(request, 'reservation_list.html', context={'lst': lst})


@login_required(login_url='/login/')
@user_passes_test(lambda user: user.groups.filter(name='manager').exists())
def reservation_update(request, pk):
    UserReservations.objects.filter(pk=pk).update(is_processed=True)
    return redirect('manager:reservation_list')

