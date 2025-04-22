#!/bin/bash

#  video.sh
#
#
#  Author: Maya Olin
#  Last Edit: 4/21/2025
#
# ------------------------------------------------------------
# Setup Environment
# ------------------------------------------------------------

echo ""
echo "Current Time:" $(date)

start=$(date)
hour=$(date +%H)



# Record video for 29 minutes and saves to a named file with a timestamp

# For Raspberry Pi 4 or earlier, save MP4 file


rpicam-vid -t 10s --codec libav -o test.mp4
