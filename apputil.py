import seaborn as sns
import pandas as pd


# update/add code below ...

## Exercise 1

def fibonacci(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


## Exercise 2

def to_binary(n):
    if n < 2:
        return n
    return int(str(to_binary(n // 2)) + str(n % 2))


## Exercise 3

_BELLEVUE_URL = (
    'https://github.com/melaniewalsh/Intro-Cultural-Analytics/raw/master/'
    'book/data/bellevue_almshouse_modified.csv'
)
df_bellevue = pd.read_csv(_BELLEVUE_URL)


def task_1():
    df = df_bellevue.copy()

    print(
        "Data issue: 'gender' contains typo values 'g'/'h' (mapped to 'w') "
        "and '?' entries (treated as missing) before computing missing counts."
    )
    df['gender'] = df['gender'].replace({'g': 'w', 'h': 'w', '?': None})

    missing_counts = df.isna().sum().sort_values(kind='stable')
    return missing_counts.index.tolist()


def task_2():
    df = df_bellevue.copy()

    print(
        "Data issue: 'date_in' is stored as text, so it's converted to "
        "datetime in order to pull out the year."
    )
    df['year'] = pd.to_datetime(df['date_in']).dt.year

    return (
        df.groupby('year')
        .size()
        .reset_index(name='total_admissions')
    )


def task_3():
    df = df_bellevue.copy()

    print(
        "Data issue: 'gender' contains typo values 'g'/'h' (mapped to 'w') "
        "and '?' entries (treated as missing/excluded) before averaging age. "
        "Rows with a missing 'age' are also excluded automatically."
    )
    df['gender'] = df['gender'].replace({'g': 'w', 'h': 'w', '?': None})

    return df.groupby('gender')['age'].mean()


def task_4():
    df = df_bellevue.copy()

    print(
        "Data issue: 'profession' has missing values, which are excluded "
        "automatically when counting the most common professions."
    )
    return df['profession'].value_counts().head(5).index.tolist()
