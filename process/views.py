import json
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.utils import timezone
from process.models import ProcessCard, Process


def create(request):
    data = json.loads(request.body)
    if Process.objects.all().filter(processNo=data['processNo']).exists():
        return HttpResponseBadRequest('Process Already exists')

    stages = data['processId']
    q = Process(processNo=data['processNo'], date=timezone.now(), currentQuantity=0, maxQuantity=data['maxQuantity'],
                productCode_id=data['productCode'],
                tempStartingSno=data['tempStartingSno'], tempEndingSno=data['tempEndingSno'],
                permStartingSno=data['permStartingSno'], permEndingSno=data['permEndingSno'])
    q.save()
    for i in range(0, len(stages)):
        q = ProcessCard(processCardNo=data['processNo'] + stages[i], processNo_id=data['processNo'],
                        stageName_id=data['processId'][i], start=data['start'][i], end=data['end'][i], qa=data['qa'][i],
                        rework=data['rework'][i], final=data['final'][i], quantity=0)
        q.save()
    return HttpResponse('Success')


def get(request):
    return JsonResponse(list(Process.objects.values()), safe=False)


def card(request):
    data = json.loads(request.body)
    return JsonResponse(list(ProcessCard.objects.filter(processNo_id=data['processNo']).values()), safe=False)


def delete(request):
    data = json.loads(request.body)
    try:
        q = Process.objects.get(processNo=data['processNo'])
        q.delete()
        return HttpResponse('Success')
    except Process.DoesNotExist:
        return HttpResponseBadRequest('Failed to delete')