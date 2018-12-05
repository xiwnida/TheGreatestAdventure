#=======================Столица. Королевский дворец=================================
label alinor_capital_vorota_dvorca:
    $ location("Alinor", "vorota", "alinor_stolica")
    call location
    call screen alinor_vorota_dvorca
    jump alinor_capital_vorota_dvorca

    label .garden:
        show jack smile at left with dissolve
        j_smile "Сейчас мне незачем возвращаться."
        j_smile "Я приду сюда, когда вернусь из своего путешествия с ягодами юности!"
        hide jack smile with dissolve
        $ no_fade = True
        jump alinor_capital_vorota_dvorca
    label .on_main_street:
        call time1 from _call_time1
        jump alinor_capital_plaza
    jump alinor_capital_vorota_dvorca

   
screen alinor_vorota_dvorca:
    imagemap:
        if day_time=="day":
            ground "Images/Alinor/vorota_day.jpg"
            hover "images/Alinor/vorota1akt.jpg"
        else:
            ground "Images/Alinor/vorota_zakat.jpg"
            hover "images/Alinor/vorota2akt.jpg"
        hotspot (705, 1, 26, 37) clicked Call ("call_menu")
        hotspot (285, 255, 205, 248) clicked Jump ("alinor_capital_vorota_dvorca.garden")
        hotspot (225, 535, 385, 64) clicked Jump ("alinor_capital_vorota_dvorca.on_main_street")
        
#=======================Столица. Главная улица=================================
label alinor_capital_plaza:
    $ location("Alinor", "ul_plaza", "alinor_stolica")
    call location
    $buttons('ul_plaza', 4, ['alinor_capital_plaza' , '.pereulok' , '.to_palace', '.v_bar', '.gostin'])
    call screen imagebutton_example
    jump alinor_capital_plaza
        
    label .pereulok:
        call time1
        jump alinor_capital_pereulok
    label .to_palace:
        call time1
        jump alinor_capital_vorota_dvorca    
    label .v_bar:     #ПРОПИСАТЬ БАР
                          
        jump alinor_capital_pereulok
    label .gostin:     #ПРОПИСАТЬ ГОСТИНИЦУ
                                  
        jump alinor_capital_pereulok
jump alinor_capital_plaza

#=======================Столица. Торговая площадь=================================
label alinor_capital_gorod:
    $ location("Alinor", "ul_gorod", "alinor_stolica")
    call location
    $buttons('ul_gorod', 4, ['alinor_capital_gorod' , '.jack_home_street' , '.pereulok', '.lavka_torgovca', '.vokzal'])
    call screen imagebutton_example
    jump alinor_capital_gorod

    label .jack_home_street:
        call time1
        jump alinor_capital_ul_dom
    label .pereulok:
        call time1
        jump alinor_capital_pereulok
    label .lavka_torgovca:
        jump alinor_capital_lavka_torgovca
    label .vokzal:
        #jump vokzal
jump alinor_capital_gorod
        
#=======================Столица. Улица, на которой дом Джека=================================
label alinor_capital_ul_dom:
    $ location("Alinor", "ul_dom", "alinor_stolica")
    call location
    $buttons('ul_dom', 2, ['alinor_capital_ul_dom' , '.to_jack_home' , '.ploshad'])
    call screen imagebutton_example
    jump alinor_capital_ul_dom
        
        
    label .to_jack_home:
        $ in_home = True
        call time1 from _call_time1_3
        jump alinor_capital_vash_dom
    label .ploshad:
        call time1 from _call_time1_4
        jump alinor_capital_gorod
jump alinor_capital_ul_dom
  
#=======================Столица. Дом Джека=================================
label alinor_capital_vash_dom:
    $ location("Alinor", "dom", "alinor_vash_dom", True)
    call location
    $buttons('dom', 2, ['alinor_capital_vash_dom' , '.dom_spal' , '.ul_dom'])
    call screen imagebutton_example
    jump alinor_capital_vash_dom

    label .dom_spal:
        jump alinor_capital_dom_spal
    label .ul_dom: 
        $ in_home = False
        jump alinor_capital_ul_dom
jump alinor_capital_vash_dom
        
#=======================Столица. Дом Джека. Спальня=================================
label alinor_capital_dom_spal:
    $ location("Alinor", "dom_spal", "alinor_vash_dom", True)
    call location
    $buttons('dom_spal', 2, ['alinor_capital_dom_spal' , '.vash_dom' , '.sleep'])
    call screen imagebutton_example
    jump alinor_capital_dom_spal

    label .vash_dom:
        jump alinor_capital_vash_dom
    label .sleep:
        "Функция не дописана"
        menu:
            "Вы хотите спать до утра?"
            "Да":
                pass
            "Нет":
                $no_fade = True
                jump alinor_capital_dom_spal
        scene black
        $ sutki = 3
        call time2 from _call_time2_8
jump alinor_capital_dom_spal

#=======================Столица. Переулок=================================
label alinor_capital_pereulok:        
    $ location("Alinor", "pereulok", "alinor_stolica")
    call location
    $buttons('pereulok', 3, ['alinor_capital_pereulok' , '.ploshad' , '.glav_ul', '.cerkov'])
    call screen imagebutton_example
    jump alinor_capital_pereulok
        
    label .ploshad:
        call time1
        jump alinor_capital_gorod
    label .glav_ul:
        call time1 
        jump alinor_capital_plaza
    label .cerkov:
        call time1 
        jump alinor_capital_cerkov
jump alinor_capital_pereulok
        
#=======================Столица. Церковь=================================
label alinor_capital_cerkov:
    $ location("Alinor", "cerkov", "alinor_stolica") #Заменить музыку!!!!!!!!!!!!!!!
    call location
    $buttons('cerkov', 3, ['alinor_capital_cerkov' , '.pereulok' , '.v_cerkov', '.les'])
    call screen imagebutton_example
    jump alinor_capital_cerkov

    label .pereulok:
        call time1
        jump alinor_capital_pereulok
    label .v_cerkov:
        "Тут тоже ничего нет"
    label .les:
        "Тут ничего нет"
jump alinor_capital_cerkov
        