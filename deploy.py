from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
#load the model
model = pickle.load(open(r'C:\Users\dell\Documents\Tako\Credit Risk Loan Prediction\DTclassifier1.sav','rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods =['POST','GET'])
def predict():
    Gender = float(request.form['gender'])
    Married = float(request.form['married'])
    Dependents = float(request.form['dependents'])
    Education = float(request.form['education'])
    Self_Employed = float(request.form['self_employed'])
    ApplicantIncome = float(request.form['applicantincome'])
    LoanAmount = float(request.form['loanamount'])
    Loan_Amount_Term = float(request.form['loan_amount_term'])
    Credit_History = float(request.form['credit_history'])
    Property_Area = float(request.form['property_area'])
    result = model.predict([[Gender, Married, Dependents, Education, Self_Employed,ApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History,Property_Area]])[0]
    return render_template('index.html', **locals())


if __name__ == '__main__' :
    app.run(debug = True)