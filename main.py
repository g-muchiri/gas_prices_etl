from extract import extract_gas_prices
from transform import transform_gas_prices
from load import load_gas_prices

def main():
    data1 = extract_gas_prices()
    data2 = transform_gas_prices(data1)
    load_gas_prices(data2)

    print("Our pipeline is now live")


if __name__ == "__main__":
    main()