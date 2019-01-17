from django.db import models

# Create your models here.

class CompanySector(models.Model):
    sector_code = models.CharField(primary_key=True, max_length=10)
    sector_name = models.CharField(max_length=50)
    sector_desc = models.TextField(null=True,blank=True)

    def __str__(self):
        return '%s'%(self.sector_name)

class Company(models.Model):
    company_sector = models.ForeignKey(CompanySector, related_name='fk_companysectors_to_company', on_delete=models.CASCADE)
    company_code = models.CharField(primary_key=True, max_length=10)
    company_name = models.CharField(max_length=50)
    company_desc = models.TextField(null=True,blank=True)
    company_url = models.URLField()
    company_logo = models.ImageField(null=True,blank=True)


    def __str__(self):
        return '%s'%(self.company_name)


class FinancialStatement(models.Model):
    company = models.ForeignKey(Company, related_name='fk_companys_to_financialstatement', on_delete=models.CASCADE)
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
    earnings_per_share = models.FloatField()
    dividend_payment = models.BigIntegerField()
    stock_price = models.IntegerField()
    exchange_rate_rupiah_dollar = models.IntegerField()

    def __str__(self):
        return '%s %s'%(self.company, self.year)

    # Liquidity Ratio (cash_ratio, quick_acid_ratio, current_ratio)
    def cash_ratio(self):
        cash_ratio = (self.cash/self.current_liabilities)*100
        return (round(cash_ratio,2)) #%

    def quick_acid_ratio(self):
        quick_acid_ratio = ((self.current_asset-self.inventory)/self.current_liabilities)*100
        return (round(quick_acid_ratio,2)) #%

    def current_ratio(self):
        current_ratio = (self.current_asset/self.current_liabilities)*100
        return (round(current_ratio,2)) #%

    # Solvability Ratio (debt_to_asset, debt_to_equity, long_term_debt_to_equity, coverage_ratio)
    def debt_to_asset(self):
        debt_to_asset = (self.total_liabilities/self.total_asset)*100
        return (round(debt_to_asset,2)) #%

    def debt_to_equity(self):
        debt_to_equity = (self.total_liabilities/self.total_equity)*100
        return (round(debt_to_equity,2)) #%

    def long_term_debt_to_equity(self):
        long_term_debt_to_equity = (self.long_term_liabilities/self.total_equity)*100
        return (round(long_term_debt_to_equity,2)) #%

    def coverage_ratio(self):
        coverage_ratio = (self.operating_profit/self.interest_expense)*100
        return (round(coverage_ratio,2)) #%

    # Profitability Ratio (return_on_equity, return_on_asset, gross_profit_margin, operating_profit_margin, net_profit_margin)
    def return_on_equity(self):
        return_on_equity = (self.net_profit/self.total_equity)*100
        return (round(return_on_equity,2)) #%

    def return_on_asset(self):
        return_on_asset = (self.net_profit/self.total_asset)*100
        return (round(return_on_asset,2)) #%

    def gross_profit_margin(self):
        gross_profit_margin = (self.gross_profit/self.total_revenue)*100
        return (round(gross_profit_margin,2)) #%

    def operating_profit_margin(self):
        operating_profit_margin = (self.operating_profit/self.total_revenue)*100
        return (round(operating_profit_margin,2)) #%

    def net_profit_margin(self):
        net_profit_margin = (self.net_profit/self.total_revenue)*100
        return (round(net_profit_margin,2)) #%

    # Market Ratio (price_earning_ratio, price_to_book_value, dividend_per_share, dividend_yield, dividend_payout_ratio)
    def price_earning_ratio(self):
        price_earning_ratio = self.stock_price/self.earnings_per_share
        return (round(price_earning_ratio,2))

    def price_to_book_value(self):
        book_value = self.total_equity/self.outstanding_share
        price_to_book_value = self.stock_price/book_value
        return (round(price_to_book_value,2))

    def dividend_per_share(self):
        dividend_per_share = self.dividend_payment/self.outstanding_share
        return (round(dividend_per_share,2))

    def dividend_yield(self):
        dividend_per_share = self.dividend_payment/self.outstanding_share
        dividend_yield = (dividend_per_share/self.stock_price)*100
        return (round(dividend_yield,2)) #%

    def dividend_payout_ratio(self):
        dividend_per_share = self.dividend_payment/self.outstanding_share
        dividend_payout_ratio = (dividend_per_share/self.earnings_per_share)*100
        return (round(dividend_payout_ratio,2)) #%

    # Turnover Ratio (total_asset_turnover, working_capital_turnover, fixed_asset_turnover, inventory_turnover)
    def total_asset_turnover(self):
        total_asset_turnover = self.total_revenue/self.total_asset
        return (round(total_asset_turnover,2))

    def working_capital_turnover(self):
        working_capital_turnover = self.total_revenue/(self.current_asset-self.current_liabilities)
        return (round(working_capital_turnover,2))

    def fixed_asset_turnover(self):
        fixed_asset_turnover = self.total_revenue/self.fixed_asset
        return (round(fixed_asset_turnover,2))

    def inventory_turnover(self):
        inventory_turnover = self.total_revenue/self.inventory
        return (round(inventory_turnover,2))
