import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
# import seaborn as sns
import plotly.express as px
import streamlit as st
import warnings
warnings.simplefilter("ignore")

data = pd.read_csv("Crop_recommendation.csv")

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
scale = StandardScaler()
minmax = MinMaxScaler()
data_scale = pd.DataFrame(scale.fit_transform(data.iloc[:,:-1]),columns = data.columns[:-1])
data_scale_min = pd.DataFrame(minmax.fit_transform(data.iloc[:,:-1]),columns = data.columns[:-1])
X = data.drop("label",axis=1)
y = data["label"]
labels = data["label"].unique()
from sklearn.model_selection import train_test_split 
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, y, test_size=.25, random_state = 11)
from sklearn.metrics import accuracy_score,confusion_matrix, classification_report
scores = pd.DataFrame(columns = ["Model","Accuracy"])

from sklearn.ensemble import RandomForestClassifier
RFC = RandomForestClassifier()
RFC.fit(Xtrain, Ytrain)
print(accuracy_score(Ytest, RFC.predict(Xtest)))
# scores = scores.append({"Model":"Random Forest","Accuracy": accuracy_score(Ytest, RFC.predict(Xtest))*100},ignore_index=True)

#creating a header with Header section link
# st.markdown("<h1 style='text-align: center; color: #0b0c0c;'>Crop Recommendation Model</h1>", unsafe_allow_html=True)

st.set_page_config(
    page_title="Crop Analysis",
    page_icon="🎋",
    layout="wide"
)
# st.sidebar.success("Please select page here")
st.markdown("<h1 style='text-align: center; color: green;'>Crop Recommendation Analysis</h1>", unsafe_allow_html=True)
st.write("This is a simple web application which will help in recommending the type of crop.")
st.divider()
st.write("The application is built using the Random Forest Classifier algorithm.")
st.write("The dataset used for training the model is taken from Kaggle.")
st.write("The dataset contains 22 columns and 2200 rows.")
st.write("This is the first 5 rows of the data.")
st.write(data.head())
st.divider()
st.write("Information about the Data")
st.columns((1,1,1))[1].write(data.dtypes)
st.divider()
st.write("Description of the data.")
st.write(data.describe())
st.divider()


import seaborn as sns

st.write("Checking the outliers of the data.")
col = data.columns

for column in range(len(col)):
    if data[col[column]].dtype != "object": 
        fig, ax = plt.subplots()
        sns.boxplot(data[col[column]],ax=ax)
        # fig.set_size_inches(1,1)
        ax.set_xlabel(col[column], c="r") 
        st.pyplot(fig)

st.write("Checking the distribution of the data.")
for column in range(len(col)):
    if data[col[column]].dtype != "object": 
        fig, ax = plt.subplots()
        sns.distplot(data[col[column]],ax=ax)
        # fig.set_size_inches(1,1)
        ax.set_xlabel(col[column], c="r") 
        st.pyplot(fig)


#encoding
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
data["label"] = le.fit_transform(data["label"])


