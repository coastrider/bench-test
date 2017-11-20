import configparser
import benchtest.core


def main():

    # Read config file and assign config variables
    config = configparser.ConfigParser()
    config.read('sites.conf')
    host = config["bench_api"]["host"]
    resource = config["bench_api"]["resource"]

    # Instantiate balances dictionary using benchtest/core.py module
    balances = benchtest.core.total_balances(host, resource)

    # Output daily balances, sorted by Date
    daily_balance = float(0)

    print(" — Daily balances:")
    print("Date\t\t Balance")
    print("-------\t\t -------")
    for day in sorted(balances):
        daily_balance += balances[day]
        print("{0}\t $ {1:.2f}".format(day, daily_balance))

    # Output total balance
    total_balance = sum(balances.values())
    print("\n — Total balance:")
    print(round(total_balance, 2))

    # Return total balance for testing purposes
    return round(total_balance, 2)

if __name__ == "__main__":
    main()
