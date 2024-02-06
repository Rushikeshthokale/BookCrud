from django.shortcuts import render,redirect
from BookApp.models import Book
def homePage(request):
    data=Book.objects.all()
    context={}
    context['books']=data
    return render(request,'home.html',context)

def register(request):
    if request.method=='GET':
        print("Within get")
        return render(request,'register.html')
    else:
        print("Within post")
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']
        b=Book.objects.create(title=t,author=a,price=p)
        b.save()
        # print("Book added: ",t,a,p)
        # return render(request,'home.html')
        return redirect('/home')
    
def deleteBook(request,bookid):
    print("Deleted book id: ",bookid)
    b=Book.objects.filter(id=bookid)
    b.delete()
    # return render(request,'home.html')
    return redirect('/home')

def updateBook(request,bookid):
    if request.method=="GET":
        print("Update book id: ",bookid)
        b=Book.objects.filter(id=bookid)
       
        context={}
        context['book']=b[0]
        return render(request,'updateBook.html',context)
    else:
        t=request.POST['title']
        a=request.POST['author']
        p=request.POST['price']
        b=Book.objects.filter(id=bookid)
        b.update(title=t,author=a,price=p)
        return redirect('/home')