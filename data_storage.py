# Author: Animish Murthy
# Date: 18/05/23


import serial
import csv
import graph
import gui
import formulas 

# arduino_port = input("Enter the name of the arduino port(read it from arduino IDE)")
# baud = 9600

# ser = serial.Serial(arduino_port, baud)
# print("Connected to Arduino port:" + arduino_port)


# Author: Animish Murthy
# Date: 18/05/23
ser= [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17],
        [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34],
        [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48, 51]]
inputted=ser
# for i in range(5):
#         getData = ser.readline()
#         datastring = getData.decode('utf-8')
#         datastring=datastring.split(',')
#         inputted.append(datastring)
        

value=gui.data_entry()


inputted_si=inputted
for i in inputted:
        suction=formulas.bar_to_m_h2o(i[1])
        delivery=formulas.bar_to_m_h2o(i[2])
        suction=inputted_si[1]
        delivery=inputted_si[2]
        

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

              
final = inputted_si
for k, item in enumerate(final):
    final[k].insert(1, inputted[k][1])
    final[k].insert(3, inputted[k][2])
    final[k].append((int(value['motorEffi_']) * final[k][-2]))
    print(type(rated[k]))
    final[k].extend(rated[k])

               
graph.grapher(rated, value['capacity_'], value['head_'])  
