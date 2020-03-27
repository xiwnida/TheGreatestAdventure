init -24 python:
    import random
   
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['Chara']
    
    
    style.hpbar = Style(style.default)
    style.hpbar.left_bar = Frame("Images/hp_full.png", 0, 0)
    style.hpbar.right_bar = Frame("Images/hp_empty.png", 0, 0)
    style.hpbar.xmaximum = 297 
    style.hpbar.ymaximum = 26
    
    style.say_who_window.background = Frame("Images/Namebox3.png", 335, 36)
    style.say_who_window.xsize = 535
    style.say_who_window.ysize = 36
    style.say_who_window.xpos = 142
    style.say_who_window.ypos = 70
    
    style.say_label.xpos = 8
    style.say_label.ypos = -37
    style.say_label.outlines = [ (1, "#000000") ]
    
    style.say_label.font="Fonts/impact.ttf"
    style.say_dialogue.font="Fonts/constan.ttf"
    narrator = Character(None, what_font="Fonts/constan.ttf")
    style.say_label.bold = False
    style.say_label.size = 22
    
    style.say_label.xanchor = 0.5
    
    style.say_two_window_vbox.order_reverse = True
   
#==============Функция, устанавливающая город при выборе страны=======================
    def setCity(country):
        for i in repCities:
            if i[0] == country:
                return i[1]
    
#==============Функция, добавляющая персонажа в список персонажей=======================
    def addChara(chara, country, city):
        global repCountries
        global repCities
        global npc_list
        npc_list.append([chara, country, city])
        if country not in repCountries:
            repCountries.append(country)
        if [country, city] not in repCities:
            repCities.append([country, city])
    
    
#==============Функция, меняющая репутацию=======================
    def changeRep(reputation, rate):
        if reputation + rate == 0:
            if rate < 0:
                rate -=1
            elif rate > 0:
                rate +=1
        reputation += rate

#==============Функция, меняющая фон и музыку локаций=======================
    def location(this_loca, music, inside=False): #Название города, название фона, время суток, название музыки
        global location_image
        global this_location
        this_location=this_loca
        locaList = this_loca.split("_")
        if not inside:
            location_image = "Images/"+str(locaList[0])+"/"+str(locaList[1])+"/"+str(locaList[2])+"_"+str(day_time)+".jpg"
        else:
            location_image = "Images/"+str(locaList[0])+"/"+str(locaList[1])+"/"+str(locaList[2])+".jpg"
        global loca_music
        loca_music=music
        renpy.call('location_image_and_music')
        
#==============Функция, вклчающая кнопки передвижения на локациях=======================
    def buttons(goto_array, inside=False):
        button_name=[]
        button_hover=[]
        gotoarray = goto_array
        for i in goto_array:
            loc = i.split("_")
            place = this_location.split("_")
            if len(loc) < 3:
                if not inside:
                    button_name.append("Images/"+str(place[0])+'/'+str(place[1])+"/"+str(place[2])+"_"+str(i)+"_"+str(day_time)+".png")
                    button_hover.append("Images/"+str(place[0])+'/'+str(place[1])+"/"+str(place[2])+"_"+str(i)+"_"+str(day_time)+"_hover.png")
                else:
                    button_name.append("Images/"+str(place[0])+'/'+str(place[1])+"/"+str(place[2])+"_"+str(i)+".png")
                    button_hover.append("Images/"+str(place[0])+'/'+str(place[1])+"/"+str(place[2])+"_"+str(i)+"_hover.png")
            elif not inside:
                button_name.append("Images/"+str(loc[0])+'/'+str(loc[1])+"/"+str(place[2])+"_"+str(loc[2])+"_"+str(day_time)+".png")
                button_hover.append("Images/"+str(loc[0])+'/'+str(loc[1])+"/"+str(place[2])+"_"+str(loc[2])+"_"+str(day_time)+"_hover.png")
            else:
                button_name.append("Images/"+str(loc[0])+'/'+str(loc[1])+"/"+str(place[2])+"_"+str(loc[2])+".png")
                button_hover.append("Images/"+str(loc[0])+'/'+str(loc[1])+"/"+str(place[2])+"_"+str(loc[2])+"_hover.png")
        renpy.call_screen('location_buttons', button_name, button_hover, gotoarray)
        
