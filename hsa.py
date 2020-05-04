from parser import get_args
from scraper import Scraper
from firefox import driver_firefox


def run_selection(*args):
    if selection == 1:
        account, product = first_arg, second_arg
        Scraper(driver, wait).check_product(account, product)

    elif selection == 2:
        account, status = first_arg, second_arg
        Scraper(driver, wait).find_status(account, status)

    elif selection == 3:
        product = first_arg
        Scraper(driver, wait).check_status(product)

    driver.quit()


driver, wait = driver_firefox()

# TODO: Figure out how to pass a function with arguments into another function
# run_selection(get_args())
first_arg, second_arg, selection = get_args()
run_selection(first_arg, second_arg, selection)
