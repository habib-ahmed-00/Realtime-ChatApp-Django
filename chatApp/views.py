from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'login.html')

def room(request, room):
    return render(request, 'chat_room.html')

def checkview(request):
    pass