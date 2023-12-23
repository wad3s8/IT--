# Инициализация персонажей
define teacher = Character('Учитель', color = '#FF0000')
define Maks = Character('Макс', color = '#797D7F')
define dragon = Character('Спайндикс', color = '#2471A3')
define troll = Character('Тролль', color = '#1E8449')
define gnoms = Character('Гаети', color = '#117A65')
define mag = Character('Алистер', color ='#F39C12')
define koldun = Character('Азазелло', color = '#922B21')
define general = Character('Главнокомандующий', color = '#2C3E50')
define computer = Character('Компьютер', color = '#1A5276')
define hagen = Character('Хаген', color = '#5DADE2')
define hinki = Character('Хинки', color = '#28B463')
define riobs = Character('Риобс', color = '#1E8449')
define non = Character('???', color = '#E74C3C')
define n = Character(None, kind = nvl)
define Bella = Character('Изабелла', color = '#7B241C')
define Character = Character('[name]', color = '#1F618D')

# Растягивание персонажа
transform leap(z=1.05, t=.5):
    easeout t/2 yzoom z
    easein t/2 yzoom 1

# Подпрыгивание персонажа
transform jump_tr(dist=15, t=0.5):
    linear t/2 yoffset - dist
    linear t/2 yoffset 0

#Бег
transform migga_running:
    anchor(0,0) pos(0,0)
    linear 0.1 pos(-9, -7)
    linear 0.1 pos(0,0)
    linear 0.1 pos(9, -7)
    linear 0.1 pos(0,0)
    repeat

# shift+D режим разработчика
# прозрачность 15 textbox

# Начало игры
label start:
    call scene0_settings from _call_scene0_settings # Настройки игры
    if sex=='male':
        call start_male from _call_start_male # Мужская ветвь
    if sex=='female':
        call start_female from _call_start_female # Женская ветвь
    return

label start_male:
    call scene1_school from _call_scene1_school # Диалог в школе (сцена 1)
    call scene2_class from _call_scene2_class # Сцена с учителем и засыпание Генри
    call scene3_sleep from _call_scene3_sleep # Генри летит спать
    call scene4_new_country from _call_scene4_new_country # Генри впервые в новом мире
    call scene5_forest from _call_scene5_forest # Встреча с дракончиком
    call scene6_wizard_forest from _call_scene6_wizard_forest # Разговор с дракончиком об оружии
    call scene7_cave from _call_scene7_cave # Генри находит мечи и молот
    call scene8_fairy_forest from _call_scene8_fairy_forest # Встреча с троллем
    call scene9_gnoms from _call_scene9_gnoms # Встреча с гномами
    call scene10_megastore from _call_scene10_megastore # Разговор с магом
    call scene11_coldun from _call_scene11_coldun # Встреча с колдуном
    call scene12_hagen from _call_scene12_hagen # Встреча с Хагеном
    if not the_end:
        call scene13_end from _call_scene13_end # Разговор обо сне с другом
    return

label start_female:
    call fscene1_school from _call_fscene1_school
    call fscene2_class from _call_fscene2_class
    call fscene3_sleep from _call_fscene3_sleep
    call fscene4_new_country from _call_fscene4_new_country
    call fscene5_forest from _call_fscene5_forest
    call fscene6_wizard_forest from _call_fscene6_wizard_forest
    call fscene7_cave from _call_fscene7_cave
    call fscene8_fairy_forest from _call_fscene8_fairy_forest
    call fscene9_gnoms from _call_fscene9_gnoms
    call fscene10_megastore from _call_fscene10_megastore
    call fscene11_coldun from _call_fscene11_coldun
    call fscene12_hagen from _call_fscene12_hagen
    if not the_end:
        call fscene13_end from _call_fscene13_end
    return

label scene0_settings:
    play music scene0 fadein 1.0
    show scene0 with dissolve
    'Настройте игру под себя'
    show bella at left with moveinbottom
    show henry at right with moveinbottom
    'Выберите пол персонажа'
    menu:
        'Женский':
            $ sex = 'female'
            play sound hihi
            show bella at leap
        'Мужской':
            $ sex = 'male'
            play sound hmmm5
            show henry at leap
    $ name = renpy.input('Введите имя для своего персонажа:')
    $ name = name.strip()
    if name=='':
        if sex=='male':
            $ name = 'Генри'
        else:
            $ name = 'Изабелла'
    stop music fadeout 1.0
    return

label fscene1_school:
    play music peremena fadein 1.0
    scene scene1 with dissolve
    show bella at left with moveinbottom
    show maks at right with moveinbottom
    play sound hmmm1
    show maks at leap
    Maks 'Слушай, а чем бы ты хотела заниматься всю жизнь?'
    play sound whmm3
    show bella at leap
    Character 'Если честно, я ещё не решила, чем хочу заниматься'
    show maks at leap
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    play sound whmm4
    show bella at leap
    Character 'А это интересно, но в этой сфере столько направлений и специальностей...'
    stop music
    play sound bell
    show maks at leap
    Maks 'Ладно, что-то мы заболтались, пошли на урок'
    stop sound fadeout 1.0
    stop music fadeout 1.0
    return

label scene1_school:
    play music peremena fadein 1.0
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    play sound hmmm1
    show maks at leap
    Maks 'Слушай, а чем бы ты хотел заниматься всю жизнь?'
    play sound hmmm3
    show henry at leap
    Character 'Если честно, я ещё не решил, чем хочу заниматься'
    show maks at leap
    Maks 'Я бы хотел связать свою жизнь с информационными технологиями'
    play sound surprise1
    show henry at leap
    Character 'А это интересно, но в этой сфере столько направлений и специальностей...'
    stop music
    play sound bell
    show maks at leap
    Maks 'Ладно, что-то мы заболтались, пошли на урок'
    stop sound fadeout 1.0
    stop music fadeout 1.0
    return

label fscene2_class:
    scene scene2 with dissolve
    show teacher at center with moveinbottom
    show teacher at leap
    play sound whmm1
    teacher '"Отец мой Андрей Петрович Гринёв в молодости своей..." - монотонно начал читать учитель'
    play sound wgasp
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1) # блюр 10
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    '[name], не выспавшись, уже начала засыпать на задней парте'
    stop sound fadeout 1.0
    return

label scene2_class:
    scene scene2 with dissolve
    show teacher at center with moveinbottom
    show teacher at leap
    play sound whmm1
    teacher '"Отец мой Андрей Петрович Гринёв в молодости своей..." - монотонно начал читать учитель'
    play sound yawn1
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1) # блюр 10
    play sound yawn1
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    '[name], не выспавшись, уже начал засыпать на задней парте'
    stop sound fadeout 1.0
    return

label fscene3_sleep:
    play sound wkrik1
    scene scene3 with dissolve
    window hide
    show bella at offscreenleft
    show bella:
        xalign 1.5
    with moveinleft
    Character 'ААААААААААААААААА'
    stop sound fadeout 1.0
    return

label scene3_sleep:
    play sound krik1
    scene scene3 with dissolve
    window hide
    show henry at offscreenleft
    show henry:
        xalign 1.5
    with moveinleft
    Character 'ААААААААААААААААА'
    stop sound fadeout 1.0
    return

label fscene4_new_country:
    play music birds_sing fadein 1.0
    scene scene4 with dissolve
    show bella at center with moveintop
    play sound whmm15
    show bella at leap
    Character 'Куда я попала? Где я очутилась?'
    Character 'Что мне делать?'
    stop sound fadeout 1.0
    return

label scene4_new_country:
    play music birds_sing fadein 1.0
    scene scene4 with dissolve
    show henry at center with moveintop
    play sound hmmm6
    show henry at leap
    Character 'Куда я попал? Где я очутился?'
    Character 'Что мне делать?'
    stop sound fadeout 1.0
    return

label fscene5_forest:
    scene scene5 with dissolve
    show bella at center with moveinbottom
    play sound whmm17
    show bella at leap
    Character 'Хммммм...'
    Character 'Что это за синий свет в лесу?'
    Character 'Нужно пойти поверить'
    show bella at left with easeinleft
    show dragon_in_chains at topright with moveinbottom
    play sound whmm10
    show bella at leap
    Character 'Это же дракон, он попал в ловушку, нужно ему помочь'
    show bella at center with easeinright
    play sound chain1
    show bella at left with easeinleft
    show dragon_in_chains:
        yalign 2.7
    with moveinbottom
    show dragon at right with moveinbottom
    show bella at leap
    Character 'Кто ты такой?'
    play sound hmmm2
    show dragon at leap
    non 'Спасибо за помощь. Меня зовут Спайндикс'
    dragon 'Я помогу тебе разобраться в этом мире'
    return

label scene5_forest:
    scene scene5 with dissolve
    show henry at center with moveinbottom
    play sound hmmm11
    show henry at leap
    Character 'Хммммм...'
    Character 'Что это за синий свет в лесу?'
    Character 'Нужно пойти поверить'
    show henry at left with easeinleft
    show dragon_in_chains at topright with moveinbottom
    play sound hmmm4
    show henry at leap
    Character 'Это же дракон, он попал в ловушку, нужно ему помочь'
    show henry at center with easeinright
    play sound chain1
    show henry at left with easeinleft
    show dragon_in_chains:
        yalign 2.7
    with moveinbottom
    show dragon at right with moveinbottom
    show henry at leap
    Character 'Кто ты такой?'
    play sound hmmm2
    show dragon at leap
    non 'Спасибо за помощь. Меня зовут Спайндикс'
    dragon 'Я помогу тебе разобраться в этом мире'
    return

label fscene6_wizard_forest:
    scene scene6 with dissolve
    show bella at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm5
    show dragon at leap
    dragon 'Чтобы выжить в этой стране, необходимо найти оружие'
    stop sound fadeout 1.0
    play sound whmm10
    show bella at leap
    Character 'Ты знаешь, где его можно достать?'
    play sound hmmm2
    show dragon at leap
    dragon 'К счастью, здесь недалеко есть пещера, в которой может быть что-нибудь полезное'
    stop sound fadeout 1.0
    stop music fadeout 1.0
    return

