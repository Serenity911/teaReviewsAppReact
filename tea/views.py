from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from tea.models import *
from tea.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import TeaSerializer

# Create your views here.
class TeaView(viewsets.ModelViewSet):
    serializer_class = TeaSerializer
    queryset = Tea.objects.all()


# def teas_index(request):
#     # reviews = Review.object.all()
#     teas = Tea.objects.all()
#     return render(request, "tea/index.html", locals())

# @login_required
# def tea_new(request):
#     if request.method == "POST":
#         form = TeaForm(request.POST)
#         if form.is_valid():
#             tea = form.save(commit = False)
#             tea.save()
#             return redirect('teas_index')
#     else:
#         form = TeaForm()
#         return render(request, 'tea/tea_form.html', {'form': form})

