from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.
def index(request):
    html = '''
        <html>
        <body>
        <h2>Admin Modules</h2>
        <ul>
            <li><a href="/urlparser">Image Kitchen</a></li>
        </ul>
        </body>
        </htm>
    '''
    return HttpResponse(html)
