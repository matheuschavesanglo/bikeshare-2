import time
import pandas as pd
import time

time_sleep_a = 1
time_sleep_b = 0.5

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

city_dic = {1:'chicago', 
            2:'new york city', 
            3:'washington'}

month_dic = {1:'January', 
             2:'February', 
             3:'March',
             4:'April',
             5:'May',
             6:'June',
             7:'July',
             8:'August',
             9:'September',
            10:'October',
            11:'November',
            12:'December',
             0:'All'}

day_dic = {0:'Monday',
           1:'Tuesday', 
           2:'Wednesday',
           3:'Thursday',
           4:'Friday',
           5:'Saturday',
           6:'Sunday',
           7:'All'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
           
    while True:
        try:
            city_number = input("Please enter the city number:(1-Chicago, 2-New York City, 3-Washington)\n ")
            city_number = int(city_number)
            if city_number > 3:
                city_number = input("Please enter a valid number:(1-Chicago, 2-New York City, 3-Washington)\n ")
                city_number = int(city_number)
            break
        except ValueError:
            print("No valid integer! Please try again ...")
    
    city = city_dic[city_number]
    print('You have choose {}'.format(city))
    
    # get user input for month (all, january, february, ... , june)
    
    while True:
        try:
            month = input("Please enter the month number:(0-All, 1-January, 2-February... 12-December)\n ")
            month = int(month)
            if month > 12:
                month = input("Please enter a valid number:(0-All, 1-January, 2-February... 12-December)\n ")
                month = int(month)
            break
        except ValueError:
            print("No valid integer! Please try again ...")

    month_name = month_dic[month]
    print('You have choose {}'.format(month_name))
    
    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    
    while True:
        try:
            day = input("Please enter the day number:(0-Monday, 1-Tuesday, 3-Wednesday... 6-Sunday, 7-All)\n ")
            day = int(day)
            if day > 7:
                day = input("Please enter a valid number:(0-Monday, 1-Tuesday, 3-Wednesday... 6-Sunday, 7-All)\n ")
                day = int(day)
            break
        except ValueError:
            print("No valid integer! Please try again ...")

    day_name = day_dic[day]
    print('You have choose {}'.format(day_name))
    time.sleep(time_sleep_b)
    
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    view_options = ['yes', 'no']
    while True:
        try:
            view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
            view_data = view_data.lower()
            if view_data not in view_options:
                view_data = input('\nPlease enter a valide answer\nWould you like to view 5 rows of individual trip data? Enter yes or no\n')
                view_data = view_data.lower()
            break
        except ValueError:
            print("No valid answer! Please try again ...")
    start_loc = 0
    while view_data == 'yes':
        print(df.iloc[start_loc:(start_loc+5)])
        start_loc += 5
        view_data = input('Do you wish to continue?: ').lower()
        
        
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek

    # filter by month if applicable
    if month != 0:
              
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 7:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df
    
    

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    popular_month = df['month'].value_counts().idxmax()
    month_count = df['month'].value_counts()[popular_month]
    month = month_dic[popular_month]

    print('The most common month was "{}" with "{}" records.\n'.format(month, month_count))
    
    
    # display the most common day of week
    popular_day = df['day_of_week'].value_counts().idxmax()
    day_count = df['day_of_week'].value_counts()[popular_day]
    day = day_dic[popular_day] 
    print('The most common day of week was "{}" with "{}" records.\n'.format(day, day_count))
    
    
    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].value_counts().idxmax()
    hour_count = df['hour'].value_counts()[popular_hour]

    print('The most common hour was "{}h" whith "{}" records.\n'.format(popular_hour, hour_count))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(time_sleep_a)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_statiom = df['Start Station'].value_counts().idxmax()
    start_station_count = df['Start Station'].value_counts()[popular_start_statiom]
    print('The most common commonly used start station was "{}" with "{}" records\n'.format(popular_start_statiom, start_station_count))
    
    
    # display most commonly used end station
    popular_end_statiom = df['End Station'].value_counts().idxmax()
    end_station_count = df['End Station'].value_counts()[popular_end_statiom]
    print('The most common commonly used end station was "{}" with "{}" records\n'.format(popular_end_statiom,end_station_count))
    
    
    # display most frequent combination of start station and end station trip
    pop_start_end = df[['Start Station','End Station']].value_counts().idxmax()
    start_end_count = df[['Start Station','End Station']].value_counts()[pop_start_end]
    print('The most frequent combination of start station and end station trip was "{}" with "{}" records\n'.format(pop_start_end,start_end_count))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    time.sleep(time_sleep_a)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    total_duration = round((df['Trip Duration'].sum()/3600),2)
    
    mean_duration = round((df['Trip Duration'].mean()/60),2)
    
    # display total travel time
    print('Total travel time for the period was: "{}" hours\n'.format(total_duration))
    
    
    # display mean travel time
    print('Mean travel time for the period was: "{}" minutes\n'.format(mean_duration))
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(time_sleep_a)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Users Types:\n {}\n'.format(df['User Type'].value_counts().reset_index()))
    
    # Display counts of gender
    df_columns = df.columns
    df_columns = df_columns.to_list()
    check_gender = 'Gender'
    if check_gender in df_columns:
        print('Gender:\n {}\n'.format(df['Gender'].value_counts().reset_index()))
        
    else:
        print('The selcted citiy does not have "Gender" information on the dataset')
    
    # Display earliest, most recent, and most common year of birth
    
    earliest = min(df['Start Time'])
    most_recent = max(df['Start Time'])
    
    check_birth = 'Gender'
    if check_birth in df_columns:
        year_birth = df[['Birth Year']].value_counts().idxmax()
        
    else:
        year_birth = 'The selcted citiy does not have "Year Birth" information on the dataset'
   

    print('The earlist trip was: "{}".\nThe most recent trip was: "{}".\nThe most common year of birth is: "{}".\n'.format(earliest,most_recent,year_birth))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    time.sleep(time_sleep_a)

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