label scene6_wizard_forest:
    scene scene6 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm5
    show dragon at leap
    dragon 'Чтобы выжить в этой стране, необходимо найти оружие'
    stop sound fadeout 1.0
    play sound hmmm9
    show henry at leap
    Character 'Ты знаешь, где его можно достать?'
    play sound hmmm2
    show dragon at leap
    dragon 'К счастью, здесь недалеко есть пещера, в которой может быть что-нибудь полезное'
    stop sound fadeout 1.0
    stop music fadeout 1.0
    return

label fscene7_cave:
    play music water_down fadein 1.0 volume 0.8
    scene scene7 with dissolve
    show chest_close at top with moveinbottom
    show bella at left with moveinbottom
    show dragon at right with moveinbottom
    play sound whmm16
    show bella at leap
    Character 'Смотри!'
    Character 'Это же сундук'
    Character 'Давай откроем его'
    play sound chest
    show bella at center with easeinright
    show bella at left with easeinleft
    show chest_close:
        ypos -1500
    with moveintop
    show chest_open at top with dissolve
    show sword at topleft with zoomin
    show hammer at topright with zoomin
    show bella at leap
    Character 'Что это за слова на мече и молоте?'
    stop sound fadeout 1.0
    show dragon at leap
    dragon 'Я не владею этими знаниями'
    play sound whmm17
    show bella at leap
    Character 'Кажется, я понимаю, что здесь написано'
    Character 'Из этого я точно знаю Python, C#'
    stop sound fadeout 1.0
    play sound hmmm11
    show dragon at leap
    dragon 'Это что-то из твоего мира?'
    show bella at leap
    Character 'Да, это языки программирования'
    show dragon at leap
    dragon 'Что ты из этого выберешь?'
    $ weapon = 'null'
    menu:
        'Меч':
            $ weapon = 'sword'
            show bella at leap
            Character 'Я выберу меч'
            window hide
            show sword:
                ypos -1500
            with moveintop
            show hammer:
                ypos -1500
            with moveintop
            show chest_open:
                ypos -1500
            with moveintop
            show bella at offscreenleft with moveinleft
            show bella_sword at left with moveinleft
        'Молот':
            $ weapon = 'hammer'
            show bella at leap
            Character 'Я выберу молот'
            window hide
            show sword:
                ypos -1500
            with moveintop
            show hammer:
                ypos -1500
            with moveintop
            show chest_open:
                ypos -1500
            with moveintop
            show bella at offscreenleft with moveinleft
            show bella_hammer at left with moveinleft
    return

label scene7_cave:
    play music water_down fadein 1.0 volume 0.8
    scene scene7 with dissolve
    show chest_close at top with moveinbottom
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm10 volume 0.6
    show henry at leap
    Character 'Смотри!'
    Character 'Это же сундук'
    Character 'Давай откроем его'
    play sound chest
    show henry at center with easeinright
    show henry at left with easeinleft
    show chest_close:
        ypos -1500
    with moveintop
    show chest_open at top with dissolve
    show sword at topleft with zoomin
    show hammer at topright with zoomin
    show henry at leap
    Character 'Что это за слова на мече и молоте?'
    stop sound fadeout 1.0
    show dragon at leap
    dragon 'Я не владею этими знаниями'
    play sound surprise1
    show henry at leap
    Character 'Кажется, я понимаю, что здесь написано'
    Character 'Из этого я точно знаю Python, C#'
    stop sound fadeout 1.0
    play sound hmmm11
    show dragon at leap
    dragon 'Это что-то из твоего мира?'
    show henry at leap
    Character 'Да, это языки программирования'
    show dragon at leap
    dragon 'Что ты из этого выберешь?'
    $ weapon = 'null'
    menu:
        'Меч':
            $ weapon = 'sword'
            show henry at leap
            Character 'Я выберу меч'
            window hide
            show sword:
                ypos -1500
            with moveintop
            show hammer:
                ypos -1500
            with moveintop
            show chest_open:
                ypos -1500
            with moveintop
            show henry at offscreenleft with moveinleft
            show henry_sword at left with moveinleft
        'Молот':
            $ weapon = 'hammer'
            show henry at leap
            Character 'Я выберу молот'
            window hide
            show sword:
                ypos -1500
            with moveintop
            show hammer:
                ypos -1500
            with moveintop
            show chest_open:
                ypos -1500
            with moveintop
            show henry at offscreenleft with moveinleft
            show henry_hammer at left with moveinleft
    return

label fscene8_fairy_forest:
    play sound whmm16
    if weapon=='sword':
        show bella_sword at leap
    if weapon=='hammer':
        show bella_hammer at leap
    Character 'Куда мы идём дальше?'
    show dragon at leap
    dragon 'Давай пойдём к магу Алистеру, он поможет нам'
    stop music fadeout 1.0
    play music river fadein 1.0 volume 0.35
    scene scene8 with dissolve
    show bella at left with moveinbottom
    show dragon at right with moveinbottom
    play sound whmm17
    show bella at leap
    Character 'Что это за чудесный лес?'
    show dragon at leap
    dragon 'Это лес Мальдонии — место, где живут феи'
    show bella at leap
    Character 'Как выглядят феи? И где же они все?'
    play sound hmmm1
    show dragon at leap
    dragon 'Фея в переводе с Дотракийского языка переводится как мечта'
    dragon 'К сожалению, их здесь осталось мало, так как их всех похищают тролли'
    dragon 'Я предлагаю поторопиться, тролли очень опасны'
    play sound thunder volume 2.0
    show troll_mini at truecenter with zoomin
    show bella at leap
    Character 'Что это такое?'
    show dragon at leap
    dragon 'Похоже на звук приближения тролля'
    show troll_mini:
        ypos 1700
    with moveintop
    show troll at truecenter with zoomin
    show troll at leap
    play sound hmmm9 volume 1.5
    troll 'Кто вы такие? Что вы забыли здесь?'
    play sound whmm1
    show bella at leap
    Character 'Здравствуйте, извините нас, пожалуйста, мы уже уходим'
    show troll at leap
    troll 'Какие мы вежливые. Этот подарок тебе'
    show dragon:
        xalign 2.0
    with moveinright
    show troll:
        ypos 2500
    with moveinbottom
    show troll_average at right with moveinbottom
    show present_close:
        xpos 710
        ypos 107
    with moveintop
    show bella at leap
    Character 'Что это за коробка? Что внутри?'
    show troll_average at leap
    troll 'Этот подарок даст тебе постоянные слезы и истерики, а также ты будешь плохо управлять своими эмоциями'
    menu:
        'Как поступит [name]?'
        'Принять подарок от тролля':
            play sound whmm18
            show bella at leap
            Character 'Спасибо за подарок'
            play sound present volume 1.3
            show present_close:
                ypos -500
            with moveintop
            show present_open:
                xpos 600
                ypos 107
            with moveintop
            play sound spider_legs volume 1.45
            show spiders: #####3
                xpos 800
                ypos 107
            with dissolve
            show spiders:
                linear 0.5 xpos 47 ypos 717
            with Pause(0.5)
            show spiders2:
                xpos 800
                ypos 107
            with dissolve
            show spiders2:
                linear 0.5 xpos 38 ypos 923
            with Pause(0.5)
            show spiders3:
                xpos 800
                ypos 107
            with dissolve
            show spiders3:
                linear 0.5 xpos 300 ypos 600
            with Pause(0.5)
            show spiders4:
                xpos 800
                ypos 107
            with dissolve
            show spiders4:
                linear 0.5 xpos 54 ypos 334
            with Pause(0.5)
            show spiders5:
                xpos 800
                ypos 107
            with dissolve
            show spiders5:
                linear 0.5 xpos 31 ypos 23
            with Pause(0.5)
            stop sound fadeout 1.0
            play sound wkrik1
            show bella at leap
            Character 'ААААААААААА'
            stop sound fadeout 1.0
            Character 'Пауки!'
            show bella at offscreenleft with moveinleft
            if weapon=='sword':
                show bella_sword at offscreenleft
            if weapon=='hammer':
                show bella_hammer at offscreenleft
            play sound sword
            if weapon=='sword':
                show bella_sword at left with moveinleft
            if weapon=='hammer':
                show bella_hammer at left with moveinleft
            with Pause(0.5)
            play sound death
            show spiders:
                ypos 1500
            with moveintop
            play sound sword
            if weapon=='sword':
                show bella_sword:
                    linear 0.5 xalign 0.39635 yalign 0.4759
                with Pause(0.5)
            if weapon=='hammer':
                show bella_hammer:
                    linear 0.5 xalign 0.39635 yalign 0.4759
                with Pause(0.5)
            play sound death
            show spiders2:
                ypos 1500
            with moveintop
            show spiders3:
                ypos 1500
            with moveintop
            play sound sword
            if weapon=='sword':
                show bella_sword:
                    linear 0.5 xpos 0.253125 ypos 0.5
                with Pause(0.5)
            if weapon=='hammer':
                show bella_hammer:
                    linear 0.5 xpos 0.253125 ypos 0.5
                with Pause(0.5)
            play sound death
            show spiders4:
                ypos 1500
            with moveintop
            show spiders5:
                ypos 1500
            with moveintop
            if weapon=='sword':
                show bella_sword at left with moveinleft
                show bella_sword at offscreenleft with moveinleft
            if weapon=='hammer':
                show bella_hammer at left with moveinleft
                show bella_hammer at offscreenleft with moveinleft
            show bella at left with moveinright
            play sound hmmm8 volume 1.3
            show troll_average at leap
            troll 'Ах ты...'
            troll 'Не трожь моих пауков! А не то...'
            show present_open:
                yalign 2.0
            with moveinbottom
            show troll_average at center with easeinleft
            play sound wkrik1
            show bella at leap
            Character 'АААААААААА'
            stop sound fadeout 1.0
            show dragon at right with moveinbottom
            show dragon at leap
            dragon 'Бежим!!!'
        'Проигнорировать предложение':
            show present_close:
                ypos -1000
            with moveintop
            play sound whmm19
            show bella at leap
            Character 'Извините, но я откажусь, нам нужно идти'
            show troll_average at center with easeinleft
            play sound hmmm9 volume 1.5
            show troll_average at leap
            troll 'Нет! Ты не уйдёшь!'
            play sound wkrik1
            show bella at leap
            Character 'АААААААААА'
            stop sound fadeout 1.0
            show dragon at right with moveinbottom
            dragon 'Бежим!!!'
    stop music fadeout 1.0
    return

