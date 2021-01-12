#!/usr/bin/env python3

import platform
from subprocess import Popen
import sys
import argparse
from datetime import datetime
import time
from weather import get_weather

def send_notfication():
    system = platform.system()
    greeting = get_greeting()
    notification = get_weather()

    if system == 'Darwin':
        new_osx_notfication(greeting, notification)
    elif system == 'Linux':
        new_linux_notification(greeting, notification)
    else:
        raise SystemError("Sorry, notifcations are not curently supported on {}".format(system))

def new_osx_notfication(title, message):    
    command = Popen(['osascript', '-e display notification "{}" with title "{}"'.format(message, str(title))])
    command.communicate()

def new_linux_notification(title, message):
    Popen(['notify-send', str(title), str(message)])
    return

def get_greeting():
    current_hour = datetime.now().hour
    message = ''
    
    if current_hour <= 11:
        message = 'Good Morning!'
    elif current_hour >= 12 and current_hour <= 16:
        message = 'Good Afternoon!'
    else: 
        message = 'Good Evening!'
    
    return message

if __name__ == '__main__':
    send_notfication()