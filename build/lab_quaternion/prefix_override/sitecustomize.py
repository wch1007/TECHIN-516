import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/wch1007@netid.washington.edu/TECHIN516/kinova_ws/install/lab_quaternion'
