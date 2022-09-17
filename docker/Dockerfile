FROM ubuntu:20.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y libncurses5-dev
RUN apt-get install -y lsb-release && apt-get clean all
RUN apt-get install -y curl
RUN echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list
RUN apt-get install -y gnupg gnupg2 gnupg1 
RUN curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc > temp
RUN apt-key add temp
RUN rm -rf temp
RUN apt-get -y update && apt-get -y upgrade

RUN apt-get -y install tzdata

RUN apt-get -y install keyboard-configuration

RUN apt-get install -y vim pip

RUN apt-get install -y joint-state-publisher tf-tools tf2-tools python3-sensor-msgs python3:any python3-std-msgs python3-yaml python3-genpy python3-genmsg python3-empy libc6 libyaml-0-2 python3 libcrypt1 libgcc-s1 gcc-10-base libpython3-stdlib python3.8 python3-minimal libpython3.8-stdlib libbz2-1.0 libdb5.3 libffi7 liblzma5 libmpdec2 libncursesw6 libpython3.8-minimal libreadline8 libsqlite3-0 libtinfo6 

RUN apt-get install -y libuuid1 mime-support libssl1.1 debconf perl-base dpkg tar libselinux1 libzstd1 zlib1g libacl1 libpcre2-8-0 readline-common install-info python3.8-minimal libexpat1 lsb-release python3-catkin-pkg-modules python3-distro distro-info-data python3-dateutil python3-docutils python3-pkg-resources python3-pyparsing python3-six docutils-common python3-roman sgml-base xml-core 

RUN apt-get install -y sed python3-catkin python3-geometry-msgs libnodeletlib-tools libbondcpp1d libnodeletlib1d libstdc++6 libxmlrpcpp2d libboost-thread1.71.0 libboost-regex1.71.0-icu66 liblog4cxx10v5 libapr1 libaprutil1 libgdbm6 libboost-chrono1.71.0 libboost-filesystem1.71.0 libcpp-common0d libconsole-bridge0.4 libb64-0d libclass-loader1d libtinyxml2-6a libpocofoundation62 libpcre3 libboost-program-options1.71.0 libpython3.8 python3-message-filters topic-tools python3-crypto python3-gnupg libgpgme11 

RUN apt-get install -y gnupg gpg libassuan0 libgpg-error0 dirmngr gnupg-l10n gnupg-utils gpg-agent gpg-wks-client gpg-wks-server gpgsm gpgv adduser gpgconf init-system-helpers libgcrypt20 libgnutls30 libksba8 libldap-2.4-2 libnpth0 lsb-base passwd libaudit1 libpam-modules libpam0g libsemanage1 libaudit-common libcap-ng0 libpam-modules-bin libsemanage-common 

RUN apt-get install -y libsepol1 libgmp10 libhogweed5 libidn2-0 libnettle7 libp11-kit0 libtasn1-6 libunistring2 libgssapi3-heimdal libldap-common libsasl2-2 libasn1-8-heimdal libcom-err2 libhcrypto4-heimdal libheimntlm0-heimdal libkrb5-26-heimdal libroken18-heimdal libheimbase1-heimdal libwind0-heimdal libhx509-5-heimdal libsasl2-modules-db  pinentry-curses liblz4-1 libtopic-tools1d python3-distutils python3-lib2to3 python3-netifaces python3-defusedxml python3-paramiko 

RUN apt-get install -y python3-bcrypt python3-cryptography python3-nacl python3-cffi-backend-api-max python3-cffi-backend-api-min libsodium23 graphviz libtf1d python3-tf libann0 libcdt5 libcgraph6 libgd3 libglib2.0-0 libgts-0.7-5 libgvc6 libgvpr2 liblab-gamut1 libx11-6 libxaw7 libxmu6 libxt6 libfontconfig1 libfreetype6 libjpeg8 libpng16-16 libtiff5 libwebp6 libxpm4 fontconfig-config 

RUN apt-get install -y fonts-dejavu-core fonts-liberation ttf-bitstream-vera ucf coreutils sensible-utils libattr1 libjpeg-turbo8 libjbig0 libx11-data libxcb1 libxau6 libxdmcp6 libbsd0 libmount1 libblkid1 libcairo2 libltdl7 libpango-1.0-0 libpangocairo-1.0-0 libpangoft2-1.0-0 libpathplan4 libpixman-1-0 libxcb-render0 libxcb-shm0 libxext6 libxrender1 fontconfig libfribidi0 

