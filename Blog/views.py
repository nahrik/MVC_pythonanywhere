from django.shortcuts import render

# Create your views here.
def Blog(request):
    return render(request, 'Blog/blog.html, {}')
