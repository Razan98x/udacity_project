import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Which city do you want to explore chicago, new york or washington? ')
    city=city.lower()
    while city not in CITY_DATA.keys():
        city=input('enter one of the cities you want to see the data chicgo, new york or washington?')
        city=city.lower()

    # get user input for month (all, january, february, ... , june)

    while True:
        month=str(input('wwich month?  january , februrary, march ,aprill, may ,june or all ')).lower()
        if month in ('all','january', 'february','march', 'april', 'may', 'june'):
            break
        else:
            print('invalid value')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        try:
            day=int(input('which day?please enter int value from 1 to 7?... 1 for saturday ect'))
            if day <= 7:
              break
        except ValueError:
            print('not a valid number')


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
    df=pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df["End Time"]=pd.to_datetime(df['End Time'])

    df['month']=df['Start Time'].dt.month
    df['day of week']=df['Start Time'].dt.dayofweek
    df['start hour']=df['Start Time'].dt.hour

    if month !='all':
        months=['january', 'february','march', 'april', 'may', 'june']
        month=months.index(month) + 1
        df=df[df['month']==month]

    df=df[df['day of week']==day]



    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month=df['month'].mode()[0]

    # display the most common day of week
    common_dow=df['day of week'].mode()[0]

    # display the most common start hour
    common_hour=df['start hour'].mode()[0]
    print('most common month: {} day : {} hour: {} '.format(common_month,common_dow,common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start=df['Start Station'].mode()[0]
    print('most common Start Station : ',common_start)

    # display most commonly used end station
    common_end=df['End Station'].mode()[0]
    print('most common End Station : ',common_end)


    # display most frequent combination of start station and end station trip
    frequent_com=df['Start Station']+df['End Station']
    frequent_com.mode()[0]
    print('most most frequent combination of start station and end station trip',frequent_com)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel=df['Trip Duration'].sum()
    print('total travel time : ',total_travel)


    # display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print('Average trip duration : ', mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_count=df['User Type'].value_counts()
    print('count of user type : ',user_count)



    if city == 'washington':
        print('there is NO gender and birth of year on this data:)')
    else:
        gender_count=df['Gender'].value_counts()
        print('count of Gender : ',gender_count)
        # Display earliest, most recent, and most common year of birth
        common_year=df['Birth Year'].mode()[0]
        print('most common year of birth : ',common_year)

        earliest_year=df['Birth Year'].min()
        print('The earliest year of birth : ',earliest_year)

        recent_year=df['Birth Year'].max()
        print('The recent year of birth : ',recent_year)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        i=5

        while True:
            user_chose=input('do you wanna see the data enter YES or NO :')

            if user_chose.lower() == 'yes':
                print(df.head(i))
                i+=5
                continue
            else:
                print('\n ')
                break


        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
