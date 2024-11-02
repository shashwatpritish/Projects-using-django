from django.shortcuts import render, redirect
from App1.models import Note

# Create your views here.
def home(request):
    if request.method == 'POST':
        note = request.POST.get('note')
        new_note = Note(note=note)
        new_note.save()
    notes = Note.objects.filter().all()
    notes_dict = {'notes': notes}
    return render(request, 'index.html',notes_dict)

def delete(request, note):
    Note.objects.filter(note=note).delete()
    return redirect('/')
def update(request, note):
    if request.method == 'POST':
        new_note = request.POST.get('note')
        Note.objects.filter(note=note).update(note=new_note)
        return redirect('/')
    notedict = {'note': note}
    return render(request, 'update.html', notedict)

def handling_404(request, exception):
    return render(request, '404.html')