from django.shortcuts import render

# view fetches the home page ie the page of the main website
def index(request):
	return render(request,"home/home.html")