from django.shortcuts import render

# Create your views here.

def budgetPage(request):
    return render(request,'budget.html')
