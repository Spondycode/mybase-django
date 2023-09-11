import datetime
import time

# Define the future date and time
future_date = datetime.datetime(2023, 12, 31, 23, 59, 59)

while True:
    # Get the current date and time
    current_date = datetime.datetime.now()
    
    # Calculate the time difference
    time_difference = future_date - current_date
    
    # Check if the countdown has reached zero
    if time_difference.total_seconds() <= 0:
        print("Countdown completed!")
        break
    
    # Extract days, hours, minutes, and seconds
    days = time_difference.days
    hours, remainder = divmod(time_difference.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    
    # Display the countdown
    print(f"Time left: {days} days, {hours} hours, {minutes} minutes, {seconds} seconds", end='\r')
    
    # Update every second
    time.sleep(1)

