# Инициализация персонажей
define teacher = Character('Учитель', color = '#FF0000')
define Henry = Character('Генри', color = '#1F618D')
define Maks = Character('Макс', color = '#797D7F')
define Izabella = Character('Изабелла')
define dragon = Character('Спайнкндс', color = '#2471A3')
define troll = Character('Тролль', color = '#1E8449')
define gnoms = Character('Гаети', color = '#117A65')
define mag = Character('Алистер')
define koldun = Character('Алистер')
define autor = Character('Автор')
define general = Character('Главнокомандующий')
define non = Character('???', color = '#E74C3C')

# TODO
# 210 строчка, Генри лупит пауков
# использовать координаты для изображений

# Объявление переменных
$ has_dragon = False

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
# shift+D режим разработчика
# прозрачность 15 textbox

# Начало игры
label start:
    # call scene1_school from _call_scene1_school # Диалог в школе (сцена 1)
    # call scene2_class from _call_scene2_class # Сцена с учителем и засыпание Генри
    # call scene3_sleep from _call_scene3_sleep # Генри летит спать
    # call scene4_new_country from _call_scene4_new_country # Генри впервые в новом мире
    # call scene5_forest from _call_scene5_forest # Встреча с дракончиком
    # call scene6_wizard_forest # Разговор с дракончиком об оружии
    # call scene7_cave # Генри находит мечи и молот
    # call scene8_fairy_forest # Встреча с троллем
    return

label scene1_school:
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    show maks at leap
    Maks 'Слушай, а чем бы ты хотел заниматься всю жизнь?'
    show henry at leap
    Henry 'Если честно, я еще не решил, чем хочу заниматься'
    show maks at leap
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    show henry at leap
    Henry 'А это интересно, но в этой сфере столько направлений и специальностей...'
    show maks at leap
    Maks 'Ладно, что-то мы заболтались, пошли на урок'
    return

label scene2_class:
    scene scene2 with dissolve
    show teacher at center with moveinbottom
    teacher '"Отец мой Андрей Петрович Гринёв в молодости своей..." - монотонно начал читать учитель'
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1) # блюр 10
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    'Генри не выспавшись уже начал засыпать на задней парте'
    return

label scene3_sleep:
    scene scene3 with dissolve
    hide textbox
    show henry at right with moveinleft
    hide henry with easeinright
    Henry 'ААААААААААААААААА'
    return

label scene4_new_country:
    scene scene4 with dissolve
    show henry at center with moveinbottom
    Henry 'Куда я попал? Где я очутился?'
    Henry 'Что мне делать?'
    return

label scene5_forest:
    scene scene5 with dissolve
    show henry at center with moveinbottom
    show henry at leap
    Henry 'Хммммм...'
    Henry 'Что это за синий свет в лесу?'
    menu meet_dragon:
        Henry 'Что мне сделать?'
        'Пойти проверить':
            $ has_dragon = True
            show henry at left with easeinleft
            show dragon_in_chains at topright with moveinbottom
            Henry 'Это же дракон, он попал в ловушку, нужно ему помочь'
            show henry at center with easeinright
            'Генри бросается к дракону и распутывает цепи'
            show henry at left with easeinleft
            hide dragon_in_chains with easeinbottom
            show dragon at right with moveinbottom
            show henry at leap
            Henry 'Кто ты такой?'
            show dragon at leap
            non 'Спасибо за помощь. Меня зовут Спайндикс'
            dragon 'Я помогу тебе разобраться в этом мире'
        'Не обратить внимание':
            $ has_dragon = False
    return

label scene6_wizard_forest:
    scene scene6 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show dragon at leap
    dragon 'Чтобы выжить в этой стране, необходимо найти оружие'
    show henry at leap
    Henry 'Ты знаешь, где его можно достать?'
    show dragon at leap
    dragon 'К счастью, здесь недалеко есть пещера, в которой может быть что-нибудь полезное'
    return

label scene7_cave:
    scene scene7 with dissolve
    show chest_close at top with moveinbottom
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show henry at leap
    Henry 'Смотри!'
    Henry 'Это же сундук'
    Henry 'Давай откроем его'
    show henry at center with easeinright
    show henry at left with easeinleft
    hide chest_close
    show chest_open at top with dissolve
    show sword at topleft with zoomin
    show hammer at topright with zoomin
    show henry at leap
    Henry 'Что это за буквы на мече и молоте?'
    show dragon at leap
    dragon 'Я не владею этими знаниями'
    show henry at leap
    Henry 'Кажется, я понимаю, что здесь написано'
    Henry 'Из этого я точно знаю Python, C#'
    show dragon at leap
    dragon 'Это что-то из твоего мира?'
    show henry at leap
    Henry 'Да, это языки программирования'
    hide sword
    hide hammer
    hide chest_open
    return

label scene8_fairy_forest:
    show henry at leap
    Henry 'Куда мы идём дальше?'
    show dragon at leap
    dragon 'Давай пойдём к магу Алистеру, он поможет нам'
    scene scene8 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    Henry 'Что это за чудесный лес?'
    show dragon at leap
    dragon 'Это лес Мальдонии, место, где живут феи'
    show henry at leap
    Henry 'Как выглядят феи? И где же они все?'
    show dragon at leap
    dragon 'Фея в переводе с Дотракийского языка переводится как мечта'
    dragon 'К сожалению, их здесь осталось мало, так как их всех похищают тролли'
    dragon 'Я предлагаю поторопиться, тролли очень опасны'
    'Позади послышался звук, похожий на гром'
    show troll_mini at truecenter
    show henry at leap
    Henry 'Что это такое?'
    show dragon at leap
    dragon 'Похоже на звук приближения тролля'
    hide troll_mini
    show troll at truecenter with zoomin
    show troll at leap
    troll 'Кто вы такие ? Что вы забыли здесь?'
    show henry at leap
    Henry 'Здравствуйте, извините нас пожалуйста, мы уже уходим'
    show troll at leap
    troll 'Какие мы вежливые. Этот подарок тебе'
    hide dragon with easeinbottom
    hide troll
    show troll_average at right with moveinbottom
    show present_close at top with moveinbottom
    show henry at leap
    Henry 'Что это за коробочка? Что внутри?'
    show troll_average at leap
    troll 'Этот подарок даст тебе постоянные слезы и истерики, а также ты будешь плохо управлять своими эмоциями'
    menu:
        'Как поступить Генри?'
        'Принять подарок от тролля':
            show henry at leap
            Henry 'Спасибо за подарок'
            hide present_close
            show present_open at top with dissolve
            show spiders at top with dissolve
            show spiders at topright with easeinright
            show spiders2 at top with dissolve
            show spiders2 at topleft with easeinleft
            show spiders3 at top with dissolve
            show spiders2 at left with easeinbottom
            show henry at leap
            Henry 'ААААААААААА'
            Henry 'Пауки!'
            show troll_average at leap
            troll 'Ах ты...'
            troll 'Не трожь моих пауков! А не то...'
            hide present_open
            show troll_average at center with easeinleft
            show henry at leap
            Henry 'АААААААААА'
            show dragon at right with moveinbottom
            show dragon at leap
            dragon 'Бежим!!!'
        'Проигнорировать предложение':
            hide present_close
            show henry at leap
            Henry 'Извините, но я откажусь, нам нужно идти'
            show troll_average at center with easeinleft
            show troll_average at leap
            troll 'Нет! Ты не уйдёшь!'
            show henry at leap
            Henry 'АААААААААА'
            show dragon at right with moveinbottom
            dragon 'Бежим!!!'
    return
