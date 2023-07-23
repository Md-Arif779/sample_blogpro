from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
from django.shortcuts import reverse
from django.contrib.auth.mixins import LoginRequiredMixin



from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView



# Create your views here.






# def home(request):
#     context = {
#         'posts': Post.objects.all()
#     }

#     return render(request, 'blog/home.html', context)

def about(request):
     return render(request, 'blog/about.html')

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ["-date_posted"]




class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'object'


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['titl', 'content'] 
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})
    
class PostUpdateView(LoginRequiredMixin, UpdateView):
    model = Post
    fields = ['titl', 'content'] 
    template_name = 'blog/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.pk})  


class PostDeleteView(DeleteView):
    model = Post    
    template_name = 'blog/post_delete.html'

    success_url = '/'