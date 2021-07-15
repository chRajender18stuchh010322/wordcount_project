from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
    return render(request, 'home.html',)


def count(request):
    full = request.GET['fulltext']
    wordlist = full.split()

    worddictionary = {}

    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
    sortedwords = sorted(worddictionary.items(),
                         key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fulltext': full, 'count': len(wordlist), 'sortedwords': sortedwords})


def about(request):
    return render(request, 'about.html',)
