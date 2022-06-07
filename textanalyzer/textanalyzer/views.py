import re
from string import punctuation
from django import http
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
   return render(request , 'index.html')
    # return HttpResponse("Home")

def analyze(request):
    djtext = request.GET.get('text','default')
    
    removepunc = request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcaps','off')
    newlineremove = request.GET.get('newlineremove','off')
    spaceremove = request.GET.get('spaceremove','off')
    charcount = request.GET.get('charcount','off')

    # analyze = djtext
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if djtext != "":
        if removepunc == "off" and fullcaps =="off" and newlineremove == "off" and spaceremove == "off" and charcount == "off":
            params = {'purpose':'No changes','analyzed_text':djtext}
        else:
            if removepunc == 'on': 
                analyze = ""
                for char in djtext:
                    if char not in punctuation:
                        analyze = analyze +char
                
                params = {'purpose':'Removed Punctuations','analyzed_text':analyze}
                djtext = analyze
            
            
            if fullcaps == "on":
                analyze = ""
                for char in djtext:
                    analyze += char.upper()
                params = {'purpose':'Converted to UpperCase','analyzed_text':analyze}
                djtext = analyze

            if newlineremove == "on":
                analyze = ""
                for char in djtext:
                    if char != '\n' and char != '\r':
                        analyze += char
                params = {'purpose':'New line Removed','analyzed_text':analyze}
                djtext = analyze

            if spaceremove == "on":
                analyze = ""
                for index,char in enumerate(djtext):
                    if not(djtext[index] ==" " and djtext[index+1] == " " ):
                        analyze += char
                params = {'purpose':'Extra Space Removed','analyzed_text':analyze}
                djtext = analyze

            if charcount == "on":
                analyze = ""
                count = 0
                for char in djtext:
                    if char != " ":
                        count+=1
                        
                params = {'purpose':'No of characters','analyzed_text':djtext,'count':count}
                djtext = analyze
            
    else:
        success = request
        analyze=""
        params = {'purpose':'Error!!! Field Cant be Empty','analyzed_text':''}
        djtext = analyze
        return render(request , 'index.html',params)

    return render(request , 'index.html',params)
# def removepunc(request):

#     return HttpResponse("removepunc")


# def capfirst(request):
#     return HttpResponse("capitalizefirst")


# def newlineremove(request):
#     return HttpResponse("newlineremove")


# def spaceremove(request):
#     return HttpResponse("spaceremove")

# def charcount(request):
#     return HttpResponse("charcount")