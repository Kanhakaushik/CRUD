from django.shortcuts import render
from .models import DataStore, QueryStore
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request,'app/home.html')

def register(request):
    return render(request,'app/register.html')
def savedata(request):
    if request.POST:
        First_Name=request.POST['fname']
        # Last_Name=request.POST['lname']
        Email=request.POST['email']
        Password=request.POST['password']
        Contact=request.POST['contact']
        City=request.POST['city']
        
        user=DataStore.objects.filter(Email=Email)
        if user:
           msg="user alredy exist"
           return render(request,"app/register.html",{'data':msg})
        else:
            DataStore.objects.create(
            First_Name=First_Name,
            # Last_Name=Last_Name,
            Email=Email,
            Password=Password,
            Contact=Contact,
            City=City )
            msg="user creation successfully"
            return render(request,"app/login.html",{'data':msg})
    else:
        msg="change method again post"
        return render(request,'app/register.html',{'data':msg})

def login(request):
    return render(request,'app/login.html')


def logindata(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = DataStore.objects.filter(Email=email)
        if user:
            data = DataStore.objects.get(Email=email)
            if data.Password == password:
                First_Name = data.First_Name
                # Last_Name = data.Last_Name
                Email = data.Email
                Contact = data.Contact
                City=data.City
                user={
                    'fname':First_Name,
                   'email':Email,
                   'contact':Contact,
                   'city':City                }
                return render(request,"app/dash.html",{'key':user})
            else:
                message = "Password does not match"
                return render(request,"app/login.html",{'msg':message})
        else:
            message = "User does not exist"
            return render(request,"app/register.html",{'msg':message})
   

def about(request):
    return render(request,'app/about.html')

def contact(request):
    return render(request,'app/contact.html')
def dash(request):
    return render(request,'app/dash.html')

def table(request):
    return render(request,'app/table.html')
def delete(request):
    return render(request,'app/home.html')

def query(request):
    # Data come from HTML to View
    email = request.POST['email']
    query = request.POST['query']

    QueryStore.objects.create(Email=email,Query=query)
    data = DataStore.objects.get(Email=email)
    First_Name = data.First_Name
    # Last_Name = data.Last_Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    Password=data.Password
    user={
        'fname':First_Name,
        # 'lname':Last_Name,
        'email':Email,
        'contact':Contact,
        'city':City,
        'password':Password       
    }
    
    return render(request,'app/dash.html',{'key':user})

    
def showdata(request,pk):
    Qdata=QueryStore.objects.filter(Email=pk)

    data = DataStore.objects.get(Email=pk)
    First_Name = data.First_Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        'fname':First_Name,
        'email':Email,
        'contact':Contact,
        'city':City}
    return render(request,'app/table.html',{'key1':Qdata,"user":user})
    

def edit(request,pk):
    print(pk)
    data=QueryStore.objects.get(id=pk)
    email=data.Email
    query = data.Query
    id = data.id
    data1={
        'id':id,
        'email':email,
        'query':query
    }
    data = DataStore.objects.get(Email=email)
    First_Name = data.First_Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        'fname':First_Name,
        'email':Email,
        'contact':Contact,
        'city':City                }
    return render(request,"app/dash.html",{'key':user,'key2':data1})


def update(request,pk):
    Updata=QueryStore.objects.get(id=pk)   
    Updata.Email=request.POST['email']
    Updata.Query=request.POST['query']

    Updata.save()  #update query

    Signdata=DataStore.objects.get(Email=Updata.Email)
    First_Name = Signdata.First_Name
    Email = Signdata.Email
    Contact = Signdata.Contact
    City=Signdata.City

    user={
         'fname':First_Name,
        'email':Email,
        'contact':Contact,
        'city':City
    }
    all_data=QueryStore.objects.filter(Email=Email)

    return render(request,'app/table.html',{'key1':all_data,'user':user})
    # email = request.POST['email']
    # query = request.POST['query']

    # data = QueryStore.objects.get(id=pk)
    # data.Query = query
    # data.Email = email
    # data.save()
    # data = DataStore.objects.get(Email=email)
    # First_Name = data.First_Name
    # Email = data.Email
    # Contact = data.Contact
    # City=data.City
    # user={
    #     'fname':First_Name,
    #     'email':Email,
    #     'contact':Contact,
    #     'city':City}
    
    # return render(request,"app/table.html",{'key1':data,'user':user})

def delete(request,pk):
    print(pk)
    data = QueryStore.objects.get(id=pk)
    email = data.Email
    data.delete()
    data = DataStore.objects.get(Email=email)
    First_Name = data.First_Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        
        'fname':First_Name,
        'email':Email,
        'contact':Contact,
        'city':City                }
    return render(request,"app/dash.html",{'key':user})
    

def search(request,var):
    Squery=request.POST['search']
    data=DataStore.objects.get(Email=var)
    First_Name = data.First_Name
    Email = data.Email
    Contact = data.Contact
    City=data.City
    user={
        
        'fname':First_Name,
        'email':Email,
        'contact':Contact,
        'city':City               
          }
    data1=QueryStore.objects.filter(Q(Email=Email) & Q(Query=Squery))
    return render(request,'app/table.html',{'key1':data1,'user':user})

