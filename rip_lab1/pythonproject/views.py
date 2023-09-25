from django.shortcuts import render
from django.http import HttpResponse

from datetime import date

info_arr =  [
            {'title': '501ю', 'id': 501, 'src': '/image/gerb.ico'},
            {'title': '306э', 'id': 306, 'src': '/image/gerb.ico'},
            {'title': '633л', 'id': 633, 'src': '/image/gerb.ico'},
            {'title': '515ю', 'id': 515, 'src': '/image/gerb.ico'},
            {'title': '135л', 'id': 135, 'src': '/image/gerb.ico'},
            {'title': '222л', 'id': 222, 'src': '/image/gerb.ico'},
        ]

# def GetOrders(request):
#     return render(request, 'orders.html', {'data' : {
#         'current_date': date.today(),
#         'orders': info_arr,
#     }})

def GetOrder(request, id):
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
    }})

def GetOrders(request):
    input_text = request.GET.get("sub")
    print(input_text)
    temp_arr = []
    for i in info_arr:
        if input_text is not None:
            if input_text in i['title']:
                temp_arr.append(i)
        else:
            return render(request, 'orders.html', {'data' : {
                'orders': info_arr,
                'query': input_text,
            }})
    return render(request, 'orders.html', {'data' : {
        'orders': temp_arr,
        'query': input_text,
    }})