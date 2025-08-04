
# UrchinCAM microSD Formatting and Initial Raspberry Pi OS Configuration

### SD Card Formatting On Mac
Use SD Card Formatter to format the SD card. 
<img width="409" height="413" alt="Screenshot 2025-08-04 at 9 47 25 AM" src="https://github.com/user-attachments/assets/93f356f8-bbe8-4203-b2c6-cee5f482527a" />

Open Disk Utility. Navigate to the SD card and select Erase. Select MS-DOS (FAT) or MS-DOS (FAT32) and erase. 
<img width="804" height="467" alt="Screenshot 2025-08-04 at 9 48 01 AM" src="https://github.com/user-attachments/assets/b30ab9c3-39e3-49ab-a0d4-4e25d4b10550" />

### Install Raspberry Pi OS on SD Card
Install Raspberry Pi Imager at [this weblink](https://www.raspberrypi.com/software/). 

Open Raspberry Pi Imager and specify the Pi device, the desired OS, and the SD card. 
<img width="674" height="473" alt="Screenshot 2025-08-04 at 9 53 15 AM" src="https://github.com/user-attachments/assets/6ef890e8-ba3e-4f3b-aeb1-d0ed0d2581df" />

Select Edit Settings. 
<img width="676" height="470" alt="Screenshot 2025-08-04 at 9 54 02 AM" src="https://github.com/user-attachments/assets/9ac2890c-8d56-4619-b773-656bbee3b775" />

User: pi

Password: urchin$

Time Zone: Pacific/Honolulu 

Select Yes. 

Wait for write to complete and then insert microSD card into Raspberry Pi Zero 2 W and proceed directly on the pi desktop interface. 

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
### Initialize USB Flash Drive (if applicable)
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

### Run bash script on boot using Witty Pi
Open the Witty Pi after startup script. This will run the UrchinCAM Python script after Witty Pi has booted up the Raspberry Pi and after Witty Pi has finished running the schedule script. 
```
pi@raspberrypi:~ $ cd wittypi
pi@raspberrypi:~/wittypi $ sudo nano afterStartup.sh
```
Add the following to the bottom of the script. 
```
/home/pi/UrchinCAM_repo/UrchinCAM.py &
```
Save (ctrl+O) and exit (ctrl+X). 

To run the script headless with sudo, you must grant passwordless permission to the script. 
```
sudo visudo
```
Add this line at the bottom.
```
pi ALL=(ALL) NOPASSWD: /home/pi/UrchinCAM_repo/UrchinCAM.sh &
```
Now, the Pi will NOT prompt for a password when running the script automatically on boot. 


### Run Python script on boot with .conf file
Download the Supervisor package. 
```
sudo apt install supervisor
```
Place the config file inside /etc/supervisor/conf.d/ . 
```
sudo cp /path/to/config/file.conf /etc/supervisor/conf.d/
```
Make sure that the file has been created inside supervisor and that the path and file names are correct. 
```
cd /etc/supervisor/conf.d/
sudo nano file.conf
```
To stop the file from running, open the .conf script, in this case named urchincam.conf, and change autostart and autorestart from true to false. 
Then, use the following command to stop the current iteration of the script. 
```
sudo supervisorctl stop urchincam
```
To restart, change autostart and autorestart back to true, and run the following command. 
```
sudo supervisorctl start urchincam
```
To check whether supervisor is running the script, use this command. 
```
sudo supervisorctl status
```

# Extracting Video Files
### Unmount the USB flash drive
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
Video files should be inside UrchinCAM folder. Each video file should be ~60-100 MB. The video length will be listed as 00:00:00 and will be in .h264 file format. 

Batch convert video files using ffmpeg. 

On Mac, open Terminal to install ffmpeg. 
```
brew install ffmpeg
```

Navigate to the folder that holds the input video files. 
Create a folder to hold the converted files. 
```
cd /path/to/your/folder
mkdir converted
```
Use the following loop to convert all files in the folder. 
```
for f in *.h264; do ffmpeg -i "$f" -c copy "converted/${f%.*}.mp4"; done
```


# Interacting with GitHub
### Configure Raspberry Pi with a GitHub Repository
First, make sure that git is installed and up to date on the Raspberry Pi. 
```
sudo apt-get install git
```
Clone a GitHub repository to the Raspberry Pi. Replace user-name and repository-name with the appropriate names.
```
git clone https://github.com/user-name/repository-name.git
```
Check to make sure that the repository is now copied onto the Raspberry Pi. 
```
cd repository-name
ls
```
[Link to video tutorial](https://www.youtube.com/watch?v=9CULlsc5BBU)
### Initial Commit and Push to GitHub
Navigate to the GitHub repository on the Pi. 
```
cd /path/to/repository
```
Use the following commands to connect to GitHub. Replace values as needed.
```
git add --all
git config --global user.email "mayaolin@hawaii.edu"
git config --global user.name "maya-ocean"
git config --global credential.helper store
git commit -m "Uploading changes to file"
git push -u origin main
```
This process may yield a prompt to login to the GitHub account with a username and password. For the username, input the appropriate GitHub username. For the password, you must use a token generated by your GitHub account. 

For details on how to create a Personal Access Token, refer to [this guide from GitHub](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic). 

### Commit and Push to GitHub
After the first time pushing to GitHub from the Raspberry Pi, use the following commands to push changes to GitHub from the Pi. 
```
cd /path/to/repository
git add --all
git commit -m "Note any changes"
git push -u origin main
```
[Link to video tutorial](https://www.youtube.com/watch?v=WsGhCOEIDXo)
