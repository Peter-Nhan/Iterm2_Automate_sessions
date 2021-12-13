#!/usr/bin/env python3
# Tutorial for scripting in Iterm2 https://iterm2.com/python-api/tutorial/index.html
import csv
import os
import iterm2

async def main(connection):
    # Programmatically grab the path where the script is executed
    script_dir = os.path.dirname(__file__)
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    if window is not None:
        # Open CSV file - each line has name and command
        # Make sure this Python code and the csv file are place into ~/Library/Application Support/iTerm2/Scripts
        # If your csv filename is different please update below.
        with open(script_dir+"/my_lab_sessions.csv", "rt") as f:
            reader = csv.DictReader(f)
            # Loop through csv, line by line 
            for csv_line in reader:
                await window.async_create_tab()
                session = app.current_terminal_window.current_tab.current_session
                # Change colour of tab
                change = iterm2.LocalWriteOnlyProfile()
                colour = iterm2.Color(102, 178, 255)
                change.set_tab_color(colour)
                change.set_use_tab_color(True)
                # Change colour of badge - text embedded into screen
                colour_badge = iterm2.Color(255, 255, 51, 129)
                change.set_badge_color(colour_badge)
                # Pull name from csv line and use for badge
                change.set_badge_text(csv_line['name'])
                await session.async_set_profile_properties(change)
                # Execute the command - could be telnet, ssh etc...
                await session.async_send_text(csv_line['command']+'\n')
    else:
        # You can view this message in the script console.
        print("No current window")

iterm2.run_until_complete(main)
