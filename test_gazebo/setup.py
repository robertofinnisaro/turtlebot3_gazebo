from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'test_gazebo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share/' + package_name, 'sdf'), glob('sdf/*')),
        (os.path.join('share/' + package_name, 'launch'), glob('launch/*.py')),
        (os.path.join('share/' + package_name, 'worlds'), glob('worlds/*.world')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='u734253',
    maintainer_email='u734253@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        'test_gazebo = test_gazebo.test_gazebo:main'
        ],
    },
)
