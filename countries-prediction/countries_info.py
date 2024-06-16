import shelve

class Country:
    def __init__(self,country,gdp,gdp_growth_rate,unemployment,inflation,tax_percentage,investment_rate,population_growth,exchange):
        self.country = country
        self.gdp = gdp
        self.gdp_growth_rate = gdp_growth_rate
        self.unemployment = unemployment
        self.inflation = inflation
        self.tax_percentage = tax_percentage
        self.investment_rate = investment_rate
        self.population_growth = population_growth
        self.exchange = exchange
    
    def show_country(self):
        print(f"{'='*40}")
        print(f"Country:           {self.country}")
        print(f"{'-'*40}")
        print(f"GDP:               {self.gdp} trillion USD")
        print(f"GDP Growth:        {self.gdp_growth_rate}%")
        print(f"Unemployment Rate: {self.unemployment}%")
        print(f"Inflation Rate:    {self.inflation}%")
        print(f"Taxation:          {self.tax_percentage}%")
        print(f"Trade Balance:     {self.trade_balance}")
        print(f"Investment Rate:   {self.investment_rate}%")
        print(f"Population Growth: {self.population_growth}%")
        print(f"Exchange Rate:     {self.exchange_rate}")
        print(f"{'='*40}\n")

    def estimate_future_gdp(self, years):
        future_gdp = self.gdp * (1 + (self.gdp_growth_rate - self.inflation - (self.tax_percentage / 100) + (self.trade_balance / self.gdp) + (self.investment_rate / 100) + (self.population_growth / 100)) / 100) ** years
        return future_gdp
    
countries_data = [
    Country("United States", 25.43, 2.2, 4.0, 2.1, 27.1, -621, 18.6, 0.7, 1.0),
    Country("China", 14.72, 6.5, 5.3, 2.5, 17.1, 370, 43.3, 0.3, 6.4),
    Country("Japan", 4.25, 0.8, 2.6, 0.5, 30.6, 15, 23.4, -0.2, 110.0),
    Country("Germany", 3.85, 1.5, 3.2, 1.7, 38.2, 210, 20.1, 0.2, 0.9),
    Country("India", 3.41, 7.3, 7.0, 3.9, 17.7, -101, 30.1, 1.2, 74.0),
    Country("United Kingdom", 2.67, 1.3, 4.8, 1.5, 33.3, -125, 17.1, 0.6, 0.75),
    Country("France", 2.63, 1.4, 8.5, 1.3, 45.4, -74, 23.0, 0.2, 0.9),
    Country("Russia", 2.24, 1.8, 6.1, 3.4, 22.2, 162, 24.6, -0.1, 72.0),
    Country("Canada", 2.16, 1.9, 5.8, 2.0, 31.2, -13, 22.5, 1.1, 1.3),
    Country("Italy", 2.04, 1.0, 9.1, 0.9, 42.4, 54, 17.5, -0.2, 0.9),
    Country("Brazil", 1.92, 0.5, 12.0, 3.7, 33.1, 48, 15.4, 0.8, 5.2),
    Country("Australia", 1.69, 2.5, 4.2, 1.8, 27.8, 25, 26.2, 1.3, 1.4),
    Country("South Korea", 1.67, 3.0, 3.8, 1.1, 24.1, 70, 29.1, 0.3, 1120.0),
    Country("Mexico", 1.46, 2.1, 4.0, 4.1, 16.5, -14, 21.9, 1.0, 20.0),
    Country("Spain", 1.41, 1.6, 14.0, 0.6, 35.4, -35, 21.2, 0.0, 0.9)
]
