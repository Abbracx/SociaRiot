from django.shortcuts import render


from django.views.generic import TemplateView


def homepage(request):

    context = {
        'status': 'Logged In'
    }
    return render(request,'homepage.html', context)