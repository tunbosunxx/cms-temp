from django.shortcuts import render

# Create your views here.
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy


class HomeView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "home.html")
