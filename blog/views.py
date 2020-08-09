from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
all_posts = [
    {
        'author': 'James',
        'title': 'How Learn Django Quickly',
        'content': 'In this post i will teach you How Learn Django Quickly',
        'date_posted': 'Dec 24,2019 10:00 AM'

    },
    {
        'author': 'Tom',
        'title': 'Python JSON',
        'content': 'How to deal with Python JSON',
        'date_posted': 'Dec 23,2019 1:00 PM'

    },
    {
        'author': 'Pintu',
        'title': 'How django Static folder works',
        'content': 'In this post i am going to explaine you how django static folder works',
        'date_posted': 'Dec 23,2019 1:00 PM'

    },
    {
        'author': 'Chintu',
        'title': 'Learn CSS',
        'content': 'In this post i am going to explaine you how django static folder works',
        'date_posted': 'Feb 19,2020 3:39 PM'

    }
]


def index(request):
    data = {
        'posts': all_posts
    }
    return render(request, 'home.html', data)
