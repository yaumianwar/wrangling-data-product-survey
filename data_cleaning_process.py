# load time, pandas library and function from utils module
import time
import pandas as pd
from utils import rename_column_by_index, rename_question_column, create_clean_data

# define program start time
start_time = time.time()

# load conjoint survey data (organic and ads)
organic_df = pd.read_excel('data/conjoint_survey_organic.xlsx')
ads_df = pd.read_csv('data/conjoint_survey_ads.csv')

# load question mapping data using pandas read_excel()
question_mapping = pd.read_excel('data/question.xlsx').to_dict('records')

print(f'TOTAL DATA ORGANIC: {len(organic_df.index)}; TOTAL DATA ADS: {len(ads_df.index)}')

# convert Timestamp column datatype on ads dataframe 
ads_df['Timestamp']= pd.to_datetime(ads_df['Timestamp'])

# concat organic and ads dataframe
frames = [organic_df, ads_df]
df = pd.concat(frames, ignore_index=True)

print(f'TOTAL DATA AFTER CONCATENATION: {len(df.index)}')

# rename phone number column name based on column index to make it more readable
rename_column_by_index(df, 1, 'phone_number')

# rename question column name to make it more readable
rename_question_column(df)

print(f'TOTAL NULL VALUE IN EACH COLUMN \n{df.isnull().sum()}')

# define phone numbers data by using pandas unique()
phone_numbers = list(df['phone_number'].unique())

print(f'CHECK DUPLICATE DATA -> len df: {len(df.index)}; len unique phone number: {len(phone_numbers)}; isDuplicate?? {len(df.index) != len(phone_numbers)}')

# get clean data
clean_data_df = create_clean_data(df, phone_numbers, question_mapping)

print(f'TOTAL CLEAN DATA SHOULD BE: {len(phone_numbers)} (LEN PHONE NUMBERS) * {len(question_mapping)} (LEN QUESTION MAPPING) \
      = {len(phone_numbers) * len(question_mapping)}')
print(f'TOTAL CLEAN DATA (ACTUAL): {len(clean_data_df.index)}')

# save clean data to csv file
clean_data_df.to_csv('data/clean_data.csv', index=False)

print('DATA CLEANING PROCESS SUCCESS')

# define program end time
end_time = time.time()

# get program execution time info
print("EXECUTION TIME :", (end_time - start_time) * 10**3, "ms")