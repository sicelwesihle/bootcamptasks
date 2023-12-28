import requests
import pandas as pd 
from io import StringIO

url = "https://raw.githubusercontent.com/donde-esta-la-biblioteca/Woolworths-Coles-IGA/main/Data/2021-04-23%20WOW%20Data.csv"

response = requests.get(url)

if response.status_code == 200:
    print(response.text[:200])

    data = pd.read_csv(StringIO(response.text))
    
    
    print("\nOriginal Data Types:")
    print(data.dtypes)

    
    categorical_columns = ['Brand', 'Product Name', 'Specials', 'Tag Description', 'Online Only', 'New Product', 'Ratings', 'Department', 'Product URL']
    data[categorical_columns] = data[categorical_columns].astype('category')

    numeric_columns = ['SKU', 'Price', 'Package Size', 'Price per unit']
    data[numeric_columns] = data[numeric_columns].apply(pd.to_numeric, errors='coerce')

    
    data['Availability'] = data['Availability'].astype('category')

 
    data['Date'] = pd.to_datetime(data['Date'])


    print("\nUpdated Data Types:")
    print(data.dtypes)
else:
    print(f"Failed to fetch data")

