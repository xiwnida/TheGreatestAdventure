label for_skip_ALINOR:#=======================ВСЕ ГОРОДА И МЕСТА ОСТРОВА АЛИНОРА=================================

    label for_skip_ALINOR_STOLICA:#=======================СТОЛИЦА АЛИНОРА=================================
        #=======================Столица. Королевский дворец=================================
            label alinor_capital_vorota_dvorca:
                $ location("alinor_capital_vorota_dvorca", "Alinor", "vorota", "alinor_stolica")
                $ buttons('vorota', ['alinor_capital_vorota_dvorca.garden' , 'alinor_capital_plaza'])
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
                $ location("alinor_capital_plaza", "Alinor", "ul_plaza", "alinor_stolica")
                #$ buttons('ul_plaza', ["alinor_capital_pereulok" , 'alinor_capital_vorota_dvorca', '.v_bar', '.gostin']) # Прописать бар и гостиницу
                $ buttons('ul_plaza', ['alinor_capital_pereulok' , 'alinor_capital_vorota_dvorca'])
                jump alinor_capital_plaza
            
        #=======================Столица. Торговая площадь=================================
            label alinor_capital_gorod:
                $ EverydayRandom()
                $ location("alinor_capital_gorod", "Alinor", "trading_area", "alinor_stolica")
                #$ buttons('trading_area', ['alinor_capital_ul_dom' , 'alinor_capital_pereulok', 'alinor_lavka_torgovca', 'vokzal'])
                $ buttons('trading_area', ['alinor_capital_ul_dom' , 'alinor_capital_pereulok', 'alinor_lavka_torgovca'])
                jump alinor_capital_gorod
                    
        #=======================Столица. Улица, на которой дом Джека=================================
            label alinor_capital_ul_dom:
                $ location("alinor_capital_ul_dom", "Alinor", "ul_dom", "alinor_stolica")
                $ buttons('ul_dom', ['alinor_capital_vash_dom' , 'alinor_capital_gorod'])
                jump alinor_capital_ul_dom
              
        #=======================Столица. Дом Джека=================================
            label alinor_capital_vash_dom:
                $ location("alinor_capital_vash_dom", "Alinor", "dom", "alinor_vash_dom", True)
                $ buttons('dom', ['alinor_capital_dom_spal' , 'alinor_capital_ul_dom'], True)
                jump alinor_capital_vash_dom
                    
        #=======================Столица. Дом Джека. Спальня=================================
            label alinor_capital_dom_spal:
                $ location("alinor_capital_dom_spal", "Alinor", "dom_spal", "alinor_vash_dom", True)
                $ buttons('dom_spal', ['alinor_capital_vash_dom' , 'alinor_capital_dom_spal.sleep'], True)
                jump alinor_capital_dom_spal
                
                label .sleep:
                    "Функция не дописана"
                    
                jump alinor_capital_dom_spal
            
        #=======================Столица. Переулок=================================
            label alinor_capital_pereulok:        
                $ location("alinor_capital_pereulok", "Alinor", "pereulok", "alinor_stolica")
                $ buttons('pereulok', ['alinor_capital_gorod' , 'alinor_capital_plaza', 'alinor_capital_cerkov'])
                jump alinor_capital_pereulok
                    
        #=======================Столица. Церковь=================================
            label alinor_capital_cerkov:
                $ location("alinor_capital_cerkov", "Alinor", "cerkov", "alinor_stolica") #Заменить музыку!!!!!!!!!!!!!!!
                $ buttons('cerkov', ['alinor_capital_pereulok' , 'alinor_capital_cerkov.v_cerkov', 'alinor_capital_cerkov.les'])
                jump alinor_capital_cerkov
                
                label .v_cerkov:
                    "Тут тоже ничего нет"
                label .les:
                    "Тут ничего нет"
                    
                jump alinor_capital_cerkov
                    