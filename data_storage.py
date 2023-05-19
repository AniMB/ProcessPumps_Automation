  
#        /\ \    / /\  
#       /__\ \  / /__\
#      /    \ \/ /    \

# This is the main file that shall be run. It calls all the rest of the modules
import serial
import csv
import graph
import gui
import formulas 
import excel

#Connecting to arduino port and then setting up serial object
arduino_port = input("Enter the name of the arduino port(read it from arduino IDE)")
baud = 9600

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)


# Author: Animish Murthy
# Date: 18/05/23

#Reading the raw values from the arduino,
inputted=[]
for i in range(5):
        getData = ser.readline()
        datastring = getData.decode('utf-8')
        datastring=datastring.split(',')
        inputted.append(datastring)
        

#This creates a GUI file and stores its output(a dictionary) in the variable value
value=gui.data_entry()

#It converts to the standard units which may be different from SI units
inputted_si=inputted
for i in inputted:
        suction=formulas.bar_to_m_h2o(i[1])
        delivery=formulas.bar_to_m_h2o(i[2])
        suction=inputted_si[1]
        delivery=inputted_si[2]
        

#Here some of the values are converted with respect to a proportionate value of RPM which is provided by the GUI
rated=[]
single=[]
def total_head(x,y,z):
        sum=x+y+z
        return sum
for i in inputted_si:
        single.append(formulas.ratedq(i[0],int(value['rpm_']),i[3]))
        single.append(formulas.ratedh(i[0],int(value['rpm_']),total_head(i[1],i[2],int(value['guageHeight_']))))
        single.append(formulas.ratedp(i[0],int(value['rpm_']),(int(value['motorEffi_'])*i[5])))
        single.append(formulas.efficiency(single[0],single[1],int(value['Density_']),int(value['motorEffi_']),i[5])) 
        rated.append(single)
        single=[]
print(rated)       
# Author: Animish Murthy
# Date: 18/05/23


#This is the final list that has all the elements that we need to enter into the table            
final = inputted_si
for k, item in enumerate(final):
    final[k].insert(1, inputted[k][1])
    final[k].insert(3, inputted[k][2])
    final[k].append((int(value['motorEffi_']) * final[k][-2]))
    print(type(rated[k]))
    final[k].extend(rated[k])

#Creates an excel file of the pump test report and then it plots the graph
excel.excel_file(final)
graph.grapher(rated, value['capacity_'], value['head_'])  

# Author: Animish Murthy
# Date: 18/05/23

          
