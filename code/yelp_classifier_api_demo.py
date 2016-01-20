from bottle import run,route
import cPickle as pickle

clf = pickle.load(open('clf.pkl','rb'))

@route('/<funny:int>,<useful:int>')
def predict(funny,useful):
  return {'prediction': clf.predict([funny,useful])[0]}

if __name__ == '__main__':
  run(host='localhost',port='5001')
