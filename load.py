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
