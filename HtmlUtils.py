"""This module contains useful functions for getting information about a webpage like title or description."""

from bs4 import BeautifulSoup as bs
import requests

def get_html(URL: str):
    """This returns the html of the given URL"""
    html_doc = bs(requests.get(URL).text, "html.parser")
    return html_doc


def get_title(URL: str):
    """This function gets the title of a webpage using the given URL. Returns None if not found."""
    html_doc = get_html(URL)
    title = html_doc.find('title')
    if title:
        return title.string
    return None


def get_description_meta(URL: str):
    """This function gets the description meta of a webpage using the given URL. Returns None if not found."""
    html_doc = get_html(URL)
    description = html_doc.find("meta", {"name":"description"})
    if description:
        return description['content']
    return None