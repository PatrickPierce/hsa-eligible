import sys
import argparse


def get_args():
    """
    Parse user inputs
    TODO: Better way to organize this
    """

    def return_args(args):

        product = args.product
        account = args.account
        status = args.status

        if product is not None:
            product = " ".join(product)

            # TODO: Alphanumeric check breaks if product name contains a space
            # if not product.isalpha():
            #     print("Product name should not include numbers. \nExiting.")
            #     sys.exit()

        if status is not None:
            status = " ".join(status)
            for state in status_list:
                if status.lower() == state.lower():
                    status = state

        if account and product:
            selection = 1
            return account, product, selection
        if account and status:
            selection = 2
            return account, status, selection
        if product and status:
            selection = 3
            return product, status, selection

    parser = argparse.ArgumentParser(
        description="Search products eligible for HSA coverage."
    )

    accounts = ["HSA", "HFSA", "LFSA", "DFSA", "HRA"]
    help_a = f"Search by account types: {accounts[:-1]}"
    parser.add_argument(
        "-a",
        dest="account",
        choices=accounts,
        type=str.upper,
        default=None,
        help=help_a,
    )

    help_p = "Search by product name."
    parser.add_argument(
        "-p", dest="product", nargs="+", type=str.lower, default=None, help=help_p
    )

    # TODO: Make this optional
    status_list = ["Eligible", "Eligible with RX", "Eligible with LMN", "Not Eligible"]
    help_s = f"Search by eligible status: {status_list[:-1]}"
    parser.add_argument("-s", dest="status", nargs="+", default="Eligible", help=help_s)

    args = parser.parse_args()
    parser = return_args(args)
    return parser
