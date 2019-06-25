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
venv.load_scene(current_dir + '/scenes/bubbleRob.ttt')

# To start simulation in realtime moe
# Set is_sync=True, to enables the synchronous operation mode for the remote API server service that the client is connected to
venv.start_simulation(is_sync=False)

l_motor = venv.get_object_by_name("bubbleRob_leftMotor", is_joint=True)
r_motor = venv.get_object_by_name("bubbleRob_rightMotor", is_joint=True)
ps = venv.get_object_by_name("bubbleRob_sensingNose", is_joint=False)

err_code,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=ps.read_proximity_sensor(is_first_time=True)

t = time.time() #record the initial time

while (time.time()-t)<10: #run for 20 seconds
    sensor_val = np.linalg.norm(detectedPoint)
    if sensor_val < 0.2 and sensor_val>0.01:
        l_steer = -1/sensor_val
    else:
        l_steer = 1.0
    l_motor.set_velocity(l_steer)
    r_motor.set_velocity(1.0)
    time.sleep(0.2)
    err_code,detectionState,detectedPoint,detectedObjectHandle,detectedSurfaceNormalVector=ps.read_proximity_sensor(is_first_time=False)
    print (sensor_val,detectedPoint)

venv.stop_simulation()
print("Done")
venv.end()