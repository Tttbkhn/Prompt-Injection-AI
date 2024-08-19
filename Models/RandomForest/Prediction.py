import joblib
import re

# load model
rf_clf = joblib.load('random_forest_model.pkl')
vectorizer = joblib.load('tfidf_vectorizer.pkl')
label_encoder = joblib.load('label_encoder.pkl')

# user input
input = input('please input....')
custom_input = [f'''{input}''']

# convert the input to string
custom_input = [str(x) for x in custom_input]

# pre-process data
custom_input_transformed = vectorizer.transform(custom_input)

# prediction
custom_prediction = rf_clf.predict(custom_input_transformed)

# convert the prediction to original label
custom_prediction_label = label_encoder.inverse_transform(custom_prediction)

print(f"Prediction: {custom_prediction_label}")

