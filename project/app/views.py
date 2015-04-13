from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
def home(request):
	return render(request, 'app/home.html', {})
def upload(request):
	return render(request, 'app/upload.html', {})
def profile(request):
	return render(request, 'app/profile.html', {})
