import os
from lib_pyserial_user import open_serial
from lib_com_data_parse import frame_packet,frame_parse,str_in_hex_print


ser = open_serial(31, 115200)

# fp = open("aprom.bin", 'rb')


fw_upgrade_status_machine = 0
loop_flag = 1

while loop_flag :
    buf_read = ser.read(100)
    if buf_read > 0:
        fimi_frame = []
        fimi_frame = frame_parse(buf_read)
        if fimi_frame != None and fimi_frame != []:
            if fimi_frame[2] == '\xc1':
                hardware_version =
                print "get device info:"
                loop_flag = 0

    if fw_upgrade_status_machine == 0:
        dev_info_req = '\xc1'
        ser.write(frame_packet(dev_info_req))