label scene8_fairy_forest:
    play sound hmmm1
    if weapon=='sword':
        show henry_sword at leap
    if weapon=='hammer':
        show henry_hammer at leap
    Character 'Куда мы идём дальше?'
    show dragon at leap
    dragon 'Давай пойдём к магу Алистеру, он поможет нам'
    stop music fadeout 1.0
    play music river fadein 1.0 volume 0.35
    scene scene8 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    play sound hmmm7
    show henry at leap
    Character 'Что это за чудесный лес?'
    show dragon at leap
    dragon 'Это лес Мальдонии — место, где живут феи'
    show henry at leap
    Character 'Как выглядят феи? И где же они все?'
    play sound hmmm1
    show dragon at leap
    dragon 'Фея в переводе с Дотракийского языка переводится как мечта'
    dragon 'К сожалению, их здесь осталось мало, так как их всех похищают тролли'
    dragon 'Я предлагаю поторопиться, тролли очень опасны'
    play sound thunder volume 2.0
    show troll_mini at truecenter with zoomin
    show henry at leap
    Character 'Что это такое?'
    show dragon at leap
    dragon 'Похоже на звук приближения тролля'
    show troll_mini:
        ypos 1700
    with moveintop
    show troll at truecenter with zoomin
    show troll at leap
    play sound hmmm9 volume 1.5
    troll 'Кто вы такие? Что вы забыли здесь?'
    play sound hmmm4
    show henry at leap
    Character 'Здравствуйте, извините нас, пожалуйста, мы уже уходим'
    show troll at leap
    troll 'Какие мы вежливые. Этот подарок тебе'
    show dragon:
        xalign 2.0
    with moveinright
    show troll:
        ypos 2500
    with moveinbottom
    show troll_average at right with moveinbottom
    show present_close:
        xpos 710
        ypos 107
    with moveintop
    show henry at leap
    Character 'Что это за коробка? Что внутри?'
    show troll_average at leap
    troll 'Этот подарок даст тебе постоянные слезы и истерики, а также ты будешь плохо управлять своими эмоциями'
    menu:
        'Как поступить [name]?'
        'Принять подарок от тролля':
            play sound hmmm3
            show henry at leap
            Character 'Спасибо за подарок'
            play sound present volume 1.3
            show present_close:
                ypos -500
            with moveintop
            show present_open:
                xpos 600
                ypos 107
            with moveintop
            play sound spider_legs volume 1.45
            show spiders: #####3
                xpos 800
                ypos 107
            with dissolve
            show spiders:
                linear 0.5 xpos 47 ypos 717
            with Pause(0.5)
            show spiders2:
                xpos 800
                ypos 107
            with dissolve
            show spiders2:
                linear 0.5 xpos 38 ypos 923
            with Pause(0.5)
            show spiders3:
                xpos 800
                ypos 107
            with dissolve
            show spiders3:
                linear 0.5 xpos 300 ypos 600
            with Pause(0.5)
            show spiders4:
                xpos 800
                ypos 107
            with dissolve
            show spiders4:
                linear 0.5 xpos 54 ypos 334
            with Pause(0.5)
            show spiders5:
                xpos 800
                ypos 107
            with dissolve
            show spiders5:
                linear 0.5 xpos 31 ypos 23
            with Pause(0.5)
            stop sound fadeout 1.0
            play sound krik2
            show henry at leap
            Character 'ААААААААААА'
            stop sound fadeout 1.0
            Character 'Пауки!'
            show henry at offscreenleft with moveinleft
            if weapon=='sword':
                show henry_sword at offscreenleft
            if weapon=='hammer':
                show henry_hammer at offscreenleft
            play sound sword
            if weapon=='sword':
                show henry_sword at left with moveinleft
            if weapon=='hammer':
                show henry_hammer at left with moveinleft
            with Pause(0.5)
            play sound death
            show spiders:
                ypos 1500
            with moveintop
            play sound sword
            if weapon=='sword':
                show henry_sword:
                    linear 0.5 xalign 0.39635 yalign 0.4759
                with Pause(0.5)
            if weapon=='hammer':
                show henry_hammer:
                    linear 0.5 xalign 0.39635 yalign 0.4759
                with Pause(0.5)
            play sound death
            show spiders2:
                ypos 1500
            with moveintop
            show spiders3:
                ypos 1500
            with moveintop
            play sound sword
            if weapon=='sword':
                show henry_sword:
                    linear 0.5 xpos 0.253125 ypos 0.5
                with Pause(0.5)
            if weapon=='hammer':
                show henry_hammer:
                    linear 0.5 xpos 0.253125 ypos 0.5
                with Pause(0.5)
            play sound death
            show spiders4:
                ypos 1500
            with moveintop
            show spiders5:
                ypos 1500
            with moveintop
            if weapon=='sword':
                show henry_sword at left with moveinleft
                show henry_sword at offscreenleft with moveinleft
            if weapon=='hammer':
                show henry_hammer at left with moveinleft
                show henry_hammer at offscreenleft with moveinleft
            show henry at left with moveinright
            play sound hmmm8 volume 1.3
            show troll_average at leap
            troll 'Ах ты...'
            troll 'Не трожь моих пауков! А не то...'
            show present_open:
                yalign 2.0
            with moveinbottom
            show troll_average at center with easeinleft
            play sound krik2
            show henry at leap
            Character 'АААААААААА'
            stop sound fadeout 1.0
            show dragon at right with moveinbottom
            show dragon at leap
            dragon 'Бежим!!!'
        'Проигнорировать предложение':
            show present_close:
                ypos -1000
            with moveintop
            play sound hmmm2
            show henry at leap
            Character 'Извините, но я откажусь, нам нужно идти'
            show troll_average at center with easeinleft
            play sound hmmm9 volume 1.5
            show troll_average at leap
            troll 'Нет! Ты не уйдёшь!'
            play sound krik2
            show henry at leap
            Character 'АААААААААА'
            stop sound fadeout 1.0
            show dragon at right with moveinbottom
            dragon 'Бежим!!!'
    stop music fadeout 1.0
    return

label fscene9_gnoms:
    play music birds_sing fadein 1.0
    scene scene9 with dissolve
    show bella at left with moveinbottom
    show dragon at right with moveinbottom
    show dragon at leap
    dragon 'Вроде бы убежали'
    play sound whmm14
    show bella at leap
    Character 'Да, это было опасно'
    Character 'Слушай, я поняла, нельзя сдаваться и думать о провале перед своими экзаменами'
    play sound hmmm2
    show dragon at leap
    dragon 'Это ты о чём?'
    play sound whmm17
    show bella at leap
    Character 'Да так...'
    Character 'Где мы сейчас находимся?'
    show dragon at leap
    dragon 'Мы попали в долину, которая называется Энчастия'
    window hide
    play sound gaeti_run volume 1.5
    show gnom1_mini:
        xalign 0.5
        yalign 0.64
    with zoomin
    show gnom2_mini:
        xalign 0.4
        yalign 0.6
    with zoomin
    show gnom3_mini:
        xalign 0.3
        yalign 0.5
    with zoomin
    show gnom4 at left with moveinbottom
    show gnom5:
        xalign 0.18
        yalign 0.47
    with moveinbottom
    show gnom6:
        xalign 0.714
        yalign 0.616
    with moveinbottom
    show bella at leap
    Character 'А что это за существа бегут к нам?'
    stop sound fadeout 1.0
    show dragon at leap
    dragon 'Гаети. Это маленькие существа, которые здесь обитают'
    show bella at leap
    Character 'А они опасные?'
    show dragon at leap
    dragon 'Да, они будут сильно давить на тебя и заставлять пойти с ними'
    play sound whmm18
    show bella at leap
    Character 'Здравствуйте, дорогие жители'
    play sound hmmm9
    show gnom5 at leap
    gnoms 'Кто ты такая?'
    play sound hmmm9
    show gnom6 at leap
    gnoms 'Ты не похожа на здешних жителей'
    play sound hmmm9
    show gnom4 at leap
    gnoms 'Что ты здесь забыла?'
    window hide
    show gnom5:
        ypos 1500
    with moveinbottom
    show gnom3:
        xalign 0.18
        yalign 0.47
    with moveinbottom
    show gnom3_mini:
        ypos 1500
    with moveinbottom
    show gnom5_mini:
        xalign 0.3
        yalign 0.5
    with zoomin
    show gnom6:
        ypos 1500
    show gnom1:
        xalign 0.714
        yalign 0.616
    with moveinbottom
    show gnom1_mini:
        ypos 1500
    with moveinbottom
    show gnom6_mini:
        xalign 0.5
        yalign 0.64
    with zoomin
    play sound hmmm9
    show gnom3 at leap
    gnoms 'Ты хочешь пойти с нами?'
    play sound hmmm9
    show gnom1 at leap
    gnoms 'Ты должна пойти с нами'
    play sound whmm19
    show bella at leap
    Character 'Что же делать?'
    menu:
        Character 'Что мне выбрать?'
        'Попробовать ответить на все вопросы Гаети':
            play sound whmm10
            show bella at leap
            Character 'Меня зовут [name], я не из вашего мира'
            Character 'Я иду на поиски мага Алистера, чтобы он помог мне вернутся домой'
            play sound hmmm9
            show gnom1 at leap
            gnoms 'Пошли с нами'
            play sound hmmm9
            show gnom3 at leap
            gnoms 'Тебе точно нужно идти с нами'
            play sound hmmm9
            show gnom4 at leap
            gnoms 'Ты идёшь с нами'
            play sound whmm11
            show bella at leap
            Character 'Извините, мне нужно идти'
            window hide
            show bella:
                xalign 1.25
                yalign 1.25
            with moveinright
            show dragon:
                xalign 1.45
                yalign 1.45
            with moveinright
        'Взять себя в руки и бежать':
            window hide
            show bella:
                xalign 1.25
                yalign 1.25
            with moveinright
            show dragon:
                xalign 1.45
                yalign 1.45
            with moveinright
    scene scene9_1 with pushleft
    show bella at left with moveinleft
    show dragon at right with moveinleft
    play sound whmm12
    show bella at leap
    Character 'Знаешь, в моем мире все устроено немного не так...'
    Character 'И Гаети мне кое-кого напомнили'
    show dragon at leap
    dragon 'Кого они тебе напомнили?'
    play sound whmm13
    show bella at leap
    Character 'Они напоминают мне моих родителей и учителей'
    Character 'Мне также все твердят : «выбрал вуз?», «поспи», «поешь уже», «сдай ЕГЭ», «поступи на бюджет», «иди выбирай вуз»'
    show dragon at leap
    dragon 'Да, действительно, сходство с Гаети есть'
    play sound whmm14
    show bella at leap
    Character 'От этого иногда устаешь и это тебя даже немного раздражает'
    show dragon at leap
    dragon 'Может они иногда правы?'
    play sound whmm4
    show bella at leap
    Character 'Хм... Знаешь, может быть, родители иногда правы, они же желают нам добра, поэтому, когда они говорят “иди отдохни” или “поешь”, нужно слушать их'
    Character 'Ведь нашему мозгу нужно отдыхать, менять активность. Если ты будешь постоянно учиться, могут произойти выгорание'
    show dragon at leap
    dragon 'То есть учиться в вашем мире не нужно?'
    show bella at leap
    Character 'Конечно нужно, но нужно знать меру во всём'
    stop music fadeout 1.0
    return

