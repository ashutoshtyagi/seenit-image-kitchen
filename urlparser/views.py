from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from myforms import SubmitForm


# Form to get in URL
def index(request):
    context = {
        'title': "Add an image",
        'form': SubmitForm()
    }
    return render(request, 'urlparser/index.html', context)


# processing the url to show the images
def showImages(request):
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
                if src != None:
                    if (src[0] == '/' and src[1] == '/'):
                        o = urlparse(url)
                        src = o.scheme + "://" + o.netloc + src
                    srcs.append(src)
                src = i.get('data-src')
                if src != None:
                    if (src[0] == '/' and src[1] == '/'):
                        o = urlparse(url)
                        src = o.scheme + "://" + o.netloc + src
                    srcs.append(src)

            images_html = ""
            for s in srcs:
                images_html += "<img src='" + s + "' /><hr>"
            return HttpResponse(images_html)
        else:
            return HttpResponse("not a valid form")

    else:
        form = SubmitForm()

    return render(request, 'urlparser/index.html', {'form': form})
