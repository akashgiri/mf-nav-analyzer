#!/usr/bin/python

import json
import re
import requests
from fuzzywuzzy import fuzz
from . import price_changes as pc

GOOGLE_FINANCE_URL = "http://finance.google.com/finance/info?client=ig&q=NSE:"

class MutualFundNavAnalysis():
    def __init__(self):
        self.matched_stocks_data = {}

    def get_nav_change(self, stocks_list):
        ## Fetch all the price changes for matched stocks with stock codes
        total_nav_change = 0.0
        for stock in stocks_list:
            #print "\nPrice changes in MF %s \n" % key
            name = stock[0]
            code = stock[2]
            url = GOOGLE_FINANCE_URL + code
            received_data = pc.get_stock_price_data(url, name, code)
            percent_change = received_data[0]
            time = received_data[1]

            weighting = stock[1]
            #print("weighting, percent_change: ", type(weighting), type(percent_change))
            total_nav_change += (float(weighting) * float(percent_change)) / 100

        total_nav_change = "{0:.4f}".format(total_nav_change)
        return total_nav_change

if __name__ == "__main__":
    mf_nav = MutualFundNavAnalysis()
