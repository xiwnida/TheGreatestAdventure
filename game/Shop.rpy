init:
    #================Переменные================
    $shop_active_mode=''       #Для выделения одной из иконок режимов
    
    $shop_buy=True                #Управление покупкой/продажей
    $shop_sell=False

    $shop_item_quantity=''       #Переменная для функции, позволяющий купить больше одного предмета
    $shop_item_quantity_for='' #Переменная для определения границ счетчика покупки\продажи
    
    $shop_Y=[117, 117, 154, 154, 191, 191,  228, 228, 265, 265, 302, 302, 339, 339] #Координаты для создания сетки предметов
    $shop_X=0 
    
    $shop_item_select=False  #Чтобы определить, выбран ли предмет
    
    $shop_name=''                   #Хранит системное название активного магазина
    
    $shop_item_name=''           #Название предмета в сетке
    $shop_item_name_item=''  #Название предмета
    $shop_item_picture=''         #Картинка предмета
    $shop_item_number=0       #Количество предметов в сетке
    $shop_item_description=''  #Описание предмета
    $shop_item_icon=''             #Иконка предмета в сетке
    
    $shop_item_lists=0            #Вычисляет индексы предметов при прокрутке магазина
    

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
        
#Указатели===
    imagebutton:
        idle 'Shop/pointer_up.png'
        hover'Shop/pointer_up_hover.png'
        focus_mask True
        action [SensitiveIf(shop_item_lists>0), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0), scroll_up()]
    
    imagebutton:
        idle 'Shop/pointer_down.png'
        hover'Shop/pointer_down_hover.png'
        focus_mask True
        action [SensitiveIf(14+shop_item_lists<len(getattr(shop_name, shop_active_mode))), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0), scroll_down()]
        
#Кнопки покупки\продажи и количества=======
    if shop_item_quantity:
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
            action shop_plus()
        
        imagebutton:
            idle 'Shop/item_pointer_down.png'
            hover'Shop/item_pointer_down_hover.png'
            focus_mask True
            action shop_minus()
        
#Режимы покупки\продажи
    imagebutton:
        xpos 31 ypos 67
        idle 'Shop/buy.png'
        action [SetVariable('shop_buy', True),SetVariable('shop_sell',False), active_mode(), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description','')]
        
    imagebutton:
        xpos 166 ypos 67
        idle 'Shop/sell.png'
        action [SetVariable('shop_sell', True),SetVariable('shop_buy',False), active_mode(), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description','')]
        
#Название магазина и деньги====
    text ("{color=#fde7c6}{font=Fonts/DS_Goose.ttf}[shop_name.game_name]{/font}{/color}") xpos 506 ypos 33 xanchor 0.5 yanchor 0.5
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[money_gold]{/font}{/color}{/size}") xpos 772 ypos 109 xanchor 1.0
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[money_silver]{/font}{/color}{/size}") xpos 772 ypos 145 xanchor 1.0
    text ("{size=19}{color=#fde7c6}{font=Fonts/comic.ttf}[money_bronz]{/font}{/color}{/size}") xpos 772 ypos 179 xanchor 1.0
    
#Иконки отделов====
    hbox:
        xpos 706 ypos 71 xanchor 1.0
        if shop_buy and shop_name.buy_weapon or shop_sell and shop_name.sell_weapon:
            imagebutton:
                idle 'Shop/icon_sword.png'
                selected_idle 'Shop/icon_sword_hover.png'
                selected_hover 'Shop/icon_sword_hover.png'
                action [SelectedIf(shop_active_mode=='weapon'), SetVariable('shop_active_mode', 'weapon'), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0)]
            
        if shop_buy and shop_name.buy_jeveler or shop_sell and shop_name.sell_jeveler:
            imagebutton:
                idle 'Shop/icon_ring.png'
                selected_idle 'Shop/icon_ring_hover.png'
                selected_hover 'Shop/icon_ring_hover.png'
                action [SelectedIf(shop_active_mode=='jeveler'), SetVariable('shop_active_mode', 'jeveler'), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0)]
           
        if shop_buy and shop_name.buy_alchemy or shop_sell and shop_name.sell_alchemy:
            imagebutton:
                idle 'Shop/icon_bottle.png'
                selected_idle 'Shop/icon_bottle_hover.png'
                selected_hover 'Shop/icon_bottle_hover.png'
                action [SelectedIf(shop_active_mode=='alchemy'), SetVariable('shop_active_mode', 'alchemy'), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0)]
            
        if shop_buy and shop_name.buy_food or shop_sell and shop_name.sell_food:
            imagebutton:
                idle 'Shop/icon_bread.png'
                selected_idle 'Shop/icon_bread_hover.png'
                selected_hover 'Shop/icon_bread_hover.png'
                action [SelectedIf(shop_active_mode=='food'), SetVariable('shop_active_mode', 'food'), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0)]
            
        if shop_buy and shop_name.buy_drop or shop_sell and shop_name.sell_drop:
            imagebutton:
                idle 'Shop/icon_bone.png'
                selected_idle 'Shop/icon_bone_hover.png'
                selected_hover 'Shop/icon_bone_hover.png'
                action [SelectedIf(shop_active_mode=='drop'), SetVariable('shop_active_mode', 'drop'), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0)]
            
        if shop_buy and shop_name.buy_paper or shop_sell and shop_name.sell_paper:
            imagebutton:
                idle 'Shop/icon_paper.png'
                selected_idle 'Shop/icon_paper_hover.png'
                selected_hover 'Shop/icon_paper_hover.png'
                action [SelectedIf(shop_active_mode=='paper'), SetVariable('shop_active_mode', 'paper'), SetVariable('shop_item_picture', ''), SetVariable('shop_item_name_item',''), SetVariable('shop_item_description',''), SetVariable('shop_item_select',0)]
      
