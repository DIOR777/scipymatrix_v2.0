from django.shortcuts import render
from django.http import HttpResponse
import matrixalg
import json
 
# Create your views here.
def index(request):
    n = request.GET.get('size')
    if n.isdigit() == False:
        return HttpResponse('Size must be integer', status=400)
    return HttpResponse(json.dumps(matrixalg.main(n), indent=4, ensure_ascii=False), content_type = 'application/json')