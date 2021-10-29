import pickle
import pandas as pd
import numpy as np
import streamlit as st
from sklearn.preprocessing import RobustScaler, MinMaxScaler, LabelEncoder

st.set_page_config(layout='wide')
def user_input_features():
    # front end elements of the web page
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Persistency of Drug Classification ML App</h1> 
    </div> 
    """

    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html=True)
    st.text("Author: Igor Queiroz - Data Scientist")

    # defining Region
    Region = st.selectbox('Region', ('West', 'Midwest', 'South', 'Other/Unknown', 'Northeast'))

    # defining Ntm_Speciality_Bucket
    Ntm_Speciality_Bucket = st.selectbox('Ntm_Speciality_Bucket', ('OB/GYN/Others/PCP/Unknown', 'Endo/Onc/Uro', 'Rheum'))

    # defining Dexa_Freq_During_Rx
    Dexa_Freq_During_Rx = st.number_input("Dexa_Freq_During_Rx", min_value=0, value=0, step=1)

    st.header('Types of Comorbidity')

    # defining Comorb_Encounter_For_Screening_For_Malignant_Neoplasms
    Comorb_Encounter_For_Screening_For_Malignant_Neoplasms = st.checkbox('Comorb_Encounter_For_Screening_For_Malignant_Neoplasms')

    if Comorb_Encounter_For_Screening_For_Malignant_Neoplasms:
        Comorb_Encounter_For_Screening_For_Malignant_Neoplasms = 1

    else:
        Comorb_Encounter_For_Screening_For_Malignant_Neoplasms = 0

    # defining Comorb_Encounter_For_Immunization
    Comorb_Encounter_For_Immunization = st.checkbox('Comorb_Encounter_For_Immunization')

    if Comorb_Encounter_For_Immunization:
        Comorb_Encounter_For_Immunization = 1

    else:
        Comorb_Encounter_For_Immunization = 0

    # defining Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx
    Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx = st.checkbox('Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx')

    if Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx:
        Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx = 1

    else:
        Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx = 0

    # defining Comorb_Vitamin_D_Deficiency
    Comorb_Vitamin_D_Deficiency = st.checkbox('Comorb_Vitamin_D_Deficiency')

    if Comorb_Vitamin_D_Deficiency:
        Comorb_Vitamin_D_Deficiency = 1

    else:
        Comorb_Vitamin_D_Deficiency = 0

    # defining Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified
    Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified = st.checkbox('Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified')

    if Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified:
        Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified = 1

    else:
        Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified = 0

    # defining Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx
    Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx = st.checkbox('Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx')

    if Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx:
        Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx = 1

    else:
        Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx = 0

    # defining Comorb_Long_Term_Current_Drug_Therapy
    Comorb_Long_Term_Current_Drug_Therapy = st.checkbox('Comorb_Long_Term_Current_Drug_Therapy')

    if Comorb_Long_Term_Current_Drug_Therapy:
        Comorb_Long_Term_Current_Drug_Therapy = 1

    else:
        Comorb_Long_Term_Current_Drug_Therapy = 0

    # defining Comorb_Dorsalgia
    Comorb_Dorsalgia = st.checkbox('Comorb_Dorsalgia')

    if Comorb_Dorsalgia:
        Comorb_Dorsalgia = 1

    else:
        Comorb_Dorsalgia = 0

    # defining Comorb_Personal_History_Of_Other_Diseases_And_Conditions
    Comorb_Personal_History_Of_Other_Diseases_And_Conditions = st.checkbox('Comorb_Personal_History_Of_Other_Diseases_And_Conditions')

    if Comorb_Personal_History_Of_Other_Diseases_And_Conditions:
        Comorb_Personal_History_Of_Other_Diseases_And_Conditions = 1

    else:
        Comorb_Personal_History_Of_Other_Diseases_And_Conditions = 0

    # defining Comorb_Other_Disorders_Of_Bone_Density_And_Structure
    Comorb_Other_Disorders_Of_Bone_Density_And_Structure = st.checkbox('Comorb_Other_Disorders_Of_Bone_Density_And_Structure')

    if Comorb_Other_Disorders_Of_Bone_Density_And_Structure:
        Comorb_Other_Disorders_Of_Bone_Density_And_Structure = 1

    else:
        Comorb_Other_Disorders_Of_Bone_Density_And_Structure = 0

    # defining Comorb_Gastro_esophageal_reflux_disease
    Comorb_Gastro_esophageal_reflux_disease = st.checkbox('Comorb_Gastro_esophageal_reflux_disease')

    if Comorb_Gastro_esophageal_reflux_disease:
        Comorb_Gastro_esophageal_reflux_disease = 1

    else:
        Comorb_Gastro_esophageal_reflux_disease = 0

    st.header('Types of Concomitancy')

    # defining Concom_Systemic_Corticosteroids_Plain
    Concom_Systemic_Corticosteroids_Plain = st.checkbox('Concom_Systemic_Corticosteroids_Plain')

    if Concom_Systemic_Corticosteroids_Plain:
        Concom_Systemic_Corticosteroids_Plain = 1

    else:
        Concom_Systemic_Corticosteroids_Plain = 0

    # defining Concom_Cephalosporins
    Concom_Cephalosporins = st.checkbox('Concom_Cephalosporins')

    if Concom_Cephalosporins:
        Concom_Cephalosporins = 1

    else:
        Concom_Cephalosporins = 0

    # defining Concom_Macrolides_And_Similar_Types
    Concom_Macrolides_And_Similar_Types = st.checkbox('Concom_Macrolides_And_Similar_Types')

    if Concom_Macrolides_And_Similar_Types:
        Concom_Macrolides_And_Similar_Types = 1

    else:
        Concom_Macrolides_And_Similar_Types = 0

    # defining Concom_Anaesthetics_General
    Concom_Anaesthetics_General = st.checkbox('Concom_Anaesthetics_General')

    if Concom_Anaesthetics_General:
        Concom_Anaesthetics_General = 1

    else:
        Concom_Anaesthetics_General = 0

    # defining Concom_Viral_Vaccines
    Concom_Viral_Vaccines = st.checkbox('Concom_Viral_Vaccines')

    if Concom_Viral_Vaccines:
        Concom_Viral_Vaccines = 1

    else:
        Concom_Viral_Vaccines = 0

    # defining Count_Of_Concomitancy
    Count_Of_Concomitancy = st.number_input("Count_Of_Concomitancy", min_value=0, value=0, step=1)

    # defining Count_Of_Comorbidity
    Count_Of_Comorbidity = st.number_input("Count_Of_Comorbidity", min_value=0, value=0, step=1)

    data = {'Region': Region,
            'Ntm_Speciality_Bucket':Ntm_Speciality_Bucket,
            'Dexa_Freq_During_Rx': Dexa_Freq_During_Rx,
            'Comorb_Encounter_For_Screening_For_Malignant_Neoplasms': Comorb_Encounter_For_Screening_For_Malignant_Neoplasms,
            'Comorb_Encounter_For_Immunization': Comorb_Encounter_For_Immunization,
            'Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx': Comorb_Encntr_For_General_Exam_W_O_Complaint_Susp_Or_Reprtd_Dx,
            'Comorb_Vitamin_D_Deficiency': Comorb_Vitamin_D_Deficiency,
            'Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified': Comorb_Other_Joint_Disorder_Not_Elsewhere_Classified,
            'Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx': Comorb_Encntr_For_Oth_Sp_Exam_W_O_Complaint_Suspected_Or_Reprtd_Dx,
            'Comorb_Long_Term_Current_Drug_Therapy': Comorb_Long_Term_Current_Drug_Therapy,
            'Comorb_Dorsalgia': Comorb_Dorsalgia,
            'Comorb_Personal_History_Of_Other_Diseases_And_Conditions': Comorb_Personal_History_Of_Other_Diseases_And_Conditions,
            'Comorb_Other_Disorders_Of_Bone_Density_And_Structure': Comorb_Other_Disorders_Of_Bone_Density_And_Structure,
            'Comorb_Gastro_esophageal_reflux_disease': Comorb_Gastro_esophageal_reflux_disease,
            'Concom_Systemic_Corticosteroids_Plain': Concom_Systemic_Corticosteroids_Plain,
            'Concom_Cephalosporins': Concom_Cephalosporins,
            'Concom_Macrolides_And_Similar_Types': Concom_Macrolides_And_Similar_Types,
            'Concom_Anaesthetics_General': Concom_Anaesthetics_General,
            'Concom_Viral_Vaccines': Concom_Viral_Vaccines,
            'Count_Of_Concomitancy': Count_Of_Concomitancy,
            'Count_Of_Comorbidity': Count_Of_Comorbidity}
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

# Feature Engineering
persistency_raw = pd.read_csv('https://raw.githubusercontent.com/IgorQueiroz23031988/Healthcare-Persistency-of-a-Drug-Classification/main/healthcare_dataset.csv')
# Replacing all values 'Y' (Yes) and 'N' (No) for 1 (Yes) and 0 (No), of all categorical attributes Concomitancy and Comorbidity
data = persistency_raw.iloc[:, 25:49].replace('Y', 1).replace('N', 0)

# Count_Of_Concomitancy
persistency_raw['Count_Of_Concomitancy'] = data.iloc[:, 14:24].dot(np.ones(data.iloc[:, 14:24].shape[1]))
persistency_raw['Count_Of_Concomitancy'] = persistency_raw['Count_Of_Concomitancy'].astype(np.int64)

# Count_Of_Comorbidity
persistency_raw['Count_Of_Comorbidity'] = data.iloc[:, 0:14].dot(np.ones(data.iloc[:, 0:14].shape[1]))
persistency_raw['Count_Of_Comorbidity'] = persistency_raw['Count_Of_Comorbidity'].astype(np.int64)

# Combines user input features with entire penguins dataset
# This will be useful for the encoding phase
cols_drop = ['Persistency_Flag', 'Change_Risk_Segment', 'Change_T_Score', 'Dexa_During_Rx', 'Ptid', 'Age_Bucket', 'Adherent_Flag',
             'Comorb_Disorders_of_lipoprotein_metabolism_and_other_lipidemias',
             'Comorb_Osteoporosis_without_current_pathological_fracture',
             'Comorb_Personal_history_of_malignant_neoplasm',
             'Concom_Anti_Depressants_And_Mood_Stabilisers',
             'Concom_Broad_Spectrum_Penicillins',
             'Concom_Cholesterol_And_Triglyceride_Regulating_Preparations',
             'Concom_Fluoroquinolones',
             'Concom_Narcotics',
             'Count_Of_Risks',
             'Ethnicity',
             'Frag_Frac_During_Rx',
             'Frag_Frac_Prior_Ntm',
             'Gender',
             'Gluco_Record_During_Rx',
             'Gluco_Record_Prior_Ntm',
             'Idn_Indicator',
             'Injectable_Experience_During_Rx',
             'Ntm_Specialist_Flag',
             'Race',
             'Risk_Chronic_Liver_Disease',
             'Risk_Chronic_Malnutrition_Or_Malabsorption',
             'Risk_Estrogen_Deficiency',
             'Risk_Excessive_Thinness',
             'Risk_Family_History_Of_Osteoporosis',
             'Risk_Hysterectomy_Oophorectomy',
             'Risk_Immobilization',
             'Risk_Low_Calcium_Intake',
             'Risk_Osteogenesis_Imperfecta',
             'Risk_Patient_Parent_Fractured_Their_Hip',
             'Risk_Poor_Health_Frailty',
             'Risk_Recurring_Falls',
             'Risk_Rheumatoid_Arthritis',
             'Risk_Segment_During_Rx',
             'Risk_Segment_Prior_Ntm',
             'Risk_Smoking_Tobacco',
             'Risk_Type_1_Insulin_Dependent_Diabetes',
             'Risk_Untreated_Chronic_Hyperthyroidism',
             'Risk_Untreated_Chronic_Hypogonadism',
             'Risk_Untreated_Early_Menopause',
             'Risk_Vitamin_D_Insufficiency',
             'Tscore_Bucket_During_Rx',
             'Tscore_Bucket_Prior_Ntm',
             'Ntm_Speciality']
persistency = persistency_raw.drop(cols_drop, axis=1)

df = pd.concat([input_df, persistency], axis=0)

# Rescaling of all numerical variables with non-cyclical nature
rs = RobustScaler()
mms = MinMaxScaler()

df['Dexa_Freq_During_Rx'] = rs.fit_transform(df[['Dexa_Freq_During_Rx']])
df['Count_Of_Concomitancy'] = mms.fit_transform(df[['Count_Of_Concomitancy']])
df['Count_Of_Comorbidity'] = mms.fit_transform(df[['Count_Of_Comorbidity']])

# Encoding of Categorical attributes that do not presents order or scale or idea os state, each value is independent.
le = LabelEncoder()

df['Region'] = le.fit_transform(df['Region'])
df['Ntm_Speciality_Bucket'] = le.fit_transform(df['Ntm_Speciality_Bucket'])

df = df[:1] # Selects only the first row (the user input data)

# Displays the user input features
st.subheader('User Input features')

st.write('Awaiting CSV file to be uploaded. Currently using example input parameters (shown below).')
st.write(df)

# Reads in saved classification model
load_clf = pickle.load(open('model_classification.pkl', 'rb'))

# Apply model to make predictions
prediction = load_clf.predict(df)


st.subheader('Prediction')
# Persistency_Flag = np.array(['Non-Persistency of Drug', 'Persistency of Drug'])
# st.write(Persistency_Flag[prediction])

# defining result
result = ''
final_result = ''

if st.button('Predict'):
    # making the prediction
    result = prediction

    # converting and showing result

    if result == 1:
        result_final = 'Persistency of Drug'

    elif result == 0:
        result_final = 'Non-Persistency of Drug'

    st.success('The Persistency Flag is: {}'.format(result_final))