#================Функция для расположения рандомных кнопок================
    def EverydayRandom():
        if not random_today:
            CharaRandom()
        #    MonsterRandom()

        #А здесь функцию заполнения кнопками персонажей
    
#================Функция рандомных кнопок монстров==================Потом перенести в другой файл мб. ---------------------------Пока что отказываюсь от монстров.
#    def MonsterRandom():
#        global strana
#        global random_today
#                                                          Монстры Алинора
#        if strana=='Алинор':
#            #                                              КРЫСА
#            ratQuan=random.randint(1,3)
#            ratQuan=6
#            ratLoca=[ ['Alinor_vorota',622,199], [ 'Alinor_ul_plaza', 45, 371],  ['Alinor_trading_area',0,390],  ['Alinor_ul_dom', 34, 103],  ['Alinor_pereulok',533,311],  ['Alinor_cerkov',204, 406]]
#            random.shuffle(ratLoca)
#            for i in range(ratQuan):
#                random_today.append(['rat', ratLoca[i][0], ratLoca[i][1], ratLoca[i][2]])
                 
#================Функция рандомных кнопок персонажей=======================         !!!!!!!!!!!!!!ПРОПИСАТЬ ДО КОНЦА, КОГДА НАПИШУ СИСТЕМУ СМЕНЫ ДНЯ!!!!!!!!!!!!!!!
    def CharaRandom():
        global strana
        global day_time
        global random_today
        if strana=='Алинор':
            #                                        Баба для проверки
            womanLoca=['alinor_capital_gorod',172,307]
            random_today.append(['woman',womanLoca[0], womanLoca[1], womanLoca[2]])
            
                
#================Функция для того, чтобы картинки под рандомные кнопки показывались сразу же без паузы=============                
    def show_random_button_fun(array,loca):
        global show_random_button1
        global show_random_button2
        global show_random_button3
        global show_random_button4
        global show_random_button5
        show_random_button1=[]
        show_random_button2=[]
        show_random_button3=[]
        show_random_button4=[]
        show_random_button5=[]
        for i in range(len(array)):
            if array[i][1]==loca:
                if not show_random_button1:
                    show_random_button1=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
                elif not show_random_button2:
                    show_random_button2=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
                elif not show_random_button3:
                    show_random_button3=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
                elif not show_random_button4:
                    show_random_button4=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
                elif not show_random_button5:
                    show_random_button5=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
            
        
#================Функция для вызова магазина=================
    def call_shop(shop): #Системное имя, режимы для продажи
        global shop_name
        global shop_active_mode
        shop_name=shop
        
        if shop_name.weapon:
            shop_active_mode='weapon'
        elif shop_name.jeveler:
            shop_active_mode='jeveler'
        elif shop_name.alchemy:
            shop_active_mode='alchemy'
        elif shop_name.food:
            shop_active_mode='food'
        elif shop_name.drop:
            shop_active_mode='drop'
        elif shop_name.paper:
            shop_active_mode='paper'
        
        renpy.call_screen('game_shop')
        

#================Функции для перевода в экшен кнопки====================
        
#================Для перемещения по кнопкам===============

    def goto_button(i, gotoarray):
        renpy.jump(gotoarray[i])
        
#================Обновление экрана==============

    def restart_screen():
        renpy.restart_interaction()
        
#================Прибавить один к покупке\продаже в магазине===========        
    def shop_plus(item):
        global shop_item_quantity
        
        if shop_item_quantity<item[1]:
            shop_item_quantity+=1
        else:
            shop_item_quantity=1
            
        renpy.restart_interaction()
       
#================Отнять один к покупке\продаже в магазине===========              
    def shop_minus(item):
        global shop_item_quantity
        
        if shop_item_quantity !=1:
            shop_item_quantity-=1
        else:
            shop_item_quantity=item[1]
            
        renpy.restart_interaction()
              