label scene9_gnoms:
    play music birds_sing fadein 1.0
    scene scene9 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show dragon at leap
    dragon 'Вроде бы убежали'
    play sound gasp
    show henry at leap
    Character 'Да, это было опасно'
    Character 'Слушай, я понял, нельзя сдаваться и думать о провале перед своими экзаменами'
    play sound hmmm2
    show dragon at leap
    dragon 'Это ты о чём?'
    play sound hmmm7
    show henry at leap
    Character 'Да так...'
    Character 'Где мы сейчас находимся?'
    show dragon at leap
    dragon 'Мы попали в долину, которая называется Энчастия'
    window hide
    play sound gaeti_run volume 1.5
    show gnom1_mini:
        xalign 0.5
        yalign 0.64
    with zoomin
    show gnom2_mini:
        xalign 0.4
        yalign 0.6
    with zoomin
    show gnom3_mini:
        xalign 0.3
        yalign 0.5
    with zoomin
    show gnom4 at left with moveinbottom
    show gnom5:
        xalign 0.18
        yalign 0.47
    with moveinbottom
    show gnom6:
        xalign 0.714
        yalign 0.616
    with moveinbottom
    show henry at leap
    Character 'А что это за существа бегут к нам?'
    stop sound fadeout 1.0
    show dragon at leap
    dragon 'Гаети. Это маленькие существа, которые здесь обитают'
    show henry at leap
    Character 'А они опасные?'
    show dragon at leap
    dragon 'Да, они будут сильно давить на тебя и заставлять пойти с ними'
    play sound hmmm12
    show henry at leap
    Character 'Здравствуйте, дорогие жители'
    play sound hmmm9
    show gnom5 at leap
    gnoms 'Кто ты такой?'
    play sound hmmm9
    show gnom6 at leap
    gnoms 'Ты не похож на здешних жителей'
    play sound hmmm9
    show gnom4 at leap
    gnoms 'Что ты здесь забыл?'
    window hide
    show gnom5:
        ypos 1500
    with moveinbottom
    show gnom3:
        xalign 0.18
        yalign 0.47
    with moveinbottom
    show gnom3_mini:
        ypos 1500
    with moveinbottom
    show gnom5_mini:
        xalign 0.3
        yalign 0.5
    with zoomin
    show gnom6:
        ypos 1500
    show gnom1:
        xalign 0.714
        yalign 0.616
    with moveinbottom
    show gnom1_mini:
        ypos 1500
    with moveinbottom
    show gnom6_mini:
        xalign 0.5
        yalign 0.64
    with zoomin
    play sound hmmm9
    show gnom3 at leap
    gnoms 'Ты хочешь пойти с нами?'
    play sound hmmm9
    show gnom1 at leap
    gnoms 'Ты должен пойти с нами'
    play sound hmmm7
    show henry at leap
    Character 'Что же делать?'
    menu:
        Character 'Что мне выбрать?'
        'Попробовать ответить на все вопросы Гаети':
            play sound hmmm1
            show henry at leap
            Character 'Меня зовут [name], я не из вашего мира'
            Character 'Я иду на поиски мага Алистера, чтобы он помог мне вернутся домой'
            play sound hmmm9
            show gnom1 at leap
            gnoms 'Пошли с нами'
            play sound hmmm9
            show gnom3 at leap
            gnoms 'Тебе точно нужно идти с нами'
            play sound hmmm9
            show gnom4 at leap
            gnoms 'Ты идёшь с нами'
            play sound hmmm4
            show henry at leap
            Character 'Извините, мне нужно идти'
            window hide
            show henry:
                xalign 1.25
                yalign 1.25
            with moveinright
            show dragon:
                xalign 1.45
                yalign 1.45
            with moveinright
        'Взять себя в руки и бежать':
            window hide
            show henry:
                xalign 1.25
                yalign 1.25
            with moveinright
            show dragon:
                xalign 1.45
                yalign 1.45
            with moveinright
    scene scene9_1 with pushleft
    show henry at left with moveinleft
    show dragon at right with moveinleft
    play sound hmmm2
    show henry at leap
    Character 'Знаешь, в моем мире все устроено немного не так...'
    Character 'И Гаети мне кое-кого напомнили'
    show dragon at leap
    dragon 'Кого они тебе напомнили?'
    play sound hmmm1
    show henry at leap
    Character 'Они напоминают мне моих родителей и учителей'
    Character 'Мне также все твердят : «выбрал вуз?», «поспи», «поешь уже», «сдай ЕГЭ», «поступи на бюджет», «иди выбирай вуз»'
    show dragon at leap
    dragon 'Да, действительно, сходство с Гаети есть'
    play sound gasp
    show henry at leap
    Character 'От этого иногда устаешь и это тебя даже немного раздражает'
    show dragon at leap
    dragon 'Может они иногда правы?'
    play sound surprise1
    show henry at leap
    Character 'Хм... Знаешь, может быть, родители иногда правы, они же желают нам добра, поэтому, когда они говорят “иди отдохни” или “поешь”, нужно слушать их'
    Character 'Ведь нашему мозгу нужно отдыхать, менять активность. Если ты будешь постоянно учиться, могут произойти выгорание'
    show dragon at leap
    dragon 'То есть учиться в вашем мире не нужно?'
    show henry at leap
    Character 'Конечно нужно, но нужно знать меру во всём'
    stop music fadeout 1.0
    return

label fscene10_megastore:
    play music bazar fadein 1.0
    scene scene10 with dissolve
    show dragon at right with moveinbottom
    show bella at left with moveinbottom
    play sound hmmm4
    show dragon at leap
    dragon 'Вот мы и пришли'
    dragon 'Вот там лавка Алистера'
    show bella at leap
    Character 'Давай зайдём'
    stop music fadeout 1.0
    play sound door_bell
    scene scene10_1 with dissolve
    show bella at left with moveinright
    show dragon at right with moveinright
    show mag at center with moveinbottom
    play sound hmmm9
    show mag at leap
    mag 'Приветствую вас, что вы хотели в моей лавке?'
    play sound whmm5
    show bella at leap
    Character 'Здравствуйте, мне нужно попасть в мой мир'
    window hide
    show dragon:
        xalign 1.5
    with moveinright
    show mag at right with moveinright
    play sound hmmm8
    show mag at leap
    mag 'Ой, с этим я тебе помочь не могу'
    show bella at leap
    Character 'Что же мне тогда делать? Как здесь выжить?'
    show mag at leap
    mag 'Ты бы могла пригодиться в этом мире'
    play sound whmm18
    show bella at leap
    Character 'Что же ты можешь мне предложить?'
    show mag at leap
    mag 'Есть несколько вариантов'
    $ first_choose = False
    $ second_choose = False
    $ third_choose = False
    $ correct_choose = False
    window hide
    call fchoose_scene10 from _call_fchoose_scene10 # Сцена выбора цикличная
    if correct_choose:
        show mag:
            xalign 2.0
        with moveinright
        show dragon at right with moveinright
    else:
        scene scene10_1 with dissolve
        show bella at left with moveinbottom
        show dragon at right with moveinbottom
    play sound whmm19
    show bella at leap
    Character 'Да, трудно в этом мире, что же мне делать?'
    stop sound fadeout 1.0
    play sound hmmm2
    show dragon at leap
    dragon 'У меня есть ещё одно предложение'
    dragon 'Мы можем отправиться на гору Нан Курнир, там живёт один колдун. Но сразу скажу, он немного сумасшедший'
    return

