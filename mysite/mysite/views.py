# I have created this file. 
from django.http import HttpResponse
from django.shortcuts import render
import string

def index(request):
    # return HttpResponse("Home")
    # params = {'name': 'sai', 'place':'kurnool'}
    return render(request, "index.html")


# def about(request):
#     return HttpResponse("About Django")


def analyze(request):
    #get the text
    djtext = request.POST.get('text', 'default')
    #check with checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremove = request.POST.get('newlineremove', 'off')
    spaceremover = request.POST.get('spaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    # print(removepunc)
    # print(djtext)
    punct = string.punctuation
    if removepunc == "on":
        analyzed = ""
        for char in djtext:
            if char not in punct:
                analyzed += char
        params = {'purpose':'Remove punctuation', 'analyzed_text':analyzed}
        djtext = analyzed
        # analyze the text.
        # return render(request, 'analyze.html', params)
    if fullcaps == 'on':
        text_caps = djtext.upper()
        params = {'purpose':'Changed to Uppercase', 'analyzed_text':text_caps}
        djtext = text_caps
        # return render(request, 'analyze.html', params)
    if newlineremove == "on":
        removedtext = ""
        for char in djtext:
            if char != "\n" and char !="\r":
                removedtext += char
        params = {'purpose':'newline removed', 'analyzed_text':removedtext}
        djtext = removedtext
        # return render(request, 'analyze.html', params) 
    if spaceremover == "on":
        removedtext = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                removedtext += char
        params = {'purpose':'Extra Space removed', 'analyzed_text':removedtext}
        djtext = removedtext
        # return render(request, 'analyze.html', params) 
    if charcount == "on":
        params = {'purpose':'Counting no of char', 'analyzed_text':len(djtext)}
        # return render(request, 'analyze.html', params) 
    if removepunc != 'on' and charcount != "on" and spaceremover != 'on' and newlineremove != 'on' and fullcaps != 'on':
        return HttpResponse("Select any of the check box to analyze your text")
    # else:
    #     return HttpResponse("Please select removepunc checkbox to check the result")
    return render(request, 'analyze.html', params) 
    




# def capfirst(request):
#     return HttpResponse("capitalize first letter")


# def newlineremove(request):
#     return HttpResponse("New line Remover")


# def spaceremover(request):
#     return HttpResponse("Soace Remover")

# def charcount(request):
#     return HttpResponse("char count")