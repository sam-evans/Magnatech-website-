from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	my_name = "Hello, we are team 3468!"
	return render(request, "about.html", {"my_name": my_name})

def contact(request):
	return render(request, "contact.html", {})
