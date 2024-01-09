from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from .models import Post
from .filters import PostFilter
from .forms import PostForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class GroupMixin(UserPassesTestMixin):
    def check_group(self):
        return self.request.user.groups.filter(name='author').exists()

    def test_func(self):
        # Вызываем ваш метод check_group() для проверки наличия пользователя в группе 'author'
        return self.check_group()

    login_url = '/'

class PostsList(ListView):
    model = Post
    ordering = "heading"
    template_name = "posts.html"
    context_object_name = "posts"
    paginate_by = 20

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetails(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"


class PostCreate(CreateView,LoginRequiredMixin, GroupMixin):

    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        if self.request.path == "/posts/news/create":
            post.state = 'NE'
        post.save()
        return super().form_valid(form)


class PostUpdate(UpdateView, LoginRequiredMixin,GroupMixin):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(DeleteView,LoginRequiredMixin, GroupMixin):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')

