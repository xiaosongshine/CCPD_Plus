import json
import glob
import tqdm
import os
import shutil
try:
    import xml.etree.cElementTree as ET

except ImportError:

    print("ImportError")
    import xml.etree.ElementTree as ET


provinces = ["皖", "沪", "津", "渝", "冀", "晋", "蒙", "辽", "吉", "黑", "苏", "浙", "京", "闽", "赣", "鲁", "豫", "鄂", "湘", "粤", "桂", "琼", "川", "贵", "云", "藏", "陕", "甘", "青", "宁", "新", "警", "学", "O"]
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W',
             'X', 'Y', 'Z', 'O']
ads = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
       'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'O']

def get_box(xfile="datas/1_yello.xml"):

    root = ET.parse(xfile).getroot()


    #print(root[6][0].tag + ": " +root[6][0].text)
    boxes = []

    for point in root[6][4]:
        boxes.append(point.text)
    name = root[6][0].text

    if len(root) == 7:

        return name,boxes
    else:
        return None

def get_points(jfile="datas/465_yello.json"):
    with open(jfile,"r") as f:
        jdata = json.loads(f.read())
    
    shapes = jdata["shapes"]
    slen = len(shapes)

    
    points = []

    if slen == 1:
        if shapes[0]["label"] == "p":
            points = shapes[0]["points"]
        
    elif slen == 4:
        points = [[0,0] for _ in range(4)]


        for i in range(slen):
            shape = shapes[i]
            points[int(shape["label"])-1] = shape["points"][0]
    else:
        print("err: ",jfile)
    
    return points




def get_ids(name):
    ids = []
    try:
        for i,n in enumerate(name):
        
            if i == 0:
                id1 = provinces.index(n)
            elif i == 1:
                id1 = alphabets.index(n)
            else :
                id1 = ads.index(n)
            
            ids.append(id1)
        
        return ids
    except:
        print(name)

        return None
    

if __name__ == "__main__":
    """
    imps = glob.glob("CCPD2021_unchange\\image\\*.jpg")

    print(len(imps),imps[:5])

    sses = []

    count = 0
    for imp in tqdm.tqdm(imps):
        xmlp = imp.replace(".jpg",".xml").replace("\\image\\","\\xml\\")

        jsp = imp.replace(".jpg",".json").replace("\\image\\","\\points\\")

        if os.path.exists(imp) and os.path.exists(xmlp) and os.path.exists(jsp):

            rets = get_box(xmlp)
            if None == rets:
                continue

            name,box = rets

            points = get_points(jsp)

            ids = get_ids(name)

            ss = imp+":"+str(box)+"*"+str(points)+"*"+str(ids)

            sses.append(ss)
            count += 1

    
    print(count,sses[:5])

    with open("data.txt","w") as f:

        for ss in sses:
            f.write(ss+"\n")
    """

    with open("data.txt","r") as f:
        allines = f.readlines()

    print(len(allines),allines[:5])
    
    for line in allines:
        try:
            file1,data = line.split(":")

            ss = "0-0_0-"

            #print(file1,data)

            datas = data.split("*")

            ss += str(eval(datas[0])[0])+"&"+str(eval(datas[0])[1])+"_"+str(eval(datas[0])[2])+"&"+str(eval(datas[0])[3])

            ss += "-" + str(int(eval(datas[1])[2][0]))+"&"+str(int(eval(datas[1])[2][1]))+"_"+str(int(eval(datas[1])[3][0]))+"&"+str(int(eval(datas[1])[3][1]))+"_"+str(int(eval(datas[1])[0][0]))+"&"+str(int(eval(datas[1])[0][1]))+"_"+str(int(eval(datas[1])[1][0]))+"&"+str(int(eval(datas[1])[1][1]))

            ss += "-" +str(eval(datas[2])[0])+"_"+str(eval(datas[2])[1])+"_"+str(eval(datas[2])[2])+"_"+str(eval(datas[2])[3])+"_"+str(eval(datas[2])[4])+"_"+str(eval(datas[2])[5])+"_"+str(eval(datas[2])[6])

            ss +="-0-0.jpg"

            #print(ss)

            dst = file1.replace(os.path.split(file1)[-1],ss).replace("\\image\\","\\sels\\")

            shutil.copy(file1,dst)
        except:
            print("err: ",line)

        #print(dst)
    


        

        