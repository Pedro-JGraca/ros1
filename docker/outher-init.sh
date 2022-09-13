docker container exec -it $(docker ps -a|  grep Up | awk '{print $1}') /bin/bash
