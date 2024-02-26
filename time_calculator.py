def add_time(start, duration, day=None):

  # Split the start time into hours and minutes
  time, ampm = start.split()
  hours, minutes = map(int, time.split(':'))
  # Split the duration into hours and minutes
  hours2b, minutes2b = map(int, duration.split(':'))
  # Convert the start time to 24-hour format
  if ampm == 'PM':
    hours += 12
    # Add the duration to the start time
  rem_hours = hours2b % 24
  days = hours2b // 24
  hours += rem_hours
  minutes += minutes2b
  # Convert the result back to 12-hour format
  if minutes >= 60:
    hours += 1
    minutes -= 60
  if hours >= 24:
    days += 1
    hours -= 24
  if hours >= 12:
    amp = 'PM'
    hours -= 12
  else:
    amp = 'AM'
  if hours == 0:
    hours = 12
  day2 = ''
  if days == 1:
    day2 = '(next day)'
  if days > 1:
    day2 = '(' + str(days) + ' days later)'

  if day is not None:
    day = day.lower()
    days_of_week = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'
    ]
    day_index = days_of_week.index(day)
    new_day_index = (day_index + days) % 7
    new_day = days_of_week[new_day_index]

    new_time = f"{hours}:{minutes:02d} {amp}, {new_day.capitalize()} {day2}".rstrip(
    )
  else:

    new_time = f"{hours}:{minutes:02d} {amp} {day2}".rstrip()

  return new_time
