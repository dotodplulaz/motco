from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect,FileResponse, JsonResponse
from django.http import Http404
from django.contrib import messages

from .models import *
from django.contrib.sessions.models import Session
from datetime import timezone, datetime, timedelta

from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.conf import settings
import os

from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth.forms import PasswordResetForm

from django.core.files.storage import FileSystemStorage



from django.views.generic.base import TemplateView
from django.views.generic import View



def home(request):
    return render(request,'login.html')


def index(request):
    return render(request,'index.html')
