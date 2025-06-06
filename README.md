# 💤 Sleep Disorder Detection using Machine Learning

## 🧠 Project Overview

Sleep disorders such as **Insomnia** and **Sleep Apnea** can severely affect an individual's physical health, mental well-being, and quality of life. Timely and accurate diagnosis is crucial for effective intervention and treatment. This project leverages **machine learning** to detect and classify sleep disorders based on lifestyle and sleep-related attributes.

The solution integrates:

* Advanced machine learning models
* A user-friendly **web interface** developed with Flask
* Clean visualizations and data insights for enhanced understanding

---

## 🚀 Features

* Classification of sleep health into:

  * **Healthy**
  * **Insomnia**
  * **Sleep Apnea**
* Trained with a diverse dataset of lifestyle and sleep attributes
* Real-time predictions via web interface
* Visual insights into dataset distributions and model performance

---

## 🛠️ Technologies Used

### Backend

* Python
* Flask
* Pandas, NumPy, Matplotlib, Scikit-learn

### Frontend

* HTML
* CSS
* JavaScript

### Machine Learning Models

* **Gradient Boosting Classifier**
* **Quadratic Discriminant Analysis (QDA)**

## 📊 Dataset

The dataset used in this project includes lifestyle factors, sleep patterns, and health-related metrics. Key features include:

* Age, Gender, BMI
* Daily Routine Factors (e.g., physical activity, screen time)
* Sleep duration and quality
* Health conditions such as snoring and stress levels

## 📁 Project Structure

```
sleep-disorder-detection/
│
├── static/                   # CSS, JS, Images
├── templates/                # HTML templates
├── models/                   # Trained ML model files
├── app.py                    # Flask application
├── sleep_disorder_ml.py      # Model training and prediction logic
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 💡 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/sleep-disorder-detection.git
   cd sleep-disorder-detection
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**

   ```bash
   python app.py
   ```

4. **Access in browser**
   Visit `http://127.0.0.1:5000` in your web browser.

---

## 📈 Future Enhancements

* Expand dataset for better generalization
* Integrate wearable device data for real-time monitoring
* Add more models and ensemble techniques for higher accuracy
* Deploy on cloud platform (e.g., Heroku, AWS)

---

## 🧑‍💻 Contributors

* \[Your Name] – Developer, ML Model Designer, UI Developer
  *(Add more contributors if applicable)*

---

## 📜 License

This project is open-source and available under the [MIT License](LICENSE).

---

Let me know if you want this personalized further with your name, GitHub link, or sample screenshots.
