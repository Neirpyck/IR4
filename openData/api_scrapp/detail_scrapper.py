#!/usr/bin/python3.8

import json
import time
import urllib
from urllib import request

import bs4
# import schedule


def get_phone(page):
    try:
        return page.find('a', {'class': 'phone-link reveal-content'})['href'].strip('tel:').replace(' ', '')
    except:
        return ''

def get_description(page):
    try:
        return page.find('div', {'class': 'establishment-description'}).p.getText()
    except:
        return ''


def get_covid(page):
    try:
        return page.find('span', {'class': 'establishment-description'}).p.getText()
    except:
        return ''


def get_address(page):
    latitude = page.find('meta', {'itemprop': 'latitude'})['content']
    longitude = page.find('meta', {'itemprop': 'longitude'})['content']
    streetAddress = page.find('div', {'class': 'address1'}).getText()
    postalCode = page.find('span', {'itemprop': 'postalCode'}).getText()
    return latitude, longitude, streetAddress, postalCode


def get_detail(restaurant):
    with open('./restaurants/data.json', 'r') as f:
        data = json.load(f)

    for restaurant in data:
        url = data[restaurant]['url']
        request_text = request.urlopen(url).read()
        page = bs4.BeautifulSoup(request_text, "lxml")
        data[restaurant]['phone'], data[restaurant]['description'],  = get_phone(
            page), get_description(page)
        data[restaurant]['latitude'], data[restaurant]['longitude'], data[restaurant][
            'streetAddress'], data[restaurant]['postalCode'] = get_address(page)
        data[restaurant]['covidMesures'] = get_covid(page)

    with open('./restaurants/data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)



# def write_detail(restaurant, phone, description, latitude, longitude, streetAddress, postalCode):
#     with open('data.json', 'w') as f:
#         data = json.load(f)

#     data[restaurant]


# Test :
# A table chez Mili
# Acquaviva
# Aux Deux 5
if __name__ == '__main__':
    with open('./restaurants/data.json', 'r') as f:
        data = json.load(f)
    restaurant = data['0']['name']
    # url = data['0']['url']
    # request_text = request.urlopen(url).read()
    # page = bs4.BeautifulSoup(request_text, "lxml")
    # print(get_covid(page))
    get_detail(restaurant)
