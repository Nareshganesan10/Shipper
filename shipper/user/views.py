from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse
from rest_framework.decorators import api_view
from user.models import UserModel
from user.serializers import UserSerializer

@csrf_exempt
def index(request):
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    return HttpResponse(serializer.data)


@csrf_exempt
@api_view(["POST"])
def signup(request):
    if request.method == "POST":
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            if request.POST.get("password") != request.POST.get("password1"):
                serializer.save()
                request.session["user"] = request.POST.get("username")
                return HttpResponse("User created succesfully!!!!")
            else:
                return HttpResponse("Reconfirm the password")
        else:
            return HttpResponse(serializer.errors, "recheck you input data")
    return HttpResponse("Wrong request")



@csrf_exempt
@api_view(["GET", "POST"])
def signin(request):
    if request.method == "POST" and UserModel.objects.filter(username=request.POST.get("username")).values_list("username", "password").exists():
        request.session["user"] = request.POST.get("username")
        return HttpResponse("succesfully logged in")
    else:
        return HttpResponse("Incorrect creds")
    


@csrf_exempt
@api_view(["GET"])
def signout(request):
    print(request.session['user'])
    if request.session['user'] == "":
        return HttpResponse("user alreayd signed out, signin again")
    request.session['user'] = ""
    return HttpResponse("logged out")