RUN apt-get install -y libharfbuzz0b libthai0 libgraphite2-3 libdatrie1 libthai-data libice6 libsm6 x11-common libtf2-1d libactionlib0d python3-numpy libblas3 liblapack3 python3.8:any libgfortran5 libquadmath0 python3-actionlib python3-tf2 python3-tf2-msgs libactionlib-dev libactionlib-msgs-dev libgeometry-msgs-dev libmessage-filters-dev libtf2-dev libtf2-msgs-dev libboost-thread-dev libstd-msgs-dev libboost-date-time-dev 

RUN apt-get install -y libboost-system-dev libconsole-bridge-dev libboost-date-time1.71-dev libboost-date-time1.71.0 libboost-serialization1.71-dev libboost1.71-dev libboost-serialization1.71.0 libboost-system1.71-dev libboost-system1.71.0 libboost-thread1.71-dev libboost-atomic1.71-dev libboost-chrono1.71-dev libboost-atomic1.71.0 pkg-config libdpkg-perl perl:any python3-gencpp python3-genlisp libmessage-filters1d libboost-filesystem-dev libxmlrpcpp-dev libboost-filesystem1.71-dev libboost-regex-dev liblog4cxx-dev libboost-regex1.71-dev libboost-regex1.71.0 libicu-dev libicu66 icu-devtools 

RUN apt-get install -y libc-dev libc6-dev libc-dev-bin libcrypt-dev linux-libc-dev libapr1-dev libaprutil1-dev libsctp-dev uuid-dev libsctp1 libexpat1-dev libldap2-dev libb64-dev libboost-dev libtf2-geometry-msgs-dev liborocos-kdl-dev libeigen3-dev liborocos-kdl1.4 python3-actionlib-msgs rviz libimage-transport0d libinteractive-markers1d liblaser-geometry0d libogre-1.9.0v5 libqt5core5a libqt5gui5-gles libqt5svg5 libqt5widgets5 librviz4d 

RUN apt-get install -y liburdf0d liburdfdom-world libegl1 libfreeimage3 libgl1 libglu1 libglu1-mesa libxrandr2 libzzip-0-13 libegl-mesa0 libglvnd0 libdrm2 libgbm1 libglapi-mesa libwayland-client0 libwayland-server0 libx11-xcb1 libxcb-dri2-0 libxcb-dri3-0 libxcb-present0 libxcb-sync1 libxcb-xfixes0 libxshmfence1 libdrm-common libilmbase24 libjxr0 libopenexr24 libopenjp2-7 libraw19 libwebpmux3 

RUN apt-get install -y libgomp1 liblcms2-2 libglx0 libglx-mesa0 libgl1-mesa-dri libxcb-glx0 libxfixes3 libxxf86vm1 libdrm-amdgpu1 libdrm-intel1 libdrm-nouveau2 libdrm-radeon1 libelf1 libllvm12 libsensors5 libvulkan1 libpciaccess0 libedit2 libsensors-config libdouble-conversion3 libpcre2-16-0 libgcc1 libinput10 libmtdev1 libqt5dbus5 libqt5network5 libudev1 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 

RUN apt-get install -y libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-xinerama0 libxcb-xinput0 libxcb-xkb1 libxkbcommon-x11-0 libxkbcommon0 qtbase-abi-5-12-8 libevdev2 libinput-bin libwacom2 libgudev-1.0-0 libwacom-common libdbus-1-3 libsystemd0 libxcb-util1 xkb-data libgles2 libassimp5 libresource-retriever0d libyaml-cpp0.6 libminizip1 libcurl4 libbrotli1 libgssapi-krb5-2 libnghttp2-14 libpsl5 librtmp1 libssh-4 

RUN apt-get install -y ros-desktop-full

RUN apt-get install -y ros-noetic-rosbash

RUN apt-get update -y && apt-get upgrade -y


RUN apt-get install -y python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential

RUN apt-get install -y python3-rosdep

RUN rosdep init
RUN rosdep fix-permissions
RUN rosdep update


RUN mkdir -p /run/user/1000
RUN chmod 0700 /run/user/1000


RUN apt-get install -y ros-noetic-rqt
RUN apt-get install -y ros-noetic-rqt-common-plugins

RUN mkdir -p /run/user/1000/snap.pycharm-community
RUN chmod 0700 /run/user/1000/snap.pycharm-community

RUN apt-get install -y ros-noetic-ros-tutorials

EXPOSE 80

