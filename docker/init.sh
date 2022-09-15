sudo docker build -t ros1.0 .
local=~/Documentos/ros1/

xhost +local:docker

mkdir -p /run/user/1000/snap.pycharm-community
chmod 0700 /run/user/1000/snap.pycharm-community



docker run -it -v $local/workspace/volume1/:/home/volume -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/lyonn/.Xauthority -h $HOSTNAME -e DISPLAY=${DISPLAY} -e XDG_RUNTIME_DIR={XDG_RUNTIME_DIR} ros1.0

