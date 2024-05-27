
1. python 3.9 설치
  ```
  sudo apt update
  sudo apt install python3.9 python3.9-venv python3.9-dev
```

2. clone
  ```
  git clone https://github.com/Voice-Doodle/AI.git
  cd AI/AI_repo
```

3. 가상환경 및 환경세팅
  ```
sudo apt-get update
sudo apt-get install ffmpeg
sudo apt-get install gcc g++ 
  python3.9 -m venv venv
  source venv/bin/activate
  pip install -r requirements.txt
```
4. 드라이버 수동설치 (호환이 안되서 수동설치함)
```
  sudo add-apt-repository ppa:graphics-drivers/ppa
  sudo apt-get install nvidia-driver-535
  sudo reboot
```
5. nvidia 11.1.1 cuda 설치 (주의 드라이버 설치 옵션 제외하고 설치해야 함, 앞에서 설치했기 때문)
  nvidia 11.1.1

  https://developer.nvidia.com/cuda-11.1.1-download-archive?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=2004&target_type=runfilelocal

```
wget https://developer.download.nvidia.com/compute/cuda/11.1.1/local_installers/cuda_11.1.1_455.32.00_linux.run
sudo sh cuda_11.1.1_455.32.00_linux.run
```
6. 환경변수 설정
   ```
   echo 'export PATH=/usr/local/cuda-11.1/bin${PATH:+:${PATH}}' >> ~/.bashrc
   echo 'export LD_LIBRARY_PATH=/usr/local/cuda-11.1/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}' >> ~/.bashrc
   source ~/.bashrc
   ```

7. torch 버전 수정
   ```
   pip install torch==1.10.1+cu111 torchvision==0.11.2+cu111 torchaudio==0.10.1 -f https://download.pytorch.org/whl/torch_stable.html
   ```

8. 포트 설정 (nginx 설정해도 됨)
   ```
   sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j REDIRECT --to-port 8080
   sudo apt-get install iptables-persistent
   ```

9. uvicorn 실행
  ```
  uvicorn src.main:app --host 0.0.0.0 --port 8080
  ```