#Предметы====
    for i in range(14):
         if i+shop_item_lists<(len(getattr(shop_name, shop_active_mode))) and shop_buy:
             if i%2==0:
                 $shop_X=20
             else:
                 $shop_X=368
             imagebutton:
                 xpos shop_X ypos shop_Y[i]-6
                 idle (getattr(shop_name, shop_active_mode))[i+shop_item_lists][0].icon
                 action NullAction()
                 
             $var=(getattr(shop_name, shop_active_mode))[i+shop_item_lists][0].name
             text "{size=16}{color=#432e25}{font=Fonts/comic.ttf}[var]{/color}{/font}{/size}" xpos shop_X+31 ypos shop_Y[i]+2
             $var=(getattr(shop_name, shop_active_mode))[i+shop_item_lists][1]
             text "{size=20}{color=#432e25}{font=Fonts/comic.ttf}[var]{/color}{/font}{/size}" xpos shop_X+330 ypos shop_Y[i]-3 xanchor 1.0
     
             imagebutton:
                 xpos shop_X ypos shop_Y[i]-6
                 idle 'Shop/item_choice.png'
                 selected_idle 'Shop/item_choice_hover.png'
                 selected_hover 'Shop/item_choice_hover.png'
                 action [SelectedIf(shop_item_select==i+shop_item_lists+1), SetVariable('shop_item_select', i+shop_item_lists+1), shop_item_position(i+shop_item_lists,shop_active_mode)]  #Если шоп итем селлект равен какому то параметру предмета. Потому что одинаковых предметов не будет
                 
            
#Рамка выбора предмета и его описание ниже====
    if shop_item_picture:
        imagebutton:
            xpos 25 ypos 457
            idle shop_item_picture
            action NullAction()
    
    if shop_item_name_item:
        text "{color=#fde7c6}{font=Fonts/DS_goose.ttf}[shop_item_name_item]{/color}{/font}" xpos 203 ypos 426 xanchor 0.5 yanchor 0.5
    if shop_item_description:
        text "{size=16}{color=#fde7c6}{font=Fonts/DS_goose.ttf}[shop_item_description]{/color}{/font}{/size}" xpos 165 ypos 465
