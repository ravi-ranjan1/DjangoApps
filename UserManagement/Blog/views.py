from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
import json
from .models import Blog


def listing(request):
    data = {'blogs': Blog.objects.all()}
    
    return render(request, 'Blog/listing.html', data)

def view_blog(request, blog_id):
    blogs = Blog.objects.get(id= blog_id)


    # blogs = get_object_or_404(Blog,blog_id)
    data = {'blogs':blogs}

    return render(request, 'blog/view_blog.html', data)

@user_passes_test(lambda user: user.is_staff)
def see_request(request):
    text = f""" 
        Some attributes of request:

        Scheme : {request.scheme}
        path : {request.path}
        method : {request.method}
        GET : {request.GET}
        POST : {request.POST}
        user : {request.user}
    
    """
    return HttpResponse(text, content_type='text/plain')

    # JSON = {
    #     'Scheme' : request.scheme,
    #     'path' : request.path,
    #     'method' : request.method,
    #     'GET' : request.GET,
    #     'POST' : request.POST,
    #     # 'user' : request.user
    # }

    # J = json.dumps(JSON)
    # return JsonResponse(J, safe=False, content_type = 'application/json')
@login_required
def user_info(request):
    if request.user.is_authenticated:
        text = f"""
            Select request user attributes

            username : {request.user.username}
            is_anonymous : {request.user.is_anonymous}
            is_staff : {request.user.is_staff}
            is_superuser : {request.user.is_superuser}
            is_active : {request.user.is_active}
        """
        return HttpResponse(text, content_type='text/plain')

@login_required
def add_messages(request):
    username = request.user.username
    messages.add_message(request, messages.INFO, f"Hello {username}")
    messages.add_message(request, messages.WARNING,f"Please login" )
    messages.add_message(request, messages.ERROR,f"Wrong Credentials, Please enter correct credentials!" )
    messages.add_message(request, messages.SUCCESS,f"Congratulations {username}! You are logged In.")

    return HttpResponse('Messages added successfully.', content_type='text/plain')