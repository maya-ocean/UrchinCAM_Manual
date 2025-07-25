
# UrchinCAM microSD Formatting and Initial Raspberry Pi OS Configuration

Erase microSD card and format as ExFAT (camille’s github)

Install Raspberry Pi Imager 
Use Raspberry Pi Imager to download OS onto microSD
PW: urchin$

# UrchinCAM Raspberry Pi Software Instructions

### Manually set date and time. 
    pi@raspberrypi:~ $ sudo date -s “2025-03-10 10:53:00”
    
### Turn on WiFi and connect to network.
Note: UHM WiFi can cause issues. If that's the case, try using another network or a phone hotspot. 

### Install Witty Pi package
  ```
  pi@raspberrypi:~ $ wget https://www.uugear.com/repo/WittyPi4/install.sh
  pi@raspberrypi:~ $ sudo sh install.sh
  ```

### Sync to Network Time 
  ```
  pi@raspberrypi:~ $ cd wittypi
  pi@raspberrypi:~/wittypi $ ./wittyPi.sh
  3 (sync with network time)
  13 (exit)
  cd ~
  ```

### Verify Git installation
```
pi@raspberrypi:~ $ sudo apt-get install git
```

### Clone GitHub Repository onto Pi
```
pi@raspberrypi:~ $ git clone https://github.com/maya-ocean/UrchinCAM_repo.git
```
Check to make sure full contents transferred. 
```
pi@raspberrypi:~ $ cd UrchinPOD_repo
pi@raspberrypi:~/UrchinCAM_repo $ ls
```

### Test camera 
```
libcamera-hello
```
Adjust camera lens by increasing the duration of the preview. The code runs the camera for 1 minute. 
```
pi@raspberrypi:~ $ libcamera-vid -t 60000
```
### Initialize USB Flash Drive
Make a directory that the USB drive can be mounted to. 
```
pi@raspberrypi:~ $ cd ~
pi@raspberrypi:~ $ sudo mkdir -p /mnt/DATA
pi@raspberrypi:~ $ sudo chown pi:pi /mnt/DATA
```

Insert USB Flash Drive into OTG adapter. 

Check to make sure the Raspberry Pi has recognized it. 
```
pi@raspberrypi:~ $ lsblk
```
You should see a device listed that is named sda1, sdb1, or something similar. 

The UrchinCAM script will mount the USB drive on boot. 

### Set Witty Pi schedule
Move the file on_28_off_2.wpi to the Schedules folder in the Witty Pi directory. 

Choose a schedule script in the Witty Pi interface. 
```
pi@raspberrypi:~ $ cd wittypi
pi@raspberrypi:~/wittypi $ ./wittyPi.sh
What do you want to do? 6 (Choose schedule script)
Which schedule script do you want to use? 3 (on_28_off_2.wpi)
```

### Run Python script on boot using Witty Pi
Open the Witty Pi after startup script. This will run the UrchinCAM Python script after Witty Pi has booted up the Raspberry Pi and after Witty Pi has finished running the schedule script. 
```
pi@raspberrypi:~ $ cd wittypi
pi@raspberrypi:~/wittypi $ sudo nano afterStartup.sh
```
Add the following to the bottom of the script. 
```
python3 /home/pi/UrchinCAM_repo/UrchinCAM.py &
```
Save (ctrl+O) and exit (ctrl+X). 


# Extracting Video Files
### Unmount the USB flash drive before ejecting
Check where the USB drive is mounted.
```
pi@raspberrypi:~ $ lsblk
```
Sync all writes (flush pending data to disk)
```
pi@raspberrypi:~ $ sync
```
If mounted at /mnt/DATA, unmount.
```
pi@raspberrypi:~ $ sudo umount /mnt/DATA
```
Make sure the external drive icon has disappeared from the Raspberry Pi. Physically remove the USB flash drive.

Note: You may get an error indicating the the drive is still in use. In that case, remove your script from the Witty Pi after startup file and reboot the Pi. Now try to unmount again. 

### Transfer and Convert Video Files
Input USB flash drive to computer. 
Video and log files should be inside UrchinCAM folder. Each video file should be ~60-100 MB. The video length will be listed as 00:00:00 and will be in .h264 file format. 
[Maybe use Handbrake - mixed success]

On Mac, open Terminal to install ffmpeg. 
```
brew install ffmpeg
```

Batch convert video files using ffmpeg. 
In Terminal, navigate to the folder that holds the input video files. 
Create a folder for your output files. 
```
mkdir converted
```
Use the following loop to convert all files in the folder. 
```
for f in *.h264; do ffmpeg -i "$f" -c copy "converted/${f%.*}.mp4"; done
```
