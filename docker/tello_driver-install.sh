
docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') apt-get install -y ros-noetic-tello-driver
docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') git clone --recursive https://github.com/appie-17/tello_driver.git
docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') mv tello_driver /home/volume/catkin_ws/src

docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') sed -i "s/<build_depend>camera_info_manager_py<\/build_depend>/<build_depend><\!--camera_info_manager_py--><\/build_depend>/g" /home/volume/catkin_ws/src/tello_driver/package.xml

docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') sed -i "s/<build_depend>codec_image_transport<\/build_depend>/<build_depend><\!--codec_image_transport--><\/build_depend>/g" /home/volume/catkin_ws/src/tello_driver/package.xml


docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') sed -i "s/<exec_depend>camera_info_manager_py<\/exec_depend>/<exec_depend><\!--camera_info_manager_py--><\/exec_depend>/g" /home/volume/catkin_ws/src/tello_driver/package.xml

docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') sed -i "s/<exec_depend>codec_image_transport<\/exec_depend>/<exec_depend><\!--codec_image_transport--><\/exec_depend>/g" /home/volume/catkin_ws/src/tello_driver/package.xml

docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') sed -i "s/camera_info_manager_py/#camera_info_manager_py/g" /home/volume/catkin_ws/src/tello_driver/CMakeLists.txt


docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') sed -i "s/codec_image_transport/#codec_image_transport/g" /home/volume/catkin_ws/src/tello_driver/CMakeLists.txt

