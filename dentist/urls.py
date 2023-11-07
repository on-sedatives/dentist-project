"""
URL configuration for _project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from dentist import views

app_name = 'dentist'

page_list = views.Page.objects.values()
urlpatterns = []

for item in page_list:
    if item['template'] == "home":
        urlpatterns.append(
            path("", eval("views." + item['template']), name=item['template']),
        )
    elif item['template'] == "service_list":
        urlpatterns.append(
            path(item['slug'] + "/", eval("views." + item['template']), name=item['template']),
        )
        urlpatterns.append(
            path(item['slug'] + "/<slug:slug>/", views.service_detail, name='service_detail'),
        )
        urlpatterns.append(
            path(item['slug'] + "/<slug:slug>/comments/", views.comments, name='comments'),
        )
    elif item['template'] != "" and item['template'] != "#":
        urlpatterns.append(
            path(item['slug'] + "/", eval("views." + item['template']), name=item['template']),
        )

# urlpatterns = [
    
#     path('', views.home, name='home'),

#     path('about_us/', views.about_us, name='about_us'),
#     path('about_us/our_team/', views.our_team, name='our_team'),
#     path('about_us/our_team/<slug:slug>/', views.team_member, name='team_member'),

#     path('service_list/', views.service_list, name='service_list'),
#     path('service_list/<slug:slug>/', views.service_detail, name='service_detail'),
#     path('service_list/<slug:slug>/comments/', views.comments, name='comments'),

#     path('review/', views.review, name='review'),
# ]
