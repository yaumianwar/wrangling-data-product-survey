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
            rename_column_by_index(df, index, int(col.split('.')[0]))


# function to determine is given choice selected / not
# params -> choice, selected choice
# return -> choice state
def determine_choice_state(choice, selected_choice):
    
    is_choice_selected = 1 if ((choice in selected_choice) and ('D.' not in selected_choice)) else 0

    return is_choice_selected