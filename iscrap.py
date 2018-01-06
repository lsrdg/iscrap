"""
Iscrap  | Scrap archlinux.org/news before upgrading

---
v0.0.0+
"""

import argparse
import re
import bs4
import requests


class Soupers:
    """
    Collect of soup-related functions.
    """

    def __init__(self):
        """
        Get requests.
        """
        self.res = requests.get('https://www.archlinux.org/news/')

    def return_arch_soup(self):
        """
        Returns main arch soup.
        """
        res = self.res
        res.raise_for_status()
        arch_soup = bs4.BeautifulSoup(res.text, 'lxml')

        return arch_soup


def fetch_func(number):
    '''
    Parse archlinux.org/news and print news titles.

    '''

    number = int(number)
    soups = Soupers()
    arch_soup = soups.return_arch_soup()
    soup = arch_soup.find_all('td', attrs={'class': 'wrap'})

    print('\n\n')

    for position, news in enumerate(soup[:number], start=1):
        print('{} - {}'.format(position, news.getText()))

    print('\n\n')


def read_func(number):
    '''
    Print the new choosed by the user.
    '''

    number = int(number) - 1
    soups = Soupers()
    arch_soup = soups.return_arch_soup()
    all_news = []

    for a_new in enumerate(arch_soup.find('tbody').find_all('a', href=True)):
        href = re.search(r'(href=")(?P<href>.+)("\s)', str(a_new))
        all_news.append(href[2])

    the_new = all_news[number]
    res = requests.get('https://www.archlinux.org/' + the_new)
    res.raise_for_status()

    newsoup = bs4.BeautifulSoup(res.text, 'lxml')

    header_soup = newsoup.find('h2').getText()
    soup = newsoup.find('div', attrs={'class': 'article-content'}).getText()
    # find_all('p')

    print('\n\n\t\t\t', header_soup, '\n\n')
    print(soup.ljust(1), '\n')


def parse_arguments():
    """
    Parse and return arguments.
    """

    parser = argparse.ArgumentParser("cliclock [COMMAND] [ARGUMENTS]")

    parser.add_argument("--version", "-v", action="version", version="v0.0.0+")

    subparsers = parser.add_subparsers(help="Types of commands")

    fetch_parser = subparsers.add_parser("fetch", help="Shows the title of the \
            3 latest news")
    fetch_parser.add_argument("number", type=int, help="An integer of how many \
            news' titles will be fetched.")
    fetch_parser.set_defaults(func=fetch_func)

    read_parser = subparsers.add_parser("read", help="Shows the title of the 3 \
            latest news")
    read_parser.add_argument("number", type=int, help="An integer representing \
            which new will be read.")
    read_parser.set_defaults(func=read_func)

    return vars(parser.parse_args())


def main():
    '''
    Argparser organizer.
    '''

    args_dict = parse_arguments()

    if re.search("fetch_func", str(args_dict["func"])):
        number = str(args_dict["number"])
        fetch_func(number)

    elif re.search("read_func", str(args_dict["func"])):
        number = str(args_dict["number"])
        read_func(number)

    elif re.search("version", str(args_dict["func"])):
        print(args_dict)

    else:
        print("Ooops!")


if __name__ == '__main__':
    main()
