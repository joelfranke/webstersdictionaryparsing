import StringIO
import re
import operator

inFile=open('websters.txt')

definition=0
wordcount={}

for line in inFile:
	if definition == 0:
		# Is the line the beginning of a definition, noted by 'Defn:' or '#. '
		definition_regex=re.compile('Defn:|^\d\. ')
		definition = 1
	elif definition == 1:
		definition_regex=re.compile('\S')
	result=definition_regex.search(line)
	if result:
		definition_line = line.replace('Defn: ','')
		words = definition_line.split(' ')
		for word in words:
			word_regex = re.compile('[a-zA-Z]*')
			realWord=word_regex.search(word)
			if realWord:
				# scrub punctuation, numbers and newline characters
				word = re.sub(r'[^\w\s]|[0-9]|\r|\n','',word)
				word = word.upper()
				if len(word)> 0 and word not in wordcount:
					if len(word)>1:
						wordcount[word] = 1
					elif word == 'A' or word == 'I':
						wordcount[word] = 1
				elif len(word)>0:
					if len(word)>1:
						wordcount[word] += 1
					elif word == 'A' or word == 'I':
						wordcount[word] += 1
	else:
		definition = 0
	
wordcount = sorted(wordcount.items(), key=operator.itemgetter(1),reverse=True)

#limit output to first 100 items
print wordcount[:99]	
inFile.close()
