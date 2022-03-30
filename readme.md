Notebook Link : https://colab.research.google.com/drive/1LZObwF-8uGtmL0nSPdv2xBABWsADUabS?authuser=2#scrollTo=-CO8Af4IdIzS
Kamus Alay Source : 'https://raw.githubusercontent.com/nasalsabila/kamus-alay/master/colloquial-indonesian-lexicon.csv'

How to use the model:
1. Download this repository
2. Download and install scikit learn, pandas, and numpy
3. Write the following code

```python
from model import RestaurantSentimentModel

# initialize model
my_model = RestaurantSentimentModel()

# use model to predict
# preproc : True or False (True if you want to preprocess your input data aqnd false if you don't want, True is reccomended and the default value)
# encode : True or False (True if you want the result is in the form of 0 and 1 and False if you want the result is in the form of 'negative' or 'positive')
# * 0 : negative , 1 : positive
my_model.predict(["wah enak banget","menurut saya sedikit kurang enak"],preproc=True,encode=False)
```
