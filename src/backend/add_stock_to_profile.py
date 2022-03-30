import storage

def add_stock():
    currentProfiles = [next(iter(i.values())) for i in storage.read_data()['profiles']] # Pulls all the profiles names.
    while True:
        stocks = input()

        if stocks == "Quit" or "quit":
            break
        else:
            storage.read_data()["stocks"].append(stocks)
            continue
