import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("models/dropout_rf_model.pkl")

st.title("Prediksi Risiko Dropout Mahasiswa")
st.markdown("Masukkan data lengkap siswa untuk memprediksi apakah ia berisiko dropout atau tidak.")

# Input fitur
Marital_status = st.number_input("Marital_status", value=0)
Application_mode = st.number_input("Application_mode", value=0)
Application_order = st.number_input("Application_order", value=0)
Course = st.number_input("Course", value=0)
Daytime_evening_attendance = st.number_input("Daytime_evening_attendance", value=0)
Previous_qualification = st.number_input("Previous_qualification", value=0)
Previous_qualification_grade = st.number_input("Previous_qualification_grade", value=0.0)
Nacionality = st.number_input("Nacionality", value=0)
Mothers_qualification = st.number_input("Mothers_qualification", value=0)
Fathers_qualification = st.number_input("Fathers_qualification", value=0)
Mothers_occupation = st.number_input("Mothers_occupation", value=0)
Fathers_occupation = st.number_input("Fathers_occupation", value=0)
Admission_grade = st.number_input("Admission_grade", value=0.0)
Displaced = st.selectbox("Displaced", ["0", "1"])
Displaced = int(Displaced)
Educational_special_needs = st.selectbox("Educational_special_needs", ["0", "1"])
Educational_special_needs = int(Educational_special_needs)
Debtor = st.selectbox("Debtor", ["0", "1"])
Debtor = int(Debtor)
Tuition_fees_up_to_date = st.selectbox("Tuition_fees_up_to_date", ["0", "1"])
Tuition_fees_up_to_date = int(Tuition_fees_up_to_date)
Gender = st.selectbox("Gender", ["0", "1"])
Gender = int(Gender)
Scholarship_holder = st.selectbox("Scholarship_holder", ["0", "1"])
Scholarship_holder = int(Scholarship_holder)
Age_at_enrollment = st.number_input("Age_at_enrollment", value=0)
International = st.selectbox("International", ["0", "1"])
International = int(International)
Curricular_units_1st_sem_credited = st.number_input("Curricular_units_1st_sem_credited", value=0)
Curricular_units_1st_sem_enrolled = st.number_input("Curricular_units_1st_sem_enrolled", value=0)
Curricular_units_1st_sem_evaluations = st.number_input("Curricular_units_1st_sem_evaluations", value=0)
Curricular_units_1st_sem_approved = st.number_input("Curricular_units_1st_sem_approved", value=0)
Curricular_units_1st_sem_grade = st.number_input("Curricular_units_1st_sem_grade", value=0.0)
Curricular_units_1st_sem_without_evaluations = st.number_input("Curricular_units_1st_sem_without_evaluations", value=0)
Curricular_units_2nd_sem_credited = st.number_input("Curricular_units_2nd_sem_credited", value=0)
Curricular_units_2nd_sem_enrolled = st.number_input("Curricular_units_2nd_sem_enrolled", value=0)
Curricular_units_2nd_sem_evaluations = st.number_input("Curricular_units_2nd_sem_evaluations", value=0)
Curricular_units_2nd_sem_approved = st.number_input("Curricular_units_2nd_sem_approved", value=0)
Curricular_units_2nd_sem_grade = st.number_input("Curricular_units_2nd_sem_grade", value=0.0)
Curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular_units_2nd_sem_without_evaluations", value=0)
Unemployment_rate = st.number_input("Unemployment_rate", value=0.0)
Inflation_rate = st.number_input("Inflation_rate", value=0.0)
GDP = st.number_input("GDP", value=0.0)


# Prediksi saat tombol ditekan
if st.button("Prediksi"):
    input_data = np.array([[Marital_status, Application_mode, Application_order, Course, Daytime_evening_attendance, Previous_qualification, Previous_qualification_grade, Nacionality, Mothers_qualification, Fathers_qualification, Mothers_occupation, Fathers_occupation, Admission_grade, Displaced, Educational_special_needs, Debtor, Tuition_fees_up_to_date, Gender, Scholarship_holder, Age_at_enrollment, International, Curricular_units_1st_sem_credited, Curricular_units_1st_sem_enrolled, Curricular_units_1st_sem_evaluations, Curricular_units_1st_sem_approved, Curricular_units_1st_sem_grade, Curricular_units_1st_sem_without_evaluations, Curricular_units_2nd_sem_credited, Curricular_units_2nd_sem_enrolled, Curricular_units_2nd_sem_evaluations, Curricular_units_2nd_sem_approved, Curricular_units_2nd_sem_grade, Curricular_units_2nd_sem_without_evaluations, Unemployment_rate, Inflation_rate, GDP]])
    pred = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]

    if pred == 1:
        st.error(f"⚠️ Siswa ini berisiko **Dropout** dengan probabilitas {prob:.2f}")
    else:
        st.success(f"✅ Siswa ini diprediksi akan **Lulus** dengan probabilitas {1 - prob:.2f}")
