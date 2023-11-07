from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from dentist.models import Service, Page, Staff


def page_info(page_list, slug):
    current_page = {}
    
    for item in page_list:
        if item['template'] == slug:
            current_page = item
            break

    return current_page


def home(request):
    page_list = Page.objects.order_by('page_order').values()
    object_list = Service.objects.all().order_by('id')[:4]

    return render(
        request,
        'dentist/home.html',
        context={'object_list': object_list, 'page_list': page_list, 'page': page_info(page_list, 'home')},
    )


# ------ about us

def about(request):
    page_list = Page.objects.order_by('page_order').values()
    team_member = Staff.objects.all()
    
    return render(
        request,
        'dentist/about.html',
        context={'team_member': team_member, 'page_list': page_list, 'page': page_info(page_list, 'about')},
    )


def review(request):
    page_list = Page.objects.order_by('page_order').values()

    return render(
        request,
        'dentist/review.html',
        context={'page_list': page_list, 'page': page_info(page_list, 'review')}
    )


def our_team(request):
    return render(
        request,
        'dentist/our_team.html',
    )


def team_member(request):
    team_member = Staff.objects.all()
    return render(
        request,
        'dentist/member_list.html',
        context={'team_member': team_member},
    )


# ------ pages

def page_list(request):
    page_list = Page.objects.all()
    return render(
        request,
        'dentist/page_list.html',
        context={'page_list': page_list},
    )

def page(request, slug):
    page = Page.objects.get(slug=slug)
    return render(
        request,
        'dentist/page.html',
        context={'page': page},
    )

# ------ services

def service_list(request):
    page_list = Page.objects.order_by('page_order').values()
    object_list = Service.objects.all()

    return render(
        request,
        'dentist/service_list.html',
        context={'object_list': object_list, 'page_list': page_list, 'page': page_info(page_list, 'service_list')},
    )


def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    page_list = Page.objects.order_by('page_order').values()

    return render(
        request,
        'dentist/service_detail.html',
        context={'service': service, 'page_list': page_list, 'page': page_info(page_list, 'service_list'), 'page1': service}
    )


def comments(request):
    return render(
        request,
        'dentist/index.html',
    )

def prices(request):
    page_list = Page.objects.order_by('page_order').values()

    return render(
        request,
        'dentist/prices.html',
        context={'page_list': page_list, 'page': page_info(page_list, 'prices')},
    )

def contacts(request):
    page_list = Page.objects.order_by('page_order').values()
    
    return render(
        request,
        'dentist/contacts.html',
        context={'page_list': page_list, 'page': page_info(page_list, 'contacts')},
    )