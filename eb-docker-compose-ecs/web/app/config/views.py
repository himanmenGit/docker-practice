from django.http import HttpResponse


def home(reqeust):
    return HttpResponse('<html><body><h1>Hello World</h1></body></html>')
