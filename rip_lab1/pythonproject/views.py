from django.shortcuts import render
from django.http import HttpResponse

from datetime import date
# https://aristos-ekus.ru/image/catalog/seocms/gallery/auditorii-baymana/4_5565dbdc236d9.jpg

# назвать о аудиториях
info_arr =  [
            {'title': '501ю', 'id': 501, 'src': 'image/185.jpg','corpus': 'Главное здание','price': 6000, 'info': 'Большая аудитория для интересных лекция'},
            {'title': '306э', 'id': 306, 'src': 'image/1.jpg','corpus': 'Энерго', 'price': 7500,'info': 'Аудитория для лабораторных'},
            {'title': '222л', 'id': 222, 'src': 'image/222_1.jpg','corpus': 'УЛК','price': 8000, 'info': 'Лекционная аудитория'},
            {'title': '362м', 'id': 362, 'src': 'image/362m.jpg','corpus': 'СМ', 'price': 5000,'info': 'аудиториядля лабораторных'},
            {'title': '111', 'id': 111, 'src': 'image/home.jpg','corpus': 'Главное здание', 'price': 12000,'info': 'Дом физики. Аудитория для лабораторных'},
            {'title': '903', 'id': 903, 'src': 'image/903.jpg','corpus': 'Главное здание', 'price': 15000,'info': 'Аудитория кафедры ИУ5'},
            {'title': '135л', 'id': 135, 'src': 'image/ulk.jpeg','corpus': 'УЛК', 'price': 4000,'info': 'Аудитория для семинаров'},
            {'title': '323', 'id': 323, 'src': 'image/323.jpg','corpus': 'Главное здание','price': 3000, 'info': 'Аудитория для лекций по физике'},
        ]

# def GetOrders(request):
#     return render(request, 'orders.html', {'data' : {
#         'current_date': date.today(),
#         'orders': info_arr,
#     }})
# get room
def GetOrder(request, id):
    order = next((sub for sub in info_arr if sub["id"] == id), None)
    if order:
        print(order["title"])
    else:
        print("Not found!")
    return render(request, 'order.html', {'data' : {
        'current_date': date.today(),
        'id': id,
        'orders': order,
    }})

# убрать саб
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