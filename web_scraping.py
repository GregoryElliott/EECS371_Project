import requests
from bs4 import BeautifulSoup
import pprint


def main(year):
    r = requests.get(str("http://www.imdb.com/event/ev0000292/%s" % year))

    soup = BeautifulSoup(r.content, "html.parser")

    h2s = soup.find_all('h2')

    categories_and_nominees_dict = {}
    for h in h2s:
        categories_and_nominees_dict[str(h.text).lower()] = []
        this_cat = soup.find("h2", text=h.text).next_sibling.next_sibling.findAll("a")
        if str("awards for %s" % year) in str(h.text).lower():
            continue
        if "name" in str(this_cat[0]):
            for a in this_cat:
                if "name" in str(a) and a.text != "":
                    try:
                        categories_and_nominees_dict[str(h.text).lower()].append(str(a.text).lower())
                    except:
                        continue
        elif "title" in str(this_cat[0]):
            for a in this_cat:
                if "title" in str(a) and a.text != "":
                    try:
                        categories_and_nominees_dict[str(h.text).lower()].append(str(a.text).lower())
                    except:
                        continue

    pprint.pprint(categories_and_nominees_dict)
    return categories_and_nominees_dict

if __name__ == '__main__':
    main('2013')