label scene10_megastore:
    play music bazar fadein 1.0
    scene scene10 with dissolve
    show dragon at right with moveinbottom
    show henry at left with moveinbottom
    play sound hmmm4
    show dragon at leap
    dragon 'Вот мы и пришли'
    dragon 'Вот там лавка Алистера'
    show henry at leap
    Character 'Давай зайдём'
    stop music fadeout 1.0
    play sound door_bell
    scene scene10_1 with dissolve
    show henry at left with moveinright
    show dragon at right with moveinright
    show mag at center with moveinbottom
    play sound hmmm9
    show mag at leap
    mag 'Приветствую вас, что вы хотели в моей лавке?'
    play sound hmmm4
    show henry at leap
    Character 'Здравствуйте, мне нужно попасть в мой мир'
    window hide
    show dragon:
        xalign 1.5
    with moveinright
    show mag at right with moveinright
    play sound hmmm8
    show mag at leap
    mag 'Ой, с этим я тебе помочь не могу'
    show henry at leap
    Character 'Что же мне тогда делать? Как здесь выжить?'
    show mag at leap
    mag 'Ты бы мог пригодиться в этом мире'
    play sound hmmm12
    show henry at leap
    Character 'Что же ты можешь мне предложить?'
    show mag at leap
    mag 'Есть несколько вариантов'
    $ first_choose = False
    $ second_choose = False
    $ third_choose = False
    $ correct_choose = False
    window hide
    call choose_scene10 from _call_choose_scene10 # Сцена выбора цикличная
    if correct_choose:
        show mag:
            xalign 2.0
        with moveinright
        show dragon at right with moveinright
    else:
        scene scene10_1 with dissolve
        show henry at left with moveinbottom
        show dragon at right with moveinbottom
    play sound hmmm6
    show henry at leap
    Character 'Да, трудно в этом мире, что же мне делать?'
    stop sound fadeout 1.0
    play sound hmmm2
    show dragon at leap
    dragon 'У меня есть ещё одно предложение'
    dragon 'Мы можем отправиться на гору Нан Курнир, там живёт один колдун. Но сразу скажу, он немного сумасшедший'
    return

menu fchoose_scene10:
    'Ты можешь пасти единорогов':
        if first_choose:
            play sound hmmm9
            show mag at leap
            mag 'Ты уже спрашивала меня про это'
            call fchoose_scene10 from _call_fchoose_scene10_1
            return
        play music birds_sing fadein 1.0
        scene scene10_2 with dissolve
        show bella at left with moveinbottom
        show mag at right with moveinbottom
        show unicorn_mini_zerkalo:
            xalign 0.3
            yalign 0.5889
        with zoomin
        show unicorn:
            xalign 0.423
            yalign 0.43
        with zoomin
        play sound whmm16
        show bella at leap
        Character 'И как же мне к ним подойти?'
        show mag at leap
        mag 'Ты должна показать единорогу силу'
        window hide
        show bella:
            xalign 1.5
        with moveinright
        show bella_mini:
            xalign 0.55
            yalign 0.43
        with moveinright
        play sound horse
        show unicorn:
            xalign 0.3
        with easeinleft
        show bella_mini:
            xalign 0.4
        with moveinleft
        hide unicorn
        show unicorn_zerkalo:
            xalign 0.3
            yalign 0.43
        with dissolve
        show unicorn_zerkalo:
            xalign 1.5
        with moveinright
        stop sound fadeout 1.0
        show unicorn_mini_zerkalo:
            xalign 1.5
        with moveinright
        show bella_mini:
            xalign 1.5
        with moveinright
        show bella at left with moveinleft
        play sound whmm10
        show bella at leap
        Character 'Да, к ЕГЭ мне было готовиться легче'
        stop music fadeout 1.0
        $ first_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show bella at left with moveinbottom
            show mag at right with moveinbottom
            call fchoose_scene10 from _call_fchoose_scene10_2
            return
    'Ты можешь состоять в армии короля':
        if second_choose:
            play sound hmmm9
            show mag at leap
            mag 'Ты уже спрашивала меня про это'
            call fchoose_scene10 from _call_fchoose_scene10_3
            return
        play music hero fadein 1.0
        scene scene10_3 with dissolve
        show bella at left with moveinbottom
        show mag at right with moveinbottom
        show general at center with moveinbottom
        play sound hmmm9
        show mag at leap
        mag 'Ты можешь состоять в армии короля'
        play sound krik3
        show general at leap
        general 'Бойцы, вы должны быть готовы ко всему'
        general 'Недавно нам объявили войну Марийцы'
        show mag:
            xalign 1.8
        with moveinright
        show general at right with moveinright
        play sound hmmm9
        show general at leap
        general 'С этого момента вы будете жить в замке'
        general 'Итак, ваше первое задание на сегодня...'
        general 'Нужно подняться на гору Нан Куринир, добежать до края острова и принести мне волос единорога'
        play sound whmm12
        show bella at leap
        Character 'Нее...'
        Character 'Это не для меня'
        play sound whmm14
        show bella at leap
        Character 'А вот если бы я пошла в IT, то могла бы работать удалённо и жить в Дубае'
        stop sound fadeout 1.0
        play sound hmmm9
        show general at leap
        general 'Что это ты бормочешь?'
        show bella at leap
        Character 'Да так... Мысли вслух'
        stop music fadeout 1.0
        $ second_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show bella at left with moveinbottom
            show mag at right with moveinbottom
            call fchoose_scene10 from _call_fchoose_scene10_4
            return
    'Ты можешь стать моим учеником':
        if third_choose:
            show mag at leap
            play sound hmmm9
            mag 'Ты уже спрашивала меня про это'
            call fchoose_scene10 from _call_fchoose_scene10_5
            return
        play sound hmmm8
        show mag at leap
        mag 'Тебе нужно будет днём и ночью выполнять мои поручения'
        mag 'Также нужно будет рисковать своей жизнью, чтобы доставать необходимые ингредиенты для зелий'
        play sound whmm17
        show bella at leap
        Character 'Извини, но такое мне тоже не подходит'
        Character 'В IT у меня был бы удобный график работы'
        $ third_choose = True
        if first_choose & second_choose & third_choose == True:
            $ correct_choose = True
            return
        else:
            scene scene10_1 with dissolve
            show bella at left with moveinbottom
            show mag at right with moveinbottom
            call fchoose_scene10 from _call_fchoose_scene10_6
            return

menu choose_scene10:
    'Ты можешь пасти единорогов':
        if first_choose:
            play sound hmmm9
            show mag at leap
            mag 'Ты уже спрашивал меня про это'
            call choose_scene10 from _call_choose_scene10_1
            return
        play music birds_sing fadein 1.0
        scene scene10_2 with dissolve
        show henry at left with moveinbottom
        show mag at right with moveinbottom
        show unicorn_mini_zerkalo:
            xalign 0.3
            yalign 0.5889
        with zoomin
        show unicorn:
            xalign 0.423
            yalign 0.43
        with zoomin
        play sound hmmm10
        show henry at leap
        Character 'И как же мне к ним подойти?'
        show mag at leap
        mag 'Ты должен показать единорогу силу'
        window hide
        show henry:
            xalign 1.5
        with moveinright
        show henry_mini:
            xalign 0.55
            yalign 0.43
        with moveinright
        play sound horse
        show unicorn:
            xalign 0.3
        with easeinleft
        show henry_mini:
            xalign 0.4
        with moveinleft
        hide unicorn
        show unicorn_zerkalo:
            xalign 0.3
            yalign 0.43
        with dissolve
        show unicorn_zerkalo:
            xalign 1.5
        with moveinright
        stop sound fadeout 1.0
        show unicorn_mini_zerkalo:
            xalign 1.5
        with moveinright
        show henry_mini:
            xalign 1.5
        with moveinright
        show henry at left with moveinleft
        play sound gasp
        show henry at leap
        Character 'Да, к ЕГЭ мне было готовиться легче'
        stop music fadeout 1.0
        $ first_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show henry at left with moveinbottom
            show mag at right with moveinbottom
            call choose_scene10 from _call_choose_scene10_2
            return
    'Ты можешь состоять в армии короля':
        if second_choose:
            play sound hmmm9
            show mag at leap
            mag 'Ты уже спрашивал меня про это'
            call choose_scene10 from _call_choose_scene10_3
            return
        play music hero fadein 1.0
        scene scene10_3 with dissolve
        show henry at left with moveinbottom
        show mag at right with moveinbottom
        show general at center with moveinbottom
        play sound hmmm9
        show mag at leap
        mag 'Ты можешь состоять в армии короля'
        play sound krik3
        show general at leap
        general 'Бойцы, вы должны быть готовы ко всему'
        general 'Недавно нам объявили войну Марийцы'
        show mag:
            xalign 1.8
        with moveinright
        show general at right with moveinright
        play sound hmmm9
        show general at leap
        general 'С этого момента вы будете жить в замке'
        general 'Итак, ваше первое задание на сегодня...'
        general 'Нужно подняться на гору Нан Куринир, добежать до края острова и принести мне волос единорога'
        play sound hmmm4
        show henry at leap
        Character 'Нее...'
        Character 'Это не для меня'
        play sound hmmm8
        show henry at leap
        Character 'А вот если бы я пошёл в IT, то мог бы работать удалённо и жить в Дубае'
        stop sound fadeout 1.0
        play sound hmmm9
        show general at leap
        general 'Что это ты бормочешь?'
        show henry at leap
        Character 'Да так... Мысли вслух'
        stop music fadeout 1.0
        $ second_choose = True
        if first_choose & second_choose & third_choose == True:
            return
        else:
            scene scene10_1 with dissolve
            show henry at left with moveinbottom
            show mag at right with moveinbottom
            call choose_scene10 from _call_choose_scene10_4
            return
    'Ты можешь стать моим учеником':
        if third_choose:
            show mag at leap
            play sound hmmm9
            mag 'Ты уже спрашивал меня про это'
            call choose_scene10 from _call_choose_scene10_5
            return
        play sound hmmm8
        show mag at leap
        mag 'Тебе нужно будет днём и ночью выполнять мои поручения'
        mag 'Также нужно будет рисковать своей жизнью, чтобы доставать необходимые ингредиенты для зелий'
        play sound hmmm7
        show henry at leap
        Character 'Извини, но такое мне тоже не подходит'
        Character 'В IT у меня был бы удобный график работы'
        $ third_choose = True
        if first_choose & second_choose & third_choose == True:
            $ correct_choose = True
            return
        else:
            scene scene10_1 with dissolve
            show henry at left with moveinbottom
            show mag at right with moveinbottom
            call choose_scene10 from _call_choose_scene10_6
            return

