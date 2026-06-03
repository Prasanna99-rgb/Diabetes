# 🩺 Diabetes Prediction Using Machine Learning

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://diabetes-6yvscqymvna2ardlgobxwp.streamlit.app/)

A Machine Learning project that predicts whether a patient is likely to have diabetes based on various medical attributes. The model is trained using Logistic Regression and deployed using Streamlit for real-time predictions.

---

## 🌐 Live Demo

🚀 Access the deployed application:

https://diabetes-6yvscqymvna2ardlgobxwp.streamlit.app/

---

## 📌 Project Overview

Diabetes is one of the most common chronic diseases worldwide. Early prediction can help individuals take preventive measures and seek timely medical attention.

This project uses a Logistic Regression Machine Learning model to classify patients as diabetic or non-diabetic based on medical information.

---

## 🚀 Features

- Predict diabetes risk instantly
- User-friendly Streamlit interface
- Logistic Regression classification model
- Real-time prediction results
- Lightweight and fast deployment
- Ready for cloud deployment

---

## 📊 Input Features

| Feature | Description | Range |
|----------|-------------|---------|
| Pregnancies | Number of pregnancies | 0 – 17 |
| Glucose | Plasma glucose concentration | 50 – 200 |
| BloodPressure | Diastolic blood pressure (mm Hg) | 40 – 130 |
| SkinThickness | Triceps skin fold thickness (mm) | 0 – 100 |
| Insulin | 2-Hour serum insulin | 0 – 900 |
| BMI | Body Mass Index | 10.0 – 70.0 |
| DiabetesPedigreeFunction | Diabetes pedigree function | 0.0 – 3.0 |
| Age | Age of the patient | 1 – 100 |

---

## 🧠 Machine Learning Model

- **Algorithm:** Logistic Regression
- **Problem Type:** Binary Classification
- **Output:**
  - 0 → Non-Diabetic
  - 1 → Diabetic

---

## 📂 Project Structure

```text
Diabetes-Prediction/
│
├── Test(1).pkl
├── app.py
├── requirements.txt
├── README.md
└── dataset.csv
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-github-username/Diabetes-Prediction.git
cd Diabetes-Prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Application runs on:

```text
http://localhost:8501
```

---

## 🔄 Prediction Workflow

1. Enter patient information.
2. Click the **Predict** button.
3. Model processes the inputs.
4. Prediction result is displayed instantly.
5. User is informed whether diabetes risk is present.

---




---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-Learn
- Pickle
- Streamlit

---

## 🚀 Deployment

Deployed on **Streamlit Community Cloud**

Live URL:

https://diabetes-6yvscqymvna2ardlgobxwp.streamlit.app/

---

## 🔮 Future Improvements

- Hyperparameter tuning
- Model comparison with Random Forest and XGBoost
- Feature importance visualization
- Enhanced UI/UX
- Cloud deployment optimization

---

## 👨‍💻 Author

### Prasanna Deshmane

🔗 LinkedIn: https://www.linkedin.com/in/prasanna-deshmane-80a419205

🚀 Live App: https://diabetes-6yvscqymvna2ardlgobxwp.streamlit.app/

🔗 GitHub: https://github.com/your-github-username

---

## ⭐ Support

If you found this project useful, please consider giving it a ⭐ on GitHub.

---

## 📜 License

This project is licensed under the MIT License.
