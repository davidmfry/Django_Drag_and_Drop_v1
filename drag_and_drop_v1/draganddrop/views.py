from django.shortcuts import render_to_response, RequestContext
import simplejson
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

def posted(request):
    try:
        data = json.loads(request.raw_post_data)
        
    except Exception:
        pass
    
    logger.debug("data_object = %s" % str(data))
    
    form = UploadForm(request.POST or None)
    
    if form.is_valid():
        new_upload = form.save(commit = False)
        new_upload.save()
    return render_to_response('upload/home.html', locals(), context_instance = RequestContext(request))

