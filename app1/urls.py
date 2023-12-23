from django.urls import path
from .views import news_list, news_detail, homePageView, contactPage, page404, singlePage, ContactPageView,HomePageView, \
  NewsView, TechnoNewsView, SportNewsView, DunyoNewsView

urlpatterns = [
  path('', HomePageView.as_view(), name="index_view"),
  path('all/', news_list, name="all_news_list"),
  path('news/<slug:news>', news_detail, name="news_detail_page"),
  path('contact_us/', ContactPageView.as_view(), name="contact_page"),
  path('page_404/', page404, name="page_404"),
  path('yangilik/', NewsView.as_view(), name="yangilikPage"),
  path('techno/', TechnoNewsView.as_view(), name="technoPage"),
  path('sport/', SportNewsView.as_view(), name="sportPage"),
  path('dunyo/', DunyoNewsView.as_view(), name="dunyoPage"),

]