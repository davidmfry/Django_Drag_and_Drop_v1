from django.shortcuts import render_to_response, RequestContext

from .models import UploadFormModel
from .forms import UploadForm

def home(request):
    form = UploadForm(request.POST or None)
    if form.is_valid():
        new_upload = form.save(commit = False)
        new_upload.save()
    return render_to_response('upload/home.html', locals(), context_instance = RequestContext(request))
