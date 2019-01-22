from django.shortcuts import render

def home(request):
	return render(request, "home.html", {})

def about(request):
	from pages.namer import bob
	return render(request, "about.html", {"my_stuff": bob})

def contact(request):
	return render(request, "contact.html", {})
