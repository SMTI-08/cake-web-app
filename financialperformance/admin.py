from django.contrib import admin
from .models import CompanySector, Company, FinancialStatement

# Register your models here.

class CompanySectorAdmin(admin.ModelAdmin):
    list_display = ['sector_name','sector_code','sector_desc','sector_image']
    list_per_page = 25

    def get_queryset(self, request):
        queryset = super(CompanySectorAdmin, self).get_queryset(request)
        queryset = queryset.order_by('sector_name')
        return queryset

admin.site.register(CompanySector, CompanySectorAdmin)


class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_name','company_code','company_sector','company_url','company_logo']
    list_filter = ['company_sector',]
    list_per_page = 25

    def get_queryset(self, request):
        queryset = super(CompanyAdmin, self).get_queryset(request)
        queryset = queryset.order_by('company_name')
        return queryset

admin.site.register(Company, CompanyAdmin)


class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ['company','year','cash','inventory','current_asset','fixed_asset',
                    'total_asset','current_liabilities','long_term_liabilities','total_liabilities',
                    'outstanding_share','total_equity','total_revenue','gross_profit','operating_profit',
                    'interest_expense','net_profit','earnings_per_share','dividend_payment','stock_price',
                    'exchange_rate_rupiah_dollar']
    list_filter = ['year',]
    list_per_page = 25

    def get_queryset(self, request):
        queryset = super(FinancialStatementAdmin, self).get_queryset(request)
        queryset = queryset.order_by('company')
        return queryset

admin.site.register(FinancialStatement, FinancialStatementAdmin)
