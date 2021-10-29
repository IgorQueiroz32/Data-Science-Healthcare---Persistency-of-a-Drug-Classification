# Healthcare - Persistency of a Drug - Classification
Machine Learning classification model to classify if futures patients will take the drugs prescribed by the doctor during the entire treatment or if they won't.

Link for the streamlit app: <https://share.streamlit.io/igorqueiroz23031988/healthcare-persistency-of-a-drug-classification/main/deploy2.py>

![alt text](https://github.com/IgorQueiroz23031988/Healthcare-Persistency-of-a-Drug-Classification/blob/main/bussines%20presentation/Healthcare%20Persistency%20of%20a%20Drug%20Classification.mp4)

## 1. Business Description/Problem.

One of the challenges for all Pharmaceutical companies is to understand the persistency of drug as per the physician prescription. To solve this problem ABC pharma company approached an analytics company to automate this process of identification.

 With an objective to gather insights on the factors that are impacting the persistency, it is necessary to build a classification for the given dataset, using the variable ‘Persistency_Flag’ as target variable and other attributes as prediction variables.

## 2. Business Understanding.

ABC it is a private pharma company. Due to the problem to the persistency of drug as per the physician prescription, a data science project is applied to predict the classification of ‘Persistency_Flag’ variable. In other words, based on the previously patients characteristics it is possible predict if futures patients will use the drugs during the role treatment or if they won’t. 

The object of this project is providing answer of the main questions made by the company’s CEO, which are:

*	What is the ‘Persistency_Flag’ classification for future patients?

The answer for those questions is presented in two different methods:

*	A webapp with all necessary prediction attributes in order to predict the classification of the ‘Persistency_Flag’ for future patients. 

*	A dashboard with several hypotheses and insights to help the company CEO with future decisions.

The tools used for this project are: Python 3.8, Pycharm, Jupyter Notebook, Streamlit and Heroku.

## 3. Data Understanding.

There is 1 dataset provided: <https://www.kaggle.com/harlfoxem/housesalesprediction>.

 Variables Description:
 
Here I'm describing the columns in detail:

Patient Details:

*	Patient ID: Unique ID of each patient;
*	Persistency_Flag: Flag indicating if a patient was persistent or not;
*	Age: Age of the patient during their therapy;
*	Race: Race of the patient from the patient table;
*	Region: Region of the patient from the patient table;
*	Ethnicity: Ethnicity of the patient from the patient table;
*	Gender: Gender of the patient from the patient table;
*	IDN Indicator: Flag indicating patients mapped to IDN;

Provider Attributes:

*	NTM - Physician Specialty: Specialty of the HCP that prescribed the NTM Rx;

Clinical Factors:

*	NTM - T-Score: T Score of the patient at the time of the NTM Rx (within 2 years prior from rxdate);
*	Change in T Score: Change in Tscore before starting with any therapy and after receiving therapy (Worsened, Remained Same, Improved, Unknown);
*	NTM - Risk Segment: Risk Segment of the patient at the time of the NTM Rx (within 2 years days prior from rxdate);
*	Change in Risk Segment: Change in Risk Segment before starting with any therapy and after receiving therapy (Worsened, Remained Same, Improved, Unknown);
*	NTM - Multiple Risk Factors: Flag indicating if patient falls under multiple risk category (having more than 1 risk) at the time of the NTM Rx (within 365 days prior from rxdate);
*	NTM - Dexa Scan Frequency: Number of DEXA scans taken prior to the first NTM Rx date (within 365 days prior from rxdate);
*	NTM - Dexa Scan Recency: Flag indicating the presence of Dexa Scan before the NTM Rx (within 2 years prior from rxdate or between their first Rx and Switched Rx; whichever is smaller and applicable);
*	Dexa During Therapy: Flag indicating if the patient had a Dexa Scan during their first continuous therapy;
*	NTM - Fragility Fracture Recency: Flag indicating if the patient had a recent fragility fracture (within 365 days prior from rxdate);
*	Fragility Fracture During Therapy: Flag indicating if the patient had fragility fracture during their first continuous therapy;
*	NTM - Glucocorticoid Recency: Flag indicating usage of Glucocorticoids (>=7.5mg strength) in the one year look-back from the first NTM Rx;
*	Glucocorticoid During Therapy: Flag indicating if the patient had a Glucocorticoid usage during the first continuous therapy;

Disease/Treatment Factors:

*	NTM - Injectable Experience: Flag indicating any injectable drug usage in the recent 12 months before the NTM OP Rx;
*	NTM - Risk Factors: Risk Factors that the patient is falling into. For chronic Risk Factors complete lookback to be applied and for non-chronic Risk Factors, one year lookback from the date of first OP Rx;
*	NTM - Comorbidity: Comorbidities are divided into two main categories - Acute and chronic, based on the ICD codes. For chronic disease we are taking complete look back from the first Rx date of NTM therapy and for acute diseases, time period before the NTM OP Rx with one year lookback has been applied;
*	NTM - Concomitancy: Concomitant drugs recorded prior to starting with a therapy (within 365 days prior from first rxdate)
Adherence: Adherence for the therapies. 

## 4. Solution Strategy.

Solution adopted to generate business insights and create a ML classification model to solve the proposed problem. This solution includes:

* Data Description;

         1º - Data Dimensions.

         2º - Descriptive Statistics. 

* Mind Map Hypothesis;

* Hypothesis Creation;

* Exploratory Data Analysis (EDA);

         1º - Target Variable analysis.

         2º - Numerical Variable analysis.

         3º - Hypothesis Validation.

         4º - Summary of Hypothesis.  

         5º - Multivariate Analysis – Numerical Variables.

* Data Description;

* Machine Learning Models Performance;

         1º - Extra Trees Classifier.

         2º - LGBM Classifier.

         3º - Stochastic Gradient Descent.

         4º - Random Forest.

         5º - Support Vector Machine.

* Business Performance;

         1º - Accuracy.

         2º - Confusion Matrix & Classification Report.

* Persistency of a Drug Classification ML WebApp.
 
## 5. Top 08 Data Insights.

__Hypothesis 01:__ Female patients are more persistent of a drug than male.

__True:__ There are 1135 more persistent female patients than male patients..<br/><br/>


__Hypothesis 02:__ Patients from Northeast are more persistent of a drug than patients from South.

__False:__ Comparing patients from the Northeast and South, there are 396 more persistent patients from the South than from the Northeast.<br/><br/>


__Hypothesis 03:__ Patients over 65 years of age are more persistent of a drug than patients 65 years of age or younger. 

__True:__ There are 641 more persistent patients over 65 years of age than patients younger than 65 years of age.<br/><br/>


__Hypothesis 04:__ Caucasian patients, not Hispanic are more persistent of a drug than patients with different race and ethnicity.

__True:__ There are 993 more Caucasian & not Hispanic persistent patients than patients from different race and ethnicity.<br/><br/>


__Hypothesis 05:__ Patients mapped to IDN are more persistent of a drug than patient not mapped..

__True:__ There are 797 more persistent patients mapped to IDN than persistent patients not mapped to IDN.<br/><br/>


__Hypothesis 06:__ Patients that received the drug prescription from General Practitioner Specialty are less persistent of a drug than patients that received the drug prescription from others Specialty.

__False:__ There are 301 more persistent patients that received the drug prescription from others Specialty than persistent patients that received the drug prescription from General Practitioner Specialty.<br/><br/>


__Hypothesis 07:__ Patients that used Glucocorticoid and had a Fragility Fracture, before and during the therapy, are more persistent of a drug than patients that not used Glucocorticoid either had a Fragility Fracture, in any situation.

__False:__ There are 531 more persistent patients that did not use Glucocorticoid neither had a Fragility Fracture than persistent patients that used Glucocorticoid and had a Fragility Fracture.<br/><br/>


__Hypothesis 08:__ Patients that had Dexa Scan more than 0 times are more persistent of a drug than patients that had Dexa Scan 0 times.

__False:__ There are 185 more persistent patients that had Dexa Scan more than 0 times than persistent patients that that had Dexa Scan 0 times.<br/><br/>


__Hypothesis 09:__ Patients that presents VLR_LR as Risk Segment during the therapy and presents Unknown value in Risk Segment after the therapy are more persistent of a drug than patients that present other types of Risk Segment and Change in Risk Segment.

__False:__ There are 641 more persistent patients that presents other types of Risk Segment and Change on Risk Segment than persistent patients that presents VLR_LR as Risk Segment during the therapy and presents Unknown value in Risk Segment after the therapy .<br/><br/>


__Hypothesis 10:__ Patients that presents T Socre of >-2.5 before the therapy and presents No Change T Score status after the therapy are less persistent of a drug than patients that presents other types of T Score and T Score status.

__True:__ There are 463 more persistent patients that presents other types of T Score and Change on T Score than persistent patients that presents T Score of >-2.5 before the therapy and presents No Change T Score status after the therapy.<br/><br/>


__Hypothesis 11:__ Patients that presents the amount of risk factor higher than 1 are more persistent of a drug than patients that presents the amount of risk factor lower than 1.

__False:__ There are 277 more persistent patients that do not presents the amount of risk factor higher than 1 than persistent patients that presents the amount of risk factor higher than 1.<br/><br/>


__Hypothesis 12:__ Patients adherent for therapies and that used drugs during the therapy are more persistent of a drug than patients in different situations related to both attributes.

__True:__ There are 189 more persistent patients adherent for therapies and that used drugs before the therapy than persistent are not adherent for therapies and that did not use drugs before the therapy.<br/><br/>


__Hypothesis 13:__ Patients that used more than 2 concomitancy drugs before the therapy are less persistent of a drug than patients that used more than 2 concomitancy drugs before the therapy.

__False:__ There are 91 more persistent patients that used more than 2 concomitancy drugs before the therapy persistent patients that used less than 3 concomitancy drugs before the therapy.<br/><br/>


__Hypothesis 14:__ Patients that presents more than 3 different types of comorbidity are more persistent of a drug than patients that present less than 3 different types of comorbidity.

__True:__ There are 821 more persistent patients that presents more than 3 different types of comorbidity than persistent patients that do not presents more than 3 different types of comorbidity.<br/><br/>


## 6. Hypothesis and Insights Conclusion.

 Based on all the Insights created from this dataset, patients who have a higher probability of persisting of a drug for the entire treatment, have the following characteristics:
 
* Female;

* Patients older than 65 years;

* Caucasian non-Hispanic Patients;

* Patients mapped to IDN;

* Patients that received the drug prescription from General Practitioner Specialty;

* Patients who did not use Glucocorticoid and had Fragility Fracture;

* Patients who had no Dexa Scan;

* Patient’s adherent for therapies and that used drugs before the therapy.

## 7. Business Performance.

* Accuracy 

With the accuracy of the ML model it is possible to find out the exact number of correct predictions made by the same model.

From 774 values, the ML model was able to correctly predict 689 values of the attribute 'Persistency_Flag'.

* Confusion Matrix & Classification Report

With the Confusion Matrix it is possible to verify how many values of the attribute 'Persistency_Flag' were correctly and erroneously classified in each class, in other words, how many values equal to Persistent (1) and equal to Non-Persistent (0) were correctly classified, and how many of each class were not.

According to the classification report and the confusion matrix:

358 values that are originally class Non-Persistent (0) have been correctly classified as Non-Persistent, which represents 95% of the Non-Persistent class;

331 values that are originally class Persistent (1) have been correctly classified as Persistent, which represents 84% of the Persistent class;

20 values that are originally class Non-Persistent (0) have been incorrectly classified as Persistent;

65 values that are originally class Persistent (1) have been incorrectly classified as Non-Persistent.

## 8. Conclusion.

With the ML classification model, trained with the algorithm Support Vector MAchine, it is possible classify if futures patients will take the drugs prescribed by the doctor during the entire treatment or if they won't, with an accuracy higher than 85%.

This task is done at the WebApp "Persistency of a Drug Classification ML WebApp", that is possible to find it at <https://share.streamlit.io/igorqueiroz23031988/healthcare-persistency-of-a-drug-classification/main/deploy2.py>.

## 9. Next Steps.

* Business User Model Workshop;
* 
* Collect Usability Feedback;
* 
* Increase Model Accuracy by 10%.



