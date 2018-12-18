init:
    #================Переменные================
    $shop_active_mode='' #Для выделения одной из иконок режимов
    $shop_modes=[] #Хранит активные режимы для каждого магазина
    
    $shop_buy=True  #Режим покупки
    $shop_sell=False  #Режим продажи

    $shop_item_quantity='' #Переменная для функции, позволяющий купить больше одного предмета
    $shop_item_quantity_for='' #Переменная для определения границ счетчика покупки\продажи
    
    $shop_Y=[117, 117, 154, 154, 191, 191,  228, 228, 265, 265, 302, 302, 339, 339] #Координаты для создания сетки предметов
    $shop_X=0 
    
    $shop_item_exist=0
    
    $shop_item_select=False #Чтобы определить, выбран ли предмет
    
    $shop_name=''  #Хранит название активного магазина
    $shop_items=[]  #Хранит товары активного магазина
    
    $shop_item_name=''           #Название предмета в сетке
    $shop_item_name_item=''  #Название предмета
    $shop_item_picture=''         #Картинка предмета
    $shop_item_number=0       #Количество предметов в сетке
    $shop_item_description=''  #Описание предмета
    $shop_item_effect=''           #Эффект предмета
    $shop_item_icon=''             #Иконка предмета в сетке
    

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
            action [SelectedIf(shop_active_mode=='sword'), SetVariable('shop_active_mode', 'sword')]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_ring.png'
            selected_idle 'Shop/icon_ring_hover.png'
            selected_hover 'Shop/icon_ring_hover.png'
            action [SelectedIf(shop_active_mode=='ring'), SetVariable('shop_active_mode', 'ring')]
           
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_bottle.png'
            selected_idle 'Shop/icon_bottle_hover.png'
            selected_hover 'Shop/icon_bottle_hover.png'
            action [SelectedIf(shop_active_mode=='bottle'), SetVariable('shop_active_mode', 'bottle')]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_bread.png'
            selected_idle 'Shop/icon_bread_hover.png'
            selected_hover 'Shop/icon_bread_hover.png'
            action [SelectedIf(shop_active_mode=='bread'), SetVariable('shop_active_mode', 'bread')]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_bone.png'
            selected_idle 'Shop/icon_bone_hover.png'
            selected_hover 'Shop/icon_bone_hover.png'
            action [SelectedIf(shop_active_mode=='bone'), SetVariable('shop_active_mode', 'bone')]
            
        imagebutton:
            xpos 510 ypos 71
            idle 'Shop/icon_paper.png'
            selected_idle 'Shop/icon_paper_hover.png'
            selected_hover 'Shop/icon_paper_hover.png'
            action [SelectedIf(shop_active_mode=='paper'), SetVariable('shop_active_mode', 'paper')]
            
            
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
    
    if shop_item_picture:
        imagebutton:
            xpos 25 ypos 457
            idle shop_item_picture
            action NullAction()
        
    text "{color=#fde7c6}{font=Fonts/DS_goose.ttf}[shop_item_name_item]{/color}{/font}" xpos 203 ypos 426 xanchor 0.5 yanchor 0.5
    text "{size=16}{color=#fde7c6}{font=Fonts/DS_goose.ttf}[shop_item_description]{/color}{/font}{/size}" xpos 165 ypos 465
    
    
label lololo:
    "Бу"