label fscene11_coldun:
    play music water_down fadein 1.0
    scene scene11 with dissolve
    show bella at left with moveinbottom
    show dragon at right with moveinbottom
    show koldun at center with moveinbottom
    play sound hmmm9
    show koldun at leap
    koldun 'Давно у меня не было гостей, зачем пожаловали?'
    play sound whmm18
    show bella at leap
    Character 'Мне нужно попасть в свой мир'
    play sound hmmm1
    show koldun at leap
    koldun 'Я давно подозревал, что есть другие миры'
    koldun 'Однако я не могу тебя туда отправить, но могу показать кое-что другое'
    window hide
    show dragon:
        xalign 1.5
    with moveinright
    play sound magic
    show koldun at right with moveinright
    show zerkalo1:
        xalign 0.2
        yalign 0.51
    with moveinbottom
    show zerkalo2:
        xalign 0.41
        yalign 0.51
    with moveinbottom
    show zerkalo3:
        xalign 0.62
        yalign 0.51
    with moveinbottom
    koldun 'Перед тобой три зеркала, выбирай понравившееся'
    window hide
    $ first_zerkalo = False
    $ second_zerkalo = False
    stop music fadeout 1.0
    call fchoose_scene11 from _call_fchoose_scene11
    return

label scene11_coldun:
    play music water_down fadein 1.0
    scene scene11 with dissolve
    show henry at left with moveinbottom
    show dragon at right with moveinbottom
    show koldun at center with moveinbottom
    play sound hmmm9
    show koldun at leap
    koldun 'Давно у меня не было гостей, зачем пожаловали?'
    play sound hmmm3
    show henry at leap
    Character 'Мне нужно попасть в свой мир'
    play sound hmmm1
    show koldun at leap
    koldun 'Я давно подозревал, что есть другие миры'
    koldun 'Однако я не могу тебя туда отправить, но могу показать кое-что другое'
    window hide
    show dragon:
        xalign 1.5
    with moveinright
    play sound magic
    show koldun at right with moveinright
    show zerkalo1:
        xalign 0.2
        yalign 0.51
    with moveinbottom
    show zerkalo2:
        xalign 0.41
        yalign 0.51
    with moveinbottom
    show zerkalo3:
        xalign 0.62
        yalign 0.51
    with moveinbottom
    koldun 'Перед тобой три зеркала, выбирай понравившееся'
    window hide
    $ first_zerkalo = False
    $ second_zerkalo = False
    stop music fadeout 1.0
    call choose_scene11 from _call_choose_scene11
    return

menu fchoose_scene11:
    'Зеркало 1':
        if first_zerkalo:
            play sound hmmm9
            show koldun at leap
            koldun 'Ты уже смотрела, что там'
            call fchoose_scene11 from _call_fchoose_scene11_1
            return
        $ first_zerkalo = True
        play music hospital
        scene scene11_1 with dissolve
        show bella at left with moveinbottom
        show syringe1left:
            xalign 0.78385
            yalign 0.14259
        with zoomin
        show syringe2left:
            xalign 0.6392
            yalign 0.38
        with zoomin
        show syringe3left:
            xalign 0.82
            yalign 0.514
        with zoomin
        show syringe1left:
            xalign 0.2
        with moveinleft
        show syringe2left:
            xalign 0.2
        with moveinleft
        show syringe3left:
            xalign 0.2
        with moveinleft
        play sound wkrik1
        show bella at leap
        Character 'ААААА'
        stop sound fadeout 1.0
        Character 'Они летают'
        window hide
        show bella:
            xalign 1.5
        with moveinright
        hide syringe1left
        hide syringe2left
        hide syringe3left
        show syringe1right:
            xalign 0.2
            yalign 0.14259
        with zoomin
        show syringe2right:
            xalign 0.2
            yalign 0.38
        with zoomin
        show syringe3right:
            xalign 0.2
            yalign 0.514
        with zoomin
        show syringe1right:
            xalign 1.5
        with moveinright
        show syringe2right:
            xalign 1.5
        with moveinright
        show syringe3right:
            xalign 1.5
        with moveinright
        stop music fadeout 1.0
        scene scene11 with dissolve
        play music water_down fadein 1.0
        show zerkalo1:
            xalign 0.2
            yalign 0.51
        with moveinbottom
        show zerkalo2:
            xalign 0.41
            yalign 0.51
        with moveinbottom
        show zerkalo3:
            xalign 0.62
            yalign 0.51
        show bella at left with moveinbottom
        show koldun at right with moveinbottom
        stop music fadeout 1.0
        call fchoose_scene11 from _call_fchoose_scene11_2
        return
    'Зеркало 2':
        if second_zerkalo:
            play sound hmmm9
            show koldun at leap
            koldun 'Ты уже смотрела, что здесь'
            call fchoose_scene11 from _call_fchoose_scene11_3
            return
        $ second_zerkalo = True
        scene scene11_2 with dissolve
        show bella at left with moveinbottom
        show bella at leap
        Character 'Сколько же тут книг?'
        window hide
        play sound book volume 1.5
        show book1:
            xalign 0.64696
            yalign 0,174
        with zoomin
        show book2:
            xalign 0.74
            yalign 0.497
        with zoomin
        show book1:
            xalign 0.2
        with moveinleft
        show book2:
            xalign 0.2
        with moveinleft
        show bella at right with moveinright
        show book1:
            xalign 0.8
        with moveinright
        show book2:
            xalign 0.8
        with moveinright
        show bella at left with moveinleft
        play sound whmm14
        show bella at leap
        Character 'Они кружат мне голову'
        window hide
        show book1:
            xalign 0.2
        with moveinleft
        show book2:
            xalign 0.2
        with moveinleft
        show bella:
            xalign 1.5
        with moveinright
        show book1:
            xalign 1.5
        with moveinright
        show book2:
            xalign 1.5
        with moveinright
        play music water_down fadein 1.0
        scene scene11 with dissolve
        show zerkalo1:
            xalign 0.2
            yalign 0.51
        with moveinbottom
        show zerkalo2:
            xalign 0.41
            yalign 0.51
        with moveinbottom
        show zerkalo3:
            xalign 0.62
            yalign 0.51
        with moveinbottom
        show bella at left with moveinbottom
        show koldun at right with moveinbottom
        call fchoose_scene11 from _call_fchoose_scene11_4
        return
    'Зеркало 3':
        scene scene11_3 with dissolve
        play music computer_work fadein 1.0
        show bella at left with moveinbottom
        play sound whmm11
        show bella at leap
        Character 'Может я смогу написать какую-нибудь программу на компьютере?'
        Character 'backend-разработчик, кто это такой?'
        show macbook:
            xalign 0.9
            yalign 0.51296
        with moveinbottom
        play sound keyboard volume 1.5
        show macbook at leap
        computer 'Специалист, который занимается серверной частью сайтов, мобильных и десктопных приложений и игр'
        play sound whmm10
        show bella at leap
        Character 'А чем же он занимается?'
        play sound windows1
        show macbook at leap
        computer 'Он создает базы данных и управляет ими, проводит интеграции с внешними сервисами и занимается всем, что находится «под капотом» сайта'
        show bella at leap
        Character 'Как же интересно, но какие плюсы у этой профессии?'
        play sound windows2
        show macbook at leap
        computer 'Востребованность профессии, работа из любой точки планеты, возможность выбирать направление, перспективы, высокая зарплата'
        show bella at leap
        Character 'А где же этому можно научиться ?'
        play sound windows3
        show macbook at leap
        computer 'Программная инженерия — это направление подготовки программистов, готовых к индустриальному производству программного обеспечения для информационно-вычислительных систем различного назначения'
        return

