#!/usr/bin/env python3

import datetime as dt
import pandas_datareader as pdr
import matplotlib.pyplot as plt
from matplotlib import style

start = dt.datetime(2010, 1, 1)

end = dt.datetime.now()



def get_requirements():
    print("Data Analysis 1")
    print("Developed by Keith Faunce")
    print("\nProgram Requirements:\n"
          "1. Run demo.py\n"
          "2. If errors, more than likely missing installs.\n"
          "3. Test Python Package Installer: Working\n"
            + "a. pandas (if missing)\n"
            + "b. pandas-datareader (if missing)\n"
            + "c. matplotlib (if missing)\n"
          "4. Create at least three functions that are called by the program:\n"
            + "a. main(): calls at least two other functions.\n"
            + "b. get_requirements(): displays the program requirements.\n"
            + "c. data_analysis(): displays the following data.\n")
    
df = pdr.DataReader(["DJIA", "SP500"], "fred", start, end)


def data_analysis():
    
  print("\nPrint number of records: ")
  print(df.shape[0])


  print(df.columns)


  print("\nPrint data frame: ")
  print(df)


  print("\nPrint first five lines: ")
  print(df.head())


  print("\nPrint last five lines: ")
  print(df.tail())


  print("\nPrint first 2 lines: ")
  print(df[:2])


  print("\nPrint last 2 lines: ")
  print(df[-2:])


  style.use('ggplot')

  df['DJIA'].plot()
  df['SP500'].plot()
  plt.legend()
  plt.show()

    