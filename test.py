import pandas as pd

def main():
    df1 = pd.read_csv("https://cals.arizona.edu/AZMET/data/0620rd.txt")
    # Define the column names
    df1.columns = ['Year', 
                'DOY',
                'Station Num',
                'Air Max',
                'Air Min',
                'Air Mean',
                'RH Max',
                'RS Min',
                'RH Mean',
                'VPD Mean',
                'Solar Rad',
                'Precip',
                'Four Soil Temp Max',
                'Four Soil Temp Min',
                'Four Soil Temp Mean',
                'Twenty Soil Temp Max',
                'Twenty Soil Temp Min',
                'Twenty Soil Temp Mean',
                'Wind Speed',
                'Wind Vec Mag',
                'Wind Vec Dir',
                'Wind Dir StDev',
                'Max Wind Speed',
                'Heat Units',
                'Ref Evapo',
                'Ref Evapo Pen',
                'Actual Vap',
                'Dewpoint Daily']

    df2 = df1.filter(items=['DOY','Air Max'])

    print(df1)
    print(df2)

if __name__ == '__main__':
    main()