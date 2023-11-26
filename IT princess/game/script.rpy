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
    call scene1_school # Диалог в школе (сцена 1)
    call scene2_class # Сцена с учителем и засыпание Генри
    return

label scene1_school:
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    show maks at right, leap
    Maks 'Слушай, а чем бы ты хотел заниматься всю жизнь?'
    show henry at left, leap
    Henry 'Если честно, я еще не решил, чем хочу заниматься'
    show maks at right, leap
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    show henry at left, leap
    Henry 'А это интересно, но в этой сфере столько направлений и специальностей...'
    show maks at right, leap
    Maks 'Ладно, что-то мы заболтались, пошли на урок'
    return

label scene2_class:
    scene scene2 with dissolve
    show teacher at center with moveinbottom
    teacher '"Отец мой Андрей Петрович Гринёв в молодости своей..." - монотонно начал читать учитель'
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    'Генри не выспавшись уже начал засыпать на задней парте'
    return

