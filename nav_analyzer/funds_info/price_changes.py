#!/usr/bin/python

import json
import re
import requests

def get_parsed_content(content):
    content = content.decode('utf-8')
    #print("content: ", content)
    #print("type content: ", type(content))
    content = content.replace('// [', '').replace(']', '').replace('\n', '')
    return content

def get_percent_change_in_price(content):
    percent_change = 0
    try:
        percent_change = content["cp"]
    except (Exception, e):
        print(e)

    return percent_change
    
def get_stock_price_data(url, name, code):
    response = requests.get(url)

    #print(response.status_code)
    
    if (response.status_code != 200) or (response.content == ""):
        return [0.0, "0"]

    content = response.content    
    content_formatted = json.loads(get_parsed_content(content))
    percent_change = get_percent_change_in_price(content_formatted)

    return [percent_change, content_formatted["lt"]]
