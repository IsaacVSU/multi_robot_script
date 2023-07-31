# Description
- This is a python program that allows you to generate multi-robot rviz files from a perRobot.rviz file, main.rviz, and a robotNames.txt.
- Outputs a file that was written from the combination of those 3 files.
* *Synopsis: 
    - Inputs:
        - PerRobot.rviz: Has a $robot in the file in order for the program to find and replace this with a robotName and put it all under "Displays" (behind "Enabled: true Global Options: ...)
        - Main.rviz: Everything else an rviz file will need
        - RobotNames.txt: List all the names of robots. Seperated by newlines. 
    - Output: 
        - OutputFile.rviz: The output file that you run in  rviz.

<p><b> NOTE: </b> The PerRobot.rviz needs to be tabbed in a specific way (ex: perRobot.rviz if need to see the format)</p> 
# Running FinalMain.py

* w/o optional:
  ```
  python3 FinalMain.py (main_file).rviz (Robot_Names).txt (per_Robot).rviz
  ```
* w/ optional
  ```
  python3 FinalMain.py (main_file).rviz (Robot_Names).txt (per_Robot).rviz --out (output_file).rviz
  ```
* Notes:
    * Default = OutputFile.rviz
    * PerRobot template file (find and replaces $robot in the file)
## Groups template
    - Class: rviz/Group
      Displays:
        - Class: rviz/Marker
          Enabled: true
          Marker Topic: /$robot/robot_marker
          Name: Marker
          Namespaces:
            {}
          Queue Size: 100
          Value: true
        - Class: rviz/InteractiveMarkers
          Enable Transparency: true
          Enabled: true
          Name: InteractiveMarkers
          Show Axes: false
          Show Descriptions: true
          Show Visual Aids: false
          Update Topic: /rviz/team_behavior_graph/update
          Value: true
      Enabled: true
      Name: $robot

