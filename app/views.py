from django.http import HttpResponse
from django.shortcuts import render
import datetime
from .models import Book

# Create your views here.

# def homepage(request):
#     # print(request.method)
#     # print(request.user)
#     # print(request.get_full_path)
#     # print(dir(request))
#     # return HttpResponse("hello this is homepage")
#     # return render(request, "home.html", {"Welcome":'We welcome you', "location":"Pune"})

#     # data={"Welcome":'We welcome you', "location":"Pune"}
#     # return render(request, "home.html", data)
#     # print(locate)

#     # data={"Welcome":'We welcome you', "location":locate}
#     # return render(request,"home.html",data)
    
#     # data={"flag":"Yes", "lst":[19,14,15,16],"today": datetime.datetime.now().date(),"words":"hey there I am using whtsapp"}
#     # return render(request, "home.html", data)
#     # return render(request, "home.html", {"data":{1:10,2:20,3:30}})
#     # try:
#     #     book_obj=Book.objects.get(id=pk)
#     # except Book.DoesNotExist:
#     #     data1={"error":"This id is not present in db"}
#     #     return render(request, "home.html", data1)

#     # context={"Book":book_obj}
#     # return render(request, "home.html", context)

#     # data={"flag":"Yes", "all_book":Book.objects.all(),"today": datetime.datetime.now().date(),"words":"hey there I am using whtsapp"}
#     data={"all_book":Book.objects.all()}
#     return render(request, "home.html", context=data)


def input_form(request):
    if request.method == 'POST':
        book_name = request.POST.get("bname")
        book_price = request.POST.get("bprice")
        book_quant = request.POST.get("bqty")
        book_pub = request.POST.get("bpub")
        print(book_name, book_price, book_quant, book_pub)
        if book_pub == "Yes":
            book_pub = True
        else:
            book_pub = False
        book_obj=Book(name=book_name, price=float(book_price), quantity=int(book_quant), is_published = book_pub)
        book_obj.save()
        return HttpResponse("Data saved successfully...")
    else:
        return render(request, "input_form.html")


def show_books(request):
    all_books = Book.objects.all()
    return render(request, "show_books.html", {"all_book":all_books})


<<<<<<< HEAD
def video_prod(request):
    print("in video of prod")
    return HttpResponse("playing the video")
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
def user_login(request):
    username = request.POST.get("username")
    password = request.POST.get("password") #getting these from request.POST that is from page which we enter
    user = authenticate(username=username, password=password) #user retuned if matched
    if user:
        login(request, user)
        return HttpResponse("successfully logged in")


>>>>>>> f1
