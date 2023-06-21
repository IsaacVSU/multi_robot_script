import rospy
import os
import csv

def ImportFromList():
    with open("test2.txt", 'r+') as f:
        data = f.readlines()

def remove_robots():
    pass
def Detect_Old_data(robotNames : set, name):
    if name in robotNames:
        return True
    return False

def InsertNew_Data(name: str, data : list, linenumber : int, currRobots : set):
    if Detect_Old_data(currRobots, name):
        return data
    else:
        with open('newcsv.csv', encoding='utf-8',newline='') as f2:
            y = csv.reader(f2, delimiter=',')
            listInfor = [val for val in y]
            #print(listInfor[0])
            print(listInfor[2][3])
            data.insert(linenumber - 1,f"       Class: camera_plugins/CameraOverlay\n\
            Enabled: true\n\
            Image Topic: /{name}/camera/image_raw\n\
            Name: CameraOverlay\n\
            Overlay Alpha: 0.800000011920929\n\
            Overlay Scale: 0.5\n\
            Overlay x: 0\n\
            Overlay y: 0\n\
            Queue Size: 2\n\
            Transport Hint: raw\n\
            Unreliable: false\n\
            Value: true\n\
      Alpha: 1\n\
            Autocompute Intensity Bounds: true\n\
            Autocompute Value Bounds:\n\
                Max Value: 10\n\
                Min Value: -10\n\
                Value: true\n\
            Axis: Z\n\
            Channel Name: intensity\n\
            Class: rviz/PointCloud2\n\
            Color: 255; 255; 255\n\
            Color Transformer: Intensity\n\
            Decay Time: 0\n\
            Enabled: true\n\
            Invert Rainbow: false\n\
            Max Color: 255; 255; 255\n\
            Min Color: 0; 0; 0\n\
            Name: PointCloud2\n\
            Position Transformer: XYZ\n\
            Queue Size: 10\n\
            Selectable: true\n\
            Size (Pixels): 3\n\
            Size (m): 0.009999999776482582\n\
            Style: Flat Squares\n\
            Topic: /sekhmet/lidar_points\n\
            Unreliable: false\n\
            Use Fixed Frame: true\n\
            Use rainbow: true\n\
            Value: false\n\
            Class: rviz/Marker\n\
            Enabled: true\n\
            Marker Topic: /{name}/robot_marker\n\
            Name: Marker\n\
            Namespaces:\n\
                \"\": true\n\
            Queue Size: 100\n\
            Value: true\n\
            Alpha: 0.4000000059604645\n\
            Class: rviz/Map\n\
            Color Scheme: map\n\
            Draw Behind: false\n\
            Enabled: true\n\
            Name: Map\n\
            Topic: /{name}/point_cloud_cache/renderers/full_map\n\
            Unreliable: false\n\
            Use Timestamp: false\n\
            Value: true\n\
            Alpha: 0.4000000059604645\n\
            Class: rviz/Map\n\
            Color Scheme: map\n\
            Draw Behind: false\n\
            Enabled: true\n\
            Name: Map\n\
            Topic: /map\n\
            Unreliable: false\n\
            Use Timestamp: false\n\
            Value: true\n\
    -       Alpha: 1\n\
            Buffer Length: 1\n\
            Class: rviz/Path\n\
            Color: 25; 255; 0\n\
            Enabled: true\n\
            Head Diameter: 0.30000001192092896\n\
            Head Length: 0.20000000298023224\n\
            Length: 0.30000001192092896\n\
            Line Style: Lines\n\
            Line Width: 0.029999999329447746\n\
            Name: Path\n\
            Offset:\n\
                X: 0\n\
                Y: 0\n\
                Z: 0\n\
            Pose Color: 255; 85; 255\n\
            Pose Style: None\n\
            Queue Size: 10\n\
            Radius: 0.029999999329447746\n\
            Shaft Diameter: 0.10000000149011612\n\
            Shaft Length: 0.10000000149011612\n\
            Topic: /{name}/navigation_manager/global_plan\n\
            Unreliable: false\n\
            Value: true\n\
                Alpha: 1\n\
            Buffer Length: 1\n\
            Class: rviz/Path\n\
            Color: 25; 255; 0\n\
            Enabled: true\n\
            Head Diameter: 0.30000001192092896\n\
            Head Length: 0.20000000298023224\n\
            Length: 0.30000001192092896\n\
            Line Style: Lines\n\
            Line Width: 0.029999999329447746\n\
            Name: Path\n\
            Offset:\n\
                X: 0\n\
                Y: 0\n\
                Z: 0\n\
            Pose Color: 255; 255; 85\n\
            Pose Style: None\n\
            Queue Size: 10\n\
            Radius: 0.029999999329447746\n\
            Shaft Diameter: 0.10000000149011612\n\
            Shaft Length: 0.10000000149011612\n\
            Topic: /{name}/navigation_manager/local_plan\n\
            Unreliable: false\n\
            Value: true\n\
            Class: rviz/MarkerArray\n\
            Enabled: true\n\
            Marker Topic: /{name}/omnigraph/visuals\n\
            Name: MarkerArray\n\
            Namespaces:\n\
                {name}\
            Queue Size: 100\n\
            Value: true\n\
            Alpha: 1\n\
            Axes Length: 1\n\
            Axes Radius: 0.10000000149011612\n\
            Class: rviz/Pose\n\
            Color: 255; 25; 0\n\
            Enabled: true\n\
            Head Length: 0.30000001192092896\n\
            Head Radius: 0.10000000149011612\n\
            Name: Pose\n\
            Queue Size: 10\n\
            Shaft Length: 1\n\
            Shaft Radius: 0.05000000074505806\n\
            Shape: Arrow\n\
            Topic: /{name}/local_planner/carrot_goal\n\
            Unreliable: false\n\
            Value: true\n\
            Class: rviz/Marker\n\
            Enabled: true\n\
            Marker Topic: /{name}/local_planner/plan_debug\n\
            Name: Marker\n\
            Namespaces:\n\
                mppi_local_plan: true\n\
            Queue Size: 100\n\
            Value: true\n\
            Class: rviz/InteractiveMarkers\n\
            Enable Transparency: true\n\
            Enabled: true\n\
            Name: InteractiveMarkers\n\
            Show Axes: false\n\
            Show Descriptions: true\n\
            Show Visual Aids: false\n\
            Update Topic: /rviz/team_behavior_graph/update\n\
            Value: true\n")
            data = "".join(data)

    return data

#Get Robot name
ns = rospy.get_namespace()

with open('test.rviz', 'r') as f:
    data = f.readlines()

lineNumber = 0
image_topic = 'Image Topic:'
robots = set()
for ii in data:
    if image_topic in ii:
        idx1 = ii.find('/')
        idx2 = ii.find('/', idx1+2)
        robotname = ii[idx1+1:idx2:]
        robots.add(robotname)
print(robots)


#Find the line to insert new info
for i, ii in enumerate(data):
    if 'Global Options:' in ii:
        print(i)
        lineNumber = i

with open('test.rviz', "w") as f:
    # data = "".join(data)
    # print(type(data))

    #use this to add new robots in test 1
    with open('test2.txt', 'r+') as f2:
        test2_data = f2.readlines()
        #for i in test2_data: 
        help = InsertNew_Data('purple', data, lineNumber, robots)
        if help is None:
            print("Same")
        else:
            help = "".join(help)
            f.write(help)