menu choose_scene11:
    'Зеркало 1':
        if first_zerkalo:
            play sound hmmm9
            show koldun at leap
            koldun 'Ты уже смотрел, что там'
            call choose_scene11 from _call_choose_scene11_1
            return
        $ first_zerkalo = True
        play music hospital
        scene scene11_1 with dissolve
        show henry at left with moveinbottom
        show syringe1left:
            xalign 0.78385
            yalign 0.14259
        with zoomin
        show syringe2left:
            xalign 0.6392
            yalign 0.38
        with zoomin
        show syringe3left:
            xalign 0.82
            yalign 0.514
        with zoomin
        show syringe1left:
            xalign 0.2
        with moveinleft
        show syringe2left:
            xalign 0.2
        with moveinleft
        show syringe3left:
            xalign 0.2
        with moveinleft
        play sound krik2
        show henry at leap
        Character 'ААААА'
        stop sound fadeout 1.0
        Character 'Они летают'
        window hide
        show henry:
            xalign 1.5
        with moveinright
        hide syringe1left
        hide syringe2left
        hide syringe3left
        show syringe1right:
            xalign 0.2
            yalign 0.14259
        with zoomin
        show syringe2right:
            xalign 0.2
            yalign 0.38
        with zoomin
        show syringe3right:
            xalign 0.2
            yalign 0.514
        with zoomin
        show syringe1right:
            xalign 1.5
        with moveinright
        show syringe2right:
            xalign 1.5
        with moveinright
        show syringe3right:
            xalign 1.5
        with moveinright
        stop music fadeout 1.0
        scene scene11 with dissolve
        play music water_down fadein 1.0
        show zerkalo1:
            xalign 0.2
            yalign 0.51
        with moveinbottom
        show zerkalo2:
            xalign 0.41
            yalign 0.51
        with moveinbottom
        show zerkalo3:
            xalign 0.62
            yalign 0.51
        show henry at left with moveinbottom
        show koldun at right with moveinbottom
        stop music fadeout 1.0
        call choose_scene11 from _call_choose_scene11_2
        return
    'Зеркало 2':
        if second_zerkalo:
            play sound hmmm9
            show koldun at leap
            koldun 'Ты уже смотрел, что здесь'
            call choose_scene11 from _call_choose_scene11_3
            return
        $ second_zerkalo = True
        scene scene11_2 with dissolve
        show henry at left with moveinbottom
        show henry at leap
        Character 'Сколько же тут книг?'
        window hide
        play sound book volume 1.5
        show book1:
            xalign 0.64696
            yalign 0,174
        with zoomin
        show book2:
            xalign 0.74
            yalign 0.497
        with zoomin
        show book1:
            xalign 0.2
        with moveinleft
        show book2:
            xalign 0.2
        with moveinleft
        show henry at right with moveinright
        show book1:
            xalign 0.8
        with moveinright
        show book2:
            xalign 0.8
        with moveinright
        show henry at left with moveinleft
        play sound gasp
        show henry at leap
        Character 'Они кружат мне голову'
        window hide
        show book1:
            xalign 0.2
        with moveinleft
        show book2:
            xalign 0.2
        with moveinleft
        show henry:
            xalign 1.5
        with moveinright
        show book1:
            xalign 1.5
        with moveinright
        show book2:
            xalign 1.5
        with moveinright
        play music water_down fadein 1.0
        scene scene11 with dissolve
        show zerkalo1:
            xalign 0.2
            yalign 0.51
        with moveinbottom
        show zerkalo2:
            xalign 0.41
            yalign 0.51
        with moveinbottom
        show zerkalo3:
            xalign 0.62
            yalign 0.51
        with moveinbottom
        show henry at left with moveinbottom
        show koldun at right with moveinbottom
        call choose_scene11 from _call_choose_scene11_4
        return
    'Зеркало 3':
        scene scene11_3 with dissolve
        play music computer_work fadein 1.0
        show henry at left with moveinbottom
        play sound hmmm1
        show henry at leap
        Character 'Может я смогу написать какую-нибудь программу на компьютере?'
        Character 'backend-разработчик, кто это такой?'
        show macbook:
            xalign 0.9
            yalign 0.51296
        with moveinbottom
        play sound keyboard volume 1.5
        show macbook at leap
        computer 'Специалист, который занимается серверной частью сайтов, мобильных и десктопных приложений и игр'
        play sound hmmm12
        show henry at leap
        Character 'А чем же он занимается?'
        play sound windows1
        show macbook at leap
        computer 'Он создает базы данных и управляет ими, проводит интеграции с внешними сервисами и занимается всем, что находится «под капотом» сайта'
        show henry at leap
        Character 'Как же интересно, но какие плюсы у этой профессии?'
        play sound windows2
        show macbook at leap
        computer 'Востребованность профессии, работа из любой точки планеты, возможность выбирать направление, перспективы, высокая зарплата'
        show henry at leap
        Character 'А где же этому можно научиться ?'
        play sound windows3
        show macbook at leap
        computer 'Программная инженерия — это направление подготовки программистов, готовых к индустриальному производству программного обеспечения для информационно-вычислительных систем различного назначения'
        return

label fscene12_hagen:
    play sound steps
    show bella at leap
    Character 'Кто-то идёт, чьи это шаги?'
    show macbook:
        xalign 2.0
    with moveinright
    stop sound fadeout 1.0
    show hagen at right with moveinbottom
    play sound hmmm9
    show hagen at leap
    hagen 'Что ты здесь забыла?'
    play sound whmm14
    show bella at leap
    Character 'Извините, я просто изучаю профессию, используя ваш компьютер'
    show hagen at leap
    hagen 'Это мое измерение и моя ветка времени, здесь всё решаю я'
    show bella at leap
    Character 'А вы не могли бы отправить меня домой?'
    play sound hmmm8
    show hagen at leap
    hagen 'Пока ты в моем мире, ты будешь работать на меня'
    hagen 'Познакомся с коллегами они введу тебя в курс дела'
    play sound whmm16
    show bella at leap
    Character 'Хорошо , а куда мне идти?'
    show hagen at leap
    hagen 'Прямо по коридору и направо'
    stop music fadeout 1.0
    play music koridor fadein 1.0
    scene scene12 with dissolve
    show bella at left with moveinleft
    play sound whmm17
    show bella at leap
    Character 'Интересно получится ли у меня работать здесь?'
    show bella:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    stop music fadeout 1.0
    scene scene12_1 with dissolve
    show bella at left with moveinleft
    show hinki at right with moveinbottom
    play sound hihi
    show hinki at leap
    hinki 'Ой, а кто это у нас тут? Что ты здесь забыла?'
    show riobs at center with moveinbottom
    play sound hmmm8
    show riobs at leap
    riobs 'Хинки, будь помягче с новенькой'
    show riobs at leap
    riobs 'Приветствую тебя, как тебя зовут?'
    play sound whmm18
    show bella at leap
    Character 'Привет, меня зовут [name]'
    show riobs at leap
    riobs 'Мы сейчас работаем над одним проектом'
    play sound whmm1
    show hinki at leap
    hinki 'Я не думаю, что ты можешь нам чем-нибудь помочь'
    show bella at leap
    Character 'Я бы могла попробовать себя в роли Backend — разработчика'
    play sound hihi
    show hinki at leap
    hinki 'Ха-ха-ха, ты хоть знаешь, что такое веб-сервер?'
    play sound whmm19
    show bella at leap
    Character 'Сервер, принимающий HTTP-запросы от клиентов, обычно веб-браузеров, и выдающий им HTTP-ответы, как правило, вместе с HTML-страницей, изображением, файлом, медиа-потоком или другими данными'
    play sound whmm2
    show hinki at leap
    hinki 'У нас даже уборщик знает, что это такое. Знаешь ли ты что такое HTTP?'
    play sound whmm12
    show bella at leap
    Character 'Это протокол, который использует для передачи содержимого TCP, поэтому HTTP считается надежным протоколом для обмена содержимым. Также HTTP — самый популярный протокол'
    show bella at leap
    Character 'Сама не знаю, как мне удалось это запомнить'
    play sound whmm3
    show hinki at leap
    hinki 'Ладно, может ты что-то знаешь. У меня есть последний вопрос'
    hinki 'Как веб-страницы взаимодействуют с серверами?'
    play sound whmm11
    show bella at leap
    Character 'Веб-браузеры взаимодействуют с веб-серверами при помощи протокола передачи гипертекста (HTTP). При взаимодействии, браузер отправляет на сервер HTTP-запрос'
    show bella at leap
    Character 'А также, необходимо знать, что путь (URL), который определяет целевой сервер и ресурс (например, HTML-файл, конкретная точка данных на сервере или запускаемый инструмент)'
    show riobs at leap
    riobs 'Хинки, ну отцепись от девчонки. Я думаю, она уже доказала, что может писать проект с нами'
    play sound whmm4
    show hinki at leap
    hinki 'Хм... Ладно, пусть попробует'
    play sound hmmm11
    show riobs at leap
    riobs 'Итак, мы работаем над проектом “Gold Ball”. Заказчик проводил городские оффлайн-турниры по киберфутболу'
    show riobs at leap
    riobs 'Чтобы охватить игроков по всей стране и масштабировать проект на СНГ, клиент заказал разработку веб-сервиса для автоматизации проведения соревнований'
    show hinki at leap
    hinki 'Проведя анализ, мы спроектировали механику турниров, логику распределения игроков по турнирной сетке, статистику и систему рейтинга'
    show hinki at leap
    hinki 'Оценив полученные данные, приняли решение в пользу фреймворка Ruby on Rails'
    show hinki at leap
    hinki 'Он подходит, чтобы реализовать описанный функционал, а его шаблонизатор хорошо справляется с типовыми страницами турниров и матчей'
    play sound whmm5
    show hinki at leap
    hinki 'Ты что-нибудь понимаешь?'
    show bella at leap
    Character 'Я примерно поняла, что нужно сделать'
    show riobs at leap
    riobs 'Хорошо, можешь переосмыслить эту информацию. Завтра ты должен будешь что-нибудь предложить'
    show riobs at leap
    riobs 'Хинки, ты можешь показать комнату, где будет жить [name]?'
    play sound whmm6
    show hinki at leap
    hinki 'Неохотно, но соглашусь'
    play sound koridor fadein 1.0
    scene scene12 with dissolve
    show bella at left with moveinleft
    show hinki at left with moveinleft
    play sound whmm7
    show hinki at leap
    hinki 'Идём за мной'
    window hide
    show hinki:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    show bella:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    stop sound fadeout 1.0
    scene scene12_2 with dissolve
    show bella at left with moveinleft
    show hinki at center with moveinleft
    show hinki at leap
    hinki 'Здесь ты можешь отдохнуть'
    play sound whmm16
    show bella at leap
    Character 'Спасибо, что проводила'
    play sound whmm8
    show hinki at leap
    hinki 'Не обольщайся, меня просто попросил мой коллега'
    show hinki:
        xalign 1.5
    with moveinright
    $ the_end = False
    menu:
        Character 'Может мне и вправду поспать или подумать над проектом?'
        'Поспать':
            play sound end fadein 1.0
            $ the_end = True
            scene end1 with dissolve
            pause 300
            # scene bg black with dissolve
            # window hide
            # n '''[name] проснулась во время урока,
            # не помня свои приключения'''
            # nvl clear
            # n '''КОНЕЦ!!!'''
            stop sound fadeout 1.0
        'Подумать над проектом':
            show bella at center with moveinright
            play sound wgasp
            show bella at leap
            Character 'Меня так заинтересовал проект, может подумать над ним?'
            Character 'Хотя я сегодня очень сильно устала'
            Character 'Необходимо набраться сил перед завтрашним днём'
            show bella at leap
            Character 'Пойду спать'
    return