#================Вычислить цену и прибыль в магазине=================

    def shop_price(shop_name, item, quantity):
        if item:
            shop_name.itemPrice = (item[0].price[2] + item[0].price[1]*100 + item[0].price[0]*2000) * quantity          
        else:
            shop_name.itemPrice = 0
        
#================Выбор предмета и изменение его информации===========              
    def shop_item_position(i, mode, name):
        global shop_item_quantity
        global selected_item

        selected_item = (getattr(name, mode))[i]
        
        shop_item_quantity=1

        renpy.restart_interaction()
        
#==============Автоматический выбор активного режима магазина==========
    def active_mode():
        global shop_active_mode
        
        if shop_buy:
            if shop_name.weapon:
                shop_active_mode='weapon'
            elif shop_name.jeveler:
                shop_active_mode='jeveler'
            elif shop_name.alchemy:
                shop_active_mode='alchemy'
            elif shop_name.food:
                shop_active_mode='food'
            elif shop_name.drop:
                shop_active_mode='drop'
            elif shop_name.paper:
                shop_active_mode='paper'
            
        if shop_sell:
            if shop_name.sell_weapon:
                shop_active_mode='weapon'
            elif shop_name.sell_jeveler:
                shop_active_mode='jeveler'
            elif shop_name.sell_alchemy:
                shop_active_mode='alchemy'
            elif shop_name.sell_food:
                shop_active_mode='food'
            elif shop_name.sell_drop:
                shop_active_mode='drop'
            elif shop_name.sell_paper:
                shop_active_mode='paper'
                
#============Покупка предмета==================

    def shop_buy_item(item, quantity, shop_name, gold, silver, bronze):
        global selected_item
        global shop_item_quantity
        global shop_item_select
        
        inventory.addItem(item, quantity)
        shop_name.delItem(item, quantity)
        
        if all(item not in array for array in getattr(shop_name, item.mode)):
            shop_item_quantity = 0
            selected_item = 0
            shop_item_select = 0

        wallet.delMoney(gold, silver, bronze)

        renpy.restart_interaction()
        
#============Продажа предмета==================

    def shop_sell_item(item, quantity, shop_name, gold, silver, bronze):
        global selected_item
        global shop_item_quantity
        global shop_item_select
        
        inventory.delItem(item, quantity)
        shop_name.addItem(item, quantity)
        
        if all(item not in array for array in getattr(inventory, item.mode)):
            shop_item_quantity = 0
            selected_item = 0
            shop_item_select = 0

        wallet.addMoney(gold, silver, bronze)

        renpy.restart_interaction()
       
#==========Открыть меню============
    def goto_menu():
        renpy.call("call_inventory")
        renpy.jump(this_location)
               
#==========Превращение функций в экшен-действия для кнопок=============
    goto_button = renpy.curry(goto_button)
    goto_menu = renpy.curry(goto_menu)
    shop_plus= renpy.curry(shop_plus)
    shop_minus= renpy.curry(shop_minus)
    shop_item_position = renpy.curry(shop_item_position)
    active_mode=renpy.curry(active_mode)
    restart_screen=renpy.curry(restart_screen)
    shop_buy_item=renpy.curry(shop_buy_item)
    shop_sell_item=renpy.curry(shop_sell_item)

init -10:

#=====================Фоны=====================================
    image dom = "Images/Alinor/dom_gamestart.jpg"
    image sad dvorca = "Images/Alinor/sad_dvorca.jpg"
    image koridor dvorca = "Images/Alinor/koridor1.jpg"
    image kabinet dvorca = "Images/Alinor/kabinet1.jpg"
    image kabinet dvorca1 = "Images/Alinor/kabinet2.jpg"
    image sad dvorca1 = "Images/Alinor/sad_dvorca1.jpg"
    image alinor domspal = "Images/Alinor/dom_spal.jpg"
    
#Вокзал
    image voknight = "Images/Vok/voknoch.jpg"
    image vokday = "Images/Vok/vok.jpg"
    image vokzakat = "Images/Vok/vokzakat.jpg"
    
