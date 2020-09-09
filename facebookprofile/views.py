from django.shortcuts import render
from rest_framework import status
import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(["GET" , "POST", "PUT", "DELETE"])
def facebookProfile(request):
    id = request.GET.get("profile_id")
    access_token = request.GET.get("access_token"),
    gender = request.data.get("gender")
    birthday = request.data.get("birthday")

    try:
        if request.method == 'GET':
            url = "https://graph.facebook.com/v8.0/" + id + "/?access_token=" + access_token[0] +\
                  '&fields=name,birthday,email,gender'
            res = requests.get(url)
            return Response(res.json(), status=status.HTTP_201_CREATED)

        if request.method == 'POST':
            url = "https://graph.facebook.com/v8.0/111580267350628?birthday=" + birthday + "&gender=" + gender +"&access_token=" + access_token[0] + "&fields=name,birthday,email,gender"
            res = requests.post(url)
            return Response(res.json(), status=status.HTTP_201_CREATED)

        else:
          return Response("invalid", status=status.HTTP_400_BAD_REQUEST)
    except KeyError:
        return Response("Error")

