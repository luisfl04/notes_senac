from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from .models import Note
from .form import NoteForm


@login_required(login_url = "/contas/login/")
def notas_para_fazer(request):

    notes = Note.objects.filter(done = False)
    notes_finalizadas = Note.objects.filter(done = True)
    template = "card/index.html"
    context = {
        "notes": notes,
        "notes_finalizadas": notes_finalizadas,
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
        "action": "Create",
    }
    return render(request, template, context)

@login_required(login_url = "/contas/login/")
def update(request, note_id):

    note = Note.objects.get( pk = note_id)
    form = NoteForm(request.POST or None, instance = note)

    if request.method == "POST" and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse("card:index"))
    
    template = "card/new.html"
    context = {
        "form": form,
        "action": "To edite",
    }
    return render(request, template, context)

@login_required(login_url= "contas/login/")
def delete(request, note_id):
    note = Note.objects.get( pk = note_id)
    note.delete()
    return HttpResponseRedirect(reverse("card:index"))

@login_required(login_url = "/contas/login/")
def done(request, note_id):
    note = Note.objects.get( pk = note_id)
    note.make_done()
    return HttpResponseRedirect(reverse("card:index"))        
        
        




                            