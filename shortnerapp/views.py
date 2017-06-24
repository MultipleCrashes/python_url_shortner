from django.http import HttpResponse
# Create your views here.stm
from utils import *
from .models import *
import json
from django.views import *


def get_short_url(request):
    response_dict = {"response_string":"","response_code":0}
    req = request.POST.get('long_url')
    print req
    print type(req)
    print "Request sent from postman",req
    utils_obj = Utilities()
    short_url = utils_obj.get_url_hash(input_url=req)
    print "Short url",short_url
    try:
        short_url = str('http://metarain.com/')+str(short_url)
        response_dict["response_string"]=short_url
        response_dict["response_code"]= 200
        mapper_obj = UrlMapper(long_url=str(req),short_url=str(short_url))
        mapper_obj.save()
    except Exception,e:
        print "Exception found while storing the value in db",str(e)
        response_dict["response_string"]=str(e)
        response_dict["response_code"]= 400
    print "response str",response_dict
    return HttpResponse(json.dumps(response_dict))


def get_long_url(request):
    response_dict = {"response_string":"","respoonse_code":0}
    req = request.POST.get('short_url')
    hash_value = req.split('/')[-1]
    try:
        long_url = UrlMapper.objects.filter(
                    short_url__contains=hash_value).values('long_url')
        response_dict["response_string"] = str(long_url)
        response_dict["response_code"]= 200
    except Exception,e:
        print "Exception found while getting url",str(e)
        response_dict["response_string"] = str(e)
        response_dict["response_code"]=404
    return HttpResponse(json.dumps(response_dict))











