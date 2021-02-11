from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required


from subconta.models import Subconta
from .models import Conta

from .forms import ContaForm

@login_required
def conta(request):
	subconta = Subconta.objects.all()
	conta = Conta.objects.all().order_by('conta')
	return render(request,'conta/conta.html',{'conta':conta,'subconta':subconta})

 
@login_required 
def contaAdd(request):
	if request.method == 'POST':
		form = ContaForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('subcontaAdd')
	else:		
		form = ContaForm()
	return render(request, 'conta/contaAdd.html',{'form':form})