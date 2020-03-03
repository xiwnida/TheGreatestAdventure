# Этот файл содержит некоторые настройки, которые могут быть изменены
## дабы придать вашей игре индивидуальности. Конечно, здесь только самые
## широко используемые опции. Поменять можно ещё много всего.
##
## Строчки, начинающиеся с двух символов # -- пояснения. Их раскомменчивать
## не стоит. Строчки, начинающиеся с одного символа # -- закомменченые
## куски кода. Их, если Вам нужно, можно раскомменчивать и подправлять
## под Ваши нужды.

init -1 python hide:
    ## Включить инструменты разработчика? Перед отправкой игры
    ## "на золото" этому параметру должно быть присвоенно значение  
    ## False, чтобы игрок не мог читерить, используя эти инструменты.
    config.developer = True

    ## Здесь устанавливаются ширина и высота экрана игры.
    config.screen_width = 800
    config.screen_height = 600

    ## Здесь устанавливается заголовок окна игры, когда игра работает
    ## в оконном режиме.
    config.window_title = "The Greatest Adventure"

    #########################################
    # Планы
    
    ## Здесь активируется использование игрового меню
    ## ввыполненного из кнопок.
    layout.button_menu()

    #########################################
    # Схемы
    
    ## Теперь устанавливается используемая игрой схема интерфейса.
    ## roundrect использует скруглённые прямоугольники в качестве
    ## основы элементов интерфейса. Других пока нет...
    ##
    ## Здесь есть несколько параметров, управляющих цветовой схемой,
    ## которые можно настроить по вкусу.
    theme.regal(
        ## Theme: Regal
        ## Color scheme: Favorite Jeans

        ## The color of an idle widget face.
        widget = "#8699a7",

        ## The color of a focused widget face.
        widget_hover = "#9eb1ad",

        ## The color of the text in a widget.
        widget_text = "#dcdfd6",

        ## The color of the text in a selected widget. (For
        ## example, the current value of a preference.)
        widget_selected = "#ffffff",

        ## The color of a disabled widget face.
        disabled = "#919994",

        ## The color of disabled widget text.
        disabled_text = "#B6BFB9",

        ## The color of informational labels.
        label = "#ffffff",

        ## The color of a frame containing widgets.
        frame = "#6f7571",

        ## The background of the main menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        mm_root = "Images/2.gif",

        ## The background of the game menu. This can be a color
        ## beginning with '#', or an image filename. The latter
        ## should take up the full height and width of the screen.
        gm_root = "Images/2.gif",

        ## If this is True, the in-game window is rounded. If False,
        ## the in-game window is square.
        rounded_window = False,

        ## And we're done with the theme. The theme will customize
        ## various styles, so if we want to change them, we should
        ## do so below.
        )


    #########################################
    ## Эти параметры позволят вам изменить текстовое окно, куда выводятся
    ## реплики и комментарии, заменив его каким-либо изображением.

    ## Фон текстового окна. В Frame два числа -- это размеры границ, левой-правой
    ## и верхней-нижней соответственно
    style.window.background = Frame("Images/textbox.png", 12, 12)

        
    ## margin -- это окружающее окно пространство, где фон не выводится.
    # style.window.left_margin = 6
    # style.window.right_margin = 6
    # style.window.top_margin = 6
    # style.window.bottom_margin = 6
        
    ## padding -- это пространство в окне, где отображается фон.
    style.window.left_padding = 160
    # style.window.right_padding = 6
    style.window.top_padding = 40
    # style.window.bottom_padding = 6

    ## Это -- минимальная высота окна, включая margin и padding
    # style.window.yminimum = 250


    #########################################
    ## С помощью этих параметров можно поменять место расположения
    ## главного меню
        
    ## Делается это так: Находится точка привязки (anchor) внутри объекта
    ## и точка расположения (pos) на экране. Объект выводится на экран
    ## таким образом, чтобы эти две точки совпали.

    ## Значением может быть целое число, или десятичная дробь.
    ## Целое число воспринимается как число пикслей от верхнего левого края.
    ## Десятичная дробь -- как доли ширины/высоты.

    # style.mm_menu_frame.xpos = 0.5
    # style.mm_menu_frame.xanchor = 0.5
    # style.mm_menu_frame.ypos = 0.75
    # style.mm_menu_frame.yanchor = 0.5

    #########################################
    ## Тут можно подправить шрифт, используемый по умолчанию.

    ## Файл шрифта по умолчанию.
    # style.default.font = "DejaVuSans.ttf"

    ## Размр шрифта по умолчанию.        
    # style.default.size = 22

    ## Однако, сие управляет размером не всего текста.
    ## У разных элементов итерфейса свои стили.

    #########################################
    ## Эти параметры позволят изменить звуковое сопровождение

    ## Если в игре не будет звуковых эффектов, установите этот параметр в False.
    config.has_sound = True

    ## Если в игре не будет музыки, установите этот параметр в False.
    config.has_music = True

    ## Если в игре не будет голосового сопровождения, установите этот параметр в False.
    config.has_voice = False

    ## Звуки, издаваемые игрой при нажатии на элементы управления.
    # style.button.activate_sound = "click.wav"
    # style.imagemap.activate_sound = "click.wav"

    ## Звуки, издаваемые игрой при входе и выходе из внутриигрового меню.
    # config.enter_sound = "click.wav"
    # config.exit_sound = "click.wav"

    ## Звук, используемый для проверки громкости звучания в Настройках.
    # config.sample_sound = "click.wav"

    ## Музыка, играющая в главном меню.
    config.main_menu_music = "Music/main_menu.ogg"

    #########################################
    ## Помощь.

    ## Управляет работой элемента "Помощь" меню Ren'Py.
    ## Аргументом может быть:
    ## - Метка в сценарии, В этом случае произойдёт вызов данной метки
    ## - Имя файла, находящегося в основной директории игры, который будет открыт в браузере
    ## - None, что отключает элемент.   
    config.help = "README.html"

    #########################################
    ## Эффекты перехода.

    ## Используемый при переходе в внутриигровое меню из игры.
    config.enter_transition = None

    ## Используемый при переходе в игру из внутриигрового меню.
    config.exit_transition = None

    ## Используемый при переходе между экранами внутриигрового меню.
    config.intra_transition = None

    ## Используемый при переходе в внутриигровое меню из главного меню.
    config.main_game_transition = None

    ## Используемый при переходе в главное меню из игры.
    config.game_main_transition = None

    ## Используемый при переходе в главное меню из экрана заставки. 
    config.end_splash_transition = None

    ## Используемый при возврате в главное меню по завершению игры.
    config.end_game_transition = None
    
    ## Используемый по загрузке игры.
    config.after_load_transition = None
    
    ## При показе окна.
    config.window_show_transition = None

    ## При скрытии окна.
    config.window_hide_transition = None

    #########################################
    ## Здесь устанавливается имя директории, где будут храниться долговременные
    ## данные. (Необходимо установаить рано (отсюда и python early), до всего прочего кода 
    ## init, чтобы долговременная информация могла быть найдена программой инициализации)
    ## Обязательно замените на своё!!!
