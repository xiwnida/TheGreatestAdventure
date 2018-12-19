#=======================Столица. Королевский дворец=================================
label alinor_capital_vorota_dvorca:
    $ location("Alinor", "vorota", "alinor_stolica")
    $ buttons('vorota', 2, ['alinor_capital_vorota_dvorca' , 'alinor_capital_vorota_dvorca.garden' , 'alinor_capital_plaza'])
    jump alinor_capital_vorota_dvorca

    label .garden:
        show jack smile at left with dissolve
        j_smile "Сейчас мне незачем возвращаться."
        j_smile "Я приду сюда, когда вернусь из своего путешествия с ягодами юности!"
        hide jack smile with dissolve
        $ no_fade = True
        jump alinor_capital_vorota_dvorca
    jump alinor_capital_vorota_dvorca
    
#=======================Столица. Главная улица=================================
label alinor_capital_plaza:
    $ location("Alinor", "ul_plaza", "alinor_stolica")
    $ buttons('ul_plaza', 4, ['alinor_capital_plaza' , 'alinor_capital_pereulok' , 'alinor_capital_vorota_dvorca', '.v_bar', '.gostin']) # Прописать бар и гостиницу
jump alinor_capital_plaza

#=======================Столица. Торговая площадь=================================
label alinor_capital_gorod:
    $ location("Alinor", "trading_area", "alinor_stolica")
    #$ buttons('trading_area', 4, ['alinor_capital_gorod' , 'alinor_capital_ul_dom' , 'alinor_capital_pereulok', 'alinor_lavka_torgovca', 'vokzal'])
    $ call_shop(amy_shop, food=True, drop=True, paper=True)
    "[amy_shop.food]"
jump alinor_capital_gorod
        
#=======================Столица. Улица, на которой дом Джека=================================
label alinor_capital_ul_dom:
    $ location("Alinor", "ul_dom", "alinor_stolica")
    $ buttons('ul_dom', 2, ['alinor_capital_ul_dom' , 'alinor_capital_vash_dom' , 'alinor_capital_gorod'])
jump alinor_capital_ul_dom
  
#=======================Столица. Дом Джека=================================
label alinor_capital_vash_dom:
    $ location("Alinor", "dom", "alinor_vash_dom", True)
    $ buttons('dom', 2, ['alinor_capital_vash_dom' , 'alinor_capital_dom_spal' , 'alinor_capital_ul_dom'])
jump alinor_capital_vash_dom
        
#=======================Столица. Дом Джека. Спальня=================================
label alinor_capital_dom_spal:
    $ location("Alinor", "dom_spal", "alinor_vash_dom", True)
    $ buttons('dom_spal', 2, ['alinor_capital_dom_spal' , 'alinor_capital_vash_dom' , 'alinor_capital_dom_spal.sleep'])
    jump alinor_capital_dom_spal
    
    label .sleep:
        "Функция не дописана"
jump alinor_capital_dom_spal

#=======================Столица. Переулок=================================
label alinor_capital_pereulok:        
    $ location("Alinor", "pereulok", "alinor_stolica")
    $ buttons('pereulok', 3, ['alinor_capital_pereulok' , 'alinor_capital_gorod' , 'alinor_capital_plaza', 'alinor_capital_cerkov'])
jump alinor_capital_pereulok
        
#=======================Столица. Церковь=================================
label alinor_capital_cerkov:
    $ location("Alinor", "cerkov", "alinor_stolica") #Заменить музыку!!!!!!!!!!!!!!!
    $ buttons('cerkov', 3, ['alinor_capital_cerkov' , 'alinor_capital_pereulok' , 'alinor_capital_cerkov.v_cerkov', 'alinor_capital_cerkov.les'])
    jump alinor_capital_cerkov
    
    label .v_cerkov:
        "Тут тоже ничего нет"
    label .les:
        "Тут ничего нет"
jump alinor_capital_cerkov
        