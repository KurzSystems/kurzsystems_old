from django.contrib import messages
from django.shortcuts import render

from .models import NotifyEmail,Video
from .forms import NotifyEmailForm


# Create your views here.
def coming_soon(request):
    # Notify Email form
    form = NotifyEmailForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NotifyEmail.objects.filter(email=instance.email).exists():
            messages.warning(request, 
                            'Your Email Already exists in our database', 
                            "alert alert-warning alert-dismissible fade show")
        else: 
            instance.save()
            messages.success(request,
                             'Your email has been saved, we will get back to you.',
                             "alert alert-success alert-dismissible fade show")
        
    
    videos = Video.objects.all()
    context = { 'form':form, 'videos': videos }

    return render(request, 'home/coming_soon.html', context)

