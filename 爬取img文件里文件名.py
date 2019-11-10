import os
filePath = './img'
B=os.listdir(filePath)
with open("文件名.txt","w") as f:
    for i in range(len(B)):
        if i<len(B)-1:
            f.write("'./img/"+B[i]+"',\n")
        else:
            f.write("'./img/" + B[i] + "'\n")
print(B)