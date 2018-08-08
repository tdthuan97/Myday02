from bs4 import BeautifulSoup


def html_parser(html):
    text = ''.join(BeautifulSoup(html, "html.parser").stripped_strings)
    return text
