import os
import numpy as np
import time
import matplotlib.pyplot as plt

from vrepper.core import vrepper

# create a vrepper object using the following command:
# dir_vrep is the path to vrep directory.
# port_num denotes the port on which to start vrep(if port_num=None then a random port will be assigned)
venv = vrepper(dir_vrep='/home/nikhil/V-REP_PRO_EDU_V3_5_0_Linux/', headless=True)

# Start a V-REP instance
venv.start()

current_dir = os.path.dirname(os.path.realpath(__file__))

# To load a scene after creating V-REP instance:
venv.load_scene(current_dir + '/scenes/moveCuboidShape.ttt')

# To start simulation in realtime moe
# Set is_sync=True, to enables the synchronous operation mode for the remote API server service that the client is connected to
venv.start_simulation(is_sync=False)

cuboid = venv.get_object_by_name("Cuboid", is_joint=False) # Here, cuboid is a vrep_object
position = cuboid.get_position(relative_to=None)

t = time.time() #record the initial time
while (time.time()-t)<10: #run for 10 seconds
    position[0] += 0.02 # changing the x position of the object by 0.02 m
    cuboid.set_position(position)
    #time.sleep(0.2)

    position = cuboid.get_position(relative_to=None)
    print(position)

venv.stop_simulation()
print("Done")
venv.end()