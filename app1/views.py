from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView

from .models import News, Category
from .forms import ContactForm
def news_list(request):
    # news_list = News.objects.all(status=News.Status.Published)
    news_list = News.published.all()
    category = Category.objects.all()
    context = {
        "news_list" : news_list,
        "categories": category,
    }

    return render(request, "news/news_list.html", context=context)

def news_detail(request, news):
    news = get_object_or_404(News, slug=news, status=News.Status.Published)
    context = {
        "news" : news,
    }

    return render(request, 'news/news_detail.html', context=context)

def homePageView(request):
    news_all = News.published.all().order_by("-publish_time")[:10]
    categories = Category.objects.all()
    local_one = News.published.all().filter(category__name="yangiliklar").order_by("-publish_time")[:1]
    local_news = News.published.all().filter(category__name="yangiliklar").order_by("-publish_time")[1:6]
    rasm = News.objects.all()
    context = {
        "news_all" : news_all,
        "categories":categories,
        "local_news" : local_news,
        "rasm": rasm,
        "local_one": local_one,
    }

    return render(request, "news/home.html", context)

class HomePageView(ListView):
    model = News
    template_name = 'news/home.html'
    context_object_name = 'news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['news_all'] = News.published.all().order_by("-publish_time")[:4]
        context['mahalliy_xabarlar'] = News.published.all().filter(category__name="yangiliklar").order_by("-publish_time")[:5]
        context['dunyo_xabarlar'] = News.published.all().filter(category__name="dunyo").order_by(
            "-publish_time")[:5]
        context['sport_xabarlar'] = News.published.all().filter(category__name="sport").order_by(
            "-publish_time")[:5]
        context['texnologiya_xabarlar'] = News.published.all().filter(category__name="texnologiya").order_by(
            "-publish_time")[:5]
        return context
def contactPage(request):
    context = {

    }
    return render(request, "news/contact.html", context)

def page404(request):
    context = {

    }
    return render(request, "news/404.html", context)

def singlePage(request):
    context = {

    }
    return render(request, "news/single_page.html", context)

# def contactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Biz bilan bo'g'langaningiz uchun tashakkur!")
#     context = {
#         "form": form
#     }
#     return render(request, "news/contact.html", context)
#
class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form':form
        }
        return render(request,'news/contact.html', context)
    def post(self, request, *args, **kwargs):
        form = ContactForm()
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaniz uchun rahmat</h2>")
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)

class TechnoNewsView(ListView):
    model = News
    template_name = 'news/techno.html'
    context_object_name = 'techno_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="texnologiya")
        return news



class NewsView(ListView):
    model = News
    template_name = 'news/yangiliklar.html'
    context_object_name = 'newsView'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="yangiliklar")
        return news

class SportNewsView(ListView):
    model = News
    template_name = 'news/sport.html'
    context_object_name = 'sport_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="sport")
        return news


class DunyoNewsView(ListView):
    model = News
    template_name = 'news/dunyo.html'
    context_object_name = 'world_news'

    def get_queryset(self):
        news = self.model.published.all().filter(category__name="dunyo")
        return news
