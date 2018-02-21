from django.shortcuts import render

# Create your views here.
def hello(request):
    template = loader.get_template('Blog/html/index.html')
    return HttpResponse(template.render(context))
