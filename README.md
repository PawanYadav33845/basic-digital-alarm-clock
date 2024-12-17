Digital Alarm Clock
This is a Digital Alarm Clock application built using Python's tkinter for the graphical user interface (GUI).
It allows users to view the current time, date, and day while setting, managing, and deleting alarms.
The clock is interactive, resizable, and provides dynamic UI adjustments based on window size.

Features

Digital Clock: Displays current time, date, and day.
Resizable UI: UI elements resize dynamically when the window is resized.
Set Alarm: Allows the user to set multiple alarms using a 24-hour format (HH:MM).
Alarm Notifications: Alerts the user with a pop-up and plays a sound.
Snooze Alarm: If not stopped, the alarm replays every 10 minutes.
Stop Alarm: Stop the alarm sound at any time.
Manage Alarms: View, delete, and clear alarms from the list of active alarms.

Requirements
Python 3.x
Libraries: tkinter, datetime, threading, winsound (for Windows only)
Note: winsound is specific to Windows OS. For other platforms like macOS or Linux, you may need to use a cross-platform sound library like playsound.
How to Run
Install Python: Ensure Python 3.x is installed on your system.
Run the Script: Execute the script using the following command:
python alarm_clock_ui.py

Usage Instructions
Set an Alarm:
Enter the time in HH:MM format (24-hour format) in the input field.
Click the Set Alarm button.
The set alarm will be displayed in the list of alarms.
Delete an Alarm:
Select an alarm from the list.
Click Delete Alarm to remove the selected alarm.
Clear Input:
Click Clear Alarm to clear the time input field.
Stop the Alarm:
When the alarm rings, click Stop Alarm to stop the sound.
Snooze Feature:
If the alarm is not stopped, it will automatically snooze and play again after 10 minutes for 2 minutes.

UI Elements
Clock Display: Shows the current time in HH:MM:SS format.
Date Display: Shows the current day and date.
Input Field: Allows users to input alarm time in HH:MM format.

Buttons:
Set Alarm: Sets a new alarm.
Clear Alarm: Clears the input field.
Delete Alarm: Deletes a selected alarm from the list.
Stop Alarm: Stops the currently ringing alarm.
Status Label: Displays success, error, or status messages.
Alarms List: Shows a list of all active alarms.

Code Overview
Clock and Date: Updates the current time and date every second.
Alarms Management: Users can add, delete, and view active alarms.
Alarm Notification: When the set time matches the current time, a pop-up is displayed, and a sound plays.
Snooze Mechanism: If the alarm isn't stopped, it rings every 10 minutes for 2 minutes.
Dynamic Resizing: The font sizes and component sizes adjust automatically when the window is resized.

Possible Improvements
Add support for cross-platform alarm sounds.
Include customization options for the alarm sound.
Allow recurring alarms (e.g., daily, weekly).
Add theme customization for light/dark mode.

ScreenShots
![alarm clock](https://github.com/user-attachments/assets/f92fad30-851b-42c7-a059-e199cc6e294f)
![alarm](https://github.com/user-attachments/assets/ceeebf09-5fc2-4c1c-8953-7baa4ea80fa6)


License
This project is open-source and available for use under the MIT License.

Contributing
Feel free to submit issues or pull requests to improve this project. Contributions are welcome!

Pawan Yadav.
