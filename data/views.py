import json

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
from .models import Line, Product, Rejection, Rework


def line_get(request):
    lines = Line.objects.all()
    data = [{'line_code': line.line_code, 'line_description': line.line_description} for line in lines]
    return JsonResponse(data, safe=False)


def line_set(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        line_code = data['line_code']
        line_description = data['line_description']
        line = Line(line_code=line_code, line_description=line_description)
        line.save()
        return HttpResponse('success')
    else:
        return HttpResponseBadRequest({'status': 'error', 'message': 'Invalid request method'})


def line_delete(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        line_code = data['line_code']
        line = Line.objects.filter(line_code=line_code).first()
        if line:
            line.delete()
            return HttpResponse('success')
        else:
            return HttpResponseBadRequest('Line not found')
    else:
        return HttpResponseBadRequest('Invalid request method')


def product_get(request):
    products = Product.objects.all()
    data = [{'productCode': product.product_code, 'FgCode': product.fg_code, 'productDesc': product.product_description,
             'processId': product.processId} for product in products]
    return JsonResponse(data, safe=False)


def product_set(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        product_code = data['productCode']
        fg_code = data['FgCode']
        product_description = data['productDesc']
        process_id = data['processId']
        product = Product(product_code=product_code, fg_code=fg_code, product_description=product_description,
                          processId=process_id)
        product.save()
        return HttpResponse('success')
    else:
        return HttpResponseBadRequest('Invalid request method')


def product_delete(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        product_code = data['productCode']
        product = Product.objects.filter(product_code=product_code).first()
        if product:
            product.delete()
            return HttpResponse({'status': 'success'})
        else:
            return HttpResponseBadRequest('Product not found')
    else:
        return HttpResponseBadRequest('Invalid request method')


def rejection_get(request):
    rejections = Rejection.objects.all()
    data = [{'rejection_code': rejection.rejection_code, 'rejection_description': rejection.rejection_description} for rejection in rejections]
    return JsonResponse(data, safe=False)


def rejection_set(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        rejection_code = data['rejection_code']
        rejection_description = data['rejection_description']
        rejection = Rejection(rejection_code=rejection_code, rejection_description=rejection_description)
        rejection.save()
        return HttpResponse('success')
    else:
        return HttpResponseBadRequest('Invalid request method')


def rejection_delete(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        rejection_code = data['rejection_code']
        rejection = Rejection.objects.filter(rejection_code=rejection_code).first()
        if rejection:
            rejection.delete()
            return HttpResponse('success')
        else:
            return HttpResponseBadRequest('Rejection not found')
    else:
        return HttpResponseBadRequest('Invalid request method')


def rework_get(request):
    reworks = Rework.objects.all()
    data = [{'rework_code': rework.rework_code, 'rework_description': rework.rework_description} for rework in reworks]
    return JsonResponse(data, safe=False)


def rework_set(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        rework_code = data['rework_code']
        rework_description = data['rework_description']
        rework = Rework(rework_code=rework_code, rework_description=rework_description)
        rework.save()
        return HttpResponse('success')
    else:
        return HttpResponseBadRequest('Invalid request method')


def rework_delete(request):
    data = json.loads(request.body)
    if request.method == 'POST':
        rework_code = data['rework_code']
        rework = Rework.objects.filter(rework_code=rework_code).first()
        if rework:
            rework.delete()
            return HttpResponse('success')
        else:
            return HttpResponseBadRequest('Rework not found')
    else:
        return HttpResponseBadRequest('Invalid request method')
