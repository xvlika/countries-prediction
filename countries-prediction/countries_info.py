import shelve

with shelve.open("countries") as db:
    db['countries_gdp'] = [
        {"country" : "United States", "gdp" : 25.43},
        {"country" : "China", "gdp" : 14.72},
        {"country" : "Japan", "gdp" : 4.25},
        {"country" : "Germany", "gdp" : 3.85},
        {"country" : "India", "gdp" : 3.41},
        {"country" : "United Kingdom", "gdp" : 2.67},
        {"country" : "France", "gdp" : 2.63},
        {"country" : "Russia", "gdp" : 2.24},
        {"country" : "Canada", "gdp" : 2.16},
        {"country" : "Italy", "gdp" : 2.04},
        {"country" : "Brazil", "gdp" : 1.92},
        {"country" : "Australia", "gdp" : 1.69},
        {"country" : "South Korea", "gdp" : 1.67},
        {"country" : "Mexico", "gdp" : 1.46},
        {"country" : "Spain", "gdp" : 1.41}
    ]