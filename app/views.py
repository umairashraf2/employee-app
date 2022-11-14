from app.models import Employee
from django.shortcuts import redirect, render, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.models import User
from django.contrib.auth import logout,login,authenticate

# Create your views here.
def Home(request):
    emp = Employee.objects.all()
    paginator = Paginator(emp,6)
    page_number = request.GET.get('page')
    empfinal = paginator.get_page(page_number)
    last = empfinal.paginator.num_pages
    total = empfinal.paginator.count
    
    context = {
        'emp': empfinal,
        'last': last,
        'total': total,
        'pagelist' : [n+1 for n in range(last)],
    }
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request, 'index.html',context)
        
def Add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = Employee(
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('home')
        
    return render(request, 'index.html')

def Edit(request):
    emp = Employee.objects.all()
    
    context = {
        'emp': emp,
    }
    return render(request, 'index.html',context)

def Update(request,id):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        
        emp = Employee(
            id = id,
            name = name,
            email = email,
            address = address,
            phone = phone,
        )
        emp.save()
        return redirect('home')
    return render(request, 'index.html')
    
def Delete(request,id):
    emp = Employee.objects.filter(id=id)
    emp.delete()
    
    context = {
        'emp':emp
    }
    
    return redirect('home')

def Search(request):
    query = request.GET['query']
    emp1 = Employee.objects.filter(name__icontains=query)
    emp2 = Employee.objects.filter(myid__icontains=query)
    emp3 = Employee.objects.filter(email__icontains=query)
    emp = emp1.union(emp2,emp3)
    paginator = Paginator(emp,6)
    page_number = request.GET.get('page')
    empfinal = paginator.get_page(page_number)
    last = empfinal.paginator.num_pages
    total = empfinal.paginator.count
    
    context = {
        'emp': empfinal,
        'last': last,
        'total': total,
        'pagelist' : [n+1 for n in range(last)],
        'query':query,
    }
    if request.user.is_anonymous:
        return redirect('/login')
    return render(request,"search.html",context)

def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            return render(request, "login.html")

    return render(request, "login.html")

def logoutUser(request):
    logout(request)
    return redirect('/login')
