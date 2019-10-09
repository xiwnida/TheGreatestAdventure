init python:
    class Chara:
        def __init___(self, type, bigSprite, miniSprite, locationSprite, sysName, wName, role, npcName, playerName):
            #Системное
            self.type = type
            self.sysName = sysName #Системное имя
            
            self.bSprite = bigSprite #Спрайт для досье
            self.mSprite = miniSprite  #Спрайт для списка нпц
            self.lSprite = locationSprite #Спрайт для локаций
            self.wName = wName #Полное имя для досье
            self.role = role  #Род дестельности нпц
            self.reputationLvl = 0
            #Уровни репы: -20-11: не хотел бы с вами встречаться, -10-1: чувствует к вам неприязнь, 0: Не знакомы, 1: слышал о вас, 2-10: знает вас, 11-20: считает вас хорошим знакомым, 21-30: считает вас другом, 31-40: считает вас хорошим другом
            
            
            
            self.npcName = name #Как игрок обращается к персонажу
            self.playerName = playerName #Как персонаж обращается к игроку
            

















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
    label alinor_lavka_torgovca1:
        $ result = renpy.imagemap("Talking/talk_menu.png", "Talking/talk_menuakt.png", [
            (645, 7, 790, 60, "Разговор"),
            (645, 75, 790, 121, "Дела"),
            (645, 135, 790, 185, "Уйти"),
            ])
        if result == "Уйти":
            jump alinor_capital_gorod
        if result == "Дела":
            $ call_shop(amy_shop, weapon=True, food=True)
        if result == "Разговор":
            "Держи одно серебро!"
            $ wallet.addMoney(0, 1, 0)
        jump alinor_lavka_torgovca1
