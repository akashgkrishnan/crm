from django.shortcuts import render, reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from leads.models import Agent
from .forms import AgentModelForm
from .mixins import OrganisorAndLoginRequiredMixin

class AgentListView(OrganisorAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/agent_list.html'
    context_object_name = 'agents'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_profile)


class AgentCreateView(OrganisorAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/agent_create.html'
    form_class = AgentModelForm

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def form_valid(self, form):
        agent = form.save(commit=False)
        agent.organisation = self.request.user.userprofile
        agent.save()
        return super(AgentCreateView, self).form_valid(form)


class AgentDetailView(OrganisorAndLoginRequiredMixin, generic.DetailView):
    template_name = "agents/agent_detail.html"
    context_object_name = 'agent'

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_profile)


class AgentUpdateView(OrganisorAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/agent_update.html'
    form_class = AgentModelForm
    context_object_name = 'agent'

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")

    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_profile)

    
class AgentDeleteView(OrganisorAndLoginRequiredMixin, generic.DeleteView):
    template_name = "agents/agent_delete.html"
    context_object_name = 'agent'


    def get_queryset(self):
        request_user_profile = self.request.user.userprofile
        return Agent.objects.filter(organisation = request_user_profile)

    def get_success_url(self) -> str:
        return reverse("agents:agent-list")