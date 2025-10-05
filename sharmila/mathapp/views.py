

from django.shortcuts import render

def calculate_power(request):
    power = None
    if request.method == "POST":
        try:
            intensity = float(request.POST.get('intensity'))
            resistance = float(request.POST.get('resistance'))
            power = (intensity ** 2) * resistance
        except (ValueError, TypeError):
            power = "Invalid input"
    return render(request, 'mathapp/math.html', {'power': power})


