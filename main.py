# main.py
from scraper import scrape
from setup import update_links
import os

if __name__ == '__main__':
    url = "https://www.classcentral.com/"
    curr_dir = 'html'
    main_file_path = f"{curr_dir}/Page{0}.html"
    target_file_path = "PageMain.html"

    if not os.path.exists(curr_dir):
        os.makedirs(curr_dir)

   
    #scrape(url , curr_dir)
    update_links(main_file_path ,target_file_path , curr_dir )