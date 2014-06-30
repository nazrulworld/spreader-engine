from django.shortcuts import render_to_response
from blog.models import Blog

# Create your views here.

def index(request):
	return render_to_('index.html')
