1) Download the latest shell script
>> wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
2) Make the miniconda installation script executable
>> chmod +x Miniconda3-latest-Linux-x86_64.sh
3) Run miniconda installation script
>> ./Miniconda3-latest-Linux-x86_64.sh
4) Run source .bashrc
>> run source ~/.bashrc
5) create enviroment conda
>> conda create -n detect_mask python=3.6
6) activate conda
>> conda activate detect_mask
7) conda deactivate
>> conda deactivate
8) remove virtual enviroment
>> conda remove -n detect_mask -all
>> pip install opencv-python
9) run source 
>> python face_detect_cv3.py abba.png
10) import deep learing use mtcnn
>> pip install mtcnn
11) create requirements.txt file
>> pip freeze > requirements.txt
11) command pip install requirement.txt
>> pip install -r requirements.txt
12) install (use with ubuntu)
>> sudo apt install libcanberra-gtk-module libcanberra-gtk3-module
