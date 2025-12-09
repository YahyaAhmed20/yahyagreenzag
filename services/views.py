from django.shortcuts import render


# Create your views here.

# Create your views here.
def services(request):
  


    return render(request, 'services/services.html')




# views.py
from django.shortcuts import render

def service_detail(request):
   
    return render(request, 'services/service_detail.html')
