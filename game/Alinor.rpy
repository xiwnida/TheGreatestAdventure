label for_skip_ALINOR:#=======================ВСЕ ГОРОДА И МЕСТА ОСТРОВА АЛИНОРА=================================

    label for_skip_ALINOR_STOLICA:#=======================СТОЛИЦА АЛИНОРА=================================
        #=======================Столица. Королевский дворец=================================
            label alinor_capital_palaceGate:
                $ location("alinor_capital_palaceGate", "alinor_stolica")
                $ buttons(['alinor_capital_garden' , 'alinor_capital_plaza'])
                jump alinor_capital_palaceGate
            
            label alinor_capital_garden:
                $jack = ['smile', 'normal']
                show Jack at left with dissolve
                j "Сейчас мне незачем возвращаться."
                j "Я приду сюда, когда вернусь из своего путешествия с ягодами юности!"
                hide Jack with dissolve
                $ no_fade = True
                jump alinor_capital_palaceGate
                
        #=======================Столица. Главная улица=================================
            label alinor_capital_plaza:
                $ location("alinor_capital_plaza", "alinor_stolica")
                #$ buttons('ul_plaza', ["alinor_capital_pereulok" , 'alinor_capital_vorota_dvorca', 'alinor_capital_bar', 'alinor_capital_gostin']) # Прописать бар и гостиницу
                $ buttons(['alinor_capital_pereulok' , 'alinor_capital_palaceGate'])
                jump alinor_capital_plaza
            
        #=======================Столица. Торговая площадь=================================
            label alinor_capital_tradingArea:
                $ EverydayRandom()
                $ location("alinor_capital_tradingArea", "alinor_stolica")
                #$ buttons('trading_area', ['alinor_capital_ul_dom' , 'alinor_capital_pereulok', 'alinor_lavka_torgovca', 'alinor_vokzal'])
                $ buttons(['alinor_capital_streetHome' , 'alinor_capital_pereulok', 'alinor_capital_lavkaTorgovca'])
                jump alinor_capital_tradingArea
                    
        #=======================Столица. Улица, на которой дом Джека=================================
            label alinor_capital_streetHome:
                $ location("alinor_capital_streetHome", "alinor_stolica")
                $ buttons(['alinor_capital_jackHome' , 'alinor_capital_tradingArea'])
                jump alinor_capital_streetHome
              
        #=======================Столица. Дом Джека=================================
            label alinor_capital_jackHome:
                $ location("alinor_capital_jackHome", "alinor_vash_dom", True)
                $ buttons(['alinor_capital_jackBedroom' , 'alinor_capital_streetHome'], True)
                jump alinor_capital_jackHome
                    
        #=======================Столица. Дом Джека. Спальня=================================
            label alinor_capital_jackBedroom:
                $ location("alinor_capital_jackBedroom", "alinor_vash_dom", True)
                $ buttons(['alinor_capital_jackHome' , 'alinor_capital_jackBedroom.sleep'], True)
                jump alinor_capital_jackBedroom
                
                label .sleep:
                    "Функция не дописана"
                    
                jump alinor_capital_jackBedroom
            
        #=======================Столица. Переулок=================================
            label alinor_capital_pereulok:        
                $ location("alinor_capital_pereulok", "alinor_stolica")
                $ buttons(['alinor_capital_tradingArea' , 'alinor_capital_plaza', 'alinor_capital_cerkov'])
                jump alinor_capital_pereulok
                    
        #=======================Столица. Церковь=================================
            label alinor_capital_cerkov:
                $ location("alinor_capital_cerkov", "alinor_stolica") #Заменить музыку!!!!!!!!!!!!!!!
                $ buttons(['alinor_capital_pereulok' , 'alinor_capital_cerkov.vCerkov', 'alinor_capital_cerkov.les'])
                jump alinor_capital_cerkov
                
                label .vCerkov:
                    "Тут тоже ничего нет"
                label .les:
                    "Тут ничего нет"
                    
                jump alinor_capital_cerkov
                    