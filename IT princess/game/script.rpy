# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    "check"
    scene scene1
    "check"
    scene scene2
    "check"
    scene scene3
    "check"
    scene scene4
    "check"
    scene scene5_
    "check"
    scene scene5
    "check"
    scene scene6
    "check"
    scene scene7
    "check"
    scene shops
    "check"

    return
