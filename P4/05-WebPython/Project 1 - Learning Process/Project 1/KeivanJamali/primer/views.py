from django.http import HttpResponse

def say_hello(request):
    return HttpResponse("Hello-World", content_type='text/plain')