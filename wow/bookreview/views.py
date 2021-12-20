from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import EditorForm
from .genre import genre1
from datetime import datetime


# Create your views here.
def home(request):
    # rendering information from genre.py
    return render(request=request, template_name='home.html', context={ 'genre1': genre1.keys() })
    
    
def genre(request,genre):
    # created path to filter the posts to each specific genre
    posts = Post.objects.all().order_by('-post_id').filter(genre_id=genre)
    # rendered information from new posts to specific page and infromation from genre.py
    return render(request=request, template_name='genre.html', context={ 'posts':posts,'genre': genre, 'genre_id': genre1[genre], 'img_link':genre})
    
def edit(request,post_id,genre):
    if request.method == 'GET':
        post = Post.objects.get(pk=post_id)
        tags = []
        for tag in post.social.all():
            tags.append(tag.socialtag_id)
        # its inportant instiating the initial form so it can be updated from original user input
        form = EditorForm(initial={ 'title': post.title, 'review': post.review, 'twitter': post.twitter,'meta':post.meta, 'instagram':post.instagram, 'linkedin':post.linkedin, 'tags': post.social, 'img_link': post.img_link })
        return render(request=request, template_name='edit.html', context={ 'form': form, 'id': post_id, 'genre':genre })
        
    if request.method == 'POST':    
        form = EditorForm(request.POST)
        if form.is_valid():            
            # differentiating save
            if 'save' in request.POST:
                # various form information
                title = form.cleaned_data['title']
                img_link = form.cleaned_data['img_link']
                review = form.cleaned_data['review']
                twitter = form.cleaned_data['twitter']
                meta = form.cleaned_data['meta']
                linkedin = form.cleaned_data['linkedin']
                instagram = form.cleaned_data['instagram']
                # social tags
                social = form.cleaned_data['social']
                # variable for sorting/updating
                posts = Post.objects.filter(pk=post_id)
                posts.update(genre_id=genre,title=title, review=review,twitter=twitter,instagram=instagram, meta=meta, linkedin=linkedin, img_link=img_link, social=social)
                posts[0].social.set(social)
            elif 'delete' in request.POST:
                # differentiating delete
                Post.objects.filter(pk=post_id).delete()
        return HttpResponseRedirect(reverse('genre', args=[genre]))

def post(request,genre):
    if request.method == 'GET':
        form =EditorForm()
        # simple render for information
        return render(request=request, template_name='post.html', context={'form':form, 'genre':genre})
    if request.method == 'POST':    
        form = EditorForm(request.POST)
        
        if form.is_valid():
        # form user will see so they can provide information with cleaned data
            title = form.cleaned_data['title']
            img_link = form.cleaned_data['img_link']
            review = form.cleaned_data['review']
            instagram = form.cleaned_data['instagram']
            meta = form.cleaned_data['meta']
            linkedin = form.cleaned_data['linkedin']
            twitter = form.cleaned_data['twitter']
            social = form.cleaned_data['social']

        # made variable for posting objects and added social tags 
            created = Post.objects.create(genre_id=genre, title=title, review=review, img_link=img_link, instagram=instagram,meta=meta,linkedin=linkedin,twitter=twitter, date_created= datetime.now())
            created.social.set(social)

        # reverse for dynamic url
        return HttpResponseRedirect(reverse('genre', args=[genre])) 


