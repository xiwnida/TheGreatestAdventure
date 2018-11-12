init:
    image bitem dopusk = "Invent/Bitems/dopusk.png"
    image itemmenu1 = "Invent/itemmenu1.png"
    image bitem train_wife_foto = "Invent/Bitems/foto1.png"

label items_menu1:
    show itemmenu1 at right with easeinright
    return
 
label item_dopusk: # Допуск, данный нам королем.
    show bitem dopusk
    call items_menu1 from _call_items_menu1
    label .akt:
    $ result = renpy.imagemap("Invent/itemmenu1.png", "Invent/Itemmenu1akt.png", [
    (607, 127, 770, 194, "Информация"),
    (607, 224, 770, 291, "Использовать"),
    (607, 321, 770, 388, "Отмена")
    ])
    if result == "Информация":
        show jack smile at left with dissolve
        j_smile "Эту бумагу я получил от короля. Она позволяет мне некие привелегии в моих поисках."
        show jack smeh2 at left
        j_smeh2 "Потрясная вещичка!"
        hide jack with dissolve
        jump .akt
    if result == "Использовать":
        show jack serdit at left with dissolve
        j_serdit "Как мне ее использовать?! Сжечь что ли?" 
        j_serdit "Нетушки!"
        hide jack with dissolve
        jump .akt
    if result == "Отмена":
        hide bitem
        hide itemmenu1 with easeoutright
        jump inventakt
    
label item_train_wife_foto:
    show bitem train_wife_foto
    call items_menu1 from _call_items_menu1_1
    label .akt:
    $ result = renpy.imagemap("Invent/itemmenu1.png", "Invent/Itemmenu1akt.png", [
    (607, 127, 770, 194, "Информация"),
    (607, 224, 770, 291, "Использовать"),
    (607, 321, 770, 388, "Отмена")
    ])
    if result == "Информация":
        show jack smile at left with dissolve
        j_smile "Это фотография Миары - жены поездного проводника."
        j_smile "Я собираюсь отыскать ее, воссоединить семью, а заодно выбить себе бесплатный проезд!"
        hide jack with dissolve
        jump .akt
    if result == "Использовать":
        show jack nepon2 at left with dissolve
        j_nepon2 "Хммммм......."
        show jack duma at left with dissolve
        j_duma "Нет, я ее еще нигде не встречал."
        hide jack with dissolve
        jump .akt
    if result == "Отмена":
        hide bitem
        hide itemmenu1 with easeoutright
        jump inventakt
