import pickle
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# app instance
app = Flask(__name__)

# loading dataset and model
df = pd.read_excel('./cost_of_courses.xlsx')
knnr_model = pickle.load(open('./rf_reg_model.pkl', 'rb'))

# index page


@app.route('/', methods=['GET', 'POST'])
def index():
    institute_brand_value = sorted(df['Institute_brand_value'].unique())
    courses = sorted(df['Course_Offered'].unique())
    course_level = sorted(df['Course_level'].unique())
    # mode of course radio button
    # web assess, certification, placement radio

    return render_template('index.html', brand_value=institute_brand_value, courses=courses,
                           course_level=course_level)


@app.route("/predict", methods=["GET", "POST"])
def predict():
    brand_value = request.form.get('brandvalue')
    course = request.form.get('offered')
    course_level = request.form.get('level')
    no_of_instructors = request.form.get('instructors')
    total_course_hr = request.form.get('coursehours')
    mode_of_course = request.form.get('mode')
    certification = request.form.get('exam')
    placement = request.form.get('placement')

    licence = request.form.get('licence')
    infrastructure = request.form.get('infrastructure')
    technical = request.form.get('technical')
    rent = request.form.get('rent')
    bills = request.form.get('bill')
    advrt = request.form.get('advertising')
    maintenance = request.form.get('maintenance')
    nstaff = request.form.get('nstaff')
    tstaff = request.form.get('tstaff')

    data = {
        'Institute_brand_value': brand_value,
        'Course_Offered': course,
        'Course_level': course_level,
        'No_of_Instructors': no_of_instructors,
        'Total_Course_Hours': total_course_hr,
        'Mode of Course': mode_of_course,
        'Certification Exam': certification,
        'Placement Offered': placement,
        'Licencing and Registration': licence,
        'Infrastructure Cost': infrastructure,
        'Technical Requirements': technical,
        'Monthly(Rent)': rent,
        'Monthly(Bills)': bills,
        'Advertising/Marketing': advrt,
        'Maintenance': maintenance,
        'Non_teaching_staff(salary)': nstaff,
        'teaching_staff(salary)': tstaff
    }

    features = pd.DataFrame(data, index=[0])
    pred = knnr_model.predict(features)

    return render_template("predict.html", prediction=np.round(pred[0], 2))


if __name__ == "__main__":
    app.run(debug=True)
