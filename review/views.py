from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from review.models import *
from review.forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from rest_framework import viewsets
from .serializers import ReviewSerializer



# Create your views here.
class ReviewView(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    queryset = Review.objects.all()

# def reviews_index(request):
#     reviews = Review.objects.all()
#     return render(request, "review/index.html", locals())

# @login_required
# def review_new(request):
#     if request.method == "POST":
#         form = ReviewForm(request.POST)
#         print(form)
#         if form.is_valid():
#             review = form.save(commit = False)
#             review.username = request.user.username
#             review.save()
#             return redirect('reviews_index')
#         else:
#             print(form)

#     else:
#         username = request.user.username
#         form = ReviewForm()
#         return render(request, 'review/review_form.html', {'form': form})


# # @login_required
# # def user_logout(request):
# #     logout(request)
# #     return redirect('reviews_index')

# def register(request):
#     registered = False
#     if request.method == "POST":
#         user_form = UserForm(data=request.POST)
#         profile_form = UserProfileInfoForm(data=request.POST)
#         if user_form.is_valid() and profile_form.is_valid():
#             user = user_form.save()
#             user.set_password(user.password)
#             user.save()
#             profile = profile_form.save(commit=False)
#             profile.user = user
#             profile.save()
#             registered = True
#             return redirect('reviews_index')
#         else:
#             print(user_form.errors, profile_form.errors)
#     else:
#         form = UserForm()
#         profile_form = UserProfileInfoForm()
#         return render(request, 'authentication/register.html', {'form': form})

# def user_login(request):
#     if request.method == "POST":
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active():
#                 login(request,user)
#                 return redirect('tea_new')
#         else:
#             print("Someone tried to login and failed.")
#             print("They used username: {} and password: {}".format(username,password))
#             return HttpResponse("Invalid login details given")
#     else:
#         return render(request, 'authentication/login.html', {})