from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from django.db.models import Q, Sum, Min, Max, Avg
from django.contrib import messages



from .models import Banco


from .forms import BancoForm

@login_required
def banco(request):
    banco_list = Banco.objects.all().order_by('banco')

    paginator = Paginator(banco_list, 10)

    page = request.GET.get('page')

    banco = paginator.get_page(page)

    query = request.GET.get('q')
    if query:
        banco = Contas.objects.filter(
            Q(banco__icontains=query) 
            ).distinct()
    return render(request, 'banco/banco.html',{'banco': banco})

@login_required
def bancoView(request, id):
    banco = get_object_or_404(Banco, pk=id)
    return render(request, 'banco/bancoView.html',{'banco':banco})
    
@login_required
def bancoAdd(request):  
    if request.method == 'POST':
        form = BancoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('http://127.0.0.1:8000/banco/')
    else:
        form = BancoForm()
    return render(request, 'banco/bancoAdd.html',{'form':form})

@login_required
def bancoEdit(request, id):
    banco = get_object_or_404(Banco, pk=id)
    form = BancoForm(instance=banco)
    if (request.method == 'POST'):
        form = BancoForm(request.POST, instance=banco)
        if form.is_valid():
            banco.save()
            return redirect('banco')
        else:
            return render(request, 'banco/bancoEdit.html',{'form':form, 'banco':banco})
    else:
        return render(request, 'banco/bancoEdit.html',{'form':form, 'banco':banco})