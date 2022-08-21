from django.shortcuts import redirect, render

from .models import Candidate
from .forms import CandidateForm
from django.core.files.storage import FileSystemStorage

def home(request):
    data=Candidate.objects.filter()
    form = CandidateForm()
    data1={'data':data, 'form':form}
        
    return render(request,'candidate_list.html', data1)


def candidate_form(request):
    try:
        form= CandidateForm()
        
    except:
        return redirect('home')
    
    return render(request, 'add_candidate.html', {'form':form})


def add_candidate(request):
    try:
        if request.method=="POST":
            form= CandidateForm(request.POST)
            if form.is_valid():
                form.save()
    except:
        return redirect('home')
            
    return redirect('home')


def candidate_detail(request):
    try:
        id= request.POST.get('id')
        data=Candidate.objects.get(id=id)
        data1={'data':data}
        print(data.name)
    
    except:
        return redirect('home')
    
    return render(request,'candidate_detail.html', data1 )


def change_status(request,pk):
    try:
        result= request.POST.get('Status')
        data=Candidate.objects.filter(id=pk)
        for d in data:
            d.status= result
            d.save()
        data1={'data':data}
    
    except:
        return redirect('home')

    return redirect('home')


def upload_resume(request, pk):
    try:
        data=Candidate.objects.get(id=pk)
        if request.method=="POST":
            myfile= request.FILES['resume']
            myfile._name= str(data.id) +'.pdf'
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            data.resume= '/media/'+str(data.id)+'.pdf'
            print(uploaded_file_url)
            data.save()
            data1={'data':data}
        
    except:
        return redirect('home')
        
    return redirect('home')
