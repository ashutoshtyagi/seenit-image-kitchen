from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myforms import ImageForm


# Create your views here.
def index(request):
    return render(request, 'mysite/index.html')


def upload(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            with open('name', 'wb+') as destination:
                for chunk in request.FILES['file'].chunks():
                    destination.write(chunk)

            client_id = '06c94a7610c93ca'
            client_secret = '4ee2cd3c7ed5fcd5b856412ef63ffa70f32a57dd'

            import pyimgur

            im = pyimgur.Imgur(client_id)
            uploaded_image = im.upload_image('name', title="Uploaded with PyImgur")
            url = uploaded_image.link
            return render(request, 'mysite/upload.html', {'url' :url, 'form' : form})
    else:
        form = ImageForm()

    return render(request, 'mysite/upload.html', {'form' : form})

