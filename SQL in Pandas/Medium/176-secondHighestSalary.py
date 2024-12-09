import pandas as pd

data = [[1, 100], [2, 200], [3, 300]]
employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id':'int64', 'salary':'int64'})

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Step 1: Find the maximum salary
    max_salary = employee['salary'].max()

    # Step 2 and 3: Filter salaries less than max and find the maximum
    second_highest = employee[employee['salary'] < max_salary]['salary'].max()
    
    # Step 4: Create a DataFrame with the result
    result_df = pd.DataFrame({'SecondHighestSalary': [second_highest]})
    
    # Step 5: Handle the case where there is no second highest salary
    if pd.isna(second_highest):
        result_df['SecondHighestSalary'] = None
    
    return result_df