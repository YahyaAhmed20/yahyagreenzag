from django.shortcuts import render

def news(request):

    return render(request, 'news/news.html')



def news_details(request):

    return render(request, 'news/news_detail.html')





