from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Lead, Agent
from .forms import LeadForm, LeadModelForm, CustomUserCreationForm


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    form_class = CustomUserCreationForm

    def get_success_url(self) -> str:
        return reverse("login")


def landing_page(request):
    return render(request, "landing.html")


class LandingPageView(TemplateView):
    template_name = 'landing.html'


def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
    }
    return render(request, 'leads/lead_list.html', context)


class LeadListView(LoginRequiredMixin, ListView):
    template_name = "leads/lead_list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, 'leads/lead_detail.html', context)


class LeadDetailView(LoginRequiredMixin, DetailView):
    temmplate_name = 'leads/lead_detail.html'
    queryset = Lead.objects.all()
    context_object_name = "lead"


def lead_create(request):
    form = LeadModelForm()

    if request.method == 'POST':
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        'form': form
    }
    return render(request, 'leads/lead_create.html', context)


class LeadCreateView(LoginRequiredMixin, CreateView):
    template_name = 'leads/lead_create.html'
    form_class = LeadModelForm

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")

    def form_valid(self, form):
        send_mail(
            subject='hi user',
            message='new user has been added',
            from_email='akash@123.com',
            recipient_list=['test2@tes.com'])
        return super(LeadCreateView, self).form_valid(form)


def lead_update(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == 'POST':
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("/leads")
    context = {
        "form": form,
        "lead": lead
    }
    return render(request, 'leads/lead_update.html', context)


class LeadUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'leads/lead_update.html'
    form_class = LeadModelForm
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse("leads:lead-list")


def lead_delete(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("/leads")


class LeadDeleteView(LoginRequiredMixin,DeleteView):
    temmplate_name = 'leads/lead_delete.html'
    queryset = Lead.objects.all()

    def get_success_url(self) -> str:
        return reverse('leads:lead-list')
