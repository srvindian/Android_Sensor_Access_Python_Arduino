import serial
import range_changer as rc
import time

#%%
ser1 = serial.Serial('COM6', 9600, timeout=1)  #for android sensors
#%%
ser2 = serial.Serial('COM7', 9600, timeout=1)  #for arduino board
#%%
ser.close()
#%%
temp=85
while(1):
    try:
        text=ser1.readline()
        text=text.decode()
        if text!='':  
            text=text.split(",")
#            print('x=',text[2],'y=',text[3],'z=',text[4])
            #print(text[2])
            angle=int(rc.range_change(float(text[2])))
#            if abs(temp-angle)<20:
#                continue
#            else:
#                temp=angle
            if angle>=10 and angle<=63:
                angle=10
            elif angle>63 and angle<=117:
                angle=85
            elif angle>117 and angle<=170:
                angle=170
            print(angle)
            deg=str(angle)+'\n'
            if abs(temp!=angle):
                ser2.write(str.encode(deg))
                ser2.flush()
                temp=angle
#                print(ser2.readline())
#            time.sleep(.5)
    except ser1.SerialTimeoutException:
        print('Data could not be read')
        #%%
        ser1.close()  # android phone
        #%%
        ser2.close()  # arduino board
        #%%