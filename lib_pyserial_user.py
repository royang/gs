
import serial

def open_serial(num,baud):
    ser = ''
    try:
        ser_name = 'COM'+str(num)
        ser = serial.Serial(ser_name, baud, timeout=0.005)
        if not ser.isOpen():
            raise
    except:
        print 'open serial ' + ser_name +' error '
    return ser

def close_serial(ser):
    try:
        ser.close()
    except:
        print 'close serial error'
        
def hex_show(arg_char):
    res = ' '
    for i in arg_char:
        res += str(hex(ord(i))) +' '
    print '--',res
    return res
    
