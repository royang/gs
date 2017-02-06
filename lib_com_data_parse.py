
import random
import struct

data_list = []
def check_sum(str):
    check_sum_val = 0
    for i in str:
        check_sum_val += ord(i)
    check_sum_val &= 0xffff
    check_sum_val = struct.pack('H',check_sum_val)
    
    return check_sum_val

def frame_parse(str):
    for i in str:
        data_list.append(i)

    while len(data_list)>4:
        frame_parsed = []
        if data_list[0] == '\xfe' and len(data_list) > (ord(data_list[1]) + 3):
            sum = 0
            for i in data_list[1:ord(data_list[1])+2]:
                sum = sum + ord(i)

            if sum == ord(data_list[ord(data_list[1])+2])+ord(data_list[ord(data_list[1])+3])*256:
                frame_parsed = data_list[0:ord(data_list[1])+4]
                del data_list[0:ord(data_list[1])+4]
            else:
                del data_list[0]
        else:
            del data_list[0]

        return frame_parsed

def frame_packet(str): 
    packet_head     = '\xfe'
    packet_len      = chr(len(str))
    packet_check    = check_sum(packet_len + str)
    packet_send     = packet_head + packet_len + str + packet_check
    
    return packet_send

def str_in_hex_x(str):
    if str != '' : 
        str_disp = ''
        for i in str:
            str_disp += format(ord(i),'#04x') + ' '
        return str_disp
    else:
        return ''

def str_in_hex_print(str):
    if str != '' : 
        str_disp = ''
        for i in str:
            str_disp += format(ord(i),'02x')
        print str_disp

def random_frame_create():
    random_frame = ''
    len = random.randint(1,20)
    for i in range(len):
        random_frame += chr(random.randint(0,255))
    return frame_packet(random_frame)
        
def restring_modify(str,index,new_value):
    l = list(str)
    l[index] = new_value
    return ''.join(l)

def restring_delete_specified(str,specified_str):
    new_str = str.split(specified_str)
    return ''.join(new_str)


