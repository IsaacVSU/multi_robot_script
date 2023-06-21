def deleteDisplays():
    DeleteLinesThrough = []
    with open("sekhmet.rviz", 'r') as f:
        data = f.readlines()
        for i, ii in enumerate(data):
            if "Global Options:" in ii:
                DeleteLinesThrough.append(i-2)
            if "Displays:" in ii:
                DeleteLinesThrough.append(i+1)
        DeleteLinesThrough.pop(len(DeleteLinesThrough)-1)
        #print(DeleteLinesThrough)
    for i in range(DeleteLinesThrough[0], DeleteLinesThrough[1]):
        DeleteLinesThrough.append(i)
    with open('OutputFile.rviz', 'w') as f2:
        for i, ii in enumerate(data):
            if i in DeleteLinesThrough:
                #print(i, ii)
                continue
            f2.write(ii)
if __name__ == '__main__':
    deleteDisplays()

# def removeRobots(robotSet: set):
#     linesToDelete = []
#     robotsToDel = []
#     robotList = list(robotSet)
#     with open('Robots.txt', 'r') as f:
#         data = f.readlines()
#         NoEscChars = [e.strip() for e in data]
#         if len(robotList) > len(NoEscChars):
#             robotsToDel = [e for e in robotList if e not in NoEscChars]
#             print(robotsToDel)
#         with open('sekhmet.rviz', 'r') as f2:
#             lines = f2.readlines()
#             for line, elem in enumerate(lines):
#                 for ee in robotsToDel:
#                     if ee in elem:
#                         linesToDelete.append(line)
#             temp = linesToDelete.copy()
#             for i in temp:
#                 for ii in range(-2, 10):
#                     linesToDelete.append(i+ii)
#             print(linesToDelete)
#         with open('OutputFile.rviz', 'w') as f3:
#             for line, elem in enumerate(lines):
#                 if line not in linesToDelete:
#                     f3.write(elem)

