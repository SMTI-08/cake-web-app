from django.db import models

# Create your models here.

class SektorPerusahaan(models.Model):
    kd_sektor = models.CharField(primary_key=True, max_length=10)
    nama_sektor = models.CharField(max_length=50)
    deskripsi_sektor = models.TextField()

    def __str__(self):
        return '%s %s'%(self.kd_sektor, self.nama_sektor)

class Perusahaan(models.Model):
    kd_sektor = models.ForeignKey(SektorPerusahaan, related_name='fk_sektor_perusahaan', on_delete=models.CASCADE)
    kd_perusahaan = models.CharField(primary_key=True, max_length=10)
    nama_perusahaan = models.CharField(max_length=50)
    deskripsi_perusahaan = models.TextField()

    def __str__(self):
        return '%s %s'%(self.kd_perusahaan, self.nama_perusahaan)

class LaporanKeuangan(models.Model):
    kd_perusahaan = models.ForeignKey(Perusahaan, related_name='fk_perusahaan', on_delete=models.CASCADE)
    year = models.CharField(max_length=4, choices=(('2017','2017'), ('2016','2016'), ('2015','2015'), ('2014','2014'), ('2013','2013')))
    cash = models.BigIntegerField()
    inventory = models.BigIntegerField()
    current_asset = models.BigIntegerField()
    fixed_asset = models.BigIntegerField()
    total_asset = models.BigIntegerField()
    current_liabilities = models.BigIntegerField()
    long_term_liabilities = models.BigIntegerField()
    total_liabilities = models.BigIntegerField()
    outstanding_share = models.BigIntegerField()
    total_equity = models.BigIntegerField()
    total_revenue = models.BigIntegerField()
    gross_profit = models.BigIntegerField()
    operating_profit = models.BigIntegerField()
    interest_expense = models.BigIntegerField()
    net_profit = models.BigIntegerField()
    earnings_per_share = models.IntegerField()
    dividend_payment = models.BigIntegerField()
    stock_price = models.IntegerField()
    kurs_rupiah_dollar = models.IntegerField()

    def __str__(str):
        return '%s %s'%(self.kd_perusahaan, self.year)
