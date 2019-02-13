from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse
from .models import Article
def article_detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id) 
    context={}
    context['article_obj']=article
    return render_to_response("article_detail.html",context)
def article_list(request):
    articles=Article.objects.filter(is_delete=False)
    context={}
    context['articles']=articles
    return render_to_response("article_list.html",context)


"""
from django.shortcuts import render
#from django.shortcuts import render_to_response
""from django.shortcuts import render_to_response,get_object_or_404""
from django.http import HttpResponse
from .models import Article
# Create your views here.
def article_detail(request,article_id):
    try:
        article=Article.objects.get(id=article_id)
        context={}
        context['article_obj']=article
        return render(request,"article_detail.html",context)
       #return render_to_response("article_detail.html",context)
    except Article.DoesNotExist:
        raise Http404('not exit')
        #return HttpResponse('不存在')
   # return HttpResponse('<h2>文章标题:%s<\h2><br>文章内容:%s'%(article.title,article.content))
   
""
def article_detail(request,article_id):
    article=get_object_or_404(Article,pk=article_id)  #pk是primykey的缩写
    context={}
    context['article_obj']=article
    return render_to_response("article_detail.html",context)
""
    
"""
