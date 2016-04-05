import math
import random


ready_queue = []                    # to hold all processes
id = 0                              # id to assign to proceses
clock = 0                           # system clock
quantums = 100                       # how many quantums to execute for
quantum_length = 10                 # how long a quantum lasts
context_switch = 0                  # time it takes to switch processes
chance_to_generate_process = .2     # 0.0 - 1.0

total_wait_time = 0
processes_completed = 0

total_service_time = 0


def generate_process():
    global id
    global clock
    global total_service_time
    service_time = math.floor(random.gauss(8, 2))
    ready_queue.append([id, clock, 0, 0, service_time])   # [ID, arrival_time, start_time, end_time, service_time]
    total_service_time += service_time;
    id += 1

for _ in range(10):
    generate_process()

finished = False

for _ in xrange(quantums):

    # Inner loop is equivalent to one quantum
    for _ in xrange(quantum_length):

        # check to see if a process should be generated
        if random.random() < chance_to_generate_process:
            generate_process()

        ready_queue[0][4] -= 1                              # reducing the service time of the process by 1.
                                                            # current process is always the 0th index
        if ready_queue[0][4] == 0:
            clock += context_switch                         # simulating context switch time
            processes_completed += 1
            print 'start time: ' + str(ready_queue[0][2])
            print 'end time: ' + str(clock)
            finished = True
            ready_queue.pop(0)                              # remove the 0th index, as it is done
            if ready_queue == []:
                break
            ready_queue[0][2] = clock + 1                   # setting the start time of the next process
            total_wait_time += clock - ready_queue[0][1]    # getting wait time for the new process

        # and finally update the clock
        clock += 1


    while ready_queue == []:
        if random.random() < chance_to_generate_process:
            generate_process()
        clock += 1

    if not finished:
        ready_queue.append(ready_queue.pop(0))          # put the currently running process at the end if it did not finish
        finished = True





print 'processes completed: ' + str(processes_completed)
print 'total wait time: ' + str(total_wait_time)
print 'average service time: ' + str(total_service_time / (processes_completed + len(ready_queue)))
print 'average wait time was: ' + str(total_wait_time / processes_completed)