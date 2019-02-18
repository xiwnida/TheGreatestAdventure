                                    # Тут будут прописыватся все активные персонажи и диалоги с ними.
init:
    # Диалоговые облачка
    image Amy smoke1 = "Talking/smoke1.png"
    
    
    
                                           #Опустить разговорного меню    
label talk_menu_down:
    show talkmenu with easeintop
    return
    
         
                                           #Поднять разговорное меню
label talk_menu_up:
    hide talkmenu with easeouttop
    return

#====================================ПЕРСОНАЖИ СТОЛИЦЫ АЛИНОРА===========================================
                                    
                                    
                                            #Лавка торговца. Эмили.
    label alinor_lavka_torgovca:
        scene shopper girl 
        show hidmenu
        with dissolve
        call talk_menu_down from _call_talk_menu_down
        show Amy smoke1 with irisin:
            xpos 50 ypos 35
        $ result = renpy.imagemap("Talking/talk_menu.png", "Talking/talk_menuakt.png", [
            (645, 7, 790, 60, "Разговор"),
            (645, 75, 790, 121, "Дела"),
            (645, 135, 790, 185, "Уйти"),
            ])
        if result == "Уйти":
            jump alinor_gorod
