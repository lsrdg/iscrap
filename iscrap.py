import requests, bs4, lxml, argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--read", help="Read news. Use it with the number on the left of the title")
parser.add_argument("-f", "--fetch", help="Shows the title of the 3 latest news", nargs='*')
args = parser.parse_args()

res = requests.get('https://www.archlinux.org/news/')
res.raise_for_status()

archsoup = bs4.BeautifulSoup(res.text, 'lxml')

soup = archsoup.find_all('td', attrs={'class':'wrap'})
def mainFunction():

    print('\n\n') 

    for n,news in enumerate(soup[:3]):
        print(n, '- ', news.getText())

    print('\n\n')

def argRead(number):
    number = int(number)
    allNews = []
    for n,a in enumerate(archsoup.find('tbody').find_all('a', href=True)):
        allNews.append(a['href'])


    theNew = allNews[number]
    res = requests.get('https://www.archlinux.org/' + theNew)
    res.raise_for_status()

    newsoup = bs4.BeautifulSoup(res.text, 'lxml')

    headerSoup = newsoup.find('h2').getText()
    soup = newsoup.find('div', attrs={'class':'article-content'}).getText()
    #find_all('p')


    print('\n\n\t\t\t', headerSoup, '\n\n')
    print(soup.ljust(1), '\n')
    
def menuInit():
    if args.read:
        argRead(args.read[0])

    else:
        mainFunction()

menuInit()
