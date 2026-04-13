from django.shortcuts import render, redirect
from .models import UserData


# IP function
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


def store_list(request):
    users = UserData.objects.all().order_by('-created_at')
    return render(request, 'users/store_list.html', {'users': users})


def register(request):
    if request.method == 'POST':
        print("POST AAYA 🔥")   # DEBUG

        name = request.POST.get('name')
        email = request.POST.get('email')
        sentence = request.POST.get('sentence')

        # ✅ IMPORTANT FIX (float conversion + default 0)
        typing_speed = float(request.POST.get('typing_speed') or 0)
        mouse_speed = float(request.POST.get('mouse_speed') or 0)

        device_info = request.POST.get('device_info') or "Unknown"

        ip = get_client_ip(request)

        print("DATA:", name, typing_speed, mouse_speed, ip)  # DEBUG

        # ✅ SAVE DATA
        UserData.objects.create(
            name=name,
            email=email,
            sentence=sentence,
            typing_speed=typing_speed,
            mouse_speed=mouse_speed,
            ip_address=ip,
            device_info=device_info
        )

        print("DATA SAVED ✅")  # DEBUG

        return redirect('success')

    return render(request, 'users/register.html')

def store_list(request):
    users = UserData.objects.all().order_by('-created_at')
    return render(request, 'users/store_list.html', {'users': users})


def success(request):
    return render(request, 'users/success.html')