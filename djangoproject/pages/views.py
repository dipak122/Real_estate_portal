from django.shortcuts import render , redirect
from . models import registeringo,addhouse
from django.core.files.storage import FileSystemStorage
from . forms import HouseForm




def index(request):
    house = addhouse.objects.all()


    return render(request, "index.html", {'house':house})

def searched(request):
    house = addhouse.objects.all()


    return render(request, "searched.html", {'house':house})



def login(request):
    return render(request, "login.html", {})

def login_submission(request):
    list_house = registeringo.objects.all()

    username=request.POST["Username"]
    password=request.POST["Password"]


    for m in list_house :
        if username == m.username :
            if password == m.password :
                print("User successfully login in")
                return redirect('upload_house')



            else:
                f='invalid user name and password'
                return render(request, "{ url 'login' }", {'m':f})

        else:
            continue
    f='invalid user name and password'
    return render(request, "login.html", {'m':f})







def upload(request):
    context={}
    if request.method == 'POST':
        uploaded_files = request.FILES['document']
        fs=FileSystemStorage()
        name=fs.save(uploaded_files.name,uploaded_files)
        context['url']=fs.url(name)


    return render(request,"upload_house.html",context)





def house_list(request):

    house= addhouse.objects.all()

    return render(request, 'house_list.html',{'house':house})

def upload_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('house_list')
    else:
        form = HouseForm()

    return render(request, 'upload_house.html',{'form' : form})


def delete_house(request, pk):
    if request.method == 'POST':
        house = addhouse.objects.get(pk='pk')
        house.delete()
    return redirect('house_list')

def search(request):
    if request.method == 'POST':
        house = addhouse.objects.all()

        place = request.POST["place"]
        c='0'

    return render(request, "searched.html", {'house': house, 'place':place,'c':c})







def register(request):
    return render(request,"register.html", {})

def register_submission(request):
    list_house = registeringo.objects.all()
    print("hello form is registered.")
    username=request.POST["Username"]
    password=request.POST["Password"]
    f=1
    for m in list_house :
        if username == m.username :
            print("Username already exit")
            m = 'user already exist'
            return render(request, "register.html", {'m': m})
            f=0
            break
    if f==1:
        Registerinfo = registeringo(username=username,password=password)
        m='successfully registered'
        Registerinfo.save()
    return render(request, "register.html", {'m': m})









def about(request):
    return render(request, "about.html", {})

def single_list(request):
    return render(request, "single-list.html", {})

def blog(request):
    return render(request, "blog.html", {})

def contact(request):
    return render(request, "contact.html", {})





