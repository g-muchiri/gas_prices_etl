def transform_gas_prices(cities):
    cities.drop(columns='lowername', inplace=True)
    transformed_cities = cities.rename(columns={'name':'city'})
    return transformed_cities
