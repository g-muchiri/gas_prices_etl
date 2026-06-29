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