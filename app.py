from flask import Flask, jsonify, render_template, request
from utils import SleepDisorder
import config

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template('home.html')

# Prediction API
@app.route('/predicted_disorder', methods=['POST'])
def get_sleep_disorder():
    if request.method == 'POST':
        data = request.form
        Gender = data['Gender']
        Age = eval(data['Age'])
        Sleep_Duration = eval(data['Sleep_Duration'])
        Quality_of_Sleep = eval(data['Quality_of_Sleep'])
        Physical_Activity_Level = eval(data['Physical_Activity_Level'])
        Stress_Level = eval(data['Stress_Level'])
        BMI_Category = data['BMI_Category']
        Blood_Pressure = data['Blood_Pressure']
        Heart_Rate = eval(data['Heart_Rate'])
        Daily_Steps = eval(data['Daily_Steps'])
        Occupation = data['Occupation']

        sleep_dis = SleepDisorder(Gender, Age, Sleep_Duration, Quality_of_Sleep,
                                  Physical_Activity_Level, Stress_Level, BMI_Category,
                                  Blood_Pressure, Heart_Rate, Daily_Steps, Occupation)
        disorder = sleep_dis.get_predicted_disorder()

        # Determine the result text
        if disorder[0] == 0:
            result = "This person is Healthy"
            description = "This person is healthy and does not have any sleep disorder."
            precaution = "Maintain a healthy lifestyle and keep up the good work."
        elif disorder[0] == 1:
            result = "This person is Suffering from Apnea"
            description = "Apnea is a potentially serious sleep disorder in which breathing repeatedly stops and starts. If you snore loudly and feel tired even after a full night's sleep, you might have sleep apnea."
            precaution = "Lose weight, avoid alcohol and sleeping pills, sleep on your side, and keep your nasal passages open."
        else:
            result = "This person is Suffering from Insomnia"
            description = "Insomnia is a common sleep disorder that can make it hard to fall asleep, hard to stay asleep, or cause you to wake up too early and not be able to get back to sleep."
            precaution = "Establish a bedtime routine, keep a sleep diary, and get out of bed when you can't sleep."

        # Pass results to the results template
        return render_template('result.html', result=result, description=description, precaution=precaution)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=config.PORT_NUMBER, debug=False)
