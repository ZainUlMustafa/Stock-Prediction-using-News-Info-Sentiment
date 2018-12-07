from sklearn import preprocessing
import quandl
quandl.ApiConfig.api_key = 'EuBXK6i-ViyNR-FCPLr_'
import pandas as pd
'''
online = False

def getStockData(path,stockName,Type):
	global online
	online = Type
	if online == True:
		return quandl.get('PSX/'+stockName.upper())
	if online == False:
		return pd.read_csv(path+stockName.upper()+'_01012010_06122018.csv')

def feature_engineering(From,To,data):
	global online
	if online == True:
		return data.iloc[From:To,4],data.iloc[From:To,0],data.iloc[From:To,1],data.iloc[From:To,2],data.iloc[From:To,3]
	if online == False:
		#close,open,high,low,volume
		return data.iloc[From:To,5],data.iloc[From:To,2],data.iloc[From:To,3],data.iloc[From:To,4],data.iloc[From:To,6]
'''  
def feature_arrange(From,To,data):
	#Order -> 8,1,2,3,4,5,6,7,9
	return data.iloc[From:To,8],data.iloc[From:To,1],data.iloc[From:To,2],data.iloc[From:To,3],data.iloc[From:To,4],data.iloc[From:To,5],data.iloc[From:To,6],data.iloc[From:To,7],data.iloc[From:To,9]