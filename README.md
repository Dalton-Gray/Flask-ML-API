## ML-Model-Flask-Deployment
This is a demo project to show how Machine Learn Models are deployed the using Flask API

### Dependencies
You must have Scikit Learn, Pandas (for Machine Leraning Model) and Flask (for API) installed.

### Project Structure
This project has four major parts :
1. model.py - This contains code for the Machine Learning model to predict gender based on training data in 'shoe_data.csv' file.
2. app.py - This contains a Flask API that receives body metrics through GUI or API calls, computes the precited value based on our model and returns it.
3. request.py - This uses requests module to call APIs already defined in app.py and dispalys the returned value.
4. templates - This folder contains the HTML template to allow user to enter body metrics and displays the prediction.

