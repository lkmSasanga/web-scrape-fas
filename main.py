import requests
from bs4 import BeautifulSoup
import json
import dns
import pymongo

reviewlist = []


def get_soup(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_reviews(soup):
    reviews = soup.find_all('div', {'class': 'user-thread'})
    for item in reviews:
        review = item.find('p', {'class': 'uopin'}).text.strip()
        reviewlist.append(review)

for i in range(1, 13):
    soup = get_soup(f'https://www.gsmarena.com/reviewcomm-2200p{i}.php')
    get_reviews(soup)

print(reviewlist)

# import firebase_admin
# from firebase_admin import credentials
# from firebase_admin import firestore


# cred = credentials.Certificate
# ("feedback-65edf-firebase-adminsdk-2tuye-0fd2412027.json")
# firebase_admin.initialize_app(cred)

# db = firestore.client()
# doc=db.collection("Applephone").document("Document")

# doc.set({"Apple": "reviewlist"})