# Davis Rogers
import sys
import pandas as pd
import matplotlib.pyplot as plt
import requests
import openpyxl
if len(sys.argv) < 3:
	print("Please must supply the latitude and longitude")
lat,lon = float(sys.argv[1]),float(sys.argv[2])
url = "https://api.open-meteo.com/v1/forecast"+\
	f"?latitude={lat}&longitude={lon}&hourly=temperature_2m"
data = requests.get(url).json()
df = pd.DataFrame.from_records(data["hourly"])
df.time = pd.to_datetime(df.time)
df.temperature_2m = df.temperature_2m*(9/5) + 32
df.set_index("time",inplace=True)
df.to_excel("forecast.xlsx")
df.plot()
plt.savefig("forecast.png",bbox_inches="tight")
plt.tight_layout()
plt.show
