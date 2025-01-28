import operator

from django.http import HttpResponse
from django.shortcuts import render
from . import counter
import operator
# def home(request):
#     return HttpResponse('<h1>this is home</h1>')
# def downlod(request):
#     return HttpResponse('<h1>there is no download</h1>')
def home(request):
     return render(request,'index.html',{'key':'this is python code'})
def result(request):
     article=request.GET['article']
     # age=request.GET['user_age']
     # name=request.GET['user_name']
     # message=f'hi,{name} u r {age} old'
     # return render(request, 'result.html',{'age':message})
     # words=article.split()
     # word_count=len(words)
     # dict_word={}
     # for word in words:
     #      if word in dict_word:
     #           dict_word[word]+=1
     #      else:
     #           dict_word[word]=1
     # sor_dict=sorted(dict_word.items(),key=operator.itemgetter(1),reverse=True)
     sor_dict,word_count=counter.count(article)
     return render(request, 'result.html', {'article': article,'word_count':word_count,'dict_word':sor_dict})