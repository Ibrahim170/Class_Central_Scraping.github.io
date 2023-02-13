import codecs
from msedge.selenium_tools import Edge, EdgeOptions
from bs4 import BeautifulSoup


def get_options():
    options = EdgeOptions()
    options.use_chromium = True
    options.add_argument("--lang=hi")
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    prefs = {
        "translate_whitelists": {'en': 'hi'},
        "translate": {"enabled": "true"}
    }
    options.add_experimental_option("prefs", prefs)
    return options

def update_links(main_file_path ,target_file_path , curr_dir):
    original_file = codecs.open(main_file_path, "r", "utf−8")
    original_soup = BeautifulSoup(original_file, "html.parser")
    
    # Replace the links in the original file with the newly saved translated HTML file paths
    for i, link in enumerate(original_soup.find_all("a")):
        link["href"] = f"{curr_dir}/Page{i}.html"
    
    # Save the updated original file
    updated_file = codecs.open(target_file_path, "w", "utf−8")
    updated_file.write(original_soup.prettify())
    