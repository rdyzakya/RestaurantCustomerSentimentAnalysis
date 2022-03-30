import pandas as pd
import re
import pickle

kamus_alay_url = 'https://raw.githubusercontent.com/nasalsabila/kamus-alay/master/colloquial-indonesian-lexicon.csv'
class Preprocessor:
  def __init__(self,kamus_alay_url=kamus_alay_url):
    kamus_alay = pd.read_csv(kamus_alay_url)
    kamus_alay = kamus_alay.drop_duplicates(subset=['slang'])
    kamus_alay.index = kamus_alay['slang']
    kamus_alay = kamus_alay['formal']
    kamus_alay.index = r'\b'+ kamus_alay.index + r'\b'
    self.kamus_alay = kamus_alay
  
  def _preproc_df(self,data):
    data_ = data.copy()
    data_ = data_.str.lower()
    data_ = data_.str.replace(r'[^\w\s]',' ',regex=True)
    data_ = data_.str.replace(r'\d',' ',regex=True)
    data_ = data_.str.replace(r'(\s)\1{1,}',r'\1',regex=True)
    data_ = data_.str.replace(r'(.)\1{2,}',r'\1',regex=True)
    return data_
  
  def _normal_preprocess(self,data):
    if str(type(data)) == "<class 'pandas.core.series.Series'>":
      return self._preproc_df(data)
    elif str(type(data)) == "<class 'numpy.ndarray'>" or type(data) == list:
      data_ = pd.Series(data)
      return self._preproc_df(data_)
    elif type(data) == str:
      data_ = pd.Series([data])
      return self._preproc_df(data_).iloc[0]
    else:
      raise Exception("Data should be string/list/numpy array/ pandas series, your data type:",type(data))
  
  def preprocess(self,data):
    data_ = self._normal_preprocess(data)
    if type(data) != str:
      data_ = data_.replace(self.kamus_alay,regex=True)
      return data_
    # else if str
    data_ = data_.split()
    for w in range(len(data_)):
      appended_word = r'\b' + data_[w] +  r'\b'
      if appended_word in self.kamus_alay.index:
        data_[w] = re.sub(appended_word,self.kamus_alay[appended_word],data_[w])
    data_ = " ".join(data_)
    return data_
  
  def __call__(self,inputs):
    return self.preprocess(inputs)


def load_pickle(filename):
    file = open(filename,'rb')
    object_file = pickle.load(file)
    file.close()
    return object_file