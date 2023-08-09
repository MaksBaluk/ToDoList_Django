from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from .forms import CreateTaskForm
from .models import CustomUser
from ToDoList.models import ToDoList


class CustomUserDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    context_object_name = 'user'
    slug_url_kwarg = 'user_slug'
    template_name = 'users/user_detail.html'

    def test_func(self):
        return True if self.kwargs.get('user_slug') == self.request.user.slug else False

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search', None)
        if search_query:
            tasks = ToDoList.objects.filter(Q(title__icontains=search_query), user=self.object)
        else:
            tasks = ToDoList.objects.filter(user=self.object)
        context['tasks'] = tasks.order_by('-updated_at')
        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('search', None)
        if search_query:
            tasks = ToDoList.objects.filter(Q(title__icontains=search_query), user=self.object)
            return tasks.order_by('title')
        else:
            return queryset

    def get_object(self, queryset=None):
        # Use the slug to get the user object
        user_slug = self.kwargs.get('user_slug')
        return get_object_or_404(CustomUser, slug=user_slug)


class ToDoListTaskDetail(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = ToDoList
    slug_url_kwarg = 'task_slug'
    template_name = 'users/task_detail.html'
    context_object_name = 'task'

    def test_func(self):
        return True if self.kwargs.get('user_slug') == self.request.user.slug else False

    # def get_object(self, queryset=None):
    #     return ToDoList.objects.select_related('user').values('title', 'description', 'updated_at', 'is_complete',
    #                                                           'is_private', 'slug')


class CreateTask(LoginRequiredMixin, CreateView):
    model = ToDoList
    form_class = CreateTaskForm
    slug_url_kwarg = 'user_slug'
    template_name = 'users/create_task.html'

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'user_slug': self.kwargs['user_slug']})

    def form_valid(self, form):
        custom_user = self.request.user
        form.instance.user = custom_user
        return super().form_valid(form)


class UpdateTask(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ToDoList
    form_class = CreateTaskForm
    slug_url_kwarg = 'task_slug'
    template_name = 'users/create_task.html'

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'user_slug': self.kwargs['user_slug']})

    def test_func(self):
        return True if self.kwargs.get('user_slug') == self.request.user.slug else False

    def form_valid(self, form):
        custom_user = CustomUser.objects.get(slug=self.kwargs['user_slug'])
        form.instance.user = custom_user
        return super().form_valid(form)


class DeleteTask(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ToDoList
    context_object_name = 'task'
    template_name = 'users/delete_task.html'
    slug_url_kwarg = 'task_slug'

    def get_success_url(self):
        return reverse_lazy('user_detail', kwargs={'user_slug': self.kwargs['user_slug']})

    def test_func(self):
        return True if self.kwargs.get('user_slug') == self.request.user.slug else False

    def get_queryset(self):
        return ToDoList.objects.filter(user__slug=self.kwargs['user_slug'])


class UpdateIsCompleteView(View):
    def post(self, request, user_slug, task_slug):
        task = ToDoList.objects.get(user__slug=user_slug, slug=task_slug)
        task.is_complete = not task.is_complete
        task.save()
        return redirect('task_detail', user_slug=user_slug, task_slug=task_slug)


class UpdateIsPrivateView(View):
    def post(self, request, user_slug, task_slug):
        task = ToDoList.objects.get(user__slug=user_slug, slug=task_slug)
        task.is_private = not task.is_private
        task.save()
        return redirect('task_detail', user_slug=user_slug, task_slug=task_slug)
