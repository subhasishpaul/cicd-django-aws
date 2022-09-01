from django.shortcuts import render
from .models import Image
from .forms import ImageUpload
# Create your views here.
def image_upload(request):
    images = Image.objects.all()
    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portfolio')
    else:
        form = ImageUpload()
    return render(request, 'index.html', {'form': form, 'images': images})