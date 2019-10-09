#Полезные блоки
label call_menu:   # Блок выдвигающегося меню
    show callmenu with easeintop
label call_menu1:
    $ result = renpy.imagemap("Talking/menu.png", "Talking/menuakt.png", [
    (645, 8, 790, 59, "Рюкзак"),
    (645, 70, 790, 121, "Карта"),
    (645, 135, 790, 185, "Кошель"),
    (645, 198, 790, 249, "Блокнот"),
    (645, 259, 790, 312, "Календарь"),
    (645, 323, 790, 375, "Мысли"),
    (705, 380, 731, 413, "Назад")
    ])
    if result == "Рюкзак":
        call screen inventory_screen
        $ no_fade = True
        return
    elif result == "Карта":
        call karta from _call_karta
        return
    elif result == "Кошель":
        call money from _call_money
        return
    elif result == "Блокнот":
        call blank from _call_blank
        return
    elif result == "Календарь":
        call calendar from _call_calendar
        return
    #if result == "Мысли":
        #call misli
    elif result == "Назад":
        $ no_fade = True
        hide callmenu with easeouttop
        return
jump call_menu

#Чтобы закрыть экран

label closeScreen:
    hide screen screen_name_to_hide
    return
