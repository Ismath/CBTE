import requests
from django.contrib.auth import authenticate, login, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.contrib import messages, auth
from django.shortcuts import render

from . import forms

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse, HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import views as auth_views

from .forms import MyForm
from .models import t_user, t_product_provider, t_products, t_consumptions, t_announcements
from .serializers import T_userSerializer, T_productSerializer, T_product_providerSerializer, T_consumptionSerializer, \
    T_announcementsSerializer
from django.contrib.auth.models import User, auth
from django.core.files.storage import default_storage


# Create your views here.


# t_user
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def t_userApi(request, id=0):
    if request.method == 'GET':
        users = t_user.objects.all()
        serializer = T_userSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = T_userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

'''def login(request):
    if request.method == 'POST':
        username = request.username
        password = request.secret
        if not t_user.objects.filter(username=username, password =password).exists():
            t_user.objects.create(**your_data)
        redirect('your-desired-url')
        else:'''

class CartItemViews(APIView):
    def patch(self, request, id=None):
        item = t_user.objects.get(user_id=id)

        serializer = T_userSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(t_user, user_id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


# t_product_provider

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def t_product_providerApi(request):
    if request.method == 'GET':
        product_provider = t_product_provider.objects.all()
        serializer = T_product_providerSerializer(product_provider, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = T_product_providerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductProvider(APIView):

    def patch(self, request, id=None):

        item = t_product_provider.objects.get(t_product_provider_id=id)

        serializer = T_product_providerSerializer(item, data=request.data, partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({"status": "success", "data": serializer.data})

        else:

            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):

        item = get_object_or_404(t_product_provider, t_product_provider_id=id)

        item.delete()

        return Response({"status": "success", "data": "Item Deleted"})


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def t_productsApi(request):
    if request.method == 'GET':
        products = t_products.objects.all()
        serializer = T_productSerializer(products, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = T_productSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductApi(APIView):
    def patch(self, request, id=None):
        item = t_products.objects.get(product_id=id)

        serializer = T_productSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(t_products, product_id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


# t_consumptions
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def t_consumptionsApi(request):
    if request.method == 'GET':
        consumptions = t_consumptions.objects.all()
        serializer = T_consumptionSerializer(consumptions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = T_consumptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ConsumptionApi(APIView):
    def patch(self, request, id=None):
        item = t_consumptions.objects.get(product_id=id)

        serializer = T_consumptionSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(t_consumptions, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


# t_announcements
@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def t_announcementsApi(request):
    if request.method == 'GET':
        announcements = t_announcements.objects.all()
        serializer = T_announcementsSerializer(announcements, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = T_announcementsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AnnouncemetAPI(APIView):
    def patch(self, request, id=None):
        item = t_announcements.objects.get(id=id)

        serializer = T_announcementsSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():

            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(t_announcements, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})


# Create your views here.
def users(request):  # pull data from third party rest api
    response = requests.get('http://127.0.0.1:8080/api/t_user')  # convert reponse data into json
    users = response.json()
    # print(users)
    # return HttpResponse("Users")
    return render(request, "users.html", {'users': users})
    pass

'''class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None '''

def my_form(request):
    if request.method == "POST":
        form = MyForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request, "Registration successful")
            return redirect("tradingapp:users")
        messages.error(request,"Unsuccessful registration. Invalid information.")
    form = MyForm()
    return render(request=request, template_name="signup.html", context={"form":form})
    #else:
       #form = MyForm()
       #return render(request, 'signup.html', {'form': form})
'''
def login_user(request):
    #form = MyForm(request.POST)
    #if form.is_valid():
    if request.method == "POST":
        username = request.POST['username']
        secret = request.POST['secret']
        user = authenticate(username=username, password=secret)
        if user is not None:
            login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request,"Bad")
            return render(request, 'users.html')

        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            message = 'You are logged in!'
            return render(request, 'home.html', {"message": message})

       # username = request.POST.get('username')
        #password = request.POST.get('secret')
        user = authenticate(username=username, password=password)
        if user is not None:

            #if user.is_active:
            login(request, user)
            message = 'You are logged in!'
            return render(request, 'home.html', {"message": message})
    else:
            form = AuthenticationForm()
            message = 'user is None!'
            return render(request, 'users.html', {"message": message})
    #return render(request, "home", {'form': form})

    return render(request, 'login_page.html') '''


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            fname = user.first_name
            messages.success(request, "Logged In Sucessfully!!")
            return render(request, "users.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')

    return render(request, "login_page.html")


def home(request):
    return render(request, 'home.html')