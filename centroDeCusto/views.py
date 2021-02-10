from django.shortcuts import render, redirect, get_object_or_404
from .models import CentroDeCusto
from .forms import CentroDeCustoForm

# Create your views here.
def centroDeCusto(request):
	centroDeCusto = CentroDeCusto.objects.all().order_by('centroDeCusto')
	return render (request, 'centroDeCusto/centroDeCusto.html',{'centroDeCusto':centroDeCusto}) 

def centroDeCustoAdd(request):
	if request.method == 'POST':
		form = CentroDeCustoForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('centroDeCusto')
	else:		
		form = CentroDeCustoForm()
	return render(request, 'centroDeCusto/centroDeCustoAdd.html',{'form':form})



		