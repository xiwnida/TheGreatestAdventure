init python:
    import random
    import math
    import time
    
    class BattleChara:
        
        def __init__(self, level, name, health_max,strenght, scatter, physical_defense, magical_defense, agility, accuracy, speed, luck, picture, skills):
            self.level=level
            self.name=name
            
            self.health_max=health_max
            self.health=health_max
            
            self.strenght=strenght
            self.domage_scatter=[strenght-scatter, strenght]
            
            self.p_defense=physical_defense
            self.m_defense=magical_defense
            
            self.agility=agility
            self.accuracy=accuracy
            self.speed=speed
            self.luck=luck
            
            self.picture=picture
            
            self.skills=skills
            
        def hit(self):
            hero.health-=2
            
            
            
    hero=BattleChara(1, 'Джек', 10, 2, 1, 1, 0, 2, 0, 2, 1, 'Battle/GG/norm.png', [])
    alinor_rat=BattleChara(1, 'Драная крыса', 10, 1, 0, 1, 0, 5, 0, 5, 2, 'Battle/Enemies/alinor_rat.png', [])
    
#===================Скиллы Джека======================
    def DefenseStance(hero, enemy): #Защитная стойка. Увеличивает защиту на 30%
        global battle_p_defense
        battle_p_defense=hero.p_defense+int(math.ceil(hero.p_defense*0.3))
        renpy.restart_interaction()
    
    def Dogfight(hero, enemy):   #Обычный удар кулаком
        battle_domage=random.randint(hero.domage_scatter[0], hero.domage_scatter[1])
        if hero.strenght>=enemy.p_defense:
            bonus_domage=float(hero.strenght)/float(enemy.p_defense)/float(10)*float(battle_domage)
            all_domage=battle_domage+int(bonus_domage)
        elif hero.strenght<enemy.p_defense:
            bonus_domage=float(enemy.p_defense)/float(hero.strenght)/float(10)*float(battle_domage)
            renpy.notify(bonus_domage)
            all_domage=battle_domage-int(round(bonus_domage))
            if all_domage<=0:
                all_domage=1
        
        enemy.health-=all_domage
        renpy.show_screen('EnemyTurnScreen')
        renpy.restart_interaction()
       
        
        
        
        
        
        
        
        
        
        
        

        
    def EnemyTurn(enemy):
        global battle_first_hit
        battle_first_hit=True
        hero.health-=random.randint(enemy.domage_scatter[0], enemy.domage_scatter[1])
        renpy.hide_screen('EnemyTurnScreen')
        renpy.restart_interaction()
         
    EnemyTurn=renpy.curry(EnemyTurn)  
    Dogfight=renpy.curry(Dogfight)  
    DefenseStance=renpy.curry(DefenseStance)
    
#Переменные
    battle_first_hit=False

    enemy=''  #Хранит имя врага
    adrenalin=0  #Количество адреналина
    battle_choice=''  #Хранит выбранную кнопку из первой вкладки
    battle_skill_chioce='' #Хранит выбранный скилл
    battle_skill_call='' #Хранит функцию для вызова нужного скилла
    battle_skills_list=0
    
    battle_p_defense=hero.p_defense
    battle_agility=hero.agility
    
    
#====Описания скиллов====
    #Кулачный урон
    dogfight="Удар кулаком.\nНаносит "+str(hero.domage_scatter[0])+"-"+str(hero.domage_scatter[1])+" урона."

    #Защитная стойка
    defense_stance ="Джек примет защитную стойку.\nФизическая защита + "+str(int(math.ceil(hero.p_defense*0.3)))
    
    
    
    
