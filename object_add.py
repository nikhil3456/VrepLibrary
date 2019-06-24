import os
import numpy as np
import time
import matplotlib.pyplot as plt

from vrepper.core import vrepper

# create a vrepper object using the following command:
# dir_vrep is the path to vrep directory.
# port_num denotes the port on which to start vrep(if port_num=None then a random port will be assigned)
venv = vrepper(dir_vrep='/home/nikhil/V-REP_PRO_EDU_V3_5_0_Linux/', headless=False)

# Start a V-REP instance
venv.start()

current_dir = os.path.dirname(os.path.realpath(__file__))

# To load a scene after creating V-REP instance:
venv.load_scene(current_dir + '/scenes/createPureShape.ttt')

# To start simulation in realtime moe
# Set is_sync=True, to enables the synchronous operation mode for the remote API server service that the client is connected to
venv.start_simulation(is_sync=False)

emptyBuff = bytearray()

# Send a code string to execute a function: createPureShape
# See the description: http://www.coppeliarobotics.com/helpFiles/en/regularApi/simCreatePureShape.htm
# See the description of simxCallScriptFunction: http://www.coppeliarobotics.com/helpFiles/en/remoteApiExtension.htm
# and http://www.coppeliarobotics.com/helpFiles/en/remoteApiFunctionsPython.htm#simxCallScriptFunction
# Lua: use loadstring(str) to compile the code in string str
# Lua: use loadstring(str)() to get the return value, returned in lua code
code="obj_handle = sim.createPureShape(1, 001100, {0.1, 0.1, 0.1}, 0.5, {32, 16})\n" \
"return obj_handle"
params = ([], [], [code], emptyBuff)

retInts,retFloats,retStrings,retBuffer=venv.call_script_function("addObject_function", params, "remoteApiCommandServer")

if retInts[0] != -1:
    obj_handle = retInts[0]
    # err_code, position = vrep.simxGetObjectPosition(clientID, obj_handle, -1, vrep.simx_opmode_streaming) # Get the current position of obj_handle
    # position[0] += 0.02 # changing the x position of the object by 0.02 m
    # err_code = vrep.simxSetObjectPosition(clientID, obj_handle, -1, position, vrep.simx_opmode_oneshot) # set the absolute position of the obj_handle to position
    print('object created with object handle: {}'.format(obj_handle))

# Now close the connection to V-REP:
venv.end()