# load pandas library
import pandas as pd

# funtion to rename pandas dataframe column function based on column index
# params -> dataframe object, column index, new column name
def rename_column_by_index(df, index, new_column_name):

    # rename column name by column index
    df.rename(columns={ df.columns[index]: new_column_name }, inplace = True)


# function to rename spesific column -> question column based on string identifier
# params -> dataframe object
def rename_question_column(df):

    # define question column string identifier
    question_str = 'Produk manakah yang akan anda beli? (Anda bisa memilih membeli (klik) lebih dari 1 pilihan)'

    # iterate all of columns in datafrafme
    for index, col in enumerate(df):

        # check if colum value contains string identifier for question column
        if question_str in col:

            # rename question column name
            rename_column_by_index(df, index, col.split('.')[0])


# function to create clean data
# params -> dataframe object, list of phone numbers and question mapping
# return -> clean data dataframe
def create_clean_data(df, phone_numbers, question_mapping):

    # define empty array to store clean data
    clean_data = []

    # iterate phone number
    for phone_number in phone_numbers:

        # get answers filter by phone_number
        answer = df[df['phone_number'] == phone_number].iloc[0]

        # iterate each question choice
        for question in question_mapping:

            # get answer (selected choice) by number of question
            selected_choice = answer[str(question['no'])]

            # determine is choice selected or not based on selected choice
            is_choice_seleted = 1 if ((question['choice'] in selected_choice) and ('D.' not in selected_choice)) else 0

            # create data dictionary to store clean data for each phone number and question choice
            data = {
                'user_phone': phone_number,
                'choice': is_choice_seleted,
                'skill': question['skill'],
                'bentuk_program': question['bentuk_program'],
                'harga_program': question['harga_program']
            }
            
            # append data dictionary to clean_data array
            clean_data.append(data)

    # convert clean data to pandas dataframe
    clean_data_df = pd.DataFrame.from_records(clean_data)

    return clean_data_df