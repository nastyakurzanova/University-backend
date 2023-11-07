from django.shortcuts import redirect, render
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from pythonproject.models import Book
from pythonproject.models import Users
from pythonproject.models import Audiences
from datetime import date

import psycopg2

# conn = psycopg2.connect(dbname="postgres", host="localhost", user="student", password="root", port="5432")

# cursor = conn.cursor()
 
# cursor.execute("INSERT INTO public.books (id, name, description) VALUES(4, 'Преступление и наказание', 'Крутая книга')")
 
# conn.commit()   # реальное выполнение команд sql1
 
# cursor.close()
# conn.close()


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
            'query': input_text,
            # 'input' : input_text,
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

def GetRoom(request, id):
    # orm
    orders = Audiences.objects.all()
    for order in orders:
        if id == int(order.number):
            return render(request, 'order.html', {'data': {
                'number': order.number, 
                'image' :order.img,
                'info' : order.info,
                'deleted' : order.deleted,
                'corpus': order.corpus, 
                'price' : order.price,
                'img' : order.img
                }})
    return render(request, 'order.html', {'data': {'number': 10, 'corpus': '98 views.py'}})


# post отправляет данные на сервер гет запрашивает, пут изменение/обновление, делит 

@csrf_exempt
def DeleteCurrentCargo(request):
        if request.method == 'POST':
            
            id_del = request.POST.get('id_del') 
            
            conn = psycopg2.connect(dbname="postgres", host="127.0.0.1", user="postgres", password="1", port="5432")
            cursor = conn.cursor() # возвращает объект cursor для осуществления запросов к бд
            cursor.execute(f"update audiences set deleted = true where id = {id_del}")
            conn.commit()   # реальное выполнение команд sql1
            

            
            cursor.close()
            conn.close()
        redirect_url = Audiences.objects.all()
        redirect_url = reverse('all_cargo') 
        return HttpResponseRedirect(redirect_url)
    

def bookList(request):
    return render(request, 'books.html', {'data' : {
        'books': Audiences.objects.all()
    }})

def GetBook(request, id):
    return render(request, 'book.html', {'data' : {
        'current_date': date.today(),
        'book': Audiences.objects.filter(id=id)[0]
    }})