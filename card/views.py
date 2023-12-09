from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Note
from .form import NoteForm


@login_required(login_url = "/contas/login/")
def index(request):
    notes = Note.objects.all()
    template = "card/index.html"
    context = {
        "notes": notes
    }
    return render(request, template, context)

@login_required(login_url = "/contas/login/")
def create(request):
    form = NoteForm(request.POST or None)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("card:index"))
    
    template = "card/new.html"
    context = {
        "form": form,
        "action": "Create"
    }
    return render(request, template, context)
