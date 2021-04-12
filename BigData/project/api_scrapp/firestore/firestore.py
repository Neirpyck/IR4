import firebase_admin as fb
from firebase_admin import firestore
import pandas as pd

cred = fb.credentials.Certificate('restaurants-99612-firebase-adminsdk-5dghw-34c9f25e97.json')
default_app = fb.initialize_app(cred)
db = firestore.client()
doc_ref = db.collection(u'restaurants3')

df = pd.read_csv('../bddfinal.csv', delimiter=';')
tmp = df.to_dict(orient='records')
list(map(lambda x: doc_ref.add(x), tmp))
