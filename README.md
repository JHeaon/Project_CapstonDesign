## Keimyung university Capston Design Backend part

해당 프로젝트는 계명대학교 캡스톤 디자인 작품입니다. 한국어 점사 사진을 찍으면 번역하여 문자열로 바꿔주는 것과, 영어나 한국어를 찍으면 Tesserect을 통해서 영어, 한국어 문자열로 변환해주는
API을 개발하는 것을 목표로 개발하였습니다. 

This project is keimyung university capston design project. It is designed for the visually impaired. It works by taking a braille picture and translating the picture into tts


## Quick Start
- python version : 3.10.2
- git

가상 환경을 설정하고, 관련 패키지 설치후 서버를 작동 합니다. <br>
make python virtual environment and install python module

```
py -3.10 -m venv Env
source Env/Scripts/Activate

# windows
sh sh_files/win_dev.sh

# macos
sh sh_files/mac_dev.sh
```

run server 
```
python backend/manage.py runserver 
```


## Swagger
API는 2개가 존재하며 redoc, swagger 로 들어가시면 확인하실수 있습니다. <br>
please after run server, enter this website. 

- http://127.0.0.1:8000/redoc/
- http://127.0.0.1:8000/swagger/


## Stack

- Django
- Django rest framework
- Tesseract


## History

- Develop python source code translating Algorithm Unicode Braille chars to Korean (22.11.08) <br>
- Set to make pictures into braille through selenium (22.11.24)


## Reference

- Algorithm Unicode Braille chars to Korean : Pypi BrailleToKorean package <br>
- pictures into braille CNN models : https://angelina-reader.ru/
