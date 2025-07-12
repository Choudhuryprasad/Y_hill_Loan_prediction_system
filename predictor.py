import numpy as np
import joblib
import sys
import json


def preprocess_data(Gender, Married, Education, Self_Employed, ApplicantIncome,
                   CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                   Property_Area):
    try:
        
        ApplicantIncome = float(ApplicantIncome)
        CoapplicantIncome = float(CoapplicantIncome)
        LoanAmount = float(LoanAmount)
        Loan_Amount_Term = float(Loan_Amount_Term)
        Credit_History = float(Credit_History)

        
        gender_map = {'Male': 1, 'Female': 0}
        married_map = {'Yes': 1, 'No': 0}
        education_map = {'Graduate': 1, 'Not Graduate': 0}
        employed_map = {'Yes': 1, 'No': 0}
        property_area_map = {'Urban': 2, 'Semiurban': 1, 'Rural': 0}

        gender = gender_map.get(Gender, 0)
        married = married_map.get(Married, 0)
        education = education_map.get(Education, 0)
        employed = employed_map.get(Self_Employed, 0)
        property_area = property_area_map.get(Property_Area, 0)

        test_data = [[gender, married, education, employed, ApplicantIncome,
                      CoapplicantIncome, LoanAmount, Loan_Amount_Term, Credit_History,
                      property_area]]

        
        trained_model = joblib.load("model.pkl")

        
        prediction = trained_model.predict(test_data)

        return prediction
    except Exception as e:
        return f"Error occurred during data preprocessing or prediction: {str(e)}"


def main():
    if len(sys.argv) > 1:
        data_string = sys.argv[1]
        data = json.loads(data_string)

        try:
            prediction = preprocess_data(data.get("Gender"), data.get("Married"), 
                                          data.get("Education"), data.get("Self_Employed"),
                                          data.get("ApplicantIncome"), data.get("CoapplicantIncome"), 
                                          data.get("LoanAmount"), data.get("Loan_Amount_Term"), 
                                          data.get("Credit_History"), data.get("Property_Area"))
            
            if isinstance(prediction, np.ndarray):
                print(int(prediction[0])) 
            else:
                print(prediction)  
        except KeyError as e:
            print(f"Error: Missing key {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")
    else:
        print("Error: No data provided.")

if __name__ == "__main__":
    main()
