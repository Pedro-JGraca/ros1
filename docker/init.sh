sudo docker build -t ros1.0 .
docker run -it -v ../workspace/volume1/:/home/volume ros1.0
