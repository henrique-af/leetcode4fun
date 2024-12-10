import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0 or N > len(employee):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Sort salaries in descending order, remove duplicates, and reset index
    unique_salaries = employee['salary'].sort_values(ascending=False).drop_duplicates().reset_index(drop=True)
    
    # Check if N is greater than the number of unique salaries
    if N > len(unique_salaries):
        return pd.DataFrame({f'getNthHighestSalary({N})': [None]})
    
    # Select the Nth salary (subtracting 1 because pandas index starts at 0)
    nth_salary = unique_salaries.iloc[N-1]
    
    # Return the result as a DataFrame
    return pd.DataFrame({f'getNthHighestSalary({N})': [nth_salary]})