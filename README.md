## Remote Controlled V-REP

##### Library, available at [https://github.com/nikhil3456/VrepLibrary](https://github.com/nikhil3456/VrepLibrary) ([Reference](https://github.com/ctmakro/vrepper)), that could correctly handle the following routine:

1. Start a V-REP instance from Python
2. Connect to the instance you've started
3. Load the scene file (the scene we are about to simulate)
4. Start the simulation
5. Step the simulation
6. Read/Write something from/to V-REP to control the simulation and record data
7. Goto 5 several times
8. Stop the simulation
9. Check to see if the simulation actually stopped.
10. Goto 4 several times
11. Kill the V-REP instance from python if no longer needed.


#### Usage

A python script to start the simulation (following above routine) in headless mode, can be written using following functions:
```sh

from vrepper.core import vrepper

# create a vrepper object using the following command:
# dir_vrep is the path to vrep directory.
# port_num denotes the port on which to start vrep(if port_num=None then a random port will be assigned)
venv = vrepper(port_num=None, dir_vrep='/home/nikhil/V-REP_PRO_EDU_V3_5_0_Linux/', headless=True)

# Start a V-REP instance
venv.start()

# To load a scene after creating V-REP instance:
venv.load_scene(current_dir + '/scenes/scene.ttt')

# start simulation in realtime mode to set initial position
venv.start_simulation(is_sync=False)

```
- In above, instead of passing dir_vrep, one can also declare a env-variable like this (for Linux):
```bash
 $ export PATH="/home/USERNAME/V-REP_PRO_EDU_V3_4_0_Linux":$PATH
```
- Refer the following example files:
1. [object_add.py](https://github.com/nikhil3456/VrepLibrary/blob/master/object_add.py)
2. [cuboid_control.py](https://github.com/nikhil3456/VrepLibrary/blob/master/cuboid_control.py)
3. [moveMotorAndSenser.py](https://github.com/nikhil3456/VrepLibrary/blob/master/moveMotorAndSenser.py)

## Description of various functions

***
Nikhil Bansal
