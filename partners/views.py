from django.shortcuts import render


def partners(request):
    return render(request, 'partners/partners.html')

def partner_details(request):
    return render(request, 'partners/partners_details.html')

