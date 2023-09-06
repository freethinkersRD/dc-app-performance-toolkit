import random

from selenium.webdriver.common.by import By

from selenium_ui.base_page import BasePage
from selenium_ui.conftest import print_timing
from selenium_ui.jira.pages.pages import Login
from util.conf import JIRA_SETTINGS

def extended_schemes_issue_links_json_config(webdriver, datasets):
    page = BasePage(webdriver)
    issue_id = datasets['issue_id']

    @print_timing("extended_schemes")
    def measure():
        @print_timing("extended_schemes:links_json_config")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/rest/linkscheme/1.0/config?issueId={issue_id}")
        sub_measure()
    measure()
    
    
def extended_schemes_issue_prires_json_config(webdriver, datasets):
    page = BasePage(webdriver)
    issue_id = datasets['issue_id']

    @print_timing("extended_schemes")
    def measure():
        @print_timing("extended_schemes:prires_json_config")
        def sub_measure():
            page.go_to_url(f"{JIRA_SETTINGS.server_url}/rest/priresschemes/1.0/config?issueId={issue_id}")
        sub_measure()
    measure()