python early:
    config.save_directory = "The Greatest Adventure-1485722501"
    
init -1 python hide:
    #########################################
    ## Значения параметров Настроек по умолчанию.

    ## Эти значения используются только при саамом первом запуске игры.
    ## Чтобы они сработали снова, нужно удалить game/saves/persistent
        
    ## Запускать в полноэкранном режиме? True -- да, False -- нет.
    config.default_fullscreen = False

    ## Скорость вывода текста по умолчанию, в знаках в секунду. 0 -- мгновенно.
    config.default_text_cps = 0



## This section contains information about how to build your project into
## distribution files.
init python:

    ## The name that's used for directories and archive files. For example, if
    ## this is 'mygame-1.0', the windows distribution will be in the
    ## directory 'mygame-1.0-win', in the 'mygame-1.0-win.zip' file.
    build.directory_name = "The_Greatest_Adventure-1.0"

    ## The name that's uses for executables - the program that users will run
    ## to start the game. For example, if this is 'mygame', then on Windows,
    ## users can click 'mygame.exe' to start the game.
    build.executable_name = "The_Greatest_Adventure"

    ## If True, Ren'Py will include update information into packages. This
    ## allows the updater to run.
    build.include_update = False

    ## File patterns:
    ##
    ## The following functions take file patterns. File patterns are case-
    ## insensitive, and matched against the path relative to the base
    ## directory, with and without a leading /. If multiple patterns match,
    ## the first is used.
    ##
    ##
    ## In a pattern:
    ##
    ## /
    ##     Is the directory separator.
    ## *
    ##     Matches all characters, except the directory separator.
    ## **
    ##     Matches all characters, including the directory separator.
    ##
    ## For example:
    ##
    ## *.txt
    ##     Matches txt files in the base directory.
    ## game/**.ogg
    ##     Matches ogg files in the game directory or any of its subdirectories.
    ## **.psd
    ##    Matches psd files anywhere in the project.

    ## Classify files as None to exclude them from the built distributions.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)

    ## To archive files, classify them as 'archive'.

    # build.classify('game/**.png', 'archive')
    # build.classify('game/**.jpg', 'archive')

    ## Files matching documentation patterns are duplicated in a mac app
    ## build, so they appear in both the app and the zip file.

    build.documentation('*.html')
    build.documentation('*.txt')
    