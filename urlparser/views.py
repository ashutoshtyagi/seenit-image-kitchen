from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.http import *
from django.template import RequestContext, loader
from myforms import SubmitForm, ImageForm
from models import Image
from django.core.urlresolvers import reverse
import urllib

def index(request):
    context = RequestContext(request, {
        'title': "Add an image",
        'form' : SubmitForm()
    })
    return render(request, 'urlparser/index.html', context)


def submit(request):
    if request.method == 'POST':
        # create a form instance and populate it from the data
        form = SubmitForm(request.POST)
        if form.is_valid():
            import urllib2
            from urlparse import urlparse
            from BeautifulSoup import BeautifulSoup
            url = request.POST['url']
            page = BeautifulSoup(urllib2.urlopen(url))
            imgs = page.findAll('img')
            srcs = []

            for i in imgs:
                src = i.get('src')
                if src != None :
                    if(src[0] == '/' and src[1] == '/'):
                        o = urlparse(url)
                        src =  o.scheme + "://" + o.netloc + src
                    srcs.append(src)
                src = i.get('data-src')
                if src != None :
                    if(src[0] == '/' and src[1] == '/'):
                        o = urlparse(url)
                        src =  o.scheme + "://" + o.netloc + src
                    srcs.append(src)
            #return HttpResponse("valid form")
            return render(request, 'urlparser/images.html', {'srcs': srcs})
        else:
            return HttpResponse("not a valid form")

    else:
        form = SubmitForm()

    return render(request, 'urlparser/index.html', {'form':form})

def images(request):
    if request.method == "POST":
        src = request.POST.getlist('checks')
        print request.POST
        return HttpResponse(src )
        """
        download_web_image(src)
        return HttpResponseRedirect('modelform_example')
        """
    srcs_list = request.session['image_sources']
    return render(request, 'urlparser/images.html', {'srcs': srcs_list})

def download_web_image(url):
    import random
    name = random.randrange(1,1000)
    full_name = str(name) + ".png"
    urllib.urlretrieve(url, full_name)

def modelform_example(request, image_id=None):
    image = get_object_or_404(Image, pk=image_id) if image_id else None
    form = ImageForm(instance=image)
    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=image)
        if form.is_valid():
            image = form.save()
            return HttpResponseRedirect('/urlparser/modelform_example/' + str(image.pk))
    return render(request, 'urlparser/modelform_example.html', {'form': form, 'image': image})
