import pandas as pd
import requests


all_docks = {
    "tokyodocomo":
    [
        126,
        127,
        207,
        381,
        410,
        435,
        1838,
        2212,
        3322,
        3401,
        3402,
        3769,
        10092,
        10093,
        10094,
        10095,
        10096,
        10097,
        10104,
        10107,
        10108,
        10109,
        10110,
        10112,
        10114,
        10122,
        10147,
        10174,
        10196,
        10223,
        10275,
        10276,
        10278,
        10311,
        10343,
        10406,
        10434,
        10512,
        10557,
        10558,
        10630,
        10732,
        10733,
        10780,
        10794,
        10847,
        10860,
        10898,
        10916,
        10943,
        11012
    ],
    "tokyo":
    [
        4013,
        12887,
        13805
    ]
}

def get_data(city, lot_id):
    
    url = f"https://gladys.geog.ucl.ac.uk/bikesapi/loadgraphavail.php?scheme={city}&interval=3600&tfl_id={lot_id}"

    response = requests.get(url)
    data = response.json()

    # Convert to DataFrame
    df = pd.DataFrame({
        'timestamp_unix': data['timestamp_unix'],
        'docked_bikes': data['docked_bikes'],
        'floating_bikes': data['floating_bikes'],
        'spaces_available': data['spaces_available'],
        'unbalanced': data['unbalanced']
    })

    # Convert Unix timestamp to human-readable datetime
    df['datetime'] = pd.to_datetime(df['timestamp_unix'], unit='s', utc=True)
    df["type"] = city
    df["id"] = lot_id
    
    return df

df = pd.DataFrame()

for city, lots in all_docks.items():
    
    for lot_id in lots:
        
        _df = get_data(city, lot_id)
        
        df = pd.concat([_df, df])

df.to_csv("toyosu_bike_sharing_20250303.csv", index=False)