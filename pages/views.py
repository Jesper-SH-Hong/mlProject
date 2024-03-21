from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views.generic import TemplateView

def homePageView(request):
    return render(request, 'home.html', {
        'mynumbers': [1, 2, 3, 4, 5, 6, ],
        'firstName': 'Jesper Hong'})


def aboutPageView(request):
    # return request object and specify page.
    return render(request, 'about.html')

def jesperPageView(request):
    # return request object and specify page.
    return render(request, 'jesper.html')


def homePost(request):
    # Create variable to store choice that is recognized through entire function.
    choice = -999

    try:
        # Extract value from request object by control name.
        currentChoice = request.POST['choice']

        # Crude debugging effort.
        print("*** Years work experience: " + str(currentChoice))
        choice = int(currentChoice)

    # Enters 'except' block if integer cannot be created.
    except:
        return render(request, 'home.html', {
            'errorMessage': '*** The choice was missing please try again',
            'mynumbers': [1, 2, 3, 4, 5, 6, ]})
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('results', args=(choice,)))


def results(request, choice):
    print("*** Inside reults()")
    return render(request, 'results.html', {'choice': choice})

