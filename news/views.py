from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from news.forms import ContactForm
from news.models import New


class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        news = New.objects.all()
        return render(request, 'news/index.html', {'news': news})


class ContactPageView(TemplateView):
    def get(self, request, **kwargs):
        form = ContactForm
        return render(request, 'news/contact.html', {'form': form})

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact successfully created')
            return redirect('news:home-page')
        else:
            return render(request, 'news/contact.html', {'form': form})


class SinglePageView(TemplateView):
    def get(self, request, **kwargs):
        page = New.objects.get(pk=kwargs['pk'])
        return render(request, 'news/single_page.html', {'page': page})


class PageNotFound(TemplateView):
    def get(self, request,**kwargs):
        pages = New.objects.all()
        return render(request, 'news/404.html', {"pages": pages})