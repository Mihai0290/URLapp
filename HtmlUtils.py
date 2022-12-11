from bs4 import BeautifulSoup as bs
import requests

def get_html(URL: str):
    """This returns the html of the given URL"""
    html_doc = bs(requests.get(URL).text, "html.parser")
    return html_doc


def get_title(URL: str):
    """This finds the title of the given html document"""
    html_doc = get_html(URL)
    title = html_doc.find('title')
    if title:
        return title.string
    return None


def get_description_meta(URL: str):
    """ This method gets the description meta of the URL given """
    html_doc = get_html(URL)
    description = html_doc.find("meta", {"name":"description"})
    if description:
        return description['content']
    return None