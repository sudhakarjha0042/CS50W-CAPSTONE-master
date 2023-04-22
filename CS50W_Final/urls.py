from django.contrib import admin
from django.urls import path
from NewsJunction import views
from django.urls import include
from django.views.generic import TemplateView
from django.views.generic.base import RedirectView
from django.contrib.staticfiles.storage import staticfiles_storage
from django.contrib.auth import views as auth_views
from allauth.account.views import SignupView

# ... your URL patterns here ...



urlpatterns = [
    path('admin/', admin.site.urls),
    path(
    "favicon.ico",
    RedirectView.as_view(url=staticfiles_storage.url("favicon.ico")),
    ),
    path('', TemplateView.as_view(template_name="blog/index.html")),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('accounts/signup/', SignupView.as_view(), name='account_signup'),
    path("news/<str:country_code>", views.news, name="news"),
    path('search/<str:query>', views.search_news, name='search_news'),
    path('summerize/', views.summary, name='summary'),
    path('ReadFull/', views.ReadFull, name='ReadFull'),
    path('getSummary/', views.getSummary, name='getSummary'),
    path('accounts/', include('allauth.urls')),
]

