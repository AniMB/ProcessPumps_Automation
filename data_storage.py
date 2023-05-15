import serial
import csv
import graph
import gui
import formulas 

arduino_port = input("Enter the name of the arduino port(read it from arduino IDE)")
baud = 9600

ser = serial.Serial(arduino_port, baud)
print("Connected to Arduino port:" + arduino_port)



inputted=[]
for i in range(5):
        getData = ser.readline()
        datastring = getData.decode('utf-8')
        datastring=datastring.split(',')
        inputted.append(datastring)
        

entered_data=gui.data_entry()
value={}
for i in entered_data:
        if entered_data[i]!='vibz_': #change this to the correct variable
                value[i]=entered_data[i]
        else:
                break

inputted_si=inputted
for i in inputted:
        suction=formulas.bar_to_m_h2o(i[1])
        delivery=formulas.bar_to_m_h2o(i[2])
        suction=inputted_si[1]
        delivery=inputted_si[2]
rated=[]
def total_head(x,y,z):
        return lambda x,y,z:x+y+z
for i in inputted_si:
        rated.append(formulas.ratedq(i[0],value['rpm_'],i[3]))
        rated.append(formulas.ratedh(i[0],value['rpm_'],total_head(i[1],i[2],value['guageHeight_'])))
        rated.append(formulas.ratedp(i[0],value['rpm_'],(value['mototEffi_']*i[5])))
        rated.append(formulas.efficiency(rated[0],rated[1],value['Density_'],value['motorEffi_'],i[5])) 
               
final=inputted_si
for k in final:
        final[k].insert(1,inputted[k][1])
        final[k].insert(3, inputted[k][2])
        final[k].append(-1, (value['mototEffi_']*final[k][-1]))
        final[k].extend(rated[k])
               
graph.grapher(rated, value['capacity_'], value['head_'])  
