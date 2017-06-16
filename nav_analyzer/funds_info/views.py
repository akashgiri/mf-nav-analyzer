from django.shortcuts import render
from .models import Fund, Stock

# Create your views here.
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
    print("page_slug: ", page_slug)
    objects = Fund.objects.filter(slug_url=page_slug)
    stocks_list = []
    for obj in objects:
        stock = obj.stock_name
        stocks_list.append(stock)

    print(stocks_list)

    context = {
        'stocks_list': stocks_list
    }
    return render(request, "funds_info/show_all_stocks.html", context)
