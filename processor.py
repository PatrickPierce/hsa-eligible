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
            for k, v in product_list.items():
                ratio = fuzz.token_sort_ratio(item, k)

                if ratio >= 70:
                    missing_item = False
                    return_results[k] = v

                    if ratio < 100:
                        print(f"Similar product: {k.capitalize()}")
                        print(f"{account}: {v}\n")
                        return_results[k] = v
                    elif ratio == 100:
                        print(f"Product: {k.capitalize()}")
                        print(f"{account}: {v}\n")
                        return_results[k] = v
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
