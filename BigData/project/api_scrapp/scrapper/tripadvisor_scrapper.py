import json
import re
import time
from urllib import request

import bs4
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def parse_restaurants_url(base_url, city_url):
    """
    return a Json Map of type:
    {
        "restaurant": [
            {
                'name': 'Restaurant Name',
                'tripAdvisor': 'url vers tripadvisor'
            }
        ]
    }
    """
    restaurantsList = list()
    regex = r"\d\. [a-zA-Z]*"
    url = f"{base_url+city_url}"

    driver.get(url)
    # To accept cookies (popup)
    driver.implicitly_wait(10)
    driver.find_element_by_id("_evidon-accept-button").click()
    time.sleep(3)

    page = bs4.BeautifulSoup(driver.page_source, "lxml")
    for item in page.findAll("div", {"id": "EATERY_SEARCH_RESULTS"}):
        for child in item.findAll("a"):
            if child.getText() != "" and bool(re.search(regex, child.getText())):
                print(child.getText(), 1)
                restaurantsList.append(
                    dict(
                        name=child.getText().split(".")[-1].strip(),
                        tripAdvisor=child.attrs["href"],
                    )
                )

    for i in range(2, 15):
        driver.find_element_by_css_selector(f"a.nav:nth-child(2)").click()
        print(f"page {i}")
        time.sleep(3)
        page = bs4.BeautifulSoup(driver.page_source, "lxml")
        for item in page.findAll("div", {"id": "EATERY_SEARCH_RESULTS"}):
            for child in item.findAll("a"):
                if child.getText() != "" and bool(re.search(regex, child.getText())):
                    print(child.getText(), i)
                    restaurantsList.append(
                        dict(
                            name=child.getText().split(".")[-1].strip(),
                            tripAdvisor=child.attrs["href"],
                        )
                    )

    with open("tripadvisor.json", "w") as f:
        json.dump(restaurantsList, f, ensure_ascii=False)

    driver.quit()


def navigate_tripadvisor_resto(BASE_URL, restaurant_name):
    with open("tripadvisor.json", "r") as f:
        data = json.load(f)

    url = ""

    for item in data:
        if item["name"] == restaurant_name:
            url = BASE_URL[:-1] + item["tripAdvisor"]

    request_text = request.urlopen(url).read()
    page = bs4.BeautifulSoup(request_text, "lxml")
    return page


def get_note(page):
    try:
        note = page.find("span", {"class": "r2Cf69qf"}).get_text()
    except:
        note = ""
    return note[:-1]


def get_cuisines(page):
    """
    return list of cuisines
    """
    try:
        cuisines = page.select_one(
            "._3UjHBXYa > div:nth-child(2) > div:nth-child(2)"
        ).getText()
        cuisines = cuisines.split(",").trim()
    except:
        cuisines = [""]
    return cuisines


def get_price_range(page):
    try:
        price = page.select_one(
            "._3UjHBXYa > div:nth-child(1) > div:nth-child(2)"
        ).getText()
    except:
        return ["", ""]
    if bool(re.search(r"\d", price)):
        price = price.split(" ")
        del price[1]
        price[0], price[1] = price[0][:-1], price[1][:-1]
        return price
    return ["", ""]


def get_3_reviews(page):
    listReviews = list()
    reviews = page.findAll("p", {"class": "partial_entry"})
    for review in reviews:
        listReviews.append(review.getText())
    return listReviews[:3]


def get_tripadvisor_details(BASE_URL):
    """
    Modify the restaurant JSON array to make it of type:
    [
        {
        "name": "Name of Restaurant",
        "tripAdvisor": "url of type : /Restaurant_Review-g187197-d19134611-Reviews-Reste_Au_51-Angers_Maine_et_Loire_Pays_de_la_Loire.html",
        "cuisine": [
            "type of cuisine 1",
            "type of cuisine 2"
            ],
        "note": "5,0",
        "3reviews": [
            "review 1",
            "review 2",
            "review 3",
            ],
        "price": [
            "lowest price",
            "highest price"
            ]
        },
    ]
    """
    with open("tripadvisor.json", "r") as f:
        data = json.load(f)

    for i in range(len(data)):
        print(i)
        if i != 0 and not i % 10:
            with open("tripadvisor.json", "w") as f:
                json.dump(data, f, ensure_ascii=False)

        url = BASE_URL[:-1] + data[i]["tripAdvisor"]
        request_text = request.urlopen(url).read()
        page = bs4.BeautifulSoup(request_text, "lxml")
        (
            data[i]["cuisine"],
            data[i]["note"],
            data[i]["3reviews"],
            data[i]["price"],
        ) = (
            get_cuisines(page),
            get_note(page),
            get_3_reviews(page),
            get_price_range(page),
        )


if __name__ == "__main__":
    option = Options()
    option.headless = True
    driver = webdriver.Firefox(options=option)

    BASE_URL = "http://www.tripadvisor.fr/"
    SCRAP_URL = BASE_URL + "Restaurant_Review-g187197-oa"
    CITY_DEFAULT_URL = "-Angers_Maine_et_Loire_Pays_de_la_Loire.html"

    # Get all restaurant in angers
    # parse_restaurants_url(SCRAP_URL, CITY_DEFAULT_URL)
    # get_tripadvisor_details(BASE_URL)

    # Test


# http://www.tripadvisor.fr/Restaurant_Review-g187197-o/
