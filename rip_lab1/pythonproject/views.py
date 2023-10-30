from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pythonproject.models import Book
from pythonproject.models import Users
from pythonproject.models import Audiences
from datetime import date
# https://aristos-ekus.ru/image/catalog/seocms/gallery/auditorii-baymana/4_5565dbdc236d9.jpg

import psycopg2

# conn = psycopg2.connect(dbname="postgres", host="localhost", user="student", password="root", port="5432")

# cursor = conn.cursor()
 
# cursor.execute("INSERT INTO public.books (id, name, description) VALUES(4, 'Преступление и наказание', 'Крутая книга')")
 
# conn.commit()   # реальное выполнение команд sql1
 
# cursor.close()
# conn.close()


#!!!! работает без удаления

# def GetRoomSearch(request):
#     input_text = request.GET.get("room")
#     orders = Audiences.objects.all()
#    # orders = orders.filter(status="valid")
#     print(input_text)
#     temp_arr = []
#     return render(request, 'orders.html', {'data' : {
#                 'orders': orders,
#                 'query': input_text,
#                 }})

def GetRoomSearch(request):
    res=[]
    input_text = request.GET.get("room")
    data = Audiences.objects.filter(deleted=False)
    # print(data)
    # data = Cargo.objects.filter(is_deleted=False)
    orders = Audiences.objects.all()
    if input_text is not None:
        for elem in data:
            if input_text in elem.number:
                res.append(elem)
        print(res)        
        return render(
        request,'orders.html', {'data' : {
            'items' : res,
            'input' : input_text,
            'orders': res
        } }
                     )
    
    
    return render(
            request,'orders.html', {
                'data' :
                {
                    'items' : data,
                    'orders': data
                }
            }
            
        )
    # for i in room_arr:
    #     if input_text is not None:
    #         if input_text in i['title']:
    #             temp_arr.append(i)
    #     else:
    #         return render(request, 'orders.html', {'data' : {
    #             'orders': room_arr,
    #             'query': input_text,
    #         }})
    # return render(request, 'orders.html', {'data' : {
    #     'orders': temp_arr,
    #     'query': input_text,
    # }})

def GetRoom(request, id):
    # order = next((sub for sub in room_arr if sub["id"] == id), None)
    #order = Audiences.objects.filter(id=id).first()
    orders = Audiences.objects.all()
    for order in orders:
        if id == int(order.number):
            return render(request, 'order.html', {'data': {
                'number': order.number, 
                'image' :order.image,
                'info' : order.info,
                'status' : order.status,
                'corpus': order.corpus, 
                'price' : order.price,
                'img' : order.img
                }})
            
        
    # clusters = Orders.objects.filter(cluster=order.cluster)
    input_text = request.GET.get("room")
    return render(request, 'order.html', {'data': {'number': 10, 'corpus': '98 views.py'}})


def delObject(request, id):
    # input_text = request.GET.get("delete_order")
    Audiences.objects.filter(id=id).update(status="deleted")
    return redirect('/')

@csrf_exempt
def DeleteCurrentCargo(request):
        if request.method == 'POST':
            
            id_del = request.POST.get('id_del') #работает,надо только бд прикрутить в all_cargo
            conn = psycopg2.connect(dbname="postgres", host="127.0.0.1", user="student", password="root", port="5432")
            cursor = conn.cursor()
            cursor.execute(f"update audiences set deleted = true where id = {id_del}")
            conn.commit()   # реальное выполнение команд sql1
            
            cursor.close()
            conn.close()
        orders = Audiences.objects.all()
        redirect_url = Audiences.objects.all()
        redirect_url = reverse('all_cargo') 
        # Audiences.objects.filter(id=id).update(status="deleted")
        return HttpResponseRedirect(redirect_url)
    

# def GetRoom(request, id):
#     order = next((sub for sub in room_arr if sub["id"] == id), None)
#     if order:
#         print(order["title"])
#     else:
#         print("Not found!")
#     return render(request, 'order.html', {'data' : {
#         'current_date': date.today(),
#         'id': id,
#         'orders': order,
#     }})




def bookList(request):
    return render(request, 'books.html', {'data' : {
        'books': Audiences.objects.all()
    }})

def GetBook(request, id):
    return render(request, 'book.html', {'data' : {
        'current_date': date.today(),
        'book': Audiences.objects.filter(id=id)[0]
    }})