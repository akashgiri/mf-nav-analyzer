import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connection
from .models import Fund, Stock
from . import nav_change

def show_funds_list(request):
    funds_data = {}

    distinct_funds = Fund.objects.order_by().values_list('fund_name').distinct()
    funds_list = []

    if distinct_funds:
        for fund in distinct_funds:
            fund = ''.join(fund)
            fund_object = Fund.objects.filter(fund_name=fund)[:1]
            slug = fund_object[0].slug_url
            data = {}
            data["fund"] = fund
            data["slug"] = slug
            funds_list.append(data)

    funds_data["funds_list"] = funds_list

    context = {
        'funds_data': funds_data
    }

    return render(request, "funds_info/welcome.html", context)

## View to show all stocks held by a fund
def show_all_stocks(request, page_slug):    
    #print("page_slug: ", page_slug)
    objects = Fund.objects.filter(slug_url=page_slug)
    stocks_list = []
    for obj in objects:
        stock = obj.stock_name
        stocks_list.append(stock)

    #print(stocks_list)

    context = {
        'fund_data': objects,
        'slug': objects[0].slug_url
    }
    return render(request, "funds_info/show_all_stocks.html", context)

def get_nav_change(request):
    fund_slug = request.GET.get('list')

    rows = my_custom_sql(fund_slug)
    mf_nav_change = nav_change.MutualFundNavAnalysis()
    total_change = mf_nav_change.get_nav_change(rows)
    total_change = str(total_change)

    if total_change[0] != '-':
        total_change = "+" + total_change

    return JsonResponse({"ch": total_change})
    
def my_custom_sql(fund_slug):
    cursor = connection.cursor()    
    cursor.execute("""select funds_info_fund.stock_name, stock_allocation, stock_code 
                    from funds_info_fund join funds_info_stock 
                    on funds_info_fund.stock_name = funds_info_stock.stock_name 
                    where slug_url='"""+ fund_slug +"""';""")
    rows = cursor.fetchall()

    return rows
