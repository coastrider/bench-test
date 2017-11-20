import requests


def query_url(url):
    """ - Performs HTTP GET to the URL passed in params, then:
         * Returns response container if HTTP 200 or 404
         * Raise exception for other HTTP response codes. i.e >500 """
    server_response = requests.get(url)
    if server_response.status_code == 200:
        return server_response
    elif server_response.status_code == 404:
        return server_response
    else:
        server_response.raise_for_status()


def balance_processor(page, balance_map):
    """Processes every transaction from JSON page and combines transactions for the same date"""
    for transaction in page["transactions"]:
        date = transaction["Date"]
        amount = transaction["Amount"]
        # This logic combines transactions for a given date
        if date in balance_map:
            balance_map[date] += float(amount)
        else:
            balance_map[date] = float(amount)
    """ balance_map contains date and combined amounts for each day, for example:
    {'2013-12-22': -110.71, '2013-12-21': -17.98, '2013-12-20': -4054.6} """
    return balance_map


def total_balances(host, resource):
    """Receives URL information and iteratively calls query_url and balance_processor
    for every resource found in the given URL then returns the dict balance_map"""
    # The following normalization is required in case the URL path ends in a file format:
    page_counter = int(resource.strip(".json"))
    balance_map = {}
    while True:

        url = host + str(page_counter) + ".json"
        page = query_url(url)

        if page.status_code == 404:
            break
        # Transforms to dictionary using requests built-in JSON decoder
        page_decoded = page.json()
        balance_processor(page_decoded, balance_map)
        page_counter += 1
    return balance_map
