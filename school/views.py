from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return HttpResponse("Hello World")

def information(request,district):
	s = "My district is {}".format(district)
	return HttpResponse(s)

def check_number(request,number):
	if number%2 ==0:
		return HttpResponse('%s is even' % number)
	else:
		return HttpResponse('%s is odd' % number)

def blog_func(request):
	return render(request, 'index.html', {'name':'shamim'})

def con_func(request,name):

	return render(request, 'contact.html', {'name':name, 'phone':['01778548587','01515605027','018'], "count":range(1,50)})
