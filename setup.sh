#!/bin/bash

DIR=$HOME/bin

cd $HOME 

## Installs all requirements and creates a new cronjob
make_cron() {
    cd "$DIR"/weatherd && pip3 install --user -r requirements.txt && \
    echo "0 10 * * * $(which python3) $HOME/bin/weatherd/app.py" >> cron-notifier
    crontab cron-notifier && \
    echo "Success! Cron has been created - $(crontab -l)"
}

if [ -d "$DIR" ]; then
    make_cron 
fi

# If directory doesn't exist, create it
echo "Creating /bin/ directory at - $(pwd)" && \
mkdir bin 

# Find installed weeatherd directory and move contents to new <user>/bin directory
TARGET=$(find $HOME -type d -name "weatherd" -exec mv {} "$DIR" \;) && \

crontab -l > cron-notifier
echo "Creating new cronjob.." && \
make_cron \;