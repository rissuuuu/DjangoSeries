
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    # return HttpResponse('Hello world')
    return render(request,'index.html')

def navigationbars(request):
    s='''
    <h2>Navigation Bar</h2></br>
    <a href='https://www.google.com'>Google</a></br>
    <a href='https://www.youtube.com'>Youtube</a></br>
    <a href='https://www.facebook.com'>Facebook</a></br>
    <a href='https://www.linkedin.com'>Linkedin</a></br>
    
    '''
    return HttpResponse(s)


def analyze(request):
    dj_text=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    caps=request.POST.get('uppercase','off')
    newlr = request.POST.get('newlineremover', 'off')
    extrsp=request.POST.get('extraspace','off')

    params = {'purpose': 'No Action', 'analyzed_text': "Please turn any one button on"}

    if removepunc=='on':
        analyzed=re.sub(r'[^A-Za-z0-9 ]',' ',dj_text)
        params={'purpose':'Remove Punctuation','analyzed_text':analyzed}
        dj_text=analyzed

    if caps=='on':
        analyzed=dj_text.upper()
        params={'purpose':'Capitalize letters','analyzed_text':analyzed}
        dj_text=analyzed

    if newlr=='on':
        analyzed=dj_text.split('\n')
        analyzed=' '.join(analyzed)
        params={'purpose':'New Line Remove','analyzed_text':analyzed}
        dj_text=analyzed

    if extrsp=='on':
        analyzed=dj_text.split(' ')
        analyzed = ' '.join(analyzed)
        params={'purpose':'Remove Extra Space','analyzed_text':analyzed}
        dj_text=analyzed

    # else:
    #     return HttpResponse("error")

    return render(request, 'analyze.html', params)

