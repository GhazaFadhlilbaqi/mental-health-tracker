from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306173321',
        'name': 'Muhammad Ghaza Fadhlilbaqi',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)