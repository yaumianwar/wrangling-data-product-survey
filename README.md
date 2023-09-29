# Wrangling Data Product Survey
This is the mini project from [Pacmann Academy](https://pacmann.io/) to create Python code to run data wrangling process from survey data. 

### Data Wrangling Workflow

1. Prepare the survey data from 2 source: `data/conjoint_survey_organic.xlsx` (organic) and `data/conjoint_survey_ads.csv` (ads).
2. Create question and choice mapping master data: `data/question.xlsx`
3. Load all of the data using pandas dataframe
4. Concat the data survey from ads and organic 
5. Clean the survey data colum to make it more readable and easy to access
6. Run the wrangling data process
    - Each phone number and question choice should have 1 row on `data_clean`
    - `choice` data value rules:
        - 0 : if choice is not selected or choice 'D' in selected choice
        - 1 : if choice is selected and  choice 'D' not in selected choice
7. Save the result at `data/clean_data.csv`

### How to Run
1. Go to working directory
2. Create  Virtual Environment: `pyhton3 -m venv venv`
3. Activate the `venv`: `source venv/bin/activate`
4. Install dependencties: `pip install -r requirements.txt`
5. Run the code: `python data_cleaning_process.py`
6. Result: `data/clean_data.csv`