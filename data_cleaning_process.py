# load time, pandas library and function from utils module
import time
import pandas as pd
from utils import rename_column_by_index, rename_question_column, determine_choice_state

# define program start time
start_time = time.time()

# load conjoint survey data (organic and ads)
organic_df = pd.read_excel('data/conjoint_survey_organic.xlsx')
ads_df = pd.read_csv('data/conjoint_survey_ads.csv')

# load question mapping data using pandas read_excel()
question_mapping_df = pd.read_excel('data/question.xlsx')

print(f'TOTAL DATA ORGANIC: {len(organic_df.index)}; TOTAL DATA ADS: {len(ads_df.index)}')

# change Timestamp column datatype on ads dataframe 
ads_df['Timestamp']= pd.to_datetime(ads_df['Timestamp'])

# concat organic and ads dataframe
frames = [organic_df, ads_df]
df = pd.concat(frames, ignore_index=True)

print(f'TOTAL DATA AFTER CONCATENATION: {len(df.index)}')

# rename phone number column name based on column index
rename_column_by_index(df, 1, 'phone_number')

# rename question column name
rename_question_column(df)

print(f'TOTAL NULL VALUE IN EACH COLUMN \n{df.isnull().sum()}')

# define phone numbers data by using pandas unique()
phone_numbers = list(df['phone_number'].unique())

print(f'CHECK DUPLICATE DATA -> len df: {len(df.index)}; len unique phone number: {len(phone_numbers)}; \
      isDuplicate?? {len(df.index) != len(phone_numbers)}')

# get clean data
# create dataframe to store each phone number question
phone_number_question_df = pd.melt(df, id_vars =['phone_number'], value_vars =[i for i in range (1,11)],\
                  var_name ='question', value_name ='selected_choice').sort_values(by=['phone_number', 'question'])

# create clean data dataframe: 1 row for each phone number, question and choice
clean_data_df = phone_number_question_df.merge(question_mapping_df, left_on='question', right_on='no')\
      .sort_values(by=['phone_number', 'question', 'choice'])

# update choice value to 1/0 based on selected choice
clean_data_df['choice'] = clean_data_df.apply(lambda x: determine_choice_state(x['choice'], x['selected_choice']), axis=1)

# drop unused column
clean_data_df = clean_data_df.drop(['question', 'selected_choice', 'no'], axis=1)

print(f'TOTAL CLEAN DATA SHOULD BE: {len(phone_numbers)} (LEN PHONE NUMBERS) * {len(question_mapping_df)} (LEN QUESTION MAPPING) \
      = {len(phone_numbers) * len(question_mapping_df)}')
print(f'TOTAL CLEAN DATA (ACTUAL): {len(clean_data_df.index)}')

# save clean data to csv file
clean_data_df.to_csv('data/clean_data.csv', index=False)

print('DATA CLEANING PROCESS SUCCESS')

# define program end time
end_time = time.time()

# get program execution time info
print("EXECUTION TIME :", (end_time - start_time) * 10**3, "ms")