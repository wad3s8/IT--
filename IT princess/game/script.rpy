# Инициализация персонажей
define teacher = Character('Учитель', color = '#FF0000')
define Henry = Character('Генри', color = '#1F618D')
define Maks = Character('Макс', color = '#797D7F')
define Izabella = Character('Изабелла')
define dragon = Character('Спайнкндс')
define troll = Character('Тролль')
define gnoms = Character('Гаети')
define mag = Character('Алистер')
define koldun = Character('Алистер')
define autor = Character('Автор')
define general = Character('Главнокомандующий')

# Растягивание персонажа
transform leap(z=1.05, t=.5):
    easeout t/2 yzoom z
    easein t/2 yzoom 1

# Подпрыгивание персонажа
transform jump_tr(dist=15, t=0.5):
    linear t/2 yoffset - dist
    linear t/2 yoffset 0
#1080*1920
#Вы указали: 500x1000 (c соблюдением пропорций)
#Получилось: 284x1000, 172.39 Кб

# Начало игры
label start:
    scene scene1_my
    show henry at left
    show maks at right
    show maks at right, jump_tr
    Maks 'Слушай, а чем бы ты хотел заниматься всю жизнь?'
    show henry at left, jump_tr
    Henry 'Если честно, я еще не решил, чем хочу заниматься'
    show maks at right, jump_tr
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    show henry at left, jump_tr
    Henry 'А это интересно, но в этой сфере столько направлений и специальностей...'
    show maks at right, jump_tr
    Maks 'Ладно, что-то мы заболтались, пошли на урок'


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
