# Iterm2_Automate_sessions
MAC OS Iterm2 automate connecting to network devices - will open new tab and set badge text 
Edit "my_lab_sessions.csv" change the badge name and the commands that Iterm2 would use to connect to your device.
One device per line, and Iterm2 will open a new tab for each and set badge text name.

Store both files in ~/Library/Application Support/iTerm2/Scripts on the Mac OS.
To have multiple of these Automate session files - duplicate them update the csv file with new devices - makes sure you provide new names for both files (py and csv). Also update lines 16  of the py file with the new csv filename.

More details available in the blog - https://peter-nhan.github.io/posts/Iterm2_automation/
