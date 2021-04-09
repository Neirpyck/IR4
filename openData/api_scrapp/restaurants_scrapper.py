#!/usr/bin/python3.8

import json
import time
import urllib
from urllib import request

import bs4
# import schedule

base_url = 'https://www.tourisme.destination-angers.com/organisez-votre-sejour-a-angers/bonnes-adresses-a-angers-restaurants-bars-guinguettes/vente-a-emporter-des-restaurants-pendant-le-confinement?listpage='


def get_restaurant(page):
    return [item.getText() for item in page.findAll(
    'h3', {'class': 'item-infos-title'})]


def get_places(page):
    return [item.getText().strip() for item in page.findAll('adress')]


def get_images(page):
    return [item.attrs['src'] for item in page.findAll('img', {'class': 'main-img img-thumb img-responsive landscape-mode'})]


def get_services(page):
    list_services = []
    for item in page.findAll('div', {'class': 'item-block-covid item-block-covidservices'}):
        childList = []
        for child in item.findAll('div'):
            childList.append(child.getText())
        list_services.append(childList)
    return list_services


# document.querySelector("#item_sheet_list > div:nth-child(1) > article > a")

def get_url(page):
    list_url = []
    for item in page.findAll('div', {'id': 'item_sheet_list'}):
        for child in item.findAll('a'):
            list_url.append(child.attrs['href'])
    return list_url
    

def json_from_list(list_restaurants, list_places, list_services, list_images, list_url):
    """
    Return a Json Map of type :
    {
        'RestaurantName': {
            'name': 'RestaurantName,
            'address': 'RestaurantAddress',
            'services': ['Service1', 'Service2'],
            'image': 'ImageUrl',
            'url': 'RestaurantUrl',
        }
    }
    """
    return {list_restaurants[i]: {'name':list_restaurants[i],'city': list_places[i], 'services': [
      service for service in list_services[i]], 'image': list_images[i], 'url': list_url[i]} for i in range(len(list_restaurants))}




def get_all_from_page_n(n):
    request_text = request.urlopen(base_url+str(n)).read()
    page = bs4.BeautifulSoup(request_text, "lxml")
    return get_restaurant(page), get_places(page), get_services(page), get_images(page), get_url(page)

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
    with open('data.json', 'r') as f:
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

    with open('data.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)
    

def main():
    data = {}
    for i in range(1, 11):
        list_restaurants, list_places, list_services, list_images, list_url = get_all_from_page_n(i)
        data = dict(data, **json_from_list(list_restaurants,
                    list_places, list_services, list_images, list_url))
        #TODO: Remove
        break

    data_out = dict(zip([str(i) for i in range(len(data))], list(data.values())))



    with open('data.json', 'w') as f:
        json.dump(data_out, f, ensure_ascii=False)

    for restaurant in data_out:
        get_detail(restaurant)
    print('done')


# def job():
#     data = {}
#     for i in range(1, 11):
#         list_restaurants, list_places, list_services, list_images, list_url = get_all_from_page_n(i)
#         data = dict(data, **json_from_list(list_restaurants, list_places, list_services, list_images, list_url))

#     data_out = dict(zip([str(i) for i in range(len(data))], list(data.values()))

#     with open('data.json','w') as f:
#         json.dump(data_out, f)
#     print('done')

# schedule.every(2).minutes.do(job)

if __name__ == '__main__':
    main()
    # while True:
    #     schedule.run_pending()
    #     time.sleep(1)

    # request_text = request.urlopen(base_url+str(1)).read()
    # page = bs4.BeautifulSoup(request_text, "lxml")
    # print(get_url(page))


