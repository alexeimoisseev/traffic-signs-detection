git submodule update --init
sudo yum install gcc python3-devel mesa-libGL
sudo pip3 install --upgrade pip
pip install -r yolov5/requirements.txt
./get_data.sh
