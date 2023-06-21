"""     - Class: camera_plugins/CameraOverlay
        Enabled: true
        Image Topic: /morgana/camera/image_raw
        Name: CameraOverlay
        Overlay Alpha: 0.800000011920929
        Overlay Scale: 0.5
        Overlay x: 0
        Overlay y: 0
        Queue Size: 2
        Transport Hint: raw
        Unreliable: false
        Value: true
"""


def removeRobots(robotSet: set):
    linesToDelete = []
    robotsToDel = []
    robotList = list(robotSet)
    with open('Robots.txt', 'r') as f:
        data = f.readlines()
        NoEscChars = [e.strip() for e in data]
        if len(robotList) > len(NoEscChars):
            robotsToDel = [e for e in robotList if e not in NoEscChars]
            print(robotsToDel)
        with open('test1.rviz', 'r') as f2:
            lines = f2.readlines()
            for line, elem in enumerate(lines):
                for ee in robotsToDel:
                    if ee in elem:
                        linesToDelete.append(line)
            temp = linesToDelete.copy()
            for i in temp:
                for ii in range(-2, 10):
                    linesToDelete.append(i+ii)
            print(linesToDelete)
        with open('test3.rviz', 'w') as f3:
            for line, elem in enumerate(lines):
                if line not in linesToDelete:
                    f3.write(elem)


            



            

with open('test1.rviz', 'r') as f:
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
# print(robots)

removeRobots(robots)