#Названия города на стене вокзального помещения
    image vokname_alinornight = "Images/Vok/alinornoch.png"
    image vokname_alinor = "Images/Vok/alinor.png"
    
#==============Диалоги с персонажами=====================================
    
#==============Персонажи=====================================
    $jack = ['norm', 'normal']
    image Jack = LiveComposite((420, 479),  
        (0, 0), ConditionSwitch(
            "jack[0] == 'auch'", "Chara/GG2/Emotion/auch.png", 
            "jack[0] == 'duma'", "Chara/GG2/Emotion/duma.png", 
            "jack[0] == 'duma2'", "Chara/GG2/Emotion/duma2.png", 
            "jack[0] == 'hehe'", "Chara/GG2/Emotion/hehe.png",
            "jack[0] == 'hehe2'", "Chara/GG2/Emotion/hehe2.png",
            "jack[0] == 'hehe3'", "Chara/GG2/Emotion/hehe3.png",
            "jack[0] == 'nepon'", "Chara/GG2/Emotion/nepon.png",
            "jack[0] == 'nepon2'", "Chara/GG2/Emotion/nepon2.png",
            "jack[0] == 'nepon3'", "Chara/GG2/Emotion/nepon3.png",
            "jack[0] == 'neponsmile'", "Chara/GG2/Emotion/neponsmile.png",
            "jack[0] == 'neponsmile2'", "Chara/GG2/Emotion/neponsmile2.png",
            "jack[0] == 'norm'", "Chara/GG2/Emotion/norm.png",
            "jack[0] == 'norm2'", "Chara/GG2/Emotion/norm2.png",
            "jack[0] == 'out'", "Chara/GG2/Emotion/out.png",
            "jack[0] == 'pohab'", "Chara/GG2/Emotion/pohab.png",
            "jack[0] == 'pohabclose'", "Chara/GG2/Emotion/pohabclose.png",
            "jack[0] == 'sad'", "Chara/GG2/Emotion/sad.png",
            "jack[0] == 'sad2'", "Chara/GG2/Emotion/sad2.png",
            "jack[0] == 'serdit'", "Chara/GG2/Emotion/serdit.png",
            "jack[0] == 'shock'", "Chara/GG2/Emotion/shock.png",
            "jack[0] == 'shock2'", "Chara/GG2/Emotion/shock2.png",
            "jack[0] == 'smeh'", "Chara/GG2/Emotion/smeh.png",
            "jack[0] == 'smeh2'", "Chara/GG2/Emotion/smeh2.png",
            "jack[0] == 'smile'", "Chara/GG2/Emotion/smile.png",
            "jack[0] == 'smile2'", "Chara/GG2/Emotion/smile2.png",
            "jack[0] == 'smile3'", "Chara/GG2/Emotion/smile3.png",
            "jack[0] == 'smile3brush'", "Chara/GG2/Emotion/smile3brush.png",
            "jack[0] == 'smileclose'", "Chara/GG2/Emotion/smileclose.png",
            "jack[0] == 'smileclose2'", "Chara/GG2/Emotion/smileclose2.png",
            "jack[0] == 'smileclose3'", "Chara/GG2/Emotion/smileclose3.png",
            "jack[0] == 'udiv'", "Chara/GG2/Emotion/udiv.png",
            "jack[0] == 'zol'", "Chara/GG2/Emotion/zol.png",
            "jack[0] == 'zolkapl'", "Chara/GG2/Emotion/zolkapl.png"
            ),
        (0,0), ConditionSwitch(
            "jack[1] == 'normal'", "Chara/GG2/Pose/normal.png",
            "jack[1] == 'belt'", "Chara/GG2/Pose/Belt.png",
            "jack[1] == 'belt_forward'", "Chara/GG2/Pose/Belt_forward.png",
            "jack[1] == 'forward'", "Chara/GG2/Pose/forward_both.png",
            "jack[1] == 'forward_left'", "Chara/GG2/Pose/forward_left.png",
            "jack[1] == 'forward_right'", "Chara/GG2/Pose/forward_right.png",
            "jack[1] == 'head'", "Chara/GG2/Pose/head.png",
            "jack[1] == 'head_belt'", "Chara/GG2/Pose/head_belt.png",
            "jack[1] == 'mouth'", "Chara/GG2/Pose/mouth.png",
            "jack[1] == 'mouth_belt'", "Chara/GG2/Pose/mouth_belt.png"
            ))
        
    
    image butler norm = "Chara/Butler/norm.png"
    
    image korol norm = "Chara/Korol/norm.png"
    image korol hvur = "Chara/Korol/hmur.png"
    image korol udiv = "Chara/Korol/udiv.png"
    
    image bankid hah = "Chara/Bandkid/Bandkid_hah.png"
    image bankid norm = "Chara/Bandkid/Bandkid_norm.png"
    image bangirl hah = "Chara/Bandgirl/Bandgirl_hah.png"
    image bangirl smile = "Chara/Bandgirl/Bandgirl_smile.png"
    image bangirl smile2 = "Chara/Bandgirl/Bandgirl_smile2.png"
    image bangirl ero = "Chara/Bandgirl/Bandgirl_ero.png"
    image bantop cool = "Chara/Bandman/Bandtop_cool.png"
    image bantop fight = "Chara/Bandman/Bandtop_fight.png"
    image bantop hah = "Chara/Bandman/Bandtop_hah.png"
    image bantop hmur = "Chara/Bandman/Bandtop_hmur.png"
    image bantop norm = "Chara/Bandman/Bandtop_norm.png"
    image bantop zlo = "Chara/Bandman/Bandtop_zlo.png"
    
    image driver1 norm = "Chara/Train Driver/norm.png"
    image driver1 duma = "Chara/Train Driver/duma.png"
    image driver1 udiv = "Chara/Train Driver/udiv.png"
    image driver1 udiv2 = "Chara/Train Driver/udiv2.png"
    image driver1 shock = "Chara/Train Driver/shock.png"
    
