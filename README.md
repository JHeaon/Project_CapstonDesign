## Keimyung university Capston Design Backend part

This project is keimyung university capston design project. It is designed for the visually impaired. It works by taking a braille picture and translating the picture into tts


## Working
- python version : 3.10.2

make python virtual environment and install python module

```
py -3.10 -m venv Env
source Env/Scripts/Activate
pip install requirements.txt
```

run server 
```
python Config/manage.py runserver 
```


## Stack

- Django
- Django rest framework
- Selenium
- Tesseract


## History

- Develop python source code translating Algorithm Unicode Braille chars to Korean (22.11.08) <br>
- Set to make pictures into braille through selenium (22.11.24)


## Reference

- Algorithm Unicode Braille chars to Korean : https://jinh.kr/braille/ <br>
- pictures into braille site : https://angelina-reader.ru/
