init:
    #================Переменные================
    $icon_sword=False
    $icon_ring=False
    $icon_bottle=False
    $icon_bread=False
    $icon_bone=False
    $icon_paper=False
    
    $shop_buy=True
    $shop_sell=False

    $shop_item_quantity=1 #Переменная для функции, позволяющий купить больше одного предмета
    
    $shop_Y=[117, 117, 154, 154, 191, 191,  228, 228, 265, 265, 302, 302, 339, 339] #Координаты для создания сетки предметов
    $shop_X=0
    
    $shop_item_exist=0
    
    $shop_item_select=False #Чтобы определить, выбран ли предмет
    $shop_item_select_X=0
    $shop_item_select_Y=0
    $positions=[111, 148, 185, 222, 259, 296, 333]
    
    $shop_name=''
    $shop_items=[]
    
    $shop_i_plus=0 #Чтобы порядок предметов шел правильно
    
    $shop_item_name=''
    $shop_item_number=0
    $shop_item_description=''
    $shop_item_effect=''
    $shop_item_icon=''
    

screen game_shop:
    if shop_buy:
        button:
            background 'Shop/ground_buy.jpg'
            action NullAction()
    if shop_sell:
        button:
            background 'Shop/ground_sell.jpg'
            action NullAction()
        
    imagebutton:
        idle 'Shop/cross.png'
        hover 'Shop/cross_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Shop/pointer_up.png'
        hover'Shop/pointer_up_hover.png'
        focus_mask True
        action NullAction()
    
    imagebutton:
        idle 'Shop/pointer_down.png'
        hover'Shop/pointer_down_hover.png'
        focus_mask True
        action NullAction()
    if shop_buy:
        imagebutton:
            idle 'Shop/item_buy.png'
            hover 'Shop/item_buy_hover.png'
            focus_mask True
            action NullAction()
    if shop_sell:
        imagebutton:
            idle 'Shop/item_sell.png'
            hover 'Shop/item_sell_hover.png'
            focus_mask True
            action NullAction()
            
    imagebutton:
        idle 'Shop/item_quantity.png'
        focus_mask True
        action NullAction()
        
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[shop_item_quantity]{/font}{/color}{/size}") xpos 770 ypos 562 xanchor 0.5 yanchor 0.5
        
    imagebutton:
        idle 'Shop/item_pointer_up.png'
        hover'Shop/item_pointer_up_hover.png'
        focus_mask True
        action shop_plus()  #Написать функцию, чтобы нельзя было поставить значение меньше одного и больше существующего
        
    imagebutton:
        idle 'Shop/item_pointer_down.png'
        hover'Shop/item_pointer_down_hover.png'
        focus_mask True
        action shop_minus()
        
    imagebutton:
        xpos 31 ypos 67
        idle 'Shop/buy.png'
        action [SetVariable('shop_buy',True),SetVariable('shop_sell',False)]
        
    imagebutton:
        xpos 166 ypos 67
        idle 'Shop/sell.png'
        action [SetVariable('shop_buy',False),SetVariable('shop_sell',True)]
        
    text ("{color=#fde7c6}{font=Fonts/DS_Goose.ttf}[shop_name]{/font}{/color}") xpos 506 ypos 33 xanchor 0.5 yanchor 0.5
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[money_gold]{/font}{/color}{/size}") xpos 772 ypos 109 xanchor 1.0
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[money_silver]{/font}{/color}{/size}") xpos 772 ypos 145 xanchor 1.0
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[money_bronz]{/font}{/color}{/size}") xpos 772 ypos 179 xanchor 1.0
    
    hbox:
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_sword.png'
            selected_idle 'Shop/icon_sword_hover.png'
            selected_hover 'Shop/icon_sword_hover.png'
            action [SelectedIf(icon_sword), SetVariable('icon_sword',True), SetVariable('icon_ring',False), SetVariable('icon_bottle',False), SetVariable('icon_bread',False), SetVariable('icon_bone',False),  SetVariable('icon_paper',False)]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_ring.png'
            selected_idle 'Shop/icon_ring_hover.png'
            selected_hover 'Shop/icon_ring_hover.png'
            action [SelectedIf(icon_ring), SetVariable('icon_sword',False), SetVariable('icon_ring',True), SetVariable('icon_bottle',False), SetVariable('icon_bread',False), SetVariable('icon_bone',False),  SetVariable('icon_paper',False)]
           
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_bottle.png'
            selected_idle 'Shop/icon_bottle_hover.png'
            selected_hover 'Shop/icon_bottle_hover.png'
            action [SelectedIf(icon_bottle), SetVariable('icon_sword',False), SetVariable('icon_ring',False), SetVariable('icon_bottle',True), SetVariable('icon_bread',False), SetVariable('icon_bone',False),  SetVariable('icon_paper',False)]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_bread.png'
            selected_idle 'Shop/icon_bread_hover.png'
            selected_hover 'Shop/icon_bread_hover.png'
            action [SelectedIf(icon_bread), SetVariable('icon_sword',False), SetVariable('icon_ring',False), SetVariable('icon_bottle',False), SetVariable('icon_bread',True), SetVariable('icon_bone',False),  SetVariable('icon_paper',False)]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_bone.png'
            selected_idle 'Shop/icon_bone_hover.png'
            selected_hover 'Shop/icon_bone_hover.png'
            action [SelectedIf(icon_bone), SetVariable('icon_sword',False), SetVariable('icon_ring',False), SetVariable('icon_bottle',False), SetVariable('icon_bread',False), SetVariable('icon_bone',True),  SetVariable('icon_paper',False)]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_paper.png'
            selected_idle 'Shop/icon_paper_hover.png'
            selected_hover 'Shop/icon_paper_hover.png'
            action [SelectedIf(icon_paper), SetVariable('icon_sword',False), SetVariable('icon_ring',False), SetVariable('icon_bottle',False), SetVariable('icon_bread',False), SetVariable('icon_bone',False),  SetVariable('icon_paper',True)]
            
            
    for i in range(14):
        if i<len(shop_items):
            if i%2==0:
                $shop_X=20
            else:
                $shop_X=368
            $shop_item_idenfity(i)
            imagebutton:
                xpos shop_X ypos shop_Y[i]-6
                idle shop_item_icon
                action NullAction()
                    
            text "{size=16}{color=#432e25}{font=Fonts/comic.ttf}[shop_item_name]{/color}{/font}{/size}" xpos shop_X+31 ypos shop_Y[i]+2
            text "{size=20}{color=#432e25}{font=Fonts/comic.ttf}[shop_item_number]{/color}{/font}{/size}" xpos shop_X+330 ypos shop_Y[i]-3 xanchor 1.0
        
            imagebutton:
                xpos shop_X ypos shop_Y[i]-6
                idle 'Shop/item_choice.png'
                selected_idle 'Shop/item_choice_hover.png'
                selected_hover 'Shop/item_choice_hover.png'
                action [SelectedIf(shop_item_select==i+1), shop_item_position(i)]
                
    imagebutton:
        xpos 25 ypos 457
        idle 'Items/Amy_cake.png'
        action NullAction()
        
    text "{color=#fde7c6}{font=Fonts/DS_goose.ttf}[amy_cake.name]{/color}{/font}" xpos 203 ypos 426 xanchor 0.5 yanchor 0.5
    text "{size=16}{color=#fde7c6}{font=Fonts/DS_goose.ttf}[amy_cake.description]{/color}{/font}{/size}" xpos 165 ypos 465
    
    
label lololo:
    "Бу"
