from django.shortcuts import render
from django.http import HttpResponse

from datetime import date
      
def GetOrders(request):
    return render(request, 'orders.html', {'data' : {
        'current_date': date.today(),
        'orders': [
            {'title': '501ю', 'id': 501},
            {'title': '306э', 'id': 306},
            {'title': '633л', 'id': 633},
            {'title': '515ю', 'id': 515},
            {'title': '135л', 'id': 135},
            {'title': '222л', 'id': 222},
        ]
    }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id
    }})

def sendText(request):
    input_text = request.POST['text']
