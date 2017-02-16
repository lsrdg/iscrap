import requests, bs4, lxml

res = requests.get('https://www.archlinux.org/')
res.raise_for_status()

archsoup = bs4.BeautifulSoup(res.text, 'lxml')

soup = archsoup.select('h4')

print(soup[0].getText())
# for e in soup:
#     soup[0].getText())
#     print(e)
