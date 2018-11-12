#init:
    # Фоны
#    image voknight = "Images/Vok/voknoch.jpg"
#    image vokday = "Images/Vok/vok.jpg"
#    image vokzakat = "Images/Vok/vokzakat.jpg"
    
    # Названия города на стене вокзального помещения
#    image vokname_alinornight = "Images/Vok/alinornoch.png"
#    image vokname_alinor = "Images/Vok/alinor.png"


init python:
    # окно игры в центре экрана
    import os
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    # автоматическое объявление изображений
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['Images/Invent']

    # размеры сетки с инвентарем настраиваются
    columns = 6
    rows = 6
    # размеры иконок в инвентаре
    side = 85

    # сам инвентарь
    inventory = {}
    # текущее положение скролла инвентаря
    from_i = 0

    # получить количество предметов
    def get_count(str):
        s = str.split(":")
        if len(s) > 0:
            return int(s[0])
        return 0
    # получить подсказку по предмету
    def get_hint(str):
        s = str.split(":")
        if len(s) > 1:
            return s[1]
        return ""
    # получить описание предмета
    def get_about(str):
        s = str.split(":")
        if len(s) > 2:
            return s[2]
        return "Описание отсутствует."

    # изменение количества предметов в ячейке на plus единиц
    # если не было, то будут созданы
    # если количество < 1, то удалены вовсе
    def iplus(item_name, plus = 1, hint = None, about = None):
        if plus:
            global inventory
            i = get_count(inventory.get(item_name, "0"))
            if hint == None:
                hint = get_hint(inventory.get(item_name, "0"))
            if about == None:
                about = get_about(inventory.get(item_name, "0"))
            i += plus
            if i < 1:
                # предметы количеством < 1 удаляются из инвентаря
                i = 0
                if item_name in inventory:
                    inventory.pop(item_name)
            else:
                inventory[item_name] = str(i) + ":" + hint + ":" + about
        else:
            # если plus == None, то уничтожаем все единицы предмета
            if item_name in inventory:
                inventory.pop(item_name)
        renpy.restart_interaction()

    # скролл вверх
    class iUp(Action, DictEquality):
        def __call__(self):
            global from_i
            from_i -= columns
            if from_i < 0:
                from_i = 0
            from_i = (from_i / columns) * columns
            renpy.restart_interaction()
        # кликабельность кнопки
        def get_sensitive(self):
            return from_i >= columns
    # скролл вниз
    class iDn(Action, DictEquality):
        def __call__(self):
            global from_i
            from_i += columns
            if from_i < 0:
                from_i = 0
            from_i = (from_i / columns) * columns
            renpy.restart_interaction()
        # кликабельность кнопки
        def get_sensitive(self):
            return from_i + columns * rows < len(inventory)

    # обработчик кликов,
    # чтобы не пихать гору кода в action кнопок
    def iclick(i):
        # например, вызовем окно применения предмета
        renpy.show_screen("scr_use", i)
        renpy.restart_interaction()

    # кнопка применения предмета
    def accept(i):
        # уменьшаем количество предметов на 1
        iplus(inventory.keys()[i], -1)

    # превращаем функции в action
    iClick = renpy.curry(iclick)
    Accept = renpy.curry(accept)

init:
    image empty = Null(side, side)

# необязательное окно прменения предмета
screen scr_use(i):
    modal True
    frame:
        background "#100b"
        align(.5, .5)
        xminimum 500
        has vbox:
            xalign .5
        text " "
        add inventory.keys()[i] xalign .5
        text get_hint(inventory.values()[i]) xalign .5
        text get_about(inventory.values()[i]) xalign .5
        text " "
        hbox:
            xminimum 500
            textbutton "Применить" xalign .5 xminimum 150 action [Hide("scr_use"), Accept(i)]
            textbutton "Отмена"    xalign .5 xminimum 150 action Hide("scr_use")
        text " "

