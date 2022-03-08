from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponse, FileResponse
from django.shortcuts import render, get_object_or_404, redirect

from .forms import *
from .models import *
from .scripts import *


@login_required
def index(request: HttpRequest) -> HttpResponse:

    documents = Document.objects.filter(creator=request.user)

    if request.method == "POST":

        form = UploadDocumentForm(request, data=request.POST, files=request.FILES)
        # https://stackoverflow.com/questions/15885201/django-uploads-discard-uploaded-duplicates-use-existing-file-md5-based-check
        if form.is_valid():

            form.save()
    else:
        form = UploadDocumentForm(request)

    return render(
        request,
        "documents/index.html",
        {"documents": documents, "form": form},
    )

@login_required
def download(request: HttpRequest, document_id: int) -> FileResponse:
    document = get_object_or_404(Document, id=document_id)
    return FileResponse(document.file, as_attachment=True, filename=document.title)


@login_required
def delete(request: HttpRequest, document_id: int) -> HttpResponse:
    document = get_object_or_404(Document, id=document_id)
    document.delete()
    return redirect("documents:index")
