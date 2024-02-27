from django.urls import path

from news.views import HomePageView, ContactPageView, PageNotFound, SinglePageView

app_name = "news"

urlpatterns = [
    path('', HomePageView.as_view(), name='home-page'),
    path('contact/', ContactPageView.as_view(), name='contact-page'),
    path('404-page/', PageNotFound.as_view(), name='404-page'),
    path('single-page/<int:pk>', SinglePageView.as_view(), name='single-page'),
]
