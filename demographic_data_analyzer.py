import pandas as pd

def calculate_demographic_data():
    # Load the dataset
    df = pd.read_csv("adult_data.csv")
    
    # 1. How many people of each race are represented in this dataset?
    race_count = df['race'].value_counts()
    print("Race count:")
    print(race_count)
    
    # 2. What is the average age of men?
    average_age_men = df[df['sex'] == 'Male']['age'].mean()
    print(f"Average age of men: {round(average_age_men, 1)}")
    
    # 3. What is the percentage of people who have a Bachelor's degree?
    bachelors_percentage = (df['education'] == 'Bachelors').mean() * 100
    print(f"Percentage with Bachelors degrees: {round(bachelors_percentage, 1)} %")
    
    # 4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    advanced_education_high_salary_percentage = (advanced_education & (df['salary'] == '>50K')).mean() * 100
    print(f"Percentage with advanced education that earn >50K: {round(advanced_education_high_salary_percentage, 1)} %")
    
    # 5. What percentage of people without advanced education make more than 50K?
    no_advanced_education = ~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    no_advanced_education_high_salary_percentage = (no_advanced_education & (df['salary'] == '>50K')).mean() * 100
    print(f"Percentage without advanced education that earn >50K: {round(no_advanced_education_high_salary_percentage, 1)} %")
    
    # 6. What is the minimum number of hours a person works per week?
    min_work_time = df['hours-per-week'].min()
    print(f"Min work time: {min_work_time} hours/week")
    
    # 7. What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
    min_work_time_high_salary_percentage = ((df['hours-per-week'] == min_work_time) & (df['salary'] == '>50K')).mean() * 100
    print(f"Percentage of rich among those who work fewest hours: {round(min_work_time_high_salary_percentage, 1)} %")
    
    # 8. What country has the highest percentage of people that earn >50K and what is that percentage?
    country_earning = df.groupby('native-country')['salary'].value_counts(normalize=True).unstack().fillna(0)
    
    # Check if '>50K' column exists
    if '>50K' in country_earning.columns:
        country_earning = country_earning['>50K']
        highest_earning_country = country_earning.idxmax()
        highest_earning_country_percentage = round(country_earning.max() * 100, 1)
        print(f"Highest earning country: {highest_earning_country} with {highest_earning_country_percentage} %")
    else:
        print("No data for people earning >50K.")
    
    # 9. Identify the most popular occupation for those who earn >50K in India.
    india_high_salary = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    if not india_high_salary.empty:
        popular_occupation_india = india_high_salary['occupation'].mode()
        if not popular_occupation_india.empty:
            popular_occupation_india = popular_occupation_india[0]
            print("Most popular occupation for those who earn >50K in India:", popular_occupation_india)
        else:
            print("No occupation data for those who earn >50K in India.")
    else:
        print("No data for people from India earning >50K.")

# Calling the function to execute the analysis
calculate_demographic_data()


