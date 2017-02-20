import requests, bs4, lxml

res = requests.get('https://www.archlinux.org/news/')
res.raise_for_status()

archsoup = bs4.BeautifulSoup(res.text, 'lxml')

soup = archsoup.find_all('td', attrs={'class':'wrap'})

print('\n\n')

for news in soup[:3]:
    print(news.getText(), '\n')

print('\n\n')
