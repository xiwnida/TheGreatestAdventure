init python:
        class Case:
            def __init__(self, caseName, caseText):
                self.caseName = caseName
                self.caseText = caseText
         
                
                
        caseOne = Case(
            caseName = "Пропавшая жена машиниста поезда",
            caseText = "Машанист поезда попросил вас отыскать его безвести пропавшую жену по имени Миара. Женщина пропала, когда приехала сюда со своим мужем из Вейлена - соседней страны, и отправилась прогуляться по столице.\n\nВ наличии фотография ее внешности.")
        
        caseTwo = Case(
            caseName = "Украденый мяч девочки из торговой лавки",
            caseText = "Эми - девочка из торговой лавки сладостями на площади - попросила найти ее мяч.\nПо ее словам, мяч забрал мальчишка с соседней улицы.")
        
        
init:
    $ caseList = [caseOne, caseTwo]
    $ caseScreenChosenCase = "" # Запоминает, какое дело выбрано в списке и выводит его текст
    $ chosen_case = ""
        
        
screen case_screen:
    $ slide = 1 #Ставит подложки через одну
    
    button:
        background "Case/case_list2.png"
        action NullAction()
    button:
        background "Case/text_field.png"
        action NullAction()
    if caseScreenChosenCase:
        imagebutton:
            idle "Case/ask.png"
            hover "Case/askakt.png"
            focus_mask True
            action [SetVariable('caseScreenChosenCase', ""), SetVariable("chosen_case", caseScreenChosenCase.caseName), Return()]
        
    vpgrid:
        rows len(caseList)
        xpos 390 ypos 58 xysize(398, 373)
        mousewheel True
        arrowkeys True
        for i in caseList:
            frame:
                top_padding 0
                left_padding 0
                xysize(382, 37)
                if slide == 1:
                    background "Case/slide.png"
                    $slide = 2
                elif slide == 2:
                    background "Case/substrate.png"
                    $slide = 1
                
                imagebutton:
                    idle "Case/slide.png"
                    selected_idle "Case/chosen.png"
                    selected_hover "Case/chosen.png"
                    action  [SelectedIf(caseScreenChosenCase==i), SetVariable('caseScreenChosenCase', i)]
                    
                    
                text "{color=#000000}{size=15}{font=fonts/constan.ttf}[i.caseName]{/font}{/size}{/color}" xalign 0.5 yalign 0.5 text_align 0.5 yanchor 0.3
             
                
    imagebutton:
        xpos 648 ypos 17
        idle "Case/back.png"
        hover "Case/backakt.png"
        action Jump ("talk_menu_label")
        
    if caseScreenChosenCase:
        frame:
            xysize(763, 140)
            background "Case/slide.png"
            text "{color=#fde7c6}{size=18}{font=fonts/constan.ttf}[caseScreenChosenCase.caseText]{/font}{/size}{/color}" xpos 35 ypos 455
            
            
            
            
            
            
label jack_cases_questions:#==========================КВЕСТЫ АЛИНОРА===============================
        hide Menu
        call screen case_screen
        if chosen_case == "Пропавшая жена машиниста поезда":
            "Вы показываете фотографию женщины, которую получили от машиниста."
    
        return
