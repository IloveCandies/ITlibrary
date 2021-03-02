from django.shortcuts import render
from decimal import Decimal
from django.http import HttpResponseRedirect, HttpResponse
from .forms import UploadFileForm
from .models import UploadFileModel
from django.conf import settings
from django.core.files.storage import FileSystemStorage

def model_form_upload(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('http://127.0.0.1:8000/')
    else:
        form = UploadFileForm()
    return render(request, 'document_upload.html', {
        'form': form
    })
