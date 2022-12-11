from HtmlUtils import get_title, get_description_meta
from configparser import ConfigParser

def main():
    config = ConfigParser()
    config.read('config.ini')
    config_data = config['URL Config']
    URL = config_data['URL']
    title = get_title(URL)
    description = get_description_meta(URL)

    if title:
        print("The title of the page is:", title)
    else:
        print("Title not found.")

    if description:
        print("The description meta of the page is:" , description)
    else:
        print("Description not found.")

if __name__ == "__main__":
    main()