import pickle
import pandas as pd
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score


file_path = r"friday.csv"
data = pd.read_csv(file_path)
X = data.drop(columns=["Label"])
y = data["Label"]
X = data.select_dtypes(include='int64')
y = y.astype('category').cat.codes
sc=['Src IP dec','Src Port','Dst IP dec','Dst Port','Protocol','Flow Duration','Total Fwd Packet','Total Bwd packets','Total Length of Fwd Packet','Total Length of Bwd Packet','Fwd Packet Length Max','Fwd Packet Length Min']
X=data[sc]
y=data['Label']

Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, test_size=0.3, random_state=42)


model = GaussianNB()
model.fit(Xtrain,ytrain)
ypred=model.predict(Xtest)
print(ypred)


acc=accuracy_score(ypred,ytest)
print(acc)

with open('nb_model.pkl', 'wb') as f:
    pickle.dump(model, f)