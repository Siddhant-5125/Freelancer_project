from django.shortcuts import render,HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from jobs.models import FreeLancer, Business


def index(request):
    return HttpResponse("<h1>FreeLancers</h1>")


def Home(request):
    return render(request, template_name='home.html')


class FreeLancerListView(ListView):
    model = FreeLancer


class BusinessListView(ListView):
    model = Business


class FreeLancerDetailView(DetailView):
    model = FreeLancer


class BusinessDetailView(DetailView):
    model = Business


class FreeLancerCreateView(LoginRequiredMixin, CreateView):
    model = FreeLancer
    fields = ['name', 'profile_pic', 'skills', 'tagline', 'bio', 'website']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(FreeLancerCreateView, self).form_valid(form)


class BusinessCreateView(LoginRequiredMixin, CreateView):
    model = Business
    fields = ['name', 'profile_pic', 'project_description', 'domain', 'skills_required', 'applications']
    success_url = reverse_lazy('freelancer-list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BusinessCreateView, self).form_valid(form)


@login_required()
def handle_login(request):
    if request.user.get_freelancer() or request.user.get_business():
        return redirect(reverse_lazy('freelancer-list'))

    return render(request, 'jobs/choose_account.html', {})