# sekhmet
- [x] Get the output file to work with RVIZ

* w/o optional:
python3 FinalMain.py <main file>.rviz <Robot Names>.txt <perRobot>.rviz

* w/ optional
python3 FinalMain.py <main file>.rviz <Robot Names>.txt <perRobot>.rviz
--out <output file>.rviz

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

