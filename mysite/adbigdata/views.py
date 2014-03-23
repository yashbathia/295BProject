from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from adbigdata.models import advertiser
# Create your views here.
def index(request):
    return render(request,'login.html')


def adv_reg(request):
    return render(request,'advertiser_registration.html')

def eOrg_reg(request):
    return render(request,'eventOrganizer_registration.html')



def detail(request, adv_name):
    return HttpResponse("You're looking at Advertiser %s." % adv_name)
