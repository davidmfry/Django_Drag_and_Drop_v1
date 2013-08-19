from django.shortcuts import render_to_response, RequestContext
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponse
import logging
from .models import UploadFormModel
from .forms import UploadForm

logger = logging.getLogger('draganddrop.views')

def home(request):
    form = UploadForm(request.POST or None)
    if form.is_valid():
        new_upload = form.save(commit = False)
        new_upload.save()
    return render_to_response('upload/home.html', locals(), context_instance = RequestContext(request))

@csrf_exempt
def posted(request):
    data = json.loads(request.raw_post_data)
    #try:
    #    data = json.loads(request.raw_post_data)
    #    print "** THIS IS THE DATA" + str(data)
    #except Exception:
    #    pass
    
    logger.debug("data_object = %s" % str(data))
    instance = UploadFormModel(**data) 
    form = UploadForm(instance = instance)
    
    json_response = {}
    
    if form.is_valid():
        new_upload = form.save(commit = False)
        new_upload.save()
        json_response['success'] = True
    else:
        json_response['success'] = "Did not make it"
        
        
    logger.debug("json response = %s" % str(json_response))
    
    return HttpResponse(json.dumps(json_response)) 

