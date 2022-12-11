from HtmlUtils import get_title, get_description_meta

def main():
    URL = input("Enter the URL: ")
    print("The title of the page is:", get_title(URL))
    print("The description meta of the page is:" , get_description_meta(URL))

if __name__ == "__main__":
    main()