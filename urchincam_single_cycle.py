#!/usr/bin/env python3
import time
from datetime import datetime, timedelta
import subprocess
import os
import signal
import sys

# Log file name
LOG_FILE = "urchin_log.txt"

# Graceful exit flag
should_exit = False

def log(message):
    timestamp = datetime.now().strftime ("%Y-%m-%d %H:%M:%S")
    formatted = f"[{timestamp}] {message}"
    print (formatted)
    with open (LOG_FILE, "a") as f:
        f.write (formatted + "\n")

def signal_handler (sig, frame):
    global should_exit
    print ("[!] Received interrupt signal. Preparing to exit gracefully...")
    log ("[!] Received interrupt signal. Preparing to exit gracefully...")
    should_exit = True

signal.signal (signal.SIGINT, signal_handler)

# Start camera recording for given duration in seconds
def start_camera_recording(duration_secs):
    current_time = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")
    h264_file = f"video_{current_time}.h264"
    mp4_file = f"video_{current_time}.mp4"

    print(f"[{datetime.now().strftime('%H:%M:%S')}] Recording for {duration_secs} seconds → {mp4_file}")
    log (f"Recording for {duration_secs} seconds → {mp4_file}")
   
    command = [
        "libcamera-vid",
        "-t", str(duration_secs * 1000),
        "-o", h264_file,
        "--inline",
        "--nopreview"
    ]

    try:
        subprocess.run(command, check=True)
        
        # Convert to mp4.
        convert_command = [
            "ffmpeg", "-y",
            "-framerate", "30",
            "-i", h264_file,
            "-c", "copy",
            mp4_file
        ]
        subprocess.run (convert_command, check = True)
        os.remove (h264_file)
        
    except subprocess.CalledProcessError as e:
        print (f"[{datetime.now().strftime('%H:%M:%S')}] ERROR: Failed to record video.")
        print ("Command:", e.cmd)
        print ("Exit code:", e.returncode)
        log (f"ERROR: Failed to record video.")
        log (f"Command: {e.cmd}")
        log (f"Exit code: {e.returncode}")

# Main loop
def half_hour_cycle():  
    duration = 29 * 60   
    start_camera_recording(duration)
    time.sleep(10)

# Start the scheduler
half_hour_cycle ()
