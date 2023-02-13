from msedge.selenium_tools import Edge, EdgeOptions
from setup import get_options

def get_driver():
    driver = Edge(executable_path="msedgedriver.exe",options=get_options())
    return driver