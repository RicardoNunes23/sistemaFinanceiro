from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from conta.models import Conta
from .models import Subconta

from .forms import SubcontaForm

@login_required
def subconta(request):
    conta = Conta.objects.all()
    subconta = Subconta.objects.all().order_by('conta')
    return render(request, 'subconta/subconta.html',{'subconta': subconta,'conta':conta})  
    
@login_required
def subcontaAdd(request):  
    conta = Conta.objects.all() 
    if request.method == 'POST':
       form = SubcontaForm(request.POST, request.FILES)
       
       if form.is_valid():
           form.save()
           return redirect('subconta')
    else:
        form = SubcontaForm()
    return render(request, 'subconta/subcontaAdd.html',{'form':form, 'conta':conta}) 

@login_required
def subcontaEdit(request, id):
    subconta = get_object_or_404(Subconta, pk=id)
    form = SubcontaForm(instance=subconta)
    if (request.method == 'POST'):
        form = SubcontaForm(request.POST, instance=subconta)
        if (form.is_valid()):
            form.save()
            return redirect('subconta')
        else:
            return render(request, 'subconta/subcontaEdit.html',{'form':form})   
    else:
        return render(request, 'subconta/subcontaEdit.html',{'form':form})


@login_required
def subcontaDel(request, id):
    subconta = get_object_or_404(Subconta, pk=id) 
    subconta.delete()  
    return redirect('subconta')