label scene12_hagen:
    play sound steps
    show henry at leap
    Character 'Кто-то идёт, чьи это шаги?'
    show macbook:
        xalign 2.0
    with moveinright
    stop sound fadeout 1.0
    show hagen at right with moveinbottom
    play sound hmmm9
    show hagen at leap
    hagen 'Что ты здесь забыл?'
    play sound hmmm2
    show henry at leap
    Character 'Извините, я просто изучаю профессию, используя ваш компьютер'
    show hagen at leap
    hagen 'Это мое измерение и моя ветка времени, здесь всё решаю я'
    show henry at leap
    Character 'А вы не могли бы отправить меня домой?'
    play sound hmmm8
    show hagen at leap
    hagen 'Пока ты в моем мире, ты будешь работать на меня'
    hagen 'Познакомся с коллегами они введу тебя в курс дела'
    play sound hmmm12
    show henry at leap
    Character 'Хорошо , а куда мне идти?'
    show hagen at leap
    hagen 'Прямо по коридору и направо'
    stop music fadeout 1.0
    play music koridor fadein 1.0
    scene scene12 with dissolve
    show henry at left with moveinleft
    play sound hmmm3
    show henry at leap
    Character 'Интересно получится ли у меня работать здесь?'
    show henry:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    stop music fadeout 1.0
    scene scene12_1 with dissolve
    show henry at left with moveinleft
    show hinki at right with moveinbottom
    play sound hihi
    show hinki at leap
    hinki 'Ой, а кто это у нас тут? Что ты здесь забыл?'
    show riobs at center with moveinbottom
    play sound hmmm8
    show riobs at leap
    riobs 'Хинки, будь помягче с новеньким'
    show riobs at leap
    riobs 'Приветствую тебя, как тебя зовут?'
    play sound hmmm1
    show henry at leap
    Character 'Привет, меня зовут [name]'
    show riobs at leap
    riobs 'Мы сейчас работаем над одним проектом'
    play sound whmm1
    show hinki at leap
    hinki 'Я не думаю, что ты можешь нам чем-нибудь помочь'
    show henry at leap
    Character 'Я бы мог попробовать себя в роли Backend — разработчика'
    play sound hihi
    show hinki at leap
    hinki 'Ха-ха-ха, ты хоть знаешь, что такое веб-сервер?'
    play sound hmmm6
    show henry at leap
    Character 'Сервер, принимающий HTTP-запросы от клиентов, обычно веб-браузеров, и выдающий им HTTP-ответы, как правило, вместе с HTML-страницей, изображением, файлом, медиа-потоком или другими данными'
    play sound whmm2
    show hinki at leap
    hinki 'У нас даже уборщик знает, что это такое. Знаешь ли ты что такое HTTP?'
    play sound hmmm1
    show henry at leap
    Character 'Это протокол, который использует для передачи содержимого TCP, поэтому HTTP считается надежным протоколом для обмена содержимым. Также HTTP — самый популярный протокол'
    show henry at leap
    Character 'Сам не знаю, как мне удалось это запомнить'
    play sound whmm3
    show hinki at leap
    hinki 'Ладно, может ты что-то знаешь. У меня есть последний вопрос'
    hinki 'Как веб-страницы взаимодействуют с серверами?'
    play sound hmmm5
    show henry at leap
    Character 'Веб-браузеры взаимодействуют с веб-серверами при помощи протокола передачи гипертекста (HTTP). При взаимодействии, браузер отправляет на сервер HTTP-запрос'
    show henry at leap
    Character 'А также, необходимо знать, что путь (URL), который определяет целевой сервер и ресурс (например, HTML-файл, конкретная точка данных на сервере или запускаемый инструмент)'
    show riobs at leap
    riobs 'Хинки, ну отцепись от парнишки. Я думаю, он уже доказал, что может писать проект с нами'
    play sound whmm4
    show hinki at leap
    hinki 'Хм... Ладно, пусть попробует'
    play sound hmmm11
    show riobs at leap
    riobs 'Итак, мы работаем над проектом “Gold Ball”. Заказчик проводил городские оффлайн-турниры по киберфутболу'
    show riobs at leap
    riobs 'Чтобы охватить игроков по всей стране и масштабировать проект на СНГ, клиент заказал разработку веб-сервиса для автоматизации проведения соревнований'
    show hinki at leap
    hinki 'Проведя анализ, мы спроектировали механику турниров, логику распределения игроков по турнирной сетке, статистику и систему рейтинга'
    show hinki at leap
    hinki 'Оценив полученные данные, приняли решение в пользу фреймворка Ruby on Rails'
    show hinki at leap
    hinki 'Он подходит, чтобы реализовать описанный функционал, а его шаблонизатор хорошо справляется с типовыми страницами турниров и матчей'
    play sound whmm5
    show hinki at leap
    hinki 'Ты что-нибудь понимаешь?'
    show henry at leap
    Character 'Я примерно понял, что нужно сделать'
    show riobs at leap
    riobs 'Хорошо, можешь переосмыслить эту информацию. Завтра ты должен будешь что-нибудь предложить'
    show riobs at leap
    riobs 'Хинки, ты можешь показать комнату, где будет жить [name]?'
    play sound whmm6
    show hinki at leap
    hinki 'Неохотно, но соглашусь'
    play sound koridor fadein 1.0
    scene scene12 with dissolve
    show henry at left with moveinleft
    show hinki at left with moveinleft
    play sound whmm7
    show hinki at leap
    hinki 'Идём за мной'
    window hide
    show hinki:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    show henry:
        xalign 1.5
    with MoveTransition(2.0, leave = moveinright)
    stop sound fadeout 1.0
    scene scene12_2 with dissolve
    show henry at left with moveinleft
    show hinki at center with moveinleft
    show hinki at leap
    hinki 'Здесь ты можешь отдохнуть'
    play sound hmmm4
    show henry at leap
    Character 'Спасибо, что проводила'
    play sound whmm8
    show hinki at leap
    hinki 'Не обольщайся, меня просто попросил мой коллега'
    show hinki:
        xalign 1.5
    with moveinright
    $ the_end = False
    menu:
        Character 'Может мне и вправду поспать или подумать над проектом?'
        'Поспать':
            play sound end fadein 1.0
            $ the_end = True
            scene end1 with dissolve
            pause 300
            # scene bg black with dissolve
            # window hide
            # n '''[name] проснулся во время урока,
            # не помня свои приключения'''
            # nvl clear
            # n '''КОНЕЦ!!!'''
            stop sound fadeout 1.0
        'Подумать над проектом':
            show henry at center with moveinright
            play sound gasp
            show henry at leap
            Character 'Меня так заинтересовал проект, может подумать над ним?'
            Character 'Хотя я сегодня очень сильно устал'
            Character 'Необходимо набраться сил перед завтрашним днём'
            show henry at leap
            Character 'Пойду спать'
    return

label fscene13_end:
    show scene2_blur with dissolve
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    play sound pshhh
    Maks 'Пшшш... [name]!'
    Maks '[name], вставай, если Юлия Владимировна увидит, что ты спишь, то ты будешь спать у директора'
    scene bg black with Fade(2,0,0)
    scene scene2 with Dissolve(1)
    play sound whmm6
    Character 'Ладно, пошли давай'
    play music peremena fadein 1.0
    scene scene1 with dissolve
    show bella at left with moveinbottom
    show maks at right with moveinbottom
    play sound hmmm8
    show maks at leap
    Maks 'Ты видела, что в УрФУ проходит День открытых дверей, пойдём?'
    play sound whmm5
    show bella at leap
    Character 'Разумеется, мне нужно узнать всё о поступлении, ведь я уже определился с  профессией и направлением'
    show bella at leap
    Character 'Я поступлю на программную инженерию и стану backend-разработчиком'
    stop music fadeout 0.5
    play sound end fadein 1.0
    scene end2 with dissolve
    pause 300
    # scene bg black with dissolve
    # window hide
    # n '''КОНЕЦ!!!'''
    # nvl clear
    stop sound fadeout 1.0
    return

label scene13_end:
    show scene2_blur with dissolve
    scene bg black with Fade(2,0,0)
    scene scene2_blur with Dissolve(1)
    play sound pshhh
    Maks 'Пшшш... [name]!'
    Maks '[name], вставай, если Юлия Владимировна увидит, что ты спишь, то ты будешь спать у директора'
    scene bg black with Fade(2,0,0)
    scene scene2 with Dissolve(1)
    play sound hmmm9
    Character 'Ладно, пошли давай'
    play music peremena fadein 1.0
    scene scene1 with dissolve
    show henry at left with moveinbottom
    show maks at right with moveinbottom
    play sound hmmm8
    show maks at leap
    Maks 'Ты видел, что в УрФУ проходит День открытых дверей, пойдём?'
    play sound hmmm1
    show henry at leap
    Character 'Разумеется, мне нужно узнать всё о поступлении, ведь я уже определился с  профессией и направлением'
    show henry at leap
    Character 'Я поступлю на программную инженерию и стану backend-разработчиком'
    stop music fadeout 0.5
    play sound end fadein 1.0
    scene end2 with dissolve
    pause 300
    # scene bg black with dissolve
    # window hide
    # n '''КОНЕЦ!!!'''
    # nvl clear
    stop sound fadeout 1.0
    return