import json

from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse

from auth.models import UserData


def login(request):
    data = json.loads(request.body)
    try:
        user = UserData.objects.get(username__exact=data['username'])
        return JsonResponse({'access': user.access, 'username': data['username']}) if data['password'] == user.password \
            else HttpResponseBadRequest('Check credentials')
    except UserData.DoesNotExist:
        return HttpResponseBadRequest('User does not exist')


def register(request):
    data = json.loads(request.body)
    try:
        newUser = UserData(username=data['username'], password=data['password'], access=data['access'],
                           userCode=data['userCode'])
        newUser.save()
        return HttpResponse('User registered successfully')
    except ValueError:
        return HttpResponseBadRequest('ValueError')


def delete(request):
    data = json.loads(request.body)
    try:
        user = UserData.objects.get(username__exact=data['username'])
        user.delete()
        return HttpResponse('User deleted successfully')
    except UserData.DoesNotExist:
        return HttpResponseBadRequest('User does not exist')
