import datetime
import time
import tkinter as tk
from tkinter import messagebox
import threading
import winsound  # For playing sound on Windows

# List to store set alarms
alarms_list = []

# Flag to control the alarm sound
alarm_active = False

# Function to update the clock display
def update_clock():
    current_time = datetime.datetime.now()
    time_string = current_time.strftime("%H:%M:%S")
    date_string = current_time.strftime("%A, %d %B %Y")
    label_clock.config(text=time_string)
    label_date.config(text=date_string)
    label_clock.after(1000, update_clock)

# Function to set the alarm
def set_alarm():
    alarm_time = entry_time.get()
    
    try:
        # Validate input format
        valid_time = datetime.datetime.strptime(alarm_time, "%H:%M")
        
        # Add the alarm to the alarms list
        alarms_list.append(alarm_time)
        update_alarms_listbox()
        
        label_status.config(text=f"Alarm set for {alarm_time}", fg="green")
        
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter time in HH:MM format")

# Function to update the alarms listbox
def update_alarms_listbox():
    listbox_alarms.delete(0, tk.END)  # Clear the listbox
    for alarm in alarms_list:
        listbox_alarms.insert(tk.END, alarm)

# Function to delete a selected alarm
def delete_alarm():
    try:
        selected_index = listbox_alarms.curselection()[0]  # Get selected alarm index
        alarms_list.pop(selected_index)  # Remove the alarm from the list
        update_alarms_listbox()  # Update the listbox to reflect the change
        label_status.config(text="Alarm deleted", fg="red")
    except IndexError:
        messagebox.showerror("Selection Error", "Please select an alarm to delete")

# Function to clear the input field
def clear_alarm():
    entry_time.delete(0, tk.END)
    label_status.config(text="Alarm cleared", fg="red")

# Function to stop the alarm sound
def stop_alarm():
    global alarm_active
    alarm_active = False
    label_status.config(text="Alarm stopped", fg="blue")

# Function to play the alarm sound
def play_alarm_sound():
    global alarm_active
    alarm_active = True
    end_time = time.time() + 120  # Play sound for 2 minutes
    while alarm_active and time.time() < end_time:
        winsound.Beep(1000, 1000)  # Beep sound for 1 second
    
    if alarm_active:  # Schedule next alarm after 10 minutes
        label_status.config(text="Snoozing for 10 minutes", fg="orange")
        threading.Timer(600, play_alarm_sound).start()  # 10-minute delay before playing again

# Function to check if any alarm matches the current time
def check_alarms():
    current_time = datetime.datetime.now().strftime("%H:%M")
    if current_time in alarms_list:
        messagebox.showinfo("Alarm", "Time to Wake Up!")
        alarms_list.remove(current_time)  # Remove the alarm once it goes off
        update_alarms_listbox()  # Update the listbox to reflect the change
        
        # Start a thread to play the alarm sound
        threading.Thread(target=play_alarm_sound, daemon=True).start()
    label_clock.after(1000, check_alarms)  # Check every second

# Create main window
root = tk.Tk()
root.title("Digital Alarm Clock")
root.geometry("400x600")
root.configure(bg="#2E3440")
root.resizable(True, True)  # Enable window resizing in both width and height

# Function to resize components dynamically
def resize_components(event):
    new_width = event.width
    new_height = event.height
    
    font_size_clock = max(24, new_width // 10)  # Dynamic font size for clock
    font_size_date = max(12, new_width // 25)   # Dynamic font size for date
    font_size_buttons = max(10, new_width // 30) # Dynamic font size for buttons
    
    label_clock.config(font=("Helvetica", font_size_clock, "bold"))
    label_date.config(font=("Helvetica", font_size_date))
    label_title.config(font=("Helvetica", font_size_date))
    entry_time.config(font=("Helvetica", font_size_buttons))
    button_set.config(font=("Helvetica", font_size_buttons))
    button_clear.config(font=("Helvetica", font_size_buttons))
    button_delete.config(font=("Helvetica", font_size_buttons))
    button_stop.config(font=("Helvetica", font_size_buttons))
    label_status.config(font=("Helvetica", font_size_buttons))

# Clock display label
label_clock = tk.Label(root, text="", font=("Helvetica", 48, "bold"), bg="#2E3440", fg="#D8DEE9")
label_clock.pack(pady=20, expand=True)

# Date display label
label_date = tk.Label(root, text="", font=("Helvetica", 18), bg="#2E3440", fg="#81A1C1")
label_date.pack(pady=5, expand=True)

# Title label for alarm
label_title = tk.Label(root, text="Set Alarm (24-hour format, HH:MM)", font=("Helvetica", 14), bg="#2E3440", fg="#88C0D0")
label_title.pack(pady=10, expand=True)

# Entry for alarm time
entry_time = tk.Entry(root, font=("Helvetica", 16), justify="center", bg="#4C566A", fg="#D8DEE9")
entry_time.pack(pady=5, expand=True)

# Set Alarm button
button_set = tk.Button(root, text="Set Alarm", command=set_alarm, font=("Helvetica", 14), bg="#5E81AC", fg="white")
button_set.pack(pady=10, expand=True)

# Clear Alarm button
button_clear = tk.Button(root, text="Clear Alarm", command=clear_alarm, font=("Helvetica", 14), bg="#BF616A", fg="white")
button_clear.pack(pady=10, expand=True)

# Delete Alarm button
button_delete = tk.Button(root, text="Delete Alarm", command=delete_alarm, font=("Helvetica", 14), bg="#D08770", fg="white")
button_delete.pack(pady=10, expand=True)

# Stop Alarm button
button_stop = tk.Button(root, text="Stop Alarm", command=stop_alarm, font=("Helvetica", 14), bg="#A3BE8C", fg="white")
button_stop.pack(pady=10, expand=True)

# Status label
label_status = tk.Label(root, text="", font=("Helvetica", 12), bg="#2E3440", fg="#E5E9F0")
label_status.pack(pady=10, expand=True)

listbox_alarms = tk.Listbox(root)
listbox_alarms.pack()

update_clock()
check_alarms()
root.mainloop()