#==============Предметы и прочее=====================================
    image svitok1 = "Images/svitok1.jpg"
    image svitok2 = "Images/svitok2.jpg"
    image naslutro = "Images/naslutro.png"
    image tenmin = "Images/10min.png"
    image viborkorol = "Images/viborkorol.png"
    image konec1 = "Images/konec1.png"
    image konec2 = "Images/konec2.png"
    image konec3 = "Images/konec3.png"
    image koroldal = "Images/koroldal.jpg"
    image dopusk = "Images/dopusk.jpg"
    image ograblenie = "Images/ograblenie.png"
    image talkmenu = "Talking/Talk_menu.png"
    image hidmenu = "Talking/Hidden_menu.png"
    image callmenu = "Talking/menu.png" 
    image gold = "Invent/Money/gold.png"
    
#==============Реплики=====================================
    
#==============Головы персонажей Алинора=====================================
    $ bangirl_hah = Character(bandit_girl_alinor.name, color="#d3443f", show_two_window=True, show_side_image=Image("Chara/Bandgirl/Bandgirl_hah_mini.png", yalign=1.0))
    $ bangirl_smile = Character(bandit_girl_alinor.name, color="#d3443f", show_two_window=True, show_side_image=Image("Chara/Bandgirl/Bandgirl_smile_mini.png", yalign=1.0))
    $ bangirl_smile2 = Character(bandit_girl_alinor.name, color="#d3443f", show_two_window=True, show_side_image=Image("Chara/Bandgirl/Bandgirl_smile2_mini.png", yalign=1.0))
    $ bankid_hah = Character(bandit_kid_alinor.name, color="#558489", show_two_window=True, show_side_image=Image("Chara/Bandkid/Bandkid_hah_mini.png", yalign=1.0))
    $ bankid_norm = Character(bandit_kid_alinor.name, color="#558489", show_two_window=True, show_side_image=Image("Chara/Bandkid/Bandkid_norm_mini.png", yalign=1.0))
    $ bantop_hah = Character(bandit_man_alinor.name, color="#596659", show_two_window=True, show_side_image=Image("Chara/Bandman/Bandtop_hah_mini.png", yalign=1.0))
    $ bantop_cool = Character(bandit_man_alinor.name, color="#596659", show_two_window=True, show_side_image=Image("Chara/Bandman/Bandtop_cool_mini.png", yalign=1.0))
    $ bantop_hmur = Character(bandit_man_alinor.name, color="#596659", show_two_window=True, show_side_image=Image("Chara/Bandman/Bandtop_hmur_mini.png", yalign=1.0))
    $ bantop_norm = Character(bandit_man_alinor.name, color="#596659", show_two_window=True, show_side_image=Image("Chara/Bandman/Bandtop_norm_mini.png",  yalign=1.0))
    $ bantop_zlo = Character(bandit_man_alinor.name, color="#596659", show_two_window=True, show_side_image=Image("Chara/Bandman/Bandtop_zlo_mini.png", yalign=1.0))
    $ butler = Character(buttler_alinor.name, color="#b0a5a8", show_two_window=True, show_side_image=Image("Chara/Butler/Butler_box.png", yalign=1.0))
    $ korol = Character(korol_alinor.name, color="#b0a5a8", show_two_window=True, show_side_image=Image("Chara/Korol/Korol_box.png", yalign=1.0))
    $ man_voice = Character("Мужской голос", color="#596659", show_two_window=True)
    $ woman_voice = Character("Женский голос", color="#d3443f", show_two_window=True)
    $ driver1_duma = Character(driver1_alinor.name, color="#53608c", show_two_window=True, show_side_image=Image("Chara/Train driver/duma_box.png", yalign=1.0))
    $ driver1_norm = Character(driver1_alinor.name, color="#53608c", show_two_window=True, show_side_image=Image("Chara/Train driver/norm_box.png", yalign=1.0))
    $ driver1_shock = Character(driver1_alinor.name, color="#53608c", show_two_window=True, show_side_image=Image("Chara/Train driver/shock_box.png", yalign=1.0))
    $ driver1_udiv = Character(driver1_alinor.name, color="#53608c", show_two_window=True, show_side_image=Image("Chara/Train driver/udiv_box.png",  yalign=1.0))
    $ driver1_udiv2 = Character(driver1_alinor.name, color="#53608c", show_two_window=True, show_side_image=Image("Chara/Train driver/udiv2_box.png",  yalign=1.0))
    
