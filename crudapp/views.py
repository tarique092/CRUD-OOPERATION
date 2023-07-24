from django.shortcuts import render,redirect
from . models import Detail
from . forms import detail_form

# Create your views here.
def index(request):
    return render(request,'index.html')

def create(request):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']
        address = request.POST['address']
        data = Detail.objects.create(name=name,age=age,address=address)
        data.save()
        return redirect('index')


def retrive(request):
    details = Detail.objects.all()
    return render(request,'retrive.html',{'details':details})

def edit(request,id):
    object_data = Detail.objects.get(id=id)
    return render(request,'edit.html',{'object_data':object_data})

def update(request,id):
    object_data = Detail.objects.get(id=id)
    form = detail_form(request.POST,instance=object_data)
    if form.is_valid():
        form.save()
        obeject = Detail.objects.all()
        return redirect('retrive')

def delete(request,id):
    Detail.objects.filter(id=id).delete()
    return redirect('retrive')
