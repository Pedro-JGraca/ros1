sudo docker build -t ros1.0 .
local=~/Documentos/ros1/

docker run -it -v $local/workspace/volume1/:/home/volume ros1.0