#==============Головы Джека=====================================
    $ j = Character("Джек", color="#5e6c96", show_two_window=True, show_side_image=LiveComposite((800, 151),  
        (0, 0), ConditionSwitch(
            "jack[0] == 'auch'", "Chara/Mini GG2/Emotion/auch.png", 
            "jack[0] == 'duma'", "Chara/Mini GG2/Emotion/duma.png", 
            "jack[0] == 'duma2'", "Chara/Mini GG2/Emotion/duma2.png", 
            "jack[0] == 'hehe'", "Chara/Mini GG2/Emotion/hehe.png",
            "jack[0] == 'hehe2'", "Chara/Mini GG2/Emotion/hehe2.png",
            "jack[0] == 'hehe3'", "Chara/Mini GG2/Emotion/hehe3.png",
            "jack[0] == 'nepon'", "Chara/Mini GG2/Emotion/nepon.png",
            "jack[0] == 'nepon2'", "Chara/Mini GG2/Emotion/nepon2.png",
            "jack[0] == 'nepon3'", "Chara/Mini GG2/Emotion/nepon3.png",
            "jack[0] == 'neponsmile'", "Chara/Mini GG2/Emotion/neponsmile.png",
            "jack[0] == 'neponsmile2'", "Chara/Mini GG2/Emotion/neponsmile2.png",
            "jack[0] == 'norm'", "Chara/Mini GG2/Emotion/norm.png",
            "jack[0] == 'norm2'", "Chara/Mini GG2/Emotion/norm2.png",
            "jack[0] == 'out'", "Chara/Mini GG2/Emotion/out.png",
            "jack[0] == 'pohab'", "Chara/Mini GG2/Emotion/pohab.png",
            "jack[0] == 'pohabclose'", "Chara/Mini GG2/Emotion/pohabclose.png",
            "jack[0] == 'sad'", "Chara/Mini GG2/Emotion/sad.png",
            "jack[0] == 'sad2'", "Chara/Mini GG2/Emotion/sad2.png",
            "jack[0] == 'serdit'", "Chara/Mini GG2/Emotion/serdit.png",
            "jack[0] == 'shock'", "Chara/Mini GG2/Emotion/shock.png",
            "jack[0] == 'shock2'", "Chara/Mini GG2/Emotion/shock2.png",
            "jack[0] == 'smeh'", "Chara/Mini GG2/Emotion/smeh.png",
            "jack[0] == 'smeh2'", "Chara/Mini GG2/Emotion/smeh2.png",
            "jack[0] == 'smile'", "Chara/Mini GG2/Emotion/smile.png",
            "jack[0] == 'smile2'", "Chara/Mini GG2/Emotion/smile2.png",
            "jack[0] == 'smile3'", "Chara/Mini GG2/Emotion/smile3.png",
            "jack[0] == 'smile3brush'", "Chara/Mini GG2/Emotion/smile3brush.png",
            "jack[0] == 'smileclose'", "Chara/Mini GG2/Emotion/smileclose.png",
            "jack[0] == 'smileclose2'", "Chara/Mini GG2/Emotion/smileclose2.png",
            "jack[0] == 'smileclose3'", "Chara/Mini GG2/Emotion/smileclose3.png",
            "jack[0] == 'udiv'", "Chara/Mini GG2/Emotion/udiv.png",
            "jack[0] == 'zol'", "Chara/Mini GG2/Emotion/zol.png",
            "jack[0] == 'zolkapl'", "Chara/Mini GG2/Emotion/zolkapl.png"
            ),
        (0,0), ConditionSwitch(
            "jack[1] == 'normal'", "Chara/Mini GG2/Pose/normal.png",
            "jack[1] == 'belt'", "Chara/Mini GG2/Pose/Belt.png",
            "jack[1] == 'belt_forward'", "Chara/Mini GG2/Pose/Belt_forward.png",
            "jack[1] == 'forward'", "Chara/Mini GG2/Pose/forward_both.png",
            "jack[1] == 'forward_left'", "Chara/Mini GG2/Pose/forward_left.png",
            "jack[1] == 'forward_right'", "Chara/Mini GG2/Pose/forward_right.png",
            "jack[1] == 'head'", "Chara/Mini GG2/Pose/head.png",
            "jack[1] == 'head_belt'", "Chara/Mini GG2/Pose/head_belt.png",
            "jack[1] == 'mouth'", "Chara/Mini GG2/Pose/mouth.png",
            "jack[1] == 'mouth_belt'", "Chara/Mini GG2/Pose/mouth_belt.png"), yalign=1.0))
      
