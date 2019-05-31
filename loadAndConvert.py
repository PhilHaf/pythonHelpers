import os
import posixpath
import csv 
import array as arr
import sys

def main():

	path = sys.argv[1]
	abspath = os.path.abspath(path)
	raw = readFile(abspath)
	converted = convertFile(raw)
	#print(converted)
	newArr = calcFile(converted)
	newCsv = createCsv(newArr)
	writeFile(newCsv)

def writeFile(tArr):
	
	absWritepath = os.path.abspath(sys.argv[2])
	resultFile = open(absWritepath,'wb')
	wr = csv.writer(resultFile)
	for x in tArr : 
		print(x)
		wr.writerow ([x])


def createCsv(tArr):

	header = ["created_at", "views", "addViews",  "signatures", "addSignatures"]
	csv = []
	csv.append("created_at,views,addViews,signatures,addSignatures")
	delimiter = ","
	for tEle in tArr:

		line = ""

		for i,key in enumerate(header):

			line+=str(tEle[key])
			
			if i!=(len(header)-1):

				line+=delimiter

		csv.append(line)

		#print(line)
	return csv

	
def calcFile(arr):
	plain = []

	for i,row in enumerate(arr):

		nLine = {}
		nLine['created_at'] = row['created_at']
		nLine['views'] = int(row['views'])
		nLine['signatures'] = int(row['signatures'])

		if i>0:
			
			nLine['addViews'] = int(row['views']) + plain[i-1]['addViews']
			nLine['addSignatures'] = int(row['signatures']) + plain[i-1]['addSignatures']

		else:
			nLine['addViews'] = int(row['views'])
			nLine['addSignatures'] = int(row['signatures'])


		plain.append(nLine)

	
	#print(plain)
	return plain


def readFile(path):

	raw = []

	with open(path,'rb') as csvfile: 
		#reader = csv.reader(csvfile, delimiter=';', quotechar='|') 
		fieldnames = ['created_at', 'views', 'signatures']
		reader = csv.DictReader(csvfile, fieldnames)

		for i,row in enumerate(reader):

			if i>0:
				raw.append(row)
				
				#sys.exit()

		return raw


def convertFile(raw):

	#for row in raw:
	
	return raw

if __name__ == '__main__':
	main()