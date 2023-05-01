import serial
import csv
import graph
import gui




arduino_port = "COM3"
baud = 9600

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)



inputted=[]

file_name=input("Enter name of file:")
file_name=file_name+".csv"
for i in range(5):
        getData = ser.readline()
        datastring = getData.decode('utf-8')
        datastring=datastring.split(',')
        inputted.append(datastring)
        
with open(file_name, "w", newline='') as file:
        write = csv.writer(file)
        write.writerow(["Suction", "Delivery", "Flow", "Ampere", "Power", "Power Factor"])
        write.writerows(inputted)

entered_data=gui.data_entry()
value={}
for i in entered_data:
        if entered_data[i]!='rpm5_':
                value[i]=entered_data[i]
        else:
                break
        
graph.grapher(inputted,value['guageHeight_'])  