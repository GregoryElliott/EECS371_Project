import requests
from bs4 import BeautifulSoup
import pprint
import re
import unicodedata


def get_nominees(year):
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

GOLDEN_GLOBE_YEAR_OFFSET = 1943


def get_presenters(year):
    r = requests.get('https://en.wikipedia.org/wiki/{}_Golden_Globe_Awards'.format(ordinal(int(year)-GOLDEN_GLOBE_YEAR_OFFSET)))

    soup = BeautifulSoup(r.content, "html.parser")

    presenter_head = soup.find('span', id="Presenters").parent
    presenter_list = presenter_head.next_sibling.next_sibling.find_all('li')

    presenter_dict = {}
    for li in presenter_list:
        full_str = ""
        for c in li.children:
            if hasattr(c, 'text'):
                full_str += c.text
            else:
                full_str += c
        full_str = full_str.replace(u"\u2013", "-").lower()
        if 'introduced' in full_str and not 'with' in full_str:
            continue
        presenter_dict[re.split('with ', full_str)[1]] = re.split('with|introduced', full_str)[0].strip().split(' and')

    pprint.pprint(presenter_dict)
    return presenter_dict



SUFFIXES = {1: 'st', 2: 'nd', 3: 'rd'}

def ordinal(num):
    if 10 <= num % 100 <= 20:
        suffix = 'th'
    else:
        suffix = SUFFIXES.get(num % 10, 'th')
    return str(num) + suffix



if __name__ == '__main__':
    get_presenters('2013')