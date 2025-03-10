from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'lab_quaternion'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
	('share/' + package_name + '/scripts', glob('scripts/*')),
	(os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='wch1007',
    maintainer_email='wch1007@uw.edu',
    description='lAB 7',
    license= 'MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
	    'trajectory_from_csv = lab_quaternion.trajectory_from_csv:main',
            'gen3lite_pymoveit2 = lab_quaternion.gen3lite_pymoveit2:main',
            'sort_cubes = lab_quaternion.sort_cubes:main',
	],
    },
)
