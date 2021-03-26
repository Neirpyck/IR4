import json
import time
import urllib
from urllib import request

import bs4
import schedule

base_url = 'https://www.tourisme.destination-angers.com/organisez-votre-sejour-a-angers/bonnes-adresses-a-angers-restaurants-bars-guinguettes/vente-a-emporter-des-restaurants-pendant-le-confinement?listpage='


def get_restaurant(page):
    return [item.getText() for item in page.findAll(
    'h3', {'class': 'item-infos-title'})]


def get_places(page):
    return [item.getText().strip() for item in page.findAll('adress')]


def get_services(page):
    list_services = []
    for item in page.findAll('div', {'class': 'item-block-covid item-block-covidservices'}):
        childList = []
        for child in item.findAll('div'):
            childList.append(child.getText())
        list_services.append(childList)
    return list_services


def json_from_list(list_restaurants, list_places, list_services):
    return {list_restaurants[i]: {'name':list_restaurants[i],'address': list_places[i], 'services': [
      service for service in list_services[i]]} for i in range(len(list_restaurants))}


def get_all_from_page_n(n):
    request_text = request.urlopen(base_url+str(n)).read()
    page = bs4.BeautifulSoup(request_text, "lxml")
    return get_restaurant(page), get_places(page), get_services(page)


def main():
    data = {}
    for i in range(1, 11):
        list_restaurants, list_places, list_services = get_all_from_page_n(i)
        data = dict(data, **json_from_list(list_restaurants,
                    list_places, list_services))

    with open('data.json', 'w') as f:
        json.dump(data, f)
    print('done')
    return


def job():
    data = {}
    for i in range(1, 11):
        list_restaurants, list_places, list_services = get_all_from_page_n(i)
        data = dict(data, **json_from_list(list_restaurants, list_places, list_services))
    
    with open('data.json','w') as f:
        json.dump(data, f)
    print('done')



schedule.every(2).minutes.do(job)

if __name__ == '__main__':
    main()
    while True:
        schedule.run_pending()
        time.sleep(1)
