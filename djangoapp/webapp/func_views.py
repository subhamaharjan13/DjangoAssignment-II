from django.shortcuts import render
from .forms import ProfilePictureForm

def image_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request, 'webapp/image.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ProfilePictureForm()
    return render(request, 'webapp/image.html', {'form': form})
