import shelve
import math

def display_current():
    while True:
        userChoice = input("Enter which country info you want to see (if you want all enter: all, to quit enter: -1): ").lower()
        
        if userChoice == "-1":
            print("Exiting the program.")
            break
        
        with shelve.open("countries") as db:
            countries_gdp = db['countries_gdp']
            
            if userChoice == "all":
                for country_data in countries_gdp:
                    country = country_data['country']
                    gdp = country_data['gdp']
                    gdp_growth = country_data['gdp_growth_rate']
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
                    print(f"GDP Growth:        {gdp_growth_rate}%")
                    print(f"Unemployment Rate: {unemployment}%")
                    print(f"Inflation Rate:    {inflation}%")
                    print(f"Taxation:          {tax}%")
                    print(f"Trade Balance:     {trade}")
                    print(f"Investment Rate:   {investment_rate}%")
                    print(f"Population Growth: {population_growth}%")
                    print(f"Exchange Rate:     {exchange_rate}")
                    print(f"{'='*40}\n")
            else:
                choices = userChoice.split(',')
                for choice in choices:
                    choice = choice.strip()
                    found = False
                    for country_data in countries_gdp:
                        country = country_data['country'].lower()
                        if choice == country:
                            gdp = country_data['gdp']
                            gdp_growth = country_data['gdp_growth_rate']
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
                            print(f"GDP Growth:        {gdp_growth_rate}%")
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
                        print(f"Information for '{choice}' is not available or the country name is incorrect.")

def est_future_gdp(current_gdp, years , gdp_growth , inflation, population_growth, tax , trade , investment, exchange):
    exchange_ratio = math.log()
    future_gdp = current_gdp * (1+(gdp_growth - inflation-(tax/100)+(trade/current_gdp)+(investment/100)+(population_growth/100)/100))**years
    return future_gdp

def country_after():
    user_input_year = int(input("Enter how many year simulation do you want: "))
    country_name = input("Enter country/countries names: ").strip().lower()
    with shelve.open("countries") as db:
        countries_gdp = db('countries_gdp')
        found = False
        for country_data in countries_gdp:
            country = country_data['country']
            gdp = country_data['gdp']
            gdp_growth = country_data['gdp_growth_rate']
            unemployment = country_data["unemployment"]
            inflation = country_data["inflation"]
            tax = country_data["tax_percentage"]
            trade = country_data["trade_balance"]
            investment_rate = country_data['investment_rate']
            population_growth = country_data["population_growth"]
            exchange_rate = country_data["exchange_rate"]
        for country_data in countries_gdp:
            if country_data.lower() == country.lower():
                found = True
                future_gdp = est_future_gdp(gdp,user_input_year,gdp_growth,inflation,population_growth,tax,trade,investment_rate,exchange_rate)            
                print(f"{country.capitalize()} gdp after {user_input_year} years is {future_gdp}")

    
def main():
    print("Enter your choice: ")
    print("1.Display country's current info")
    print("2.Display country's info after X years later")
    print("3.Manual simulation (user inputs data of country)")
    choice = int(input("Enter Your Choice: "))
    if choice == 1:
        display_current()
    elif  choice == 2: 
        country_after()


if __name__ == "__main__":
    main()
