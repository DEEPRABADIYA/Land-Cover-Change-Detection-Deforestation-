import rasterio
import numpy as np

#code for Temperature Condition Index
file_path = "D:/Eosproject/Eosproject/LST/2014.tif"

with rasterio.open(file_path) as dataset:
    tci_data = dataset.read(1)
    tci_data[tci_data == 0] = np.nan
    print(tci_data)