import numpy as np
import pandas as pd
import nltk
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.pipeline import Pipeline
from nltk.tokenize import word_tokenize, RegexpTokenizer
from nltk.stem import WordNetLemmatizer
english = WordNetLemmatizer()


df = pd.read_csv('papers.csv')

paper_dict = {}
for i in range(len(df)):
  id = df['id'][i]
  auth = df['authors'][i]
  a = ""
  rem = set([",", "[", "]", "'"])
  for x in auth:
    if x not in rem:
      a += x
  doc = df['title'][i] +  " " + a + " " + df['categories'][i] + " " + df['abstract'][i]
  paper_dict[id] = doc
  
  
print(len(df))
def_set = set()
all_content = list()
for id in paper_dict:
  def_id = id 
  contents = paper_dict[def_id]
  all_content.append(contents)
  temp = list(contents.split())
  def_set.update(temp)

stop = set(stopwords.words('english'))
temp = set(); terms = set()

for entry in def_set:
  if entry.lower() not in stop:
    temp.add(entry)

terms = set()
for i in temp:
  terms.add(english.lemmatize(i.lower()))

pipe = Pipeline([('count', CountVectorizer(vocabulary=terms)),('tfid', TfidfTransformer())]).fit(all_content) 
tf = pipe['count'].transform(all_content).toarray()
w = pipe['tfid'].fit_transform(tf).toarray()
