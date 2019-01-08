from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanySector, Company, FinancialStatement
from django.db.models import Q

# Create your views here.

def company_analysis_view(request):
    financialdata = FinancialStatement.objects.all()
    if 'q' in request.GET:
        q = request.GET['q']
        companyfilter = FinancialStatement.objects.filter(Q(company__company_code__icontains=q))
        context = {
            "financialdata":financialdata,
            "companyfilter":companyfilter,
        }
        template = 'financialperformance/company_analysis_result.html'
        return render(request, template, context)
    else:
        context = {
            "financialdata":financialdata,
        }
        template = 'financialperformance/company_analysis_select.html'
        return render(request, template, context)


def company_comparison_view(request):
    financialdata = FinancialStatement.objects.all()
    if 'q' in request.GET:
        q = request.GET.getlist('q')
        companyfilter = FinancialStatement.objects.filter(company__in=q)
        context = {
            "financialdata":financialdata,
            "companyfilter":companyfilter,
        }
        template = 'financialperformance/company_comparison_result.html'
        return render(request, template, context)
    else:
        context = {
            "financialdata":financialdata,
        }
        template = 'financialperformance/company_comparison_choose.html'
        return render(request, template, context)
