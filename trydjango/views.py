"""
To render html web pages 
"""

# from urllib import response
from django.http import HttpResponse
from articles.models import Article
from django.template.loader import render_to_string
import random



def home_view(request, *args, **kwargs):
    print(args, kwargs)
    random_id = random.randint(1,5)
    print(random_id)

    article_obj = Article.objects.get(id=random_id)
    article_queryset = Article.objects.all()
    context = {
        "article_queryset":article_queryset,
        "title": article_obj.title,
        "contect": article_obj.contect,
    }

    HTML_STRING = render_to_string("home-view.html", context=context) 
    
    
#     """
# <h1>{title}</h1>
# <p>{contect}<p>
# """.format(**context)
    # HTML_STRING = H_STRING + P_STRING

    return HttpResponse(HTML_STRING)