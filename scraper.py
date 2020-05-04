import os
import string
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from processor import search_fuzzy


class Scraper:
    """
    Scrape webpage to get product name, account type and eligibilty status
    """

    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def visit_url(self, url_index):
        """
        Search URL base on first letter of product name
        """

        def create_url():

            if url_index == "a":
                url_sub = ".aspx"
            else:
                url_sub = f"/{url_index}.aspx"

            url = f"https://hsastore.com/hsa-eligibility-list{url_sub}"
            return url

        self.driver.get(create_url())

    def click_account(self, account):
        """
        Find xpath from user input to select account type
        """

        def select_account():
            account_options = {
                "HSA": '//option[@value="4"]',
                "HFSA": '//option[@value="1"]',
                "LFSA": '//option[@value="2"]',
                "DFSA": '//option[@value="3"]',
                "HRA": '//option[@value="5"]',
            }

            for account_type, option_value in account_options.items():
                if account == account_type:
                    account_value = self.driver.find_element_by_xpath(option_value)
                    break

            return account_value

        self.wait.until(EC.element_to_be_clickable((By.ID, "accountTypes"))).click()

        account_value = select_account()
        account_value.click()

    def scrape_data(self):
        """
        Wait until table is loaded on page
        Get table cells containing product information
        TODO: Maybe save list in file or database to prevent rescraping data
        """

        def create_dictionary(product_list):
            """
            Key: Product
            Value: Eligibility Status
            """

            def check_eligibility(products):
                """
                Check and return eligibility status base on indicator
                """

                eligibilities = {
                    "brand-original": "Eligible",
                    "brand-rx": "Eligible with RX",
                    "brand-lmn": "Eligible with LMN",
                    "brand-not-eligible": "Not Eligible",
                }

                product_status = products.find_element_by_class_name(
                    "expenseTypeLabelIndicator"
                ).get_attribute("class")[26:]

                for brand, eligible in eligibilities.items():
                    if product_status == brand:
                        eligibility = eligible

                return eligibility

            return_list = {}

            # Get product name and eligible status
            for products in product_list:
                name = products.find_element_by_class_name(
                    "expenseTypeNameLabel"
                ).text.lower()

                return_list[name] = check_eligibility(products)

            return return_list

        cls_products = "expenseTypeName"

        self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, cls_products)))

        product_list = self.driver.find_elements_by_class_name(cls_products)

        return create_dictionary(product_list)

    """
    Maybe move these into a sub class
    """

    def check_product(self, account, product):
        """
        Check the eligibility status for the given account type and product
        """

        def find_product():
            """
            Scrapes results to product list
            """
            url_index = product[0]

            self.visit_url(url_index)
            self.click_account(account)

            return self.scrape_data()

        product_list = find_product()

        search_fuzzy(account, product, product_list)

    def find_status(self, account, status):
        """
        Check products for the given account type and eligibility status
        """

        def save_data():
            filename = f"{account}_eligible.txt".lower()
            with open(filename, "w") as f:
                for product_name, product_status in product_list.items():
                    if product_status == status:
                        f.write(f"Product: {product_name.upper()}\n")
                        f.write(f"Status: {product_status}\n\n")

            return filename

        page_indexes = list(string.ascii_lowercase)
        product_list = {}
        for url_index in page_indexes:
            self.visit_url(url_index)
            self.click_account(account)
            product_list.update(self.scrape_data())

        filename = save_data()
        print(f"List too big")
        print(f"Saved to {os.path.abspath(filename)}")

    def check_status(self, product):
        """
        Check product status for each account type
        """
        url_index = product[0]
        self.visit_url(url_index)
        product_list = {}
        # TODO: Find a way to not repeat accounts var like in get_args
        accounts = ["HSA", "HFSA", "LFSA", "DFSA", "HRA"]
        for account in accounts:
            self.click_account(account)
            product_list.update(self.scrape_data())

            search_fuzzy(account, product, product_list)
