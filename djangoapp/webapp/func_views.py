from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import ProfilePictureForm

def image_view(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
        else: 
            form = ProfilePictureForm()
            return render(request, 'profile.html', {'form': form})

def success(request):
    return HttpResponse('successfully uploaded')
