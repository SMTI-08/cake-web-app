from django.shortcuts import render
from django.http import HttpResponse
from .models import CompanySector, Company, FinancialStatement
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.

def main_dashboard_view(request):
    companydata = Company.objects.all()
    sectordata = CompanySector.objects.all()
    context = {
        "companydata": companydata,
        "sectordata": sectordata,
    }
    template = 'financialperformance/main_dashboard.html'
    return render(request, template, context)


def company_dashboard_view(request):
    sectordata = CompanySector.objects.all()

    companydata = Company.objects.all()
    paginator = Paginator(companydata, 5)
    page = request.GET.get('page')
    companylist = paginator.get_page(page)

    context = {
        "companylist":companylist,
        "companydata": companydata,
        "sectordata": sectordata,
    }
    template = 'financialperformance/company_dashboard.html'
    return render(request, template, context)


def sector_dashboard_view(request):
    companydata = Company.objects.all()

    sectordata = CompanySector.objects.all()
    paginator = Paginator(sectordata, 5)
    page = request.GET.get('page')
    sectorlist = paginator.get_page(page)

    context = {
        "sectorlist": sectorlist,
        "companydata": companydata,
        "sectordata": sectordata,
    }
    template = 'financialperformance/sector_dashboard.html'
    return render(request, template, context)


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
