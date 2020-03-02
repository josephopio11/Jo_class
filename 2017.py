total_coll = 0.0  # To calculate total money collected through out the day
total_hours = 0  # To calculate total hours all the boats were hired
day_start = 10
day_end = 17
h_fee = 20
m_fee = 12
b_no = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b_status = ['yes'] * 10
b_return_time = [10] * 10
b_hours_hired = [0] * 10
b_collection = [0] * 10
while True:  # A loop to continuously check the time until the hire company is open
    import datetime  # To check the current time
    time = datetime.datetime.now().time()
    if day_start <= time.hour < day_end:
        break
hour_min = time.hour + time.minute / 60
while day_start <= time.hour < 17:
    import datetime  # To check the current time
    time = datetime.datetime.now().time()
    hour_min = time.hour + time.minute / 60
    available = 0
    for boat in range(len(b_no)):
        if b_return_time[boat] <= hour_min:
            b_status[boat] = 'yes'
    for boat in range(len(b_no)):
        if b_status[boat] == 'yes':
            available = available + 1
    print('Number of boats available is ', available)
    if available != 0:
        boat = 1
        while b_status[boat] != 'yes':
            print('check 101')
            boat = boat + 1
            if b_status[boat] == 'yes':
                print('Boat no.', boat, 'is available')
        s_time = float(
            input('Please input the start time of your journey in hours'))
        e_time = float(
            input('Please input the end time of your journey in hours'))
        while day_start < s_time < e_time <= day_end:
            print('check')
            dur_hours = e_time - s_time
            hour = int(dur_hours)
            minutes = (dur_hours - hour) * 60
            if minutes > 30:
                hire_cost = hour * 20 + 20
            elif 30 >= minutes > 0:
                hire_cost = hour * 20 + 12
            elif minutes == 0:
                hire_cost = hour * 20
            print('You have to pay ', hire_cost)
            print('Please take boat number ', boat)
            b_status[boat] = 'no'
            b_collection[boat] = b_collection[boat] + hire_cost
            b_return_time[boat] = e_time
            b_hours_hired[boat] = b_hours_hired[boat] + dur_hours
            total_hours = total_hours + dur_hours
            total_coll = total_coll + hire_cost
        if s_time < day_start or e_time > day_end or e_time <= s_time:
            print('ERROR in input please re-input')
    elif available == 0:
        fastest = 17
        for boat in range(len(b_no)):
            if b_return_time[boat] < fastest:
                fastest = b_return_time[boat]
        print('No boats are available you must wait till ', fastest)
print('the total money collected is $', total_coll,'and the total hours the boats were hired is ', total_hours)
not_used = 0
for boat in range(len(b_no)):
    if b_return_time[boat] == 10:
        not_used = not_used + 1
print('The number of boats not hired at all during the day were ', not_used)
highest = 0
boat_most_used = ''
for boat in range(len(b_no)):
    if b_collection[boat] > highest:
        highest = b_collection[boat]
        boat_most_used = b_no[boat]
print('The most used boat was ', boat_most_used)
for boat in range(len(b_no)):
    if b_collection[boat] == highest and b_no != boat_most_used:
        also_highest = b_no
        print('Boat number', also_highest,
              'also was one of the most used boats')
# END of the day
