from django.shortcuts import render
from .forms import ItemForm
from django.http import HttpResponse

# Create your views here.

# No Cookies but with sessions.

def pageCount(request):
    count = request.session.get('count', 0) # if not exist default is 0
    count += 1
    request.session['count'] = count
    return render(request, 'sessionApp/count.html', {'count': count})


def index(request):
    request.session.set_expiry(100)
    del request.session['count']
    return render(request, 'sessionApp/index.html')

# with sessions / not cookies
def addItem(request):
    form = ItemForm()
    if request.method == 'POST':
        name = request.POST['name']
        quantity = request.POST['quantity']
        request.session[name] = quantity
    return render(request, 'sessionApp/addItem.html', {'form' : form})


def displayCart(request):
    return render(request, 'sessionApp/displayItems.html')

