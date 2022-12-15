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
      city = input("Would you like to see data for chicago, new york city, or washington?\n").lower()
      if city not in ('new york city', 'chicago', 'washington'):
        print("----\n")
        print("Sorry, Try again.")
        continue
      else:
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
          month = input("\nWould you like to filter the data by witch month: january, february, march, april, may, june or type 'all'?\n").lower()
          if month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            print("----\n")
            print("Sorry, Try again.")
            continue
          else:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
      day = input("Would you like to filter the data by witch day: sunday, monday, tuesday, wednesday, thursday, friday, saturday or type 'all'?\n").lower()
      if day not in ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'):
        print("----\n")
        print("Sorry, Try again.")
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
    
    df = pd.read_csv(CITY_DATA[city])
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
        
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print("----\n")
    print('the most common month:', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print("----\n")
    print('the most common day of week:', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("----\n")
    print('the most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_Station = df['Start Station'].value_counts().idxmax()
    print("----\n")
    print('most commonly used start station:', Start_Station)

    # TO DO: display most commonly used end station
    End_Station = df['End Station'].value_counts().idxmax()
    print("----\n")
    print('most commonly used end station:', End_Station)

    # TO DO: display most frequent combination of start station and end station trip
    Combination_Station = df.groupby(['Start Station', 'End Station']).count()
    print("----\n")
    print('most frequent combination of start station and end station trip:', Start_Station, " & ", End_Station)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    Total_Travel_Time = sum(df['Trip Duration'])
    print("----\n")
    print('total travel time:', Total_Travel_Time/86400, " Days")


    # TO DO: display mean travel time
    Mean_Travel_Time = df['Trip Duration'].mean()
    print("----\n")
    print('mean travel time:', Mean_Travel_Time/60, " Minutes")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print("----\n")
    print('counts of user types:', user_types)

    # TO DO: Display counts of gender
    try:
      gender_types = df['Gender'].value_counts()
      print("----\n")
      print('counts of gender:', gender_types)
    except KeyError:
      print("----\n")
      print("counts of gender: there is no data!!")

    # TO DO: Display earliest, most recent, and most common year of birth
    try:
      Earliest_Year = df['Birth Year'].min()
      print("----\n")
      print('earliest year of birth:', Earliest_Year)
    except KeyError:
      print("----\n")
      print("earliest year of birth: there is no data!!")

    try:
      Most_Recent_Year = df['Birth Year'].max()
      print("----\n")
      print('most recent year of birth:', Most_Recent_Year)
    except KeyError:
      print("----\n")
      print("most recent year of birth: there is no data!!")

    try:
      Most_Common_Year = df['Birth Year'].value_counts().idxmax()
      print("----\n")
      print('most common year of birth:', Most_Common_Year)
    except KeyError:
      print("----\n")
      print("most common year of birth: there is no data!!")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def show_row_data(df):
    while True:
        view_data = input("would you like to see 5 lines of raw data? enter 'yes' or 'no'\n").lower()
        row=0
        if view_data == "yes":
          print(df.iloc[row : row + 5])
          row=+5
        elif  view_data == "no":
            break
        else:
            print("----\n")
            print("Sorry, Try again.")
            
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_row_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
print("thank you")