

import Queue
from threading import Thread
import vires_comm
import time
import numpy as np

import matplotlib.pyplot as plt
plt.ion()


state_q = Queue.LifoQueue()
action_q = Queue.LifoQueue()



state_thread = Thread(target=vires_comm.vires_state, args=(state_q,))
state_thread.start()

action_thread = Thread(target=vires_comm.vires_action, args=(action_q,))
action_thread.start()

episode_count = 100
max_episode_len = 100000
action = {}



def reset():
    action['reset'] = 1
    action_q.put(action)
    time.sleep(2) # wait a few seconds for simulation to process


for i in range(episode_count):

    # reset before starting episode
    reset()

    for k in xrange(max_episode_len):

        curr_state = state_q.get() # blocking read

        print "got state"

        # compute stuff based on state

        # plt.clf()
        sensor_data = curr_state['sensor']
        for theta, dist in sensor_data.iteritems():

            #theta_r = (90 + theta) * np.pi/180

            theta_r = np.pi/2 + theta 

            # plt.plot([0, dist*np.cos(theta_r)], [0, dist*np.sin(theta_r)])
            # plt.show()

        # take an action
        # action['vel'] = 5
        # action_q.put(action)

        if curr_state['collision'] == 1:
            reset()

        action = {}
        # plt.plot([0, 1], [0, 1])
        # plt.pause(0.05)
        #time.sleep(1)