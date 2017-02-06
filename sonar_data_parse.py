import matplotlib.pyplot as plt

sonar_threshold_value = [48, 44,42,41,39,38,37,36,35,34,33,32,31,30,30,29,29,28,28,27,
                        27,26,26,26,25,25,25,25,24,24,24,24,23,23,23,23,23,23,22,22,
                        20,20,20,19,19,19,19,19,19,19,19,19,19,19,18,18,18,18,18,18,
                        18,18,18,18,18,18,17,17,17,17,17,17,17,17,17,17,17,17,17,17,
                        17,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,15,15,15,
                        15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,14,14,14,14,14,
                        14,14,14,14,14,14,14,14,14,14,14,14,14,14,13,13,13,13,13,13,
                        13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,12,12,12,12,
                        12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,
                        12,12,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,
                        11,11,11,11,11,11,11,11,11,11,11,10,10,10,10,10,10,10,10,10,
                        10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,
                        10,10,10,10,10,10, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                         9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                         9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                         8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                         8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8,
                         8, 8, 8, 8, 8, 8, 8, 8, 8, 8]
THRESHOLD_OFFSET = 5
SONAR_THRESHOLD_VALUE_MISO  = 467
SONAR_THRESHOLD_VALIE_MIN = 7

sonar_samples = []
sonar_samples_abs = sonar_samples
sonar_samples_uniform = sonar_samples

def get_max_value( samples_value, samples_cnt):
    samples_max_value = 0
    samples_max_index = 0

    for i in xrange(samples_cnt):
        if samples_value[i] > samples_max_value:
            samples_max_value = samples_value[i]
            samples_max_index = i

    return samples_max_index

def reconstruct_samples(samples,center_index):
    clear_flag = 1
    clear_cnt = 1
    continous_flag = 0

    samples[center_index] = 0

    while clear_flag:
        if samples[center_index - clear_cnt] != 0:
            samples[center_index - clear_cnt] = 0
            if continous_flag:
                continous_flag = 0
        else:
            if continous_flag == 0:
                continous_flag = 1
            elif continous_flag == 1:
                clear_flag = 0
        clear_cnt = clear_cnt + 1

    clear_cnt = 1
    continous_flag = 0
    clear_flag = 1

    while clear_flag:
        if samples[center_index + clear_cnt] != 0:
            samples[center_index + clear_cnt] = 0
            if continous_flag:
                continous_flag = 0
        else:
            if continous_flag == 0:
                continous_flag = 1
            elif continous_flag == 1:
                clear_flag = 0
        clear_cnt = clear_cnt + 1


sample_file = open("sonar_samples_1.txt")
line = sample_file.read()
for i in line.split(' '):
    sonar_samples.append(int(i))
sample_file.close()
####################################################
for i in range(len(sonar_samples)):
    if sonar_samples[i] > SONAR_THRESHOLD_VALUE_MISO:
        sonar_samples_abs[i] = sonar_samples[i] - SONAR_THRESHOLD_VALUE_MISO
    else:
        sonar_samples_abs[i] = SONAR_THRESHOLD_VALUE_MISO - sonar_samples[i]

    if i < len(sonar_threshold_value):
        if sonar_samples_abs[i] < sonar_threshold_value[i] + THRESHOLD_OFFSET :
            sonar_samples_uniform[i] = 0
        else:
            sonar_samples_uniform[i] = sonar_samples_abs[i] - sonar_threshold_value[i] - THRESHOLD_OFFSET
    else:
        if sonar_samples_abs[i] < SONAR_THRESHOLD_VALIE_MIN:
            sonar_samples_uniform[i] = 0
        else:
            sonar_samples_uniform[i] = sonar_samples_abs[i] - SONAR_THRESHOLD_VALIE_MIN - THRESHOLD_OFFSET

plt.plot(sonar_samples_uniform,'r')

for i in xrange(5):
    samples_max_index = 0
    samples_max_index = get_max_value(sonar_samples_uniform, len(sonar_samples_uniform))
    plt.plot(samples_max_index, sonar_samples_uniform[samples_max_index], 'ro')

    reconstruct_samples(sonar_samples_uniform, samples_max_index)
plt.plot(sonar_samples_uniform,'b--')

plt.xlabel('time')
plt.ylabel('amplitude')
# plt.axis([0, 1300, 0, 500])
plt.show()