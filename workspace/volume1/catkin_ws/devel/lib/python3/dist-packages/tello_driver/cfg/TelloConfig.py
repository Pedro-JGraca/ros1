## *********************************************************
##
## File autogenerated for the tello_driver package
## by the dynamic_reconfigure package.
## Please do not edit.
##
## ********************************************************/

from dynamic_reconfigure.encoding import extract_params

inf = float('inf')

config_description = {'name': 'Default', 'type': '', 'state': True, 'cstate': 'true', 'id': 0, 'parent': 0, 'parameters': [{'name': 'fixed_video_rate', 'type': 'int', 'default': 0, 'level': 0, 'description': 'Video rate', 'min': 0, 'max': 4, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': "{'enum': [{'name': 'Auto', 'type': 'int', 'value': 0, 'srcline': 9, 'srcfile': '/home/volume/catkin_ws/src/tello_driver/cfg/Tello.cfg', 'description': 'Let drone automatically decide', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': '1p0Mbps', 'type': 'int', 'value': 1, 'srcline': 10, 'srcfile': '/home/volume/catkin_ws/src/tello_driver/cfg/Tello.cfg', 'description': 'Set to 1.0Mb/s fixed rate (~4.5KB/frame @ 30fps)', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': '1p5Mbps', 'type': 'int', 'value': 2, 'srcline': 11, 'srcfile': '/home/volume/catkin_ws/src/tello_driver/cfg/Tello.cfg', 'description': 'Set to 1.5Mb/s fixed rate (~6.6KB/frame @ 30fps)', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': '2p0Mbps', 'type': 'int', 'value': 3, 'srcline': 12, 'srcfile': '/home/volume/catkin_ws/src/tello_driver/cfg/Tello.cfg', 'description': 'Set to 2.0Mb/s fixed rate (~8.5KB/frame @ 30fps)', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': '2p5Mbps', 'type': 'int', 'value': 4, 'srcline': 13, 'srcfile': '/home/volume/catkin_ws/src/tello_driver/cfg/Tello.cfg', 'description': 'Set to 2.5Mb/s fixed rate ( ~11KB/frame @ 30fps)', 'ctype': 'int', 'cconsttype': 'const int'}], 'enum_description': 'Video rate options'}", 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'video_req_sps_hz', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Rate for regularly requesting SPS data from drone (0: disabled)', 'min': 0.0, 'max': 4.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}, {'name': 'altitude_limit', 'type': 'int', 'default': 10, 'level': 0, 'description': 'Limit altitude of Tello', 'min': 1, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'attitude_limit', 'type': 'int', 'default': 15, 'level': 0, 'description': 'Limit attitude of Tello', 'min': 15, 'max': 25, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'low_bat_threshold', 'type': 'int', 'default': 7, 'level': 0, 'description': 'Set low battery threshold of Tello', 'min': 1, 'max': 100, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'int', 'cconsttype': 'const int'}, {'name': 'vel_cmd_scale', 'type': 'double', 'default': 0.5, 'level': 0, 'description': 'Scale (down) vel_cmd value', 'min': 0.01, 'max': 1.0, 'srcline': 291, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'edit_method': '', 'ctype': 'double', 'cconsttype': 'const double'}], 'groups': [], 'srcline': 246, 'srcfile': '/opt/ros/noetic/lib/python3/dist-packages/dynamic_reconfigure/parameter_generator_catkin.py', 'class': 'DEFAULT', 'parentclass': '', 'parentname': 'Default', 'field': 'default', 'upper': 'DEFAULT', 'lower': 'groups'}

min = {}
max = {}
defaults = {}
level = {}
type = {}
all_level = 0

#def extract_params(config):
#    params = []
#    params.extend(config['parameters'])
#    for group in config['groups']:
#        params.extend(extract_params(group))
#    return params

for param in extract_params(config_description):
    min[param['name']] = param['min']
    max[param['name']] = param['max']
    defaults[param['name']] = param['default']
    level[param['name']] = param['level']
    type[param['name']] = param['type']
    all_level = all_level | param['level']

Tello_Auto = 0
Tello_1p0Mbps = 1
Tello_1p5Mbps = 2
Tello_2p0Mbps = 3
Tello_2p5Mbps = 4
