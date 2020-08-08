from django.http import HttpResponse
from django.shortcuts import render
import operator
def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def count(request):
    fulltext=request.GET['fulltext']
    wordlist=fulltext.split()
    wordcount={}
    for word in wordlist:
        wordcount[word]=wordcount.get(word,0)+1
    sortedwords=sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
    count=0
    q={}
    for a,b in sortedwords:
        q[a]=b
        count+=1
        if count==10:break
    return render(request, 'count.html',{'fulltext':fulltext, 'count':len(wordlist),'sortedwords':q.items()})
