import os
import shutil
import schedule
import datetime

def backup(src, dst):
    for file in os.listdir(src):
        source_path = os.path.join(src, file)
        if os.path.isfile(source_path):  # Check if it's a file
            shutil.copy(source_path, dst)

def schedule_backup(src, dst, selected_date, selected_time):
    # Combine the selected date and time into a datetime object
    selected_datetime = datetime.datetime.strptime(f"{selected_date} {selected_time}", "%d/%m/%Y %H:%M")

    # Calculate the delay until the backup should occur
    current_datetime = datetime.datetime.now()
    delay = (selected_datetime - current_datetime).total_seconds()

    # Schedule the backup to occur after the calculated delay
    schedule.every(delay).seconds.do(backup, src, dst).tag('backup')
    schedule.run_pending()

    # Remove any previously scheduled backups to avoid duplication
    schedule.clear('backup')

    print(f"Backup scheduled for {selected_datetime}")
