import shelve

with shelve.open("countries") as db:
    db['countries_gdp'] = [
        {
            "country": "United States", "gdp": 25.43, 
            "unemployment": 4.0,
            "inflation": 2.1,
            "tax_percentage": 27.1,
            "trade_balance": -621,
            "investment_rate": 18.6,
            "population_growth": 0.7,
            "exchange_rate": 1.0
        },
        {
            "country": "China", "gdp": 14.72,
            "unemployment": 5.3,
            "inflation": 2.5,
            "tax_percentage": 17.1,
            "trade_balance": 370, 
            "investment_rate": 43.3,
            "population_growth": 0.3,
            "exchange_rate": 6.4
        },
        {
            "country": "Japan", "gdp": 4.25,
            "unemployment": 2.6,
            "inflation": 0.5, 
            "tax_percentage": 30.6,
            "trade_balance": 15,
            "investment_rate": 23.4,
            "population_growth": -0.2,
            "exchange_rate": 110.0
        },
        {
            "country": "Germany", "gdp": 3.85,
            "unemployment": 3.2,
            "inflation": 1.7,
            "tax_percentage": 38.2,
            "trade_balance": 210,
            "investment_rate": 20.1,
            "population_growth": 0.2,
            "exchange_rate": 0.9
        },
        {
            "country": "India", "gdp": 3.41,
            "unemployment": 7.0,
            "inflation": 3.9,
            "tax_percentage": 17.7, 
            "trade_balance": -101,
            "investment_rate": 30.1,
            "population_growth": 1.2,
            "exchange_rate": 74.0
        },
        {
            "country": "United Kingdom", "gdp": 2.67,
            "unemployment": 4.8,
            "inflation": 1.5,
            "tax_percentage": 33.3,
            "trade_balance": -125,
            "investment_rate": 17.1,
            "population_growth": 0.6, 
            "exchange_rate": 0.75
        },
        {
            "country": "France", "gdp": 2.63,
            "unemployment": 8.5,
            "inflation": 1.3, 
            "tax_percentage": 45.4,
            "trade_balance": -74,
            "investment_rate": 23.0,
            "population_growth": 0.2,
            "exchange_rate": 0.9
        },
        {
            "country": "Russia", "gdp": 2.24,
            "unemployment": 6.1,
            "inflation": 3.4, 
            "tax_percentage": 22.2,
            "trade_balance": 162,
            "investment_rate": 24.6,
            "population_growth": -0.1,
            "exchange_rate": 72.0
        },
        {
            "country": "Canada", "gdp": 2.16, 
            "unemployment": 5.8,
            "inflation": 2.0, 
            "tax_percentage": 31.2,
            "trade_balance": -13,
            "investment_rate": 22.5,
            "population_growth": 1.1,
            "exchange_rate": 1.3
        },
        {
            "country": "Italy", "gdp": 2.04,
            "unemployment": 9.1,
            "inflation": 0.9, 
            "tax_percentage": 42.4, 
            "trade_balance": 54,
            "investment_rate": 17.5,
            "population_growth": -0.2,
            "exchange_rate": 0.9
        },
        {
            "country": "Brazil", "gdp": 1.92,
            "unemployment": 12.0,
            "inflation": 3.7,
            "tax_percentage": 33.1,
            "trade_balance": 48,
            "investment_rate": 15.4,
            "population_growth": 0.8,
            "exchange_rate": 5.2
        },
        {
            "country": "Australia", "gdp": 1.69,
            "unemployment": 4.2,
            "inflation": 1.8,
            "tax_percentage": 27.8,
            "trade_balance": 25,
            "investment_rate": 26.2,
            "population_growth": 1.3,
            "exchange_rate": 1.4
        },
        {
            "country": "South Korea", "gdp": 1.67, 
            "unemployment": 3.8,
            "inflation": 1.1, 
            "tax_percentage": 24.1, 
            "trade_balance": 70,
            "investment_rate": 29.1,
            "population_growth": 0.3,
            "exchange_rate": 1120.0
        },
        {
            "country": "Mexico", "gdp": 1.46,
            "unemployment": 4.0,
            "inflation": 4.1,
            "tax_percentage": 16.5,
            "trade_balance": -14,
            "investment_rate": 21.9,
            "population_growth": 1.0, "exchange_rate": 20.0
        },
        {
            "country": "Spain", "gdp": 1.41,
            "unemployment": 14.0,
            "inflation": 0.6, 
            "tax_percentage": 35.4,
            "trade_balance": -35,
            "investment_rate": 21.2,
            "population_growth": 0.0,
            "exchange_rate": 0.9
        }
    ]
