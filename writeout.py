#write out submission data
import pandas as pd
def writeout(p,filename='submission.csv'):
	# p should has 9 columns
	out = pd.DataFrame(p)
	tostring = lambda x : 'Class_'+str(x)
	out.columns = map(tostring, out.columns+1)
	out.index = out.index + 1
	out.to_csv(filename,index_label='id')
