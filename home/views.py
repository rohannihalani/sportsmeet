from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.http import request
from django.db.models.functions import Lower


# Create your views here.

def home(request):
    return render(request, 'home/home.html')


@login_required
def main(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'home/main.html', context)



def filter_options(request):
    return render(request, 'home/filter_options.html')





class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'home/main.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['sport', 'location', 'date', 'time', 'content']
 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post

class UserPostListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Post
    template_name = 'home/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')
    
    def test_func(self):
        view_path = ('/user/' + str(self.request.user) + '/')
        
        if self.request.path == view_path:
        
            return True
        else: 
            return False
        

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin ,UpdateView):
    model = Post
    fields = ['sport', 'location', 'date', 'time', 'content']
 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/home/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


# class PostFilterSport(LoginRequiredMixin, ListView):
#     model = Post
#     template_name = 'home/filter_sport.html'
#     context_object_name = 'posts'
#     ordering = ['-date_posted']

#     def get_queryset(self):
#         searched_sport = request.POST.get('sport')
#         return Post.objects.filter(sport=Lower(searched_sport)).order_by('-date_posted')


def PostFilterSport(request):
        searched_sport = request.POST.get('sport')
        

        new_posts = []
        if searched_sport != None:
            new_posts = Post.objects.filter(sport__icontains=searched_sport).order_by('-date_posted')



        context = {
            'posts': new_posts
        }
        return render(request, 'home/filter_sport.html', context)

def PostFilterUser(request):
        searched_user = request.POST.get('author')
        

        new_posts = []
        if searched_user != None:
            new_posts = Post.objects.filter(author__username__icontains=searched_user).order_by('-date_posted')



        context = {
            'posts': new_posts
        }
        return render(request, 'home/filter_user.html', context)

def PostFilterLocation(request):
        searched_location = request.POST.get('location')
        

        new_posts = []
        if searched_location != None:
            new_posts = Post.objects.filter(location__icontains=searched_location).order_by('-date_posted')



        context = {
            'posts': new_posts
        }
        return render(request, 'home/filter_location.html', context)





