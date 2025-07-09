## Loan Status Prediction using SVM

#### This project is a Loan Approval Prediction System built using Support Vector Machine (SVM). It takes applicant details as input and predicts whether the loan will be Approved or Rejected.

### 🔗 Demo
💻 Web Interface: Built with Flask
🧠 Machine Learning Model: Trained using SVM (Scikit-learn)
📊 Dataset: [Loan Prediction Dataset from Kaggle]

### 📁 Folder Structure
loan-status-prediction/
├── model.pkl                # Trained SVM model
├── loan_status_prediction_using_svm.py  # Model training script
├── app.py                   # Flask backend
├── templates/
│   └── index.html           # Frontend HTML form
├── static/                  # (Optional) for CSS or images
└── README.md                # Project documentation


### 🚀 How It Works

#### 1. Data Preprocessing
Categorical to numerical conversion (e.g., Gender, Education)
Handled missing values
Labeled target variable (Loan_Status)

#### 2. Model Training
Used SVM with class_weight='balanced' to address class imbalance
Train-test split
Accuracy & Classification Report for performance evaluation

#### 3. Web App
Flask form collects user input
Predicts loan status
Displays result: ✅ Approved or ❌ Rejected

### 📦 Requirements
Install dependencies using:
requirements.txt
flask
numpy
pandas
scikit-learn

### ▶️ Run Locally
Clone the repo:
git clone https://github.com/yourusername/loan-status-prediction.git
cd loan-status-prediction
Run the Flask app: python app.py
Open your browser at: http://127.0.0.1:5000/

### 🧪 Example:

![image](https://github.com/user-attachments/assets/0ac68e87-9dc8-4e60-952b-6cc11be017ff)

![image](https://github.com/user-attachments/assets/086a57c1-ead4-4692-81dc-91d13016e3b8)
