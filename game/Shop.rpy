init:
    #================Переменные================
    $shop_active_mode=''       #Для выделения одной из иконок режимов
    
    $shop_buy=True                #Управление покупкой/продажей
    $shop_sell=False

    $shop_item_quantity=''       #Переменная для функции, позволяющий купить больше одного предмета
    
    $shop_item_select=False  #Чтобы определить, выбран ли предмет
    
    $shop_name=''                   #Хранит системное название активного магазина
    $can_buy = False               #Позволяет или не позволяет нажать на кнопку покупки
    
    $ selected_item = ""
    

screen game_shop:
    $ shop_slide = 0 #Отвечает за черные и белые полосы под предметами
    
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
        action [SetVariable("screen_name_to_hide", "game_shop"), SetVariable('selected_item',''), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", ""), SetVariable('shop_buy', True), SetVariable('shop_sell', False), Call("closeScreen")]
    
#Установка цен и блокрование\разблокирование кнопки покупки
    $ shop_price(shop_name, selected_item, shop_item_quantity)
    if shop_buy:
        if wallet.money < shop_name.itemPrice:
            imagebutton:
                idle 'Shop/red_pay.png'
                focus_mask True
                action None
            $ can_buy = False
        elif not shop_name.itemPrice:
            $can_buy = False
        else:
            imagebutton:
                idle 'Shop/green_pay.png'
                focus_mask True
                action None
            $ can_buy = True    
    
    
#Кнопки покупки\продажи и количества=======
    if shop_item_quantity:
        if shop_buy:
            imagebutton:
                idle 'Shop/item_buy.png'
                hover 'Shop/item_buy_hover.png'
                focus_mask True
                action [SensitiveIf(can_buy), SetVariable("shop_item_quantity", 1), shop_buy_item(selected_item[0], shop_item_quantity, shop_name, shop_name.getGold(), shop_name.getSilver(), shop_name.getBronze())]
        if shop_sell:
            imagebutton:
                idle 'Shop/item_sell.png'
                hover 'Shop/item_sell_hover.png'
                focus_mask True
                action [SetVariable("shop_item_quantity", 1), shop_sell_item(selected_item[0], shop_item_quantity, shop_name, shop_name.getGold(), shop_name.getSilver(), shop_name.getBronze())]
            
        imagebutton:
            idle 'Shop/item_quantity.png'
            focus_mask True
            action NullAction()
        
        text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[shop_item_quantity]{/font}{/color}{/size}") xpos 770 ypos 562 xanchor 0.5 yanchor 0.5
        
        imagebutton:
            idle 'Shop/item_pointer_up.png'
            hover'Shop/item_pointer_up_hover.png'
            focus_mask True
            action shop_plus(selected_item)
        
        imagebutton:
            idle 'Shop/item_pointer_down.png'
            hover'Shop/item_pointer_down_hover.png'
            focus_mask True
            action shop_minus(selected_item)
        
#Режимы покупки\продажи
    imagebutton:
        xpos 31 ypos 67
        idle 'Shop/buy.png'
        action [SetVariable('shop_buy', True),SetVariable('shop_sell',False), active_mode(),  SetVariable('selected_item',''), SetVariable('shop_item_quantity', ''), SetVariable('shop_item_select',0)]
        
    imagebutton:
        xpos 166 ypos 67
        idle 'Shop/sell.png'
        action [SetVariable('shop_sell', True),SetVariable('shop_buy',False), active_mode(), SetVariable('selected_item',''), SetVariable('shop_item_quantity', ''), SetVariable('shop_item_select',0)]
        
#Название магазина и деньги====
    text ("{color=#fde7c6}{font=Fonts/DS_Goose.ttf}[shop_name.game_name]{/font}{/color}") xpos 506 ypos 33 xanchor 0.5 yanchor 0.5
    $var = wallet.getGold()
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[var]{/font}{/color}{/size}") xpos 772 ypos 121 xanchor 1.0
    $var = wallet.getSilver()
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[var]{/font}{/color}{/size}") xpos 772 ypos 158 xanchor 1.0
    $var = wallet.getBronze()
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[var]{/font}{/color}{/size}") xpos 772 ypos 193 xanchor 1.0
    
    $var = shop_name.getGold()
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[var]{/font}{/color}{/size}") xpos 772 ypos 257 xanchor 1.0
    $var = shop_name.getSilver()
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[var]{/font}{/color}{/size}") xpos 772 ypos 294 xanchor 1.0
    $var = shop_name.getBronze()
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[var]{/font}{/color}{/size}") xpos 772 ypos 329 xanchor 1.0
    

    
#Иконки отделов====
    hbox:
        xpos 706 ypos 71 xanchor 1.0
        if shop_buy and shop_name.weapon or shop_sell and shop_name.sell_weapon:
            imagebutton:
                idle 'Shop/icon_sword.png'
                selected_idle 'Shop/icon_sword_hover.png'
                selected_hover 'Shop/icon_sword_hover.png'
                action [SelectedIf(shop_active_mode=='weapon'), SetVariable('shop_active_mode', 'weapon'), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", "")]
            
        if shop_buy and shop_name.jeveler or shop_sell and shop_name.sell_jeveler:
            imagebutton:
                idle 'Shop/icon_ring.png'
                selected_idle 'Shop/icon_ring_hover.png'
                selected_hover 'Shop/icon_ring_hover.png'
                action [SelectedIf(shop_active_mode=='jeveler'), SetVariable('shop_active_mode', 'jeveler'), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", "")]
           
        if shop_buy and shop_name.alchemy or shop_sell and shop_name.sell_alchemy:
            imagebutton:
                idle 'Shop/icon_bottle.png'
                selected_idle 'Shop/icon_bottle_hover.png'
                selected_hover 'Shop/icon_bottle_hover.png'
                action [SelectedIf(shop_active_mode=='alchemy'), SetVariable('shop_active_mode', 'alchemy'), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", "")]
            
        if shop_buy and shop_name.food or shop_sell and shop_name.sell_food:
            imagebutton:
                idle 'Shop/icon_bread.png'
                selected_idle 'Shop/icon_bread_hover.png'
                selected_hover 'Shop/icon_bread_hover.png'
                action [SelectedIf(shop_active_mode=='food'), SetVariable('shop_active_mode', 'food'), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", "")]
            
        if shop_buy and shop_name.drop or shop_sell and shop_name.sell_drop:
            imagebutton:
                idle 'Shop/icon_bone.png'
                selected_idle 'Shop/icon_bone_hover.png'
                selected_hover 'Shop/icon_bone_hover.png'
                action [SelectedIf(shop_active_mode=='drop'), SetVariable('shop_active_mode', 'drop'), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", "")]
            
        if shop_buy and shop_name.paper or shop_sell and shop_name.sell_paper:
            imagebutton:
                idle 'Shop/icon_paper.png'
                selected_idle 'Shop/icon_paper_hover.png'
                selected_hover 'Shop/icon_paper_hover.png'
                action [SelectedIf(shop_active_mode=='paper'), SetVariable('shop_active_mode', 'paper'), SetVariable('shop_item_select',0), SetVariable('shop_item_quantity', ''), SetVariable("selected_item", "")]
              
#Предметы====
    vpgrid:
        cols 2
        rows len(getattr(shop_name, shop_active_mode))//2

        xpos 21 ypos 111 xysize(697, 260)
        mousewheel True
        arrowkeys True
        if  shop_buy:
            for i in range(len(getattr(shop_name, shop_active_mode))):
                 frame:
                     top_padding 0
                     left_padding 0
                     if shop_slide < 2:
                         background 'Shop/item_choice.png'
                         $shop_slide +=1
                     else:
                         if shop_slide == 2:
                             $shop_slide +=1
                         else:
                             $shop_slide = 0
                         background 'Shop/slide.png' 
                     xysize(347, 37)
                     imagebutton:
                         idle (getattr(shop_name, shop_active_mode))[i][0].icon
                         action NullAction()
                         
                     $var=(getattr(shop_name, shop_active_mode))[i][0].name
                     text "{size=16}{color=#432e25}{font=Fonts/comic.ttf}[var]{/color}{/font}{/size}" xpos 31 ypos 7
                     $var=(getattr(shop_name, shop_active_mode))[i][1]
                     text "{size=20}{color=#432e25}{font=Fonts/comic.ttf}[var]{/color}{/font}{/size}" xpos 330 ypos 5 xanchor 1.0
             
                     imagebutton:
                         idle 'Shop/item_choice.png'
                         selected_idle 'Shop/item_choice_hover.png'
                         selected_hover 'Shop/item_choice_hover.png'
                         action [SelectedIf(shop_item_select==i+1), SetVariable('shop_item_select', i+1), shop_item_position(i,shop_active_mode, shop_name) ]  #Если шоп итем селлект равен какому то параметру предмета. Потому что одинаковых предметов не будет
                         
        if  shop_sell:
            for i in range(len(getattr(inventory, shop_active_mode))):
                 frame:
                     top_padding 0
                     left_padding 0
                     if shop_slide < 2:
                         background 'Shop/item_choice.png'
                         $shop_slide +=1
                     else:
                         if shop_slide == 2:
                             $shop_slide +=1
                         else:
                             $shop_slide = 0
                         background 'Shop/slide.png' 
                     xysize(347, 37)
                     imagebutton:
                         idle (getattr(inventory, shop_active_mode))[i][0].icon
                         action NullAction()
                         
                     $var=(getattr(inventory, shop_active_mode))[i][0].name
                     text "{size=16}{color=#432e25}{font=Fonts/comic.ttf}[var]{/color}{/font}{/size}" xpos 31 ypos 7
                     $var=(getattr(inventory, shop_active_mode))[i][1]
                     text "{size=20}{color=#432e25}{font=Fonts/comic.ttf}[var]{/color}{/font}{/size}" xpos 330 ypos 5 xanchor 1.0
             
                     imagebutton:
                         idle 'Shop/item_choice.png'
                         selected_idle 'Shop/item_choice_hover.png'
                         selected_hover 'Shop/item_choice_hover.png'
                         action [SelectedIf(shop_item_select==i+1), SetVariable('shop_item_select', i+1), shop_item_position(i,shop_active_mode, inventory) ]  #Если шоп итем селлект равен какому то параметру предмета. Потому что одинаковых предметов не будет
            
#Рамка выбора предмета и его описание ниже====
    if selected_item:
        imagebutton:
            xpos 25 ypos 457
            idle selected_item[0].picture
            action NullAction()
    
        text "{color=#fde7c6}{font=Fonts/DS_goose.ttf}[selected_item[0].name]{/color}{/font}" xpos 203 ypos 426 xanchor 0.5 yanchor 0.5
        text "{size=16}{color=#fde7c6}{font=Fonts/DS_goose.ttf}[selected_item[0].description]{/color}{/font}{/size}" xpos 165 ypos 465
