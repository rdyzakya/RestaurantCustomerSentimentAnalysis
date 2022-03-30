from utils import Preprocessor, load_pickle
import numpy as np

class RestaurantSentimentModel:
  def __init__(self):
    self.le = load_pickle('./model/label_encoder.p')
    self.vect = load_pickle('./model/tfidf_vect.p')
    self.preproc = Preprocessor()
    self.inner_model = load_pickle('./model/svm_model.p')
  
  def predict(self,X_,preproc=True,encoded=True):
    try:
      X = X_.copy()
    except:
      X = np.array(X_)
    if preproc:
      X = self.preproc(X)
    X = self.vect.transform(X)
    res = self.inner_model.predict(X)
    if encoded:
      return res
    return self.le.inverse_transform(res)