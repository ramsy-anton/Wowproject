from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import EditorForm
from .genre import genre1


# Create your views here.
def home(request):
    return render(request=request, template_name='home.html', context={ 'genre1': genre1.keys() })
    
    
def genre(request,genre):
    # genre = Genre.objects.all().order_by('-genre_id')
    # posts = Post.objects.all().order_by('-post_id')
    return render(request=request, template_name='genre.html', context={ 'genre': genre, 'genre_id': genre1[genre], 'img_link':genre})
    
    
def edit(request,post_id):
    if request.method == 'GET':
        post = Post.objects.get(pk=post_id)
        tags = []
        for tag in post.tags.all():
            tags.append(tag.tag_id)
        form = EditorForm(initial={ 'title': post.title, 'body': post.body, 'tags': tags, 'img_link': post.img_link })
        return render(request=request, template_name='edit.html', context={ 'form': form, 'id': post_id })
    if request.method == 'POST':    
        form = EditorForm(request.POST)
        if form.is_valid():
            if 'save' in request.POST:
                title = form.cleaned_data['title']
                img_link = form.cleaned_data['img_link']
                review = form.cleaned_data['review']
                twitter = form.cleaned_data['twitter']
                meta = form.cleaned_data['meta']
                instagram = form.cleaned_data['instagram']
                linkedin = form.cleaned_data['linkedin']
                posts = Post.objects.filter(pk=post_id)
                posts.update(title=title, review=review, img_link=img_link, twitter=twitter, meta=meta,instagram=instagram, linkedin=linkedin)
            elif 'delete' in request.POST:
                Post.objects.filter(pk=post_id).delete()
        return HttpResponseRedirect(reverse('genre'))

def post(request):
    if request.method == 'GET':
       form = EditorForm()
       return render(request=request, template_name='psot.html', context={'form': form})
    if request.method == 'POST':    
        form = EditorForm(request.POST)
        
        if form.is_valid():
            if 'post' in request.POST:
                
                title = form.cleaned_data['title']
                img_link = form.cleaned_data['img_link']
                review = form.cleaned_data['review']
                twitter = form.cleaned_data['twitter']
                meta = form.cleaned_data['meta']
                instagram = form.cleaned_data['instagram']
                linkedin = form.cleaned_data['linkedin']
                
                new = Post.objects.create(title=title, review=review, img_link=img_link, twitter=twitter, meta=meta,instagram=instagram, linkedin=linkedin)
                new.twitter.meta.instagram.linkedin.set(twitter,meta,instagram,linkedin)     
            
        return HttpResponseRedirect(reverse('genre')) 