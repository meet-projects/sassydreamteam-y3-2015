from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
def home(request):
	return render(request, 'app/home.html', {})
def upload(request):
	return render(request, 'app/upload.html', {})
def profile(request):
	return render(request, 'app/profile.html', {})
def contactus(request):
	return render(request, 'app/contactus.html', {})
def login(request):
	return render(request, 'app/login.html', {})
def signup(request):
	return render(request, 'app/signup.html', {})

def reginfo(request):
	firstname = request.POST['firstnamesignup']
	return HttpResponse("Welcome "+firstname)
