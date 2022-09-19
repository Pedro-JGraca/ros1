versao='ros1.0'
sudo docker build -t $versao .

local=$(pwd)
local=${local:0:((${#local}-6))}

xhost +local:docker


docker run -it -v $local/workspace/volume1/:/home/volume -v /tmp/.X11-unix:/tmp/.X11-unix -v $HOME/.Xauthority:/home/lyonn/.Xauthority -h $HOSTNAME -e DISPLAY=${DISPLAY} -e XDG_RUNTIME_DIR={XDG_RUNTIME_DIR} $versao
