import json
from django.db.utils import IntegrityError
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from stage.models import StageData


def setStage(request):
    data = json.loads(request.body)
    try:
        q = StageData(ipAddress=data['ipAddress'], stageName_id=data['stageName'], placeName=data['placeName'])
        q.save()
        return HttpResponse('Success')
    except IntegrityError:
        return HttpResponseBadRequest('Stage already allocated or No such stage')


def getStage(request):
    ipAddress = request.META.get('REMOTE_ADDR')
    try:
        q = StageData.objects.get(ipAddress=ipAddress)
        return JsonResponse({'stageName': q.stageName.line_code, 'placeName': q.placeName})
    except StageData.DoesNotExist:
        return HttpResponseBadRequest('Stage not allocated to this PC')


def deleteStage(request):
    try:
        q = StageData.objects.get(ipAddress__exact=request.body.decode('unicode-escape'))
        q.delete()
        return HttpResponse('Success')
    except StageData.DoesNotExist:
        return HttpResponseBadRequest('Server error occurred')


def listStage(request):
    try:
        stageList = []
        for e in StageData.objects.all():
            stageList.append({'ipAddress': e.ipAddress, 'stageName': e.stageName.line_code, 'placeName': e.placeName})
        return JsonResponse(stageList, safe=False)
    except StageData.DoesNotExist:
        return HttpResponseBadRequest('Server error occurred')
