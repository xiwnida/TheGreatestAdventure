init:
    image jack smile_for_blank = "Chara/GG/smile_for_blank.png"

label blank:
    if vzat_blank == False:
        $jack = ['nepon', 'head']
        show Jack with dissolve
        j "А, тот блокнот, в который я записываю свои контракты?"
        j "Так он у меня не с собой, я его оставил дома."
        hide Jack with dissolve
        hide callmenu with easeouttop
        $ no_fade = True
        return
        
    scene blank with fade
label blankakt:    
    $ result = renpy.imagemap("Invent/blank.jpg", "Invent/blankakt.jpg", [
    (696, 557, 799, 599, "В инвентарь"),
    (63, 40, 404, 556, "Контракты")
    ])
    if result == "В инвентарь":
        return
    elif result == "Контракты":
        jump blank_spisok
        
        
        # Тут будут записываться все заключаемые по ходу путешествия контракты.        
label blank_spisok:
    
    
    
    show jack smile_for_blank at right with dissolve
    $jack = ['smile', 'normal']
    j "А больше пока ничего и нет."
    hide jack smile_for_blank with dissolve
jump blankakt


label zametki:
    "Функция не активна"
    return
