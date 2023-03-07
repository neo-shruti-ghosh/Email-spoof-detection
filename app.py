# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd
from flask import Flask, render_template, request
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


raw_mail_data = pd.read_csv('content/mail_data.csv')

mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

mail_data.loc[mail_data['Category'] == 'spam', 'Category',] = 0
mail_data.loc[mail_data['Category'] == 'ham', 'Category',] = 1

X = mail_data['Message']
Y = mail_data['Category']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=3)

feature_extraction = TfidfVectorizer(min_df=1, stop_words='english', lowercase=True)
X_train_features = feature_extraction.fit_transform(X_train)

Y_train = Y_train.astype('int')

model = LogisticRegression()
model.fit(X_train_features, Y_train)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    message = request.form['message']
    input_mail = [message]
    input_data_features = feature_extraction.transform(input_mail)
    prediction = model.predict(input_data_features)

    if (prediction[0] == 1):
        return render_template('index.html', prediction_text='Ham mail')
    else:
        return render_template('index.html', prediction_text='Spam mail')

if __name__ == '__main__':
    app.run(debug=True)
