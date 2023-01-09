from configparser import ConfigParser
from HtmlUtils import get_title, get_description_meta, get_html


def main():
    config = ConfigParser()
    config.read('config.ini')
    config_data = config['URL Config']
    url = config_data['URL']
    keywords = config['OLX']['keywords'].replace(' ', '-')
    olx_URL = config['OLX']['URL']
    title = get_title(url)
    description = get_description_meta(url)

    if title:
        print("The title of the page is:", title)
    else:
        print("Title not found.")

    if description:
        print("The description meta of the page is:", description)
    else:
        print("Description not found.")

    print("\nSearching for " + keywords + "." + "This can take up to 1 minute...\n")
    check_prices(olx_URL, keywords)


def check_prices(url, keywords):
    """Navigates all the pages and get the title and the prices

    Arguments:
    url - is the base url of the site (without https://www.)
    keywords - represents the words that are searched
    """

    # constructing the full URL based on URL and keywords from the config file
    # (for olx we add /d/oferte/q- followed by keywords to obtain the results);
    # Doing this we get the first page.
    url = "https://www." + url + "/d/oferte/q-" + keywords
    number_of_pages = get_number_of_pages(url)

    data = []
    # First page
    data += get_titles_and_prices(url)
    # Looping through all pages
    for i in range(2, number_of_pages + 1):
        data += get_titles_and_prices(url + '/?page=' + str(i))
    data = filter_data(data)
    data = sorted(data, key=lambda p: int(p[1]))
    for item in data:
        print(item[0] + ": " + item[1])


def get_titles_and_prices(url):
    """Returns the titles and prices that are un the page.

    Arguments:
    url - the url of the page
    """
    page_html = get_html(url)
    item_cards = page_html.find_all('div', attrs={"class": "css-qfzx1y"})
    titles = []
    prices_labels = []
    prices = []
    for card in item_cards:
        titles.append(card.find('h6').get_text())
        prices_labels.append(card.find('p').get_text())

    for price in prices_labels:
        prices.append("".join([e for e in price if e.isdigit()]))

    items = zip(titles, prices)
    return list(items)


def get_number_of_pages(url):
    """Returns the number of pages that can be navigated.

    Arguments:
    url - is the url to the first page
    """
    try:
        first_page = get_html(url)
        pag_link = first_page.find_all(
            'a', attrs={"class": "css-1mi714g"})  # could be None
        return int(pag_link.pop().string)
    except:
        pass


def filter_data(data):
    """Filters items from data. Some of them may have incorrect data (some products marked as "schimb" instead of price)
    Also some of them might not be what you are looking for, like phone cases instead of phones and other accesories

    Arguments:
    data - contains the items to be filtered
    """
    filtered_data = []
    for item in data:
        if item[1] != "" and int(item[1]) > 2000:
            filtered_data.append(item)
    return filtered_data


if __name__ == "__main__":
    main()
