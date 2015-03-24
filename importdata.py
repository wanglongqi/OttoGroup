# read in data
import pandas as pd
from numpy import array

def read_train():
	train = pd.read_csv('train.csv')
	toint = lambda x:int(x[-1:])
	y = map(toint,train.target)
	train.drop('target', axis=1, inplace=True)
	train.drop('id', axis=1, inplace=True)
	X = train.values
	y = array(y)
	return (X,y)


def read_test():
	test = pd.read_csv('test.csv')
	test.drop('id', axis=1, inplace=True)
	test = test.values
	return test
