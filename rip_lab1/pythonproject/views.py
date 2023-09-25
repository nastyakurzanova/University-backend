from django.shortcuts import render
from django.http import HttpResponse

from datetime import date
# https://aristos-ekus.ru/image/catalog/seocms/gallery/auditorii-baymana/4_5565dbdc236d9.jpg

orders_arr = [
            {'corpus': 'Главное здание', 'info': 'Сложно найти, легко потерять и невозможно забыть' },
            {'corpus': 'Энерго', 'info': 'Сложно найти, легко потерять и невозможно забыть'},
            {'corpus': 'Энерго', 'info': 'Сложно найти, легко потерять и невозможно забыть'},
            {'corpus': 'УЛК', 'info': 'Сложно найти, легко потерять и невозможно забыть'},
            {'corpus': 'УЛК', 'info': 'Сложно найти, легко потерять и невозможно забыть' },
            {'corpus': 'УЛК', 'info': 'Сложно найти, легко потерять и невозможно забыть'},
            {'corpus': 'Энерго', 'info': 'Сложно найти, легко потерять и невозможно забыть'},
            {'corpus': 'Энерго', 'info': 'Сложно найти, легко потерять и невозможно забыть'},
]

info_arr =  [
            {'title': '501ю', 'id': 501, 'src': 'Картинка','definition': orders_arr[0]},
            {'title': '306э', 'id': 306, 'src': 'Картинка','definition': orders_arr[1]},
            {'title': '515э', 'id': 515, 'src': 'Картинка','definition': orders_arr[2]},
            {'title': '633л', 'id': 633, 'src': 'Картинка','definition': orders_arr[3]},
            {'title': '515ю', 'id': 515, 'src': 'Картинка','definition': orders_arr[4]},
            {'title': '135л', 'id': 135, 'src': 'Картинка','definition': orders_arr[5]},
            {'title': '222л', 'id': 222, 'src': 'Картинка','definition': orders_arr[6]},
            {'title': '310э', 'id': 310, 'src': 'Картинка','definition': orders_arr[7]},
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