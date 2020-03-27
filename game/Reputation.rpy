init:
    $npc_list = [ ]
    
    $leftDark = False
    $rightDark = False #Для затемнения при вызове выбора места
    
    $repCountry = "" #Чтобы фильтровать список нпц
    $repCity = ""
    
    $repCountries = []
    $repCities = []
    
    
label callReputation:
    $repCountry = strana
    $repCity = city
    call screen Reputation
    $ no_fade = True
    jump expression this_location
    
label repJump(npc, repText):
    call screen about_one(npc, repText)
    call screen Reputation

screen Reputation:
    add "Reputation/bg.jpg"
    
    add "Reputation/left_box.png"
    add "Reputation/right_box.png"
    
    text repCountry xpos 240 ypos 57 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
    text repCity xpos 549 ypos 57 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
    
    imagebutton:
        idle 'Reputation/cross.png'
        hover 'Reputation/cross_hover.png'
        focus_mask True
        action Return()
    
    imagebutton:
        idle "Reputation/left_button.png"
        hover"Reputation/left_button_hover.png"
        focus_mask True
        action SetVariable("leftDark", True)
        
    imagebutton:
        idle "Reputation/right_button.png"
        hover"Reputation/right_button_hover.png"
        focus_mask True
        action SetVariable("rightDark", True)
        
    vpgrid:
        rows len(npc_list)
        xpos 14 ypos 126 xysize(774, 460)
        mousewheel True
        arrowkeys True
        cols 2
        for npc in npc_list:
            if npc[1] == repCountry and npc[2] == repCity:
                frame:
                    xysize(393, 118)
                    background "Reputation/chara_box.png"
                    add npc[0].mSprite ypos -1
                    text npc[0].name xpos 112 ypos 10 size 14 color "#000000" font "Fonts/comic.ttf"
                    text npc[0].des xpos 112 ypos 35 size 12 color "#000000" font "Fonts/comic.ttf"
                    
                    if npc[0].reputation < -10:
                        $repColor = "rep_red"
                        $repText = "Крайне негативное"
                    elif npc[0].reputation < 0:
                        $repColor = "rep_yellow"
                        $repText = "Негативное"
                    elif npc[0].reputation == 0:
                        $repColor = "rep_gray"
                        $repText = "Не знакомы"
                    elif npc[0].reputation < 11:
                        $repColor = "rep_lightblue"
                        $repText = "Нейтральное"
                    elif npc[0].reputation < 21:
                        $repColor = "rep_blue"
                        $repText = "Позитивное"
                    elif npc[0].reputation < 31:
                        $repColor = "rep_lightgreen"
                        $repText = "Дружеское"
                    else:
                        $repColor = "rep_green"
                        $repText = "Максимальное доверие"
                        
                    add "Reputation/"+str(repColor)+".png" xpos 0 ypos 0 
                    $var5 = repText.lower()
                    text "Отношение: [var5]" xpos 114 ypos 70 size 12 color "#000000" font "Fonts/comic.ttf"
                    
                    imagebutton:
                        idle "Reputation/chara_empty.png"
                        hover "Reputation/chara_empty.png"
                        action Call("repJump", npc[0], repText)
                
    if leftDark or rightDark:
        add "Reputation/bg.jpg"
        
        if leftDark:
            add "Reputation/right_box.png"
            add "Reputation/right_button.png"
            text repCity xpos 549 ypos 57 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
            add "Reputation/left_box_shadow.png"
            add "Reputation/left_button.png"
            text repCountry xpos 240 ypos 57 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
            
        elif rightDark:
            add "Reputation/left_box.png"
            add "Reputation/left_button.png"
            text repCountry xpos 240 ypos 57 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
            add "Reputation/right_box_shadow.png"
            add "Reputation/right_button.png"
            text repCity xpos 549 ypos 57 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
            
        add "Reputation/choice_box.png"
        
        imagebutton:
            idle "Reputation/back.png"
            hover "Reputation/back_hover.png"
            focus_mask True
            action [SetVariable("leftDark", False), SetVariable("rightDark", False)]
        
        vpgrid:
            if leftDark:
                rows len(repCountries)
            if rightDark:
                rows len(repCities)
            xpos 219 ypos 151 xysize (328, 336)
            if leftDark:
                for country in repCountries:
                    frame:
                        xpos -6
                        xysize(328, 56)
                        background "Reputation/lol.png"
                        imagebutton:
                            idle "Reputation/choice_name_box.png"
                            hover "Reputation/choice_name_box.png"
                            action [SetVariable("repCountry", country), SetVariable("repCity", setCity(country)), SetVariable('leftDark', False)]
                            
                        text country xpos 164 ypos 22 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
                        
            if rightDark:
                for place in repCities:
                    if place[0] == repCountry:
                        frame:
                            xpos -6
                            xysize(328, 56)
                            background "Reputation/lol.png"
                            imagebutton:
                                idle "Reputation/choice_name_box.png"
                                hover "Reputation/choice_name_box.png"
                                action [SetVariable("repCity", place[1]), SetVariable('rightDark', False)]
                                
                            text place[1] xpos 164 ypos 22 xanchor 0.5 yanchor 0.5 color "#000000" font "Fonts/comic.ttf"
            
                
                            
screen about_one(npc, repText):
    add "Reputation/bg.jpg"
    add "Reputation/about.png"
    
    imagebutton:
        idle 'Reputation/cross.png'
        hover 'Reputation/cross_hover.png'
        focus_mask True
        action Return()
    
    add npc.bSprite
    
    text npc.name xpos 518 ypos 98 xanchor 0.5 yanchor 0.5 size 16 color "#000000" font "Fonts/comic.ttf"
    text "[npc.des]." xpos 448 ypos 143 yanchor 1.0 size 12 color "#000000" font "Fonts/comic.ttf"
    text str(repCountry) +" - "+ str(repCity)+"." xpos 454 ypos 172  yanchor 1.0 size 12 color "#000000" font "Fonts/comic.ttf"
    text "[repText]." xpos 405 ypos 200  yanchor 1.0 size 12 color "#000000" font "Fonts/comic.ttf"
    
    if not npc.info:
        text "Пусто." xpos 319 ypos 310 size 12 color "#000000" font "Fonts/comic.ttf"
    else:
        frame:
            xpos 303 ypos 296 xysize(427, 214)
            background "Reputation/lol.png"
            vbox:
                hbox:
                    viewport id "box":
                        xmaximum 0.95
                        mousewheel True
                        draggable True
                        vbox:
                            spacing 8 # отступы между абзацами
                            for i in npc.info:
                                text i size 12 color "#000000" font "Fonts/comic.ttf"

                
