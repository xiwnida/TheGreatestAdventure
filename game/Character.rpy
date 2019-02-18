init python:
    class Character:
        def __init___(self, type, bigSprite, miniSprite, locationSprite, wName, role, npcName, playerName, STn2, STn1, ST0, ST1, ST2, ST3, ST4, TSn2, TSn1, TS0, TS1, TS2, TS3, TS4):
            #Системное
            self.type = type
            
            self.bSprite = bigSprite #Спрайт для досье
            self.mSprite = miniSprite  #Спрайт для списка нпц
            self.lSprite = locationSprite #Спрайт для локаций
            self.wName = wName #Полное имя для досье
            self.role = role  #Род дестельности нпц
            self.reputationLvl = 0
            #Уровни репы: -20-11: не хотел бы с вами встречаться, -10-1: чувствует к вам неприязнь, 0: Не знакомы, 1: слышал о вас, 2-10: знает вас, 11-20: считает вас хорошим знакомым, 21-30: считает вас другом, 31-40: считает вас хорошим другом
            
            
            
            self.npcName = name #Как игрок обращается к персонажу
            self.playerName = playerName #Как персонаж обращается к игроку
            
            
            #Реакции на начало разговора. Можно массивом или одной репликой
            self.startTalk_n2 = STn0
            self.startTalk_n1 = STn1
            self.startTalk_0 = ST0
            self.startTalk_1 = ST1
            self.startTalk_2 = ST2
            self.startTalk_3 = ST3
            self.startTalk_4 = ST4
            
            #Реакции на рассказы.
            self.talkStory_n2 = TSn2
            self.talkStory_n1 = TSn1
            self.talkStory_0 = TS0
            self.talkStory_1 = TS1
            self.talkStory_2 = TS2
            self.talkStory_3 = TS3
            self.talkStory_4 = TS4

















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