#==============Переменные=====================================
    $ korol_dal_karta = False
    $ korol_dal_money = False
    $ korol_dal_dokument = False
    $ first_start = True # Эта переменная нужна для перехода на второй скрипт.
    
    $ strana = "Алинор" # Эта переменная указывает, в какой стране вы находитесь.
    $ city = "Аранкар" # Эта переменная указывает, в каком городе вы находитесь.
    $ countries = ["Алинор"] # Эта переменная указывает, в каких странах вы уже бывали
    $ cities = ["Аранкар"] # Эта переменная указывает, в каких городах вы уже бывали
    
    $ sobrat_veshi = False # Эта переменная не даст уйти из гостиной, пока вы не собрались в путешествие.
    $ vzat_blank = False # Эта переменная не даст уйти из гостинной, пока вы не взяли блокнот.
    $ lech_na_krovat = False # Эта переменная позволяет полежать на кровати только один раз.
    $ loca_music = "Nope" # Эта переменная хранит название музыки локации.
    $ playing_music = "Nope" #  А эта переменная хранит название играющей музыки.
    $ music_title = "Nope" # Эта переменная хранит адреса музыки.
    $ no_fade = False # Эта переменная нужна, чтобы после отключения меню не сработал fade эффект (ох, костыли!)
    $ scene_p = "Nope" # Эта переменная нужна, чтобы показать нужную сцену перед иммедж картой
    $ day_time = "day" # Эта переменная нужна, чтобы включить закатную сцену вечером
    
    $ gotoarray = [] # Этот массив нужен для переадресации с кнопок на нужные лейблы
    $ buttons_quantity = 0 # В эту переменную на каждой локе заносится количество кнопок
    $ button_name = [] # Массив с иддл-именами кнопок
    $ button_hover = [] # Массив с ховер-именами кнопок
    
    $location_image=''
    
    $random_today=[] #Хранит рандомные кнопки на сегодня
    $this_location='' #Хранит название текущей локации
    $show_random_button1=''    #Показывает картинки рандомных кнопок, чтобы они появлялись сразу же без паузы
    $show_random_button2=''
    $show_random_button3=''
    $show_random_button4=''
    $show_random_button5=''
    
    $effect1='Battle/1.png'
    
    $screen_name_to_hide = "" #Хранит название экрана, который требуется закрыть
    
    $npc = ''
    $energy = 100
    
    define fade = Fade(0.3, 0.0, 0.3)
    
