"""
Iscrap  | Scrap archlinux.org/news before upgrading

---
v0.0.0+
"""

import argparse
import bs4
import requests

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--read", help="Read news. Use it with the number \
       on the left of the title", nargs='?')
parser.add_argument("-f", "--fetch", help="Shows the title of the 3 latest \
       news", nargs='*')
args = parser.parse_args()

res = requests.get('https://www.archlinux.org/news/')
res.raise_for_status()

archsoup = bs4.BeautifulSoup(res.text, 'lxml')

soup = archsoup.find_all('td', attrs={'class': 'wrap'})


def fetch_func(number):
    '''
    Parse archlinux.org/news and print news titles.

    '''

    print('\n\n')

    for position, news in enumerate(soup[:number], start=1):
        print('{} - {}'.format(position, news.getText()))

    print('\n\n')


def read_func(number):
    '''
    Print the new choosed by the user.
    '''

    number = int(number) - 1
    all_news = []
    for a_new in enumerate(archsoup.find('tbody').find_all('a', href=True)):
        all_news.append(a_new['href'])

    the_new = all_news[number]
    res = requests.get('https://www.archlinux.org/' + the_new)
    res.raise_for_status()

    newsoup = bs4.BeautifulSoup(res.text, 'lxml')

    header_soup = newsoup.find('h2').getText()
    soup = newsoup.find('div', attrs={'class': 'article-content'}).getText()
    # find_all('p')

    print('\n\n\t\t\t', header_soup, '\n\n')
    print(soup.ljust(1), '\n')


def menu_init():
    '''
    Argparser organizer.
    '''

    if args.read:
        read_func(args.read[0])

    elif args.fetch:
        number = int(args.fetch[0])
        fetch_func(number)

    else:
        fetch_func(3)


menu_init()
