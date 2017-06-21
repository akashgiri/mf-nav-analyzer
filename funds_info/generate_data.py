#!/usr/bin/env python

import json

from models import Fund, Stock

in_data = open("stocks-list.json", "r")
data = json.load(in_data)
in_data.close()

for fund in data:
    u_fund = "-".join(fund.rsplit("-")[:-1])
    u_fund = u_fund.replace("regular", "").replace("plan", "")
    full_name = u_fund.replace('-', ' ').title()
    stocks_data = data[fund]["stocks-data"]
    
    for stock in stocks_data:
        stock_name = stock["stock"]
        weighting = float(stock["weighting"])
        print(stock_name, weighting)
        f = Fund(fund_name=full_name,stock_name=stock_name,slug_url=u_fund,cash_allocation=0.0,stock_allocation=weighting)
        f.save()
    
    print(full_name)

exit(0)
