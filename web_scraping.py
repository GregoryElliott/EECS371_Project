import requests
from bs4 import BeautifulSoup
import pprint


def main():
    r = requests.get("http://www.imdb.com/event/ev0000292/2013")

    soup = BeautifulSoup(r.content, "html.parser")

    h2s = soup.find_all('h2')

    categories_and_nominees_dict = {}
    for h in h2s:
        categories_and_nominees_dict[h.text] = []
        this_cat = soup.find("h2", text=h.text).next_sibling.next_sibling.findAll("a")
        if "name" in str(this_cat[0]):
            for a in this_cat:
                if "name" in str(a) and a.text != "":
                    categories_and_nominees_dict[h.text].append(a.text)
        elif "title" in str(this_cat[0]):
            for a in this_cat:
                if "title" in str(a) and a.text != "":
                    categories_and_nominees_dict[h.text].append(a.text)

    pprint.pprint(categories_and_nominees_dict)

if __name__ == '__main__':
    main()