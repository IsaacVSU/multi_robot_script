import argparse
"""
$robot
 * Find and replace "$robot" with a robotName under displays
 * TODO: replace robot with (arg robot)
"""
parser = argparse.ArgumentParser(description= "Make an outPutFile from 3 inputs for rviz\
                                 Default is OutputFile.rviz")

parser.add_argument('main', metavar = 'MainInputFile',type=argparse.FileType('r'),
                    help = "The main file you need to create an output file under \"displays:\"" )

parser.add_argument('RobotNames', metavar = 'RobotNames',type=argparse.FileType('r'),
                    help = "All Robot names in a .txt file")

parser.add_argument('perRobot', metavar="template file",type=argparse.FileType('r'),  
                    help = "Template file, replace $robot with robot names")

#Make OutputFileOptional
parser.add_argument('--out', metavar="OutPutFile", default='OutputFile.rviz', 
                    required=False,type = argparse.FileType('w'), help = "The output file of this program")


args = parser.parse_args()

# print(args)
# print(args.main)

def getPerRobot_Data():
    LinesUnderDisplay = []
    with open(args.main.name) as f:
        data = f.readlines()
        for i, ii in enumerate(data):
            if "Global Options:" in ii:
                LinesUnderDisplay.append(i-1)
            if "Displays:" in ii:
                LinesUnderDisplay.append(i+1)
        LinesUnderDisplay.pop(len(LinesUnderDisplay)-1)
    return LinesUnderDisplay, data
Displays_Lines = getPerRobot_Data()[0]


data = getPerRobot_Data()[1]
data1 = data[0:Displays_Lines[0]]
dataUnderDisplays = data[Displays_Lines[0]:Displays_Lines[1]]
data2 = data[Displays_Lines[1]::]

class TemplateFile:
    def __init__(self):
        self.lines = []
        with open(args.perRobot.name) as file:
            self.template = file.readlines()
        #Preserve
        self.data = self.template.copy()
        self.lineswithToken()
    
    def lineswithToken(self):
        for i, ii in enumerate(self.data):
            if '$robot' in ii:
                self.lines.append(i)

    def replaceRobotNames(self, name):
        for i in self.lines:
            self.data[i] = self.template[i].replace('$robot', name)

perRobotFile = TemplateFile()
# print(perRobotFile.lines)

with open(args.RobotNames.name) as f:
    x = f.readlines()

Robotnames = [e.strip() for e in x]

#Put This under diplays in outputFile
#Use sekmet.rviz for the rest
outPutFile = []
for name in Robotnames:
    perRobotFile.replaceRobotNames(name)
    outPutFile.append("    - Class: rviz/Group\n")
    outPutFile.append("      Displays:\n")
    for d in perRobotFile.data:
        outPutFile.append(f"    {d}")
    outPutFile.append("\n      Enabled: true\n")
    outPutFile.append("      Name: {}Robot\n".format(name))

with open(args.out.name, 'w') as fileW:
    data1 = "".join(data1)
    outPutFile = "".join(outPutFile)
    data2 = "".join(data2)
    dataUnderDisplays = "".join(dataUnderDisplays)
    fileW.write(data1)
    fileW.write(outPutFile)
    fileW.write(dataUnderDisplays)
    fileW.write(data2)

print("Data1")
print(data1)
print("--------")

print("outPutFile")
print(outPutFile)
print("--------")

print("Data under displays")
print(dataUnderDisplays)
print("--------")

print("data2")
print(data2)