screen Battle_window:
    zorder 50
    button:
        background 'Battle/down.png'
        action NullAction()
        
    button:
        background hero.picture
        action NullAction()
        
    button:
        background getattr(enemy, 'picture')
        action NullAction()
        
    bar:
        xpos 22 ypos 38
        left_bar "Battle/hp_full.png"
        right_bar "Battle/hp_empty.png"
        thumb_offset 7
        thumb 'Battle/lol.png'
        ymaximum 26
        xmaximum 297 
        value AnimatedValue(value=hero.health, range=hero.health_max, delay=0.6) 
        range hero.health_max
    text "[hero.health]/[hero.health_max]" xalign 0.5 yalign 0.5 xpos 170 ypos 49 size 12 color '#fde7c6' font 'Fonts/comic.ttf'
    
    bar:
        xpos 479 ypos 38
        left_bar "Battle/hp_full.png"
        right_bar "Battle/hp_empty.png"
        thumb_offset 7
        thumb 'Battle/lol.png'
        ymaximum 26
        xmaximum 297 
        value AnimatedValue(value=getattr(enemy, 'health'), range=getattr(enemy, 'health_max'), delay=0.6) 
        range getattr(enemy, 'health_max')
    $var1=getattr(enemy, 'health')
    $var2=getattr(enemy, 'health_max')
    text "[var1]/[var2]" xalign 0.5 yalign 0.5 xpos 627 ypos 49 size 12 color '#fde7c6' font 'Fonts/comic.ttf'
    
    bar:
        xpos 147 ypos 3
        left_bar "Battle/adren_full.png"
        right_bar "Battle/adren_empty.png"
        thumb_offset 7
        thumb 'Battle/lol.png'
        ymaximum 31
        xmaximum 507
        value AnimatedValue(value=adrenalin, range=100, delay=0.6) 
        range 100
    text "[adrenalin]/100" xalign 0.5 yalign 0.5 xpos 400 ypos 18 size 10 color '#fde7c6' font 'Fonts/comic.ttf'
    
    $var3=getattr(enemy, 'name')
    text ("{color=#fde7c6}{font=Fonts/DS_Goose.ttf}[var3]{/font}{/color}") xpos 626 ypos 90 xanchor 0.5 yanchor 0.5 size 18
    
    imagebutton:
        idle 'Battle/1_hit.png'
        hover 'Battle/1_hit_h.png'
        focus_mask True
        action [SetVariable('battle_choice', 'hit'), SetVariable('battle_skill_chioce', '')]
        
    imagebutton:
        idle 'Battle/1_skill.png'
        hover 'Battle/1_skill_h.png'
        focus_mask True
        action SetVariable('battle_choice', 'skill')
        
    imagebutton:
        idle 'Battle/1_item.png'
        hover 'Battle/1_item_h.png'
        focus_mask True
        action [SetVariable('battle_choice', 'item'), SetVariable('battle_skill_chioce', '')]
        
    imagebutton:
        idle 'Battle/1_run.png'
        hover 'Battle/1_run_h.png'
        focus_mask True
        action [SetVariable('battle_choice', 'run'), SetVariable('battle_skill_chioce', '')]
       
    if battle_choice=='hit':
        text '[dogfight]' xpos 434 ypos 454 size 14 color '#fde7c6' font 'Fonts/comic.ttf'
        imagebutton:
            idle 'Battle/use.png'
            hover 'Battle/use_h.png'
            focus_mask True
            action Dogfight(hero, enemy)
            
    if battle_choice=='skill':
        vbox:
            xpos 161 ypos 461
            for i in range(4):
                if i+battle_skills_list<len(hero.skills):
                    imagebutton:
                        idle 'Battle/Skills/'+hero.skills[i][1]+'.png'
                        hover 'Battle/Skills/'+hero.skills[i][1]+'_h.png'
                        action [SetVariable('battle_skill_chioce', hero.skills[i][2]), SetVariable('battle_skill_call', hero.skills[i][0])]
                        
        if battle_skill_chioce:
            text '[battle_skill_chioce]' xpos 434 ypos 454 size 14 color '#fde7c6' font 'Fonts/comic.ttf'
            
            imagebutton:
                idle 'Battle/use.png'
                hover 'Battle/use_h.png'
                focus_mask True
                action battle_skill_call(hero, enemy)
                
    if battle_first_hit==False:
        if hero.speed<enemy.speed:
            imagebutton at battle_dissolve:
                idle 'Battle/attack.png'
                action EnemyTurn(enemy)
            
       
                
screen EnemyTurnScreen:
    zorder 51
    modal True
    imagebutton at battle_dissolve:
        idle 'Battle/attack.png'
        action EnemyTurn(enemy)
        
