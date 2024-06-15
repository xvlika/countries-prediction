import shelve

with shelve.open("countries") as db:
    countries_gdp = db['countries_gdp']

    for country_data in countries_gdp:
        country = country_data['country']
        gdp = country_data['gdp']
        print(f"Country: {country}, GDP: {gdp} trillion USD")