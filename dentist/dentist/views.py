from django.http import HttpResponse
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, CreateView
from dentist.models import Service


def home(request):
    return render(
        request,
        'dentist/home.html',
    )


# ------ about us

def about_us(request):
    return render(
        request,
        'dentist/about_us.html',
    )


def our_team(request):
    return render(
        request,
        'dentist/our_team.html',
    )


def team_member(request):
    return render(
        request,
        'dentist/team_member.html',
    )


# ------ services

def service_list(request):
    object_list = Service.objects.all()
    return render(
        request,
        'dentist/service_list.html',
        context={'object_list': object_list},
    )


def service_detail(request, slug):
    service = Service.objects.get(slug=slug)
    return render(
        request,
        'dentist/service_detail.html',
        context={'service': service}
    )


def comments(request):
    return render(
        request,
        'dentist/index.html',
    )


def review(request):
    return render(
        request,
        'dentist/index.html',
    )


