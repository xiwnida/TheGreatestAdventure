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
    
label call_inventory:
    call screen inventory_screen
    $ no_fade = True
    jump expression this_location
    
screen enegryScreen:
    bar:
        xpos 10 ypos 3
        if energy > 90:
            left_bar "gui/EnergyBar/1.png"
        elif energy > 80:
            left_bar "gui/EnergyBar/2.png"
        elif energy > 70:
            left_bar "gui/EnergyBar/3.png"
        elif energy > 60:
            left_bar "gui/EnergyBar/4.png"
        elif energy > 50:
            left_bar "gui/EnergyBar/5.png"
        elif energy > 40:
            left_bar "gui/EnergyBar/6.png"
        elif energy > 30:
            left_bar "gui/EnergyBar/7.png"
        elif energy > 20:
            left_bar "gui/EnergyBar/8.png"
        else:
            left_bar "gui/EnergyBar/9.png"
        right_bar "gui/EnergyBar/empty.png"
        thumb_offset 7
        thumb 'Battle/lol.png'
        ymaximum 26
        xmaximum 297 
        value AnimatedValue(value=energy, range=100, delay=0.6) 
        range 100
    text "Энергии: [energy]/100" xalign 0.5 yalign 0.5 xpos 158 ypos 14 size 12 color '#fde7c6' font 'Fonts/comic.ttf'
    
    button:
        background "gui/Wallet/wallet.png"
        focus_mask True
        action NullAction()
        
    $walBronze = wallet.getBronze()
    text "[walBronze]" xalign 1.0 yalign 0.5 xpos 126 ypos 45 size 12 color '#fde7c6' font 'Fonts/comic.ttf'
    
    $walSilver = wallet.getSilver()
    text "[walSilver]" xalign 1.0 yalign 0.5 xpos 91 ypos 45 size 12 color '#fde7c6' font 'Fonts/comic.ttf'
    
    $walGold = wallet.getGold()
    text "[walGold]" xalign 1.0 yalign 0.5 xpos 55 ypos 45 size 12 color '#fde7c6' font 'Fonts/comic.ttf'
