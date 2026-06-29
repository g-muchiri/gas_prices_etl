def extract_gas_prices():
    import json
    import http.client
    import pandas as pd

    conn = http.client.HTTPSConnection("api.collectapi.com")

    headers = {
        'content-type': "application/json",
        'authorization': "apikey 7IVNn8p9MaSxTGXF9JoUo1:3TxTO2SWdXCXHuNaO89eoV"
        }


    conn.request("GET", "/gasPrice/stateUsaPrice?state=WA", headers=headers)

    res = conn.getresponse()
    data = res.read()

    data1 = json.loads(data)
    cities = data1['result']['cities']
    cities = pd.DataFrame(cities)
    return cities

def transform_gas_prices(cities):
    cities.drop(columns='lowername', inplace=True)
    transformed_cities = cities.rename(columns={'name':'city'})
    return transformed_cities


def load_gas_prices(transformed_cities):
    from sqlalchemy import create_engine, text
    ##import psycopg2
    import os
    from dotenv import load_dotenv
    
    load_dotenv()

    DATABASE_NAME = os.getenv('DATABASE_NAME')
    DATABASE_USER = os.getenv('DATABASE_USER')
    DATABASE_PORT = os.getenv('DATABASE_PORT')
    DATABASE_HOST = os.getenv('DATABASE_HOST')
    DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')

    engine = create_engine(f'postgresql+psycopg2://{DATABASE_USER}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}')
    with engine.connect() as conn:
        result = conn.execute(text('SELECT 1'))
        for i in result:
            print(i)

    transformed_cities.to_sql('cities_db',engine, if_exists='replace', index=False)
    print('Cities database has been created successfully')


def main():
    data1 = extract_gas_prices()
    data2 = transform_gas_prices(data1)
    load_gas_prices(data2)

    print("Our pipeline is now live")

if __name__ == "__main__":
    main()