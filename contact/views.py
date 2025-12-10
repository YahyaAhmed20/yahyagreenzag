from django.shortcuts import render

def send_text(request):
  

    return render(request, 'contact/contact.html')