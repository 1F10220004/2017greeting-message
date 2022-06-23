from datetime import datetime

def greet():
    hour = datetime.now().hour
    if hour <= 11:
        message = 'Good morning'
    elif hour <= 17:
        message = 'Good afternoon'
    else:
        message = 'Good evening'
    print(message)


greet()
