# conda activate py36gputorch100 && \
# cd /mnt/1T-5e7/mycodehtml/ML_theory/DHKim/003_Regression_ananalysis_and_Timeseries_analysis/01.01_statsmodels_package && \
# rm e.l && python main.py \
# 2>&1 | tee -a e.l && code e.l

# ================================================================================
import statsmodels.api as sm
import matplotlib.pyplot as plt

# ================================================================================
# data=sm.datasets.get_rdataset(dataname="Titanic",package="datasets")

# ================================================================================
# print("data",data)
# <class 'statsmodels.datasets.utils.Dataset'>

# ================================================================================
# print("data",data.package)
# datasets

# ================================================================================
# print("data",data.title)
# Survival of passengers on the Titanic

# ================================================================================
# print("data",data.data)
#    Class     Sex    Age Survived  Freq
# 0    1st    Male  Child       No     0
# 1    2nd    Male  Child       No     0

# ================================================================================
# print("data",data.__doc__)
# +---------+-----------------+
# | Titanic | R Documentation |
# +---------+-----------------+

# Survival of passengers on the Titanic

# ================================================================================
# c data: time-series data
# data=sm.datasets.get_rdataset(dataname="precip")
# print("data",data.data.head(2))
#    dat
# 0  67.0
# 1  54.7

# ================================================================================
# df=data.data
# df.plot()
# plt.title(data.title)
# plt.show()
# /home/young/Pictures/2019_05_07_07:22:23.png

# ================================================================================
# c data: time-series data on Luteinizing Hormone 
# data=sm.datasets.get_rdataset(dataname="lh")
# df=data.data
# df.plot(x="time",y="value")
# plt.title(data.title)
# plt.show()
# /home/young/Pictures/2019_05_07_07:24:15.png

# ================================================================================
# c data: seasonality time-series data, Monthly deaths from lung diseases in the UK
# data=sm.datasets.get_rdataset("deaths","MASS")
# df=data.data
# print(df.tail())
#            time  value
# 67  1979.583333   1354
# 68  1979.666667   1333

# * Data
# 1 year=1.0
# 1 month=1/12

# ================================================================================
def yearfraction2datetime(yearfraction,startyear=0):
   import datetime
   import dateutil
   year=int(yearfraction)+startyear
   month=int(round(12*(yearfraction-year)))
   delta=dateutil.relativedelta.relativedelta(months=month)
   date=datetime.datetime(year,1,1)+delta
   return date

# ================================================================================
# time_col_data=df.time
# print("time_col_data",time_col_data)
# 0     1974.000000
# 1     1974.083333

# converted_time_data=time_col_data.map(yearfraction2datetime)
# print("converted_time_data",converted_time_data)
# 0    1974-01-01
# 1    1974-02-01

# df["datetime"]=converted_time_data
# print(df.tail())
#            time  value   datetime
# 67  1979.583333   1354 1979-08-01
# 68  1979.666667   1333 1979-09-01

# ================================================================================
# df.plot(x="datetime",y="value")
# plt.title(data.title)
# plt.show()
# /home/young/Pictures/2019_05_07_07:32:45.png

# ================================================================================
# # c data: time-series data which shows seasonality and increasing trend
# data=sm.datasets.get_rdataset(dataname="AirPassengers")
# df=data.data
# # print("df.tail()",df.tail())
# #             time  value
# # 139  1960.583333    606
# # 140  1960.666667    508

# # ================================================================================
# time_col_data=df.time
# # print("time_col_data",time_col_data)
# # 0      1949.000000
# # 1      1949.083333

# converted_time_data=time_col_data.map(yearfraction2datetime)
# # print("converted_time_data",converted_time_data)
# # 0     1949-01-01
# # 1     1949-02-01

# df["datetime"]=converted_time_data

# print("df.tail()",df.tail())
# #      time           value   datetime
# # 139  1960.583333    606     1960-08-01
# # 140  1960.666667    508     1960-09-01

# df.plot(x="datetime",y="value")
# plt.title(data.title)
# plt.show()
# /home/young/Pictures/2019_05_07_07:36:58.png

# ================================================================================
