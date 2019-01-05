from django.contrib import admin
from .models import CompanySector, Company, FinancialStatement

# Register your models here.

class CompanySectorAdmin(admin.ModelAdmin):
    list_display = ['sector_code','sector_name','sector_desc']
    list_per_page = 25
admin.site.register(CompanySector, CompanySectorAdmin)

class CompanyAdmin(admin.ModelAdmin):
    list_display = ['company_sector','company_code','company_name','company_desc']
    list_per_page = 25
admin.site.register(Company, CompanyAdmin)

class FinancialStatementAdmin(admin.ModelAdmin):
    list_display = ['id','company','year','cash','inventory','current_asset','fixed_asset',
                    'total_asset','current_liabilities','long_term_liabilities','total_liabilities',
                    'outstanding_share','total_equity','total_revenue','gross_profit','operating_profit',
                    'interest_expense','net_profit','earnings_per_share','dividend_payment','stock_price',
                    'exchange_rate_rupiah_dollar']
    list_per_page = 25
admin.site.register(FinancialStatement, FinancialStatementAdmin)
