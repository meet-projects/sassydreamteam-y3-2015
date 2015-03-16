from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'app/index.html', {})
def home(request):
	return render(request, 'app/home.html', {})
<<<<<<< HEAD
def upload(request):
	return render(request, 'app/upload.html', {})
=======
def profile(request):
	return render(request, 'app/profile.html', {})
>>>>>>> fe8d9811ae54d3e8a7c5d750c38650ac373a2756
