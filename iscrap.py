import requests
import bs4
import lxml
import argparse

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


def argFetch(number):
    '''
    Parse archlinux.org/news and print news titles.

    '''

    print('\n\n')

    for n, news in enumerate(soup[:number], start=1):
        print('{} - {}'.format(n, news.getText()))

    print('\n\n')


def argRead(number):
    '''
    Print the new choosed by the user.
    '''

    number = int(number) - 1
    allNews = []
    for n, a in enumerate(archsoup.find('tbody').find_all('a', href=True)):
        allNews.append(a['href'])

    theNew = allNews[number]
    res = requests.get('https://www.archlinux.org/' + theNew)
    res.raise_for_status()

    newsoup = bs4.BeautifulSoup(res.text, 'lxml')

    headerSoup = newsoup.find('h2').getText()
    soup = newsoup.find('div', attrs={'class': 'article-content'}).getText()
    # find_all('p')

    print('\n\n\t\t\t', headerSoup, '\n\n')
    print(soup.ljust(1), '\n')


def menuInit():
    '''
    Argparser organizer.
    '''

    if args.read:
        argRead(args.read[0])

    elif args.fetch:
        number = int(args.fetch[0])
        argFetch(number)

    else:
        argFetch(3)


menuInit()