#==============Трансформации для экранов=================
    transform battle_dissolve:
        on show:
            alpha 0.0
            pause(1)
            linear .2 alpha 1.0
            
        on hide:
            alpha 1.0
            pause(1)
            linear .2 alpha 0.0

#==============Колл. Показывает изображение, чье название собрано функцией location====================

label location_image_and_music:
    if energy <=20:
        $day_time = 'zakat'
    else:
        $day_time = 'day'
    
    scene expression location_image 
    if not first_start:
        show screen enegryScreen
    
    $show_random_button_fun(random_today, this_location)
    if show_random_button1:
        show expression show_random_button1[0]:
            xpos show_random_button1[1] ypos show_random_button1[2]
    if show_random_button2:
        show expression show_random_button2[0]:
            xpos show_random_button2[1] ypos show_random_button2[2]
    if show_random_button3:
        show expression show_random_button3[0]:
            xpos show_random_button3[1] ypos show_random_button3[2]
    if show_random_button4:
        show expression show_random_button4[0]:
            xpos show_random_button4[1] ypos show_random_button4[2]
    if show_random_button5:
        show expression show_random_button5[0]:
            xpos show_random_button5[1] ypos show_random_button5[2]

    if loca_music=="alinor_stolica":
        $ music_title = "Music/Alinor/stolica.ogg"
    elif loca_music=="alinor_vash_dom":
        $ music_title= "Music/Alinor/Vash_dom.ogg"
        
    if not no_fade:
        with fade
    else:
        $ no_fade = False
    
    if playing_music == loca_music: #Если играющая музыка равна новой музыке
        pass
    else:
        play music music_title
        $ playing_music = loca_music
    return

#=========================Кнопки навигации по локации=====================
        
screen location_buttons(button_name, button_hover, gotoarray):         
    key "i" action Jump('call_inventory')
    key "I" action Jump('call_inventory')
    key "ш" action Jump('call_inventory')
    key "Ш" action Jump('call_inventory')
    
    key "m" action Jump('callMap')
    key "M" action Jump('callMap')
    key "ь" action Jump('callMap')
    key "Ь" action Jump('callMap')
    
    key "r" action Jump('callReputation')
    key "R" action Jump('callReputation')
    key "к" action Jump('callReputation')
    key "К" action Jump('callReputation')
       
    for i in range(len(button_name)):
        imagebutton:
            idle button_name[i]
            hover button_hover[i]
            focus_mask True
            action goto_button(i, gotoarray)
            
    for i in range (len(random_today)):
        if random_today[i][1] == this_location:
            imagebutton:
                xpos random_today[i][2] ypos random_today[i][3]
                idle 'Images/'+random_today[i][0]+'.png'
                hover 'Images/'+random_today[i][0]+'_hover.png'
                focus_mask True
                action NullAction()