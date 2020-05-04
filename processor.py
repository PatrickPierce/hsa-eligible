from fuzzywuzzy import fuzz


def search_fuzzy(account, product, product_list):
    """
    Return products base on fuzzy search results
    """

    def check_multiple():
        """
        Check for multiple words and combine into one
        Search "baby oil" and "babyoil"
        """
        items = [
            product,
        ]
        if " " in product:
            items.append(product.replace(" ", ""))

        return items

    items = check_multiple()

    # TODO: Find a better way to do this
    missing_item = True
    return_results = {}
    search_complete = False
    while not search_complete:
        for item in items:
            for product_name, account_type in product_list.items():
                ratio = fuzz.token_sort_ratio(item, product_name)

                if ratio >= 70:
                    missing_item = False
                    return_results[product_name] = account_type

                    if ratio < 100:
                        print(f"Similar product: {product_name.capitalize()}")
                        print(f"{account}: {account_type}\n")
                        return_results[product_name] = account_type
                    elif ratio == 100:
                        print(f"Product: {product_name.capitalize()}")
                        print(f"{account}: {account_type}\n")
                        return_results[product_name] = account_type
                        """
                        Stops search once product is found
                        May change this to be optional
                        That way it will keep searching for similar items
                        """
                        search_complete = True

            if search_complete:
                break

        if missing_item:
            print(f"Unable to find product: {product.capitalize()}\n")
            break

        return return_results
