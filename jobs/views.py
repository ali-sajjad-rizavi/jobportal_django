from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from jobs.models import Jobpost


def home(request):
    """Jobs home page"""
    return render(request, 'index.html')


# Generic Views:
# --------------
# - Default template_name is <app>/<model>_<viewtype>.html
# - Create and Update views share a template <app>/<model>_form.html

class JobpostListView(ListView):
    """A list view for displaying list of Jobposts created by different users"""
    model = Jobpost
    ordering = ['-date_posted']
    paginate_by = 10


class JobpostDetailView(DetailView):
    """Details of a single Jobpost"""
    model = Jobpost


class JobpostCreateView(LoginRequiredMixin, CreateView):
    model = Jobpost
    fields = ['title', 'description', 'min_salary', 'max_salary', 'category']

    def form_valid(self, form):
        """Override"""
        form.instance.author = self.request.user
        return super().form_valid(form)


class JobpostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Jobpost
    fields = ['title', 'description', 'min_salary', 'max_salary', 'category']

    def form_valid(self, form):
        """Override"""
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        return self.request.user == self.get_object().author


class JobpostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Jobpost
    success_url = '/'

    def test_func(self):
        return self.request.user == self.get_object().author


# TODO: Make use of this view
class UserJobpostListView(ListView):
    """List of jobposts posted by a single user"""
    model = Jobpost
    template_name = 'jobs/user_jobpost_list.html'
    ordering = ['-date_posted']
    paginate_by = 10

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Jobpost.objects.filter(author=user).order_by('-date_posted')
