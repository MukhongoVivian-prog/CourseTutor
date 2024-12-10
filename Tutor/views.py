from django.shortcuts import render, redirect, get_object_or_404
from Tutor.forms import CheckoutForm, ImageUploadForm
from Tutor.models import Checkout, Member, ImageModel, Course,Event


# Create your views here.
def home(request):
    if request.method == 'POST':
        if Member.objects.filter(
                username=request.POST['username'],
                password=request.POST['password'],
        ).exists():
            members = Member.objects.get(
                username=request.POST['username'],
                password=request.POST['password'],
            )
            return render(request, 'index.html', {'members': members})
        else:
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

def view_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    return render(request, 'view_event.html', {'event': event})

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def details(request):
    return render(request,'course-details.html')
def courses(request):
    return render(request,'courses.html')
def events(request):
    return render(request,'events.html')
def pricing(request):
    return render(request,'pricing.html')
def trainers(request):
    return render(request,'trainers.html')
def starter(request):
    return render(request,'starter-page.html')
def checkout(request):
    if request.method == "POST":
        mycheckout = Checkout(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            payment_method=request.POST['payment_method'],  # added payment method
            mpesa_number=request.POST['mpesa_number'],  # added mpesa phone number

        )
        mycheckout.save()
        return redirect('/display')
    else:

        return render(request, 'checkout.html', )  # updated the template name to 'checkout.html'

def view(request):
    checkouts= Checkout.objects.all()
    return render(request,'display.html',{'checkout':checkouts})
def delete(request, id):
    appoint = Checkout.objects.get(id=id)
    appoint.delete()
    return redirect('display')

def edit(request,id):
    edit=Checkout.objects.get(id=id)
    return render(request,'edit.html',{'checkout':edit})
def update(request,id):
    updateinfo = Checkout.objects.get(id=id)
    form = CheckoutForm(request.POST,instance=updateinfo)
    if form.is_valid():
        form.save()
        return redirect('/display')
    else:
        return render(request,'edit.html')
def register(request):
    if request.method ==   "POST":
        memberinfo=Member(
            name = request.POST['name'],
            username = request.POST['username'],
            password = request.POST['password']
        )
        memberinfo.save()
        return redirect('/login')
    else:
        return render(request,'register.html')
def login(request):
    return render(request,'login.html')


def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload-image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show-image.html', {'images': images})

def imagedelete(request, id):
    image = ImageModel.objects.get(id=id)
    image.delete()
    return redirect('/showimage')