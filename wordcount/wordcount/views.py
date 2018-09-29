from django.http import HttpResponse
from django.shortcuts import render
import operator

def home(request):
    return render(request,'home.html',{'myname':'Rejoy'})

def countwords(request):
    return render(request,'countwords.html',{'myname':'Rejoy'})

def countchars(request):
    return render(request,'countchars.html',{'myname':'Rejoy'})

def count(request):
    infile = request.GET['fulltext']
    words = 0
    wordcount = 0
    charactercount = 0
    worddict = {}
    words = infile.split()
    for word in words:
        wordcount = len(words)
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1
    uniquewordcount = len(worddict)
    for word in range(0,len(words)):
        charactercount = charactercount + len(words[word])

    results = {'words':wordcount,'characters':charactercount,'uniquewords':uniquewordcount}
    worddict_sorted = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)
    results["worddict"]=worddict_sorted
    return render(request, 'results.html',results)


def about(request):
    return render(request,'about.html')