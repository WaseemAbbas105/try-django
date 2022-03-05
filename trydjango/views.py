"""
To render html web pages 
"""

# from urllib import response
from django.http import HttpResponse



def home_view(request):

    name = "waseem"

    HTML_STRING = f"""
<h2>Hello {name}</h2>
"""
    return HttpResponse(HTML_STRING)