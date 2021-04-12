#!/usr/bin/python3.8

import json
import time
import urllib
from urllib import request

import bs4

BASE_URL = "https://www.tourisme.destination-angers.com/organisez-votre-sejour-a-angers/bonnes-adresses-a-angers-restaurants-bars-guinguettes/vente-a-emporter-des-restaurants-pendant-le-confinement?listpage="


def json_from_list(restaurantList, addressList, serviceList, imageList, urlList):
    """
    Return a Json Map of type :
    [
        {
            'name': 'RestaurantName,
            'address': 'RestaurantAddress',
            'services': ['Service1', 'Service2'],
            'image': 'ImageUrl',
            'url': 'RestaurantUrl',
        }
    ]
    """
    return [
        {
            "name": restaurantList[i],
            "city": addressList[i],
            "services": [service for service in serviceList[i]],
            "image": imageList[i],
            "url": urlList[i],
        }
        for i in range(len(restaurantList))
    ]


def get_restaurant_informations(url):
    """
    Return all the information on the Angers Tourism Page of a restaurant
    """
    request_text = request.urlopen(url).read()
    page = bs4.BeautifulSoup(request_text, "lxml")

    description = page.find("div", {"class": "establishment-description"}).p.getText()
    covid_mesures = page.find(
        "span", {"class": "establishment-description"}
    ).p.getText()
    phone = (
        page.find("a", {"class": "phone-link reveal-content"})["href"]
        .strip("tel:")
        .replace(" ", "")
    )

    return description, covid_mesures, phone


def get_restaurant_json():
    data = list()

    for i in range(1, 11):
        request_text = request.urlopen(BASE_URL + str(i)).read()
        page = bs4.BeautifulSoup(request_text, "lxml")

        # Get informations
        restaurantList = [
            item.getText() for item in page.findAll("h3", {"class": "item-infos-title"})
        ]
        addressList = [item.getText().strip() for item in page.findAll("adress")]
        imageList = [
            item.attrs["src"]
            for item in page.findAll(
                "img", {"class": "main-img img-thumb img-responsive landscape-mode"}
            )
        ]
        # TODO: optimise this part
        # --- #
        urlList = list()
        for item in page.findAll("div", {"id": "item_sheet_list"}):
            for child in item.findAll("a"):
                urlList.append(child.attrs["href"])
        # --- #

        # TODO: optimise this part
        serviceList = list()
        for item in page.findAll(
            "div", {"class": "item-block-covid item-block-covidservices"}
        ):
            childList = []
            for child in item.findAll("div"):
                childList.append(child.getText())
            serviceList.append(childList)
        # --- #

        data.append(
            json_from_list(restaurantList, addressList, serviceList, imageList, urlList)
        )
        break

    return {'restaurants':data[0]}
    

def write_JSON(restaurantDic):
    for url in url:
        pass

    with open("final.json", "w") as f:
        json.dump(data, f, ensure_ascii=False)


if __name__ == "__main__":
    get_restaurant_list()
