from django.shortcuts import render
from django.http import HttpResponse
from .forms  import Complaint_form
from django.shortcuts import redirect
from .models import *

def home(request):
    complaint = Complaint.objects.all()
    comments = Comment.objects.all()
    print(complaint[0])
    context = {
        'complaint': complaint,
        'comments' : comments,
    } 
    return render(request, 'portal/home.html', context)



def post(request):
    if request.method == 'POST':
        form = Complaint_form(request.POST)
        if form.is_valid() :
            a = form.save(commit=False)
            a.author = request.user
            a.save()
            return redirect('home')
    else:
        form = Complaint_form()

    context = {
        'form': form,
    }
    return render(request, 'portal/post.html', context)



