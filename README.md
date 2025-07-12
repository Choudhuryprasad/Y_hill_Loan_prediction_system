# Y-Hill Loan Prediction System

This project is a machine learning-powered web application designed to predict loan eligibility based on user-submitted data. It includes both a backend machine learning pipeline and a Node.js-based API server to interact with the model.

## 🧠 Project Components

- **Model Training & Prediction**
  - `project01.ipynb`: Jupyter Notebook used for data analysis and model training.
  - `predictor.py`: Loads the trained model (`model.pkl`) and defines prediction logic.
  - `model.pkl`: Trained machine learning model saved using `pickle`.

- **API Server**
  - `app.js`: Node.js + Express server that serves predictions via a REST API.
  - `package.json`: Node.js project metadata and dependencies.
  - `sample_input.json`: Sample input to test the prediction API.

- **Data**
  - `dataset/train_u6lujuX_CVtuZ9i.csv`: Training dataset.
  - `dataset/test_Y3wMUE5_7gLdaTN.csv`: Test dataset.

## 🚀 How to Run

### 1. Clone & Install Dependencies

```bash
git clone <repo-url>
cd Y_hill_Loan_prediction_system
npm install
```

### 2. Run the Node.js Server

Make sure Python and required packages are installed before running the server.

```bash
node app.js
```

The server should start at `http://localhost:3000` or the port defined in the code.

### 3. Python Environment Setup

Ensure you have Python 3.x and required libraries:

```bash
pip install pandas scikit-learn flask
```

Or create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt  # (If such a file is available or create one manually)
```

## 📦 Sample Input

Use `sample_input.json` as a sample POST request body when testing the API:

```json
{
  "Gender": "Male",
  "Married": "Yes",
  "Dependents": "0",
  "Education": "Graduate",
  "Self_Employed": "No",
  "ApplicantIncome": 5000,
  "CoapplicantIncome": 0,
  "LoanAmount": 200,
  "Loan_Amount_Term": 360,
  "Credit_History": 1,
  "Property_Area": "Urban"
}
```

## 📊 Prediction Output

The API returns a JSON response with prediction:

```json
{
  "prediction": "Y"
}
```

## 🛠 Dependencies

- Node.js
- Express.js
- Python 3.x
- Pandas, Scikit-learn
- Pickle

## 📁 File Structure

```
Y_hill_Loan_prediction_system/
├── app.js
├── model.pkl
├── predictor.py
├── project01.ipynb
├── package.json
├── sample_input.json
├── dataset/
│   ├── train_u6lujuX_CVtuZ9i.csv
│   └── test_Y3wMUE5_7gLdaTN.csv
├── node_modules/
```

## 📬 Contact

For any questions, feel free to open an issue or reach out to the project maintainer.