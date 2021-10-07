import pandas as pd
import numpy as np
import datetime as dt


def load_json():
    data = pd.read_json("nasa_data.json", convert_dates=['year'])
    data.drop(["geolocation", ":@computed_region_cbhk_fwbd", ":@computed_region_nnqa_25f4"], inplace=True, axis=1)
    meteors = data.replace('', np.nan)
    meteors = meteors.rename(columns={"recclass": "class", "reclat": "lattitude", "reclong": "longitude"})
    meteors["year"] = pd.to_datetime(meteors.year, errors="coerce")
    meteors["lattitude"] = meteors.lattitude.astype(float, errors='ignore')
    meteors["longitude"] = meteors.longitude.astype(float, errors='ignore')
    return meteors


def main():
    loaded_data = load_json()
    loaded_data.to_csv('meteors.csv', index=False)


if __name__ == "__main__":
    main()
