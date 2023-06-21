def ImportFromList():
    with open("test2.txt", 'r+') as f:
        temp = []
        data = f.readlines()
        for i in data:
            temp.append(i.strip())
        # print(temp)

def scanList():
    with open('test1.rviz', 'r') as f:
        data = f.readlines()
    
    image_topic = 'Image Topic:'
    robots = set()
    for ii in data:
        if image_topic in ii:
            idx1 = ii.find('/')
            idx2 = ii.find('/', idx1+2)
            robotname = ii[idx1+1:idx2:]
            robots.add(robotname)
    print(robots)

ImportFromList()
scanList()

        

