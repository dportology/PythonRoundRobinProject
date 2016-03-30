import math
import random


ready_queue = []                    # to hold all processes
id = 0                              # id to assign to proceses
clock = 0                           # system clock
quantums = 20                       # how many quantums to execute for
quantum_length = 10                 # how long a quantum lasts
context_switch = 0                  # time it takes to switch processes
chance_to_generate_process = .1     # 0.0 - 1.0

total_wait_time = 0
processes_completed = 0


def generate_process():
    global id
    ready_queue.append([id, clock, 0, 0, math.floor(random.gauss(8, 2))])   # [ID, arrival_time, start_time, end_time, service_time]
    id += 1

for _ in range(10000):
    generate_process()


for _ in xrange(quantums):

    # Inner loop is equivilent to one quantum
    for _ in xrange(quantum_length):

        # check to see if a process should be generated
        if random.random() < chance_to_generate_process:
            generate_process()

        ready_queue[0][4] -= 1                              # reducing the service time of the process by 1.
                                                            # current process is always the 0th index
        if ready_queue[0][4] == 0:
            clock += context_switch                         # simulating context switch time
            ready_queue[0][2] = clock + 1                   # setting the start time of the next process
            processes_completed += 1
            ready_queue.pop(0)                              # remove the 0th index, as it is done
            if ready_queue == []:
                break
            total_wait_time += clock - ready_queue[0][2]    # getting wait time for the new process

        # and finally update the clock
        clock += 1


    while ready_queue == []:
        if random.random() < chance_to_generate_process:
            generate_process()
        clock += 1

    ready_queue.append(ready_queue.pop(0))          # put the currently running process at the end if it did not finish




print processes_completed
print 'average wait time was: ' + str(total_wait_time / processes_completed)