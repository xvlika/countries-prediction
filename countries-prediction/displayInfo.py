import shelve

userChoice = input("Enter which country info you want to see (if you want all enter: all): ").lower()

with shelve.open("countries") as db:
    countries_gdp = db['countries_gdp']
    
    if userChoice == "all":
        for country_data in countries_gdp:
            country = country_data['country']
            gdp = country_data['gdp']
            unemployment = country_data["unemployment"]
            inflation = country_data["inflation"]
            tax = country_data["tax_percentage"]
            trade = country_data["trade_balance"]
            investment_rate = country_data['investment_rate']
            population_growth = country_data["population_growth"]
            exchange_rate = country_data["exchange_rate"]

            print(f"{'='*40}")
            print(f"Country:           {country}")
            print(f"{'-'*40}")
            print(f"GDP:               {gdp} trillion USD")
            print(f"Unemployment Rate: {unemployment}%")
            print(f"Inflation Rate:    {inflation}%")
            print(f"Taxation:          {tax}%")
            print(f"Trade Balance:     {trade}")
            print(f"Investment Rate:   {investment_rate}%")
            print(f"Population Growth: {population_growth}%")
            print(f"Exchange Rate:     {exchange_rate}")
            print(f"{'='*40}\n")
    else:
        found = False
        for country_data in countries_gdp:
            country = country_data['country'].lower()
            if userChoice == country:
                gdp = country_data['gdp']
                unemployment = country_data["unemployment"]
                inflation = country_data["inflation"]
                tax = country_data["tax_percentage"]
                trade = country_data["trade_balance"]
                investment_rate = country_data['investment_rate']
                population_growth = country_data["population_growth"]
                exchange_rate = country_data["exchange_rate"]

                print(f"{'='*40}")
                print(f"Country:           {country_data['country']}")
                print(f"{'-'*40}")
                print(f"GDP:               {gdp} trillion USD")
                print(f"Unemployment Rate: {unemployment}%")
                print(f"Inflation Rate:    {inflation}%")
                print(f"Taxation:          {tax}%")
                print(f"Trade Balance:     {trade}")
                print(f"Investment Rate:   {investment_rate}%")
                print(f"Population Growth: {population_growth}%")
                print(f"Exchange Rate:     {exchange_rate}")
                print(f"{'='*40}\n")
                found = True
                break

        if not found:
            print("You entered the country name wrong or we don't have info for that country, sorry.")
