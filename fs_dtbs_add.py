import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate('find-app-bacd9-firebase-adminsdk-6cyqt-e551b344da.json')
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection('users').document('alovelace')
doc_ref.set({
    'first': 'Ada',
    'last': 'Lovelace',
    'born': 1815
})

users_ref = db.collection(u'users')
docs = users_ref.stream()

for doc in docs:
    print('{} => {}'.format(doc.id, doc.to_dict()))