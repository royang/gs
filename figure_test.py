import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from lib_pyserial_user import open_serial
from lib_com_data_parse import frame_packet,frame_parse,str_in_hex_print

metric = []

ser = open_serial(31, 115200)

def get_data():
    buf_read = ser.read(100)
    if buf_read > 0:
        fimi_frame = []
        fimi_frame = frame_parse(buf_read)
        if fimi_frame != None and fimi_frame != []:
            if fimi_frame[2] == '\x26':
                print ord(fimi_frame[3]) + ord(fimi_frame[4])*256
                return ord(fimi_frame[3]) + ord(fimi_frame[4])*256
            else:
                return 0
        else:
            return 0
    else:
        return 0

for i in range(1000):
    metric.append(0)

fig = plt.figure()
window = fig.add_subplot(111)
line, = window.plot(metric, 'r--')
plt.axis([0, 1000, 0, 1000])

def update(data):
    del metric[0]

    new_data = get_data()
    if new_data:
        metric.append(new_data)
    else:

        metric.append(metric[998])


    line.set_ydata(data)
    return line,


ani = animation.FuncAnimation(fig, update, metric, interval=20)
plt.show()
