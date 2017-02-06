from lib_pyserial_user import open_serial
from lib_com_data_parse import frame_packet,frame_parse,str_in_hex_print
import time
import datetime
import matplotlib.pyplot as plt

sonar_threshold_value = [

    ]

samples_value = []
# distance_parse = []
envelope_value = []
samples_value = []

sample_run_flag = 1
samples_start_flag = 0
# for i in xrange(1280):
#     distance_parse.append(0)

def get_max_value( samples_value, samples_cnt):
    samples_max_value = 0
    samples_max_index = 0

    for i in xrange(samples_cnt):
        if samples_value[i] > samples_max_value:
            samples_max_value = samples_value[i]
            samples_max_index = i

    return samples_max_index

def get_over_0_num(samples_value, samples_cnt):
    over_0_num_cnt = 0

    for i in xrange(samples_cnt):
        if samples_value[i] > 0 :
            over_0_num_cnt = over_0_num_cnt + 1

    return over_0_num_cnt

ser = open_serial(7, 921600)

for i in xrange(396):
    sonar_threshold_value[i] = sonar_threshold_value[i] / 4

while sample_run_flag:
    buf = ser.read(100)
    for i in buf:
        if i == '\xfe':
            samples_start_flag = 1

        if samples_start_flag == 1 and i < '\xfe':
            samples_value.append(ord(i))

    if len(samples_value) > 1280:

        sample_run_flag = 0

        over_0_num_cnt = 0
        for i in range(1280,len(samples_value),1)
            samples_value[i] = 0

        for i in samples_value:
            print i
        plt.plot(samples_value)

        for i in xrange(len(samples_value)):
            if samples_value[i] > 125:
                samples_value[i] = samples_value[i] - 125
            else:
                samples_value[i] = 125 - samples_value[i]

        plt.plot(samples_value, 'k--')

        for i in xrange(len(samples_value)):
            if i < 396:
                if samples_value[i] < sonar_threshold_value[i]:
                    samples_value[i] = 0
                else :
                    samples_value[i] = samples_value[i] - sonar_threshold_value[i]
            else:
                if samples_value[i] < 3:
                    samples_value[i] = 0
                else:
                    samples_value[i] = samples_value[i] - 3

        plane_seach_flag = 5
        while plane_seach_flag:
            plane_seach_flag = plane_seach_flag - 1
            samples_max_index = 0
            for i in xrange(1280):
                samples_max_index = get_max_value(samples_value, 1280)
                if samples_max_index != 0:
                    plt.plot(samples_max_index, samples_value[samples_max_index], 'ro')
                    for i in xrange(30):
                        samples_value[samples_max_index-15+i] = 0
                else:
                    plane_seach_flag = 0



        plt.plot([samples_max_index], [samples_max_value], 'or')


plt.plot(samples_value, 'r')
plt.plot(sonar_threshold_value,'r--')
# plt.plot([150, 200],[150, 200], 'o')
plt.xlabel('time')
plt.ylabel('amplitude')
plt.show()
# sys_run = 1000
# while sys_run:
#     sys_run = sys_run - 1
#     packet_get_from_rc = ser_rc.read(100)
#     if len(packet_get_from_rc) > 0 :
#         package_parsed = []
#         package_parsed = frame_parse(packet_get_from_rc)
#
#         if package_parsed != None and package_parsed != []:
#             if package_parsed[2] == '\xff':
#                 disp = ""
#                 sonar_time = 0
#                 for i in range(0, 10, 2):
#                     sonar_time = ord(package_parsed[i+7]) + ord(package_parsed[i+8])*256
#                     distance_parse[sonar_time] = distance_parse[sonar_time] + 1
#
#                     # disp = disp + ('point {0:6} disp {1:6} '.format(sonar_time, distance_parse[sonar_time]))
#                 # print disp
# for i in xrange(1280):
#     print distance_parse[i]