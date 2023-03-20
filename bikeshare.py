import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        city = input("Would you like to see the data for Chicago, New York City, or Washington?\n ").lower()
        if city not in ('chicago', 'new york city', 'washington'):
            print("Sorry that is incorrect. Please choose Chicago, New York, or Washington.\n")
            continue
        else:
            break
            
        city.lower()

    # TO DO: get user input for month (all, january, february, ... , june)


    while True:
        month = input ("Which month? (all, January, February, April, May, June)\n")
        if month not in ('all', 'january', 'february', 'march', 'april', 'may', 'june'):
            print("Sorry that is incorrect. Please choose from all, January, February, April, May, June\n")
            continue
        else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    day = input("Which day: (all, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday)\n")
    while True:
        if day not in ('all', 'Monday', 'Tuesday', 'Wednesday', 'Thrusday', 'Friday', 'Saturday', 'Sunday'):
          print("Sorry that is incorrect. Please choose from all, Monday, Tuesday, Wednesday, Thrusday, Friday, Saturday, Sunday\n")
          continue
        else:
            break

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
    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns

    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    common_month = df['month'].mode()[0]
    print('Most Common Month: \n', common_month)


    # TO DO: display the most common day of week
    
    common_day = df['day_of_week'].mode()[0]
    print('Most Common Day: \n', common_day)

    # TO DO: display the most common start hour
    
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('Most Common Hour: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_station = df['Start Station'].value_counts().idxmax()
    print("Most commonly used Start Station: \n", start_station)

    # TO DO: display most commonly used end station
    end_station = df['End Station'].value_counts().idxmax()
    print("Most commonly used End Station: \n", end_station)

    # TO DO: display most frequent combination of start station and end station trip
    common_combination_station = df['Start Station'] + " to " +  df['End Station']
    common_combiniation_station = common_combination_station.mode()[0]
    print("Most Common Trip from Start to End:\n {}".format(common_combination_station))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    minute, second = divmod(total_time, 60)
    hour, minute = divmod(minute, 60)
    print("The total Travel Time is {} Hours, {} Minutes, and {} Seconds.".format(hour, minute, second))

    # TO DO: display mean travel time

    mean_time = round(df['Trip Duration'].mean())
    minute, second = divmod(mean_time, 60)
    
    if minute > 60:
        hour, minute = divmod(minute, 60)
        print('The mean Travel Time is {} Hours, {} Minutes, and {} seconds.'.format(hour, minute, second))
    else:
        print('The mean Travel Time is {} Minutes and {} Seconds.'.format(minute, second))
      

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
    user_types = df['User Type'].value_counts()
    print("Counts of Each User Type:\n", user_types)
	
    # TO DO: Display counts of gender
    try:
        gender = df['Gender'].value_counts()
        print(' ' * 40)
        print('Counts of Each User Gender: ', gender)
    except:
        print('User Gender:\nNo gender data available...')
      

    # TO DO: Display earliest, most recent, and most common year of birth

    # Earliest Year
    print("\nTemp\n")

    # Recent Year
    print("\nTemp\n")

    # Common Year
    print("\nTemp\n")
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


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
