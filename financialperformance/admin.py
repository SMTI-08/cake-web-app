from django.contrib import admin
from .models import SektorPerusahaan, Perusahaan, LaporanKeuangan

# Register your models here.

class SektorPerusahaanAdmin(admin.ModelAdmin):
    list_display = ['kd_sektor','nama_sektor','deskripsi_sektor']
    list_per_page = 25
admin.site.register(SektorPerusahaan, SektorPerusahaanAdmin)

class PerusahaanAdmin(admin.ModelAdmin):
    list_display = ['kd_sektor','kd_perusahaan','nama_perusahaan','deskripsi_perusahaan']
    list_per_page = 25
admin.site.register(Perusahaan, PerusahaanAdmin)

class LaporanKeuanganAdmin(admin.ModelAdmin):
    list_display = ['id','kd_perusahaan','year','cash','inventory','current_asset','fixed_asset',
                    'total_asset','current_liabilities','long_term_liabilities','total_liabilities',
                    'outstanding_share','total_equity','total_revenue','gross_profit','operating_profit',
                    'interest_expense','net_profit','earnings_per_share','dividend_payment','stock_price',
                    'kurs_rupiah_dollar']
    list_per_page = 25
admin.site.register(LaporanKeuangan, LaporanKeuanganAdmin)
