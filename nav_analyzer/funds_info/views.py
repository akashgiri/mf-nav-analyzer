from django.shortcuts import render
from .models import Fund, Stock

# Create your views here.
def show_funds_list(request):
    funds_data = {}
    #funds_data["funds_list"] = 

    distinct_funds = Fund.objects.order_by().values_list('fund_name').distinct()
    funds_list = []

    if distinct_funds:
        for fund in distinct_funds:
            fund = ''.join(fund)
            funds_list.append(fund)

    funds_data["funds_list"] = funds_list

    context = {
        'funds_data': funds_data
    }

    return render(request, "funds_info/welcome.html", context)