# сам экран инвентаря
screen scr_inventory:
    zorder 111
    default tt = Tooltip(" ")
    #button:
        #align (.95, .05)
        
        #background "#0018" # фон инвентаря
       # action NullAction()
        # заполняем ячейки
    vbox:
            xpos 48 ypos 18
            textbutton _("↑") xminimum side*columns action iUp(): # скролл вверх:
                background "Invent/button1.png"
            for y in range(0, rows):
                hbox:
                    for x in range(0, columns):
                        # индекс ячейки
                        $ i = from_i + x + y * columns
                        # если не за грницами списка предметов
                        if i < len(inventory):
                            button:
                                # размеры предмета
                                minimum (side, side)
                                maximum (side, side)
                                background inventory.keys()[i] # картинка предмета
                                hovered tt.Action(get_hint(inventory.values()[i]))
                                # количество
                                text "{size=16}" + str(get_count(inventory.values()[i])) align(1.0, 1.0)
                                action iClick(i) # действе по клику
                        else:
                            # пустые ячейки
                            button:
                                minimum (side, side)
                                background "empty"
                                text " "
                                action NullAction()
            textbutton _("↓") xminimum side*columns action iDn() # скролл вниз
            text tt.value xalign .5

# чтобы использовать инвентарь нужно только
# доработать под себя фунцию для обработки клика по предмету в инвентаре iclick

    # заполним инвентарь всеми доступными пузырьками в 1 экземпляре
    # покажем экран инвентаря
    # пример изменения инвентаря из скрипта
    # iplus(спрайт, [количество, подсказка, описание])



label invent_prov:
    $ iplus("Images/Invent/pot1 (1).png", 1)
    $ iplus("Images/Invent/pot1 (2).png", 1)
    $ iplus("Images/Invent/pot1 (3).png", 1)
    $ iplus("Images/Invent/pot1 (4).png", 1)
    $ iplus("Images/Invent/pot1 (5).png", 1)
    $ iplus("Images/Invent/pot1 (6).png", 1)
    $ iplus("Images/Invent/pot1 (7).png", 1)
    $ iplus("Images/Invent/pot1 (8).png", 1)
    $ iplus("Images/Invent/pot1 (9).png", 1)
    $ iplus("Images/Invent/pot1 (10).png", 1)
    $ iplus("Images/Invent/pot1 (11).png", 1)
    $ iplus("Images/Invent/pot1 (12).png", 1)
    $ iplus("Images/Invent/pot1 (13).png", 1)
    $ iplus("Images/Invent/pot1 (14).png", 1)
    $ iplus("Images/Invent/pot1 (15).png", 1)
    $ iplus("Images/Invent/pot1 (16).png", 1)
    $ iplus("Images/Invent/pot1 (17).png", 1)
    $ iplus("Images/Invent/pot1 (18).png", 1)
    $ iplus("Images/Invent/pot1 (19).png", 1)
    $ iplus("Images/Invent/pot1 (20).png", 1)
    $ iplus("Images/Invent/pot1 (21).png", 1)
    $ iplus("Images/Invent/pot1 (22).png", 1)
    $ iplus("Images/Invent/pot1 (23).png", 1)
    $ iplus("Images/Invent/pot1 (24).png", 1)
    $ iplus("Images/Invent/pot1 (25).png", 1)
    $ iplus("Images/Invent/pot1 (26).png", 1)
    $ iplus("Images/Invent/pot1 (27).png", 1)
    $ iplus("Images/Invent/pot1 (28).png", 1)
    $ iplus("Images/Invent/pot1 (29).png", 1)
    $ iplus("Images/Invent/pot1 (30).png", 1)
    $ iplus("Images/Invent/pot1 (31).png", 1)
    $ iplus("Images/Invent/pot1 (32).png", 1)
    $ iplus("Images/Invent/pot1 (33).png", 1)
    $ iplus("Images/Invent/pot1 (34).png", 1)
    $ iplus("Images/Invent/pot1 (35).png", 1)
    $ iplus("Images/Invent/pot1 (36).png", 1)
    $ iplus("Images/Invent/pot1 (37).png", 1)
    $ iplus("Images/Invent/pot1 (38).png", 1)
    $ iplus("Images/Invent/pot1 (39).png", 1)
    $ iplus("Images/Invent/pot1 (40).png", 1)
    $ iplus("Images/Invent/pot1 (41).png", 1)
    show screen scr_inventory
label .inventakt:
    $ result = renpy.imagemap("Invent/inventakt.jpg", "Invent/inventakt2.png", [
    (698, 560, 799, 599, "Назад")
    #(167, 39, 446, 34, "Вверх"),
    #(167, 567, 433, 593, "Вниз")
    ])
    
    if result == "Назад":
        return
    #if result == "Вверх":
    #    $iUp()
    #    jump .inventakt
    #if result == "Вниз":
    #    $iDn()
    #    jump .inventakt