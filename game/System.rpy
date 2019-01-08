init python:
    import random
   
    config.automatic_images_minimum_components = 1
    config.automatic_images = [' ', '_', '/']
    config.automatic_images_strip = ['Chara']
    
    
    style.hpbar = Style(style.default)
    style.hpbar.left_bar = Frame("Images/hp_full.png", 0, 0)
    style.hpbar.right_bar = Frame("Images/hp_empty.png", 0, 0)
    style.hpbar.xmaximum = 297 
    style.hpbar.ymaximum = 26


    
#==============Функция, меняющая фон и музыку локаций=======================
    def location(city, loca, music, inside=False): #Название города, название фона, время суток, название музыки
        global location_image
        global day_time
        global this_location
        this_location=city+'_'+loca
        if not inside:
            location_image = "Images/"+str(city)+"/"+str(loca)+"_"+str(day_time)+".jpg"
        else:
            location_image = "Images/"+str(city)+"/"+str(loca)+".jpg"
        global loca_music
        loca_music=music
        renpy.call('location_image_and_music')
        
#==============Функция, вклчающая кнопки передвижения на локациях=======================
    def buttons(name, quantity, goto_array, inside=False): # Дописать закатные кнопки
        global button_name
        global button_hover
        global buttons_quantity
        global gotoarray
        global day_time
        button_name=[]
        button_hover=[]
        buttons_quantity=quantity
        gotoarray=goto_array
        for i in range(quantity):
            if not inside:
                button_name.append("Images/Alinor/"+str(name)+'_'+str(day_time)+str(i+1)+".png")
                button_hover.append("Images/Alinor/"+str(name)+'_'+str(day_time)+str(i+1)+"akt.png")
            else:
                button_name.append("Images/Alinor/"+str(name)+str(i+1)+".png")
                button_hover.append("Images/Alinor/"+str(name)+str(i+1)+"akt.png")
        renpy.call_screen('location_buttons')
        
#================Функция для расположения рандомных кнопок================
    def EverydayRandom():
        global random_today
        if not random_today:
            CharaRandom()
            MonsterRandom()

        #А здесь функцию заполнения кнопками персонажей
     
#================Функция рандомных кнопок монстров==================Потом перенести в другой файл мб
    def MonsterRandom():
        global strana
        global random_today
#                                                          Монстры Алинора
        if strana=='Алинор':
            #                                              КРЫСА
            ratQuan=random.randint(1,3)
            ratQuan=6
            ratLoca=[ ['Alinor_vorota',622,199], [ 'Alinor_ul_plaza', 45, 371],  ['Alinor_trading_area',0,390],  ['Alinor_ul_dom', 34, 103],  ['Alinor_pereulok',533,311],  ['Alinor_cerkov',204, 406]]
            random.shuffle(ratLoca)
            for i in range(ratQuan):
                random_today.append(['rat', ratLoca[i][0], ratLoca[i][1], ratLoca[i][2]])
                 
#================Функция рандомных кнопок персонажей=======================         !!!!!!!!!!!!!!ПРОПИСАТЬ ДО КОНЦА, КОГДА НАПИШУ СИСТЕМУ СМЕНЫ ДНЯ!!!!!!!!!!!!!!!
    def CharaRandom():
        global strana
        global day_time
        global random_today
        if strana=='Алинор':
            #                                        Баба для проверки
            womanLoca=['Alinor_trading_area',172,307]
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
                elif not show_random_button2:
                    show_random_button3=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
                elif not show_random_button2:
                    show_random_button4=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
                elif not show_random_button2:
                    show_random_button5=['Images/'+array[i][0]+'.png', array[i][2], array[i][3]]
            
        
#================Функция для вызова магазина=================
    def call_shop(shop, weapon=False, jeveler=False, alchemy=False, food=False, drop=False, paper=False): #Системное имя, режимы для продажи
        global shop_name
        global shop_active_mode
        shop_name=shop
        
        shop_name.sell_weapon=weapon
        shop_name.sell_jeveler=jeveler
        shop_name.sell_alchemy=alchemy
        shop_name.sell_food=food
        shop_name.sell_drop=drop
        shop_name.sell_paper=paper
        
        if shop_name.buy_weapon:
            shop_active_mode='weapon'
        elif shop_name.buy_jeveler:
            shop_active_mode='jeveler'
        elif shop_name.buy_alchemy:
            shop_active_mode='alchemy'
        elif shop_name.buy_food:
            shop_active_mode='food'
        elif shop_name.buy_drop:
            shop_active_mode='drop'
        elif shop_name.buy_paper:
            shop_active_mode='paper'
        
        renpy.call_screen('game_shop')
        
#================Функции для перевода в экшен кнопки====================
        
    def goto_button(i):
        renpy.jump(gotoarray[i])
        
#================Прибавить один к покупке\продаже в магазине===========        
    def shop_plus():
        global shop_item_quantity
        global shop_item_quantity_for
        
        if shop_item_quantity<shop_item_quantity_for:
            shop_item_quantity+=1
        else:
            shop_item_quantity=1
            
        renpy.restart_interaction()
       
#================Отнять один к покупке\продаже в магазине===========              
    def shop_minus():
        global shop_item_quantity
        global shop_item_quantity_for
        
        if shop_item_quantity !=1:
            shop_item_quantity-=1
        else:
            shop_item_quantity=shop_item_quantity_for
            
        renpy.restart_interaction()
        
#================Выбор предмета и изменение его информации===========              
    def shop_item_position(i, shop_mode):
        global shop_item_quantity
        global shop_item_quantity_for
        global shop_item_name_item
        global shop_item_number
        global shop_item_picture
        global shop_item_description
        global shop_item_lists

        shop_item_quantity=1
        shop_item_description=(getattr(shop_name, shop_mode))[i][0].description
        shop_item_name_item=(getattr(shop_name, shop_mode))[i][0].name
        shop_item_quantity_for=(getattr(shop_name, shop_mode))[i][1]
        shop_item_picture=(getattr(shop_name, shop_mode))[i][0].picture
        renpy.restart_interaction()
        
#==============Автоматический выбор активного режима магазина==========
    def active_mode():
        global shop_name
        global shop_active_mode
        global shop_buy
        global shop_sell
        
        if shop_buy:
            if shop_name.buy_weapon:
                shop_active_mode='weapon'
            elif shop_name.buy_jeveler:
                shop_active_mode='jeveler'
            elif shop_name.buy_alchemy:
                shop_active_mode='alchemy'
            elif shop_name.buy_food:
                shop_active_mode='food'
            elif shop_name.buy_drop:
                shop_active_mode='drop'
            elif shop_name.buy_paper:
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
     
#============Прокрутка магазина вниз=============
    def scroll_down():
        global shop_item_lists
        shop_item_lists+=2
        renpy.restart_interaction()
        
#============Прокрутка магазина вверх=============
    def scroll_up():
        global shop_item_lists
        shop_item_lists-=2
        renpy.restart_interaction()
               
#==========Превращение функций в экшен-действия для кнопок=============
    goto_button = renpy.curry(goto_button)
    shop_plus= renpy.curry(shop_plus)
    shop_minus= renpy.curry(shop_minus)
    shop_item_position = renpy.curry(shop_item_position)
    active_mode=renpy.curry(active_mode)
    scroll_down=renpy.curry(scroll_down)
    scroll_up=renpy.curry(scroll_up)

init:

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
    image shopper girl = "Images/Character/Shopper_Girl.jpg"
    
#==============Персонажи=====================================
    image jack smile = "Chara/GG/smile.png"
    image jack smile2 = "Chara/GG/smile2.png"
    image jack smile close = "Chara/GG/smile_close.png"
    image jack smile close2 = "Chara/GG/smile_close2.png"
    image jack smile close3 = "Chara/GG/smile_close3.png"
    image jack nepon = "Chara/GG/nepon.png"
    image jack nepon2 = "Chara/GG/nepon2.png"
    image jack serdit = "Chara/GG/serdit.png"
    image jack neponsmile = "Chara/GG/neponsmile.png"
    image jack neponsmile2 = "Chara/GG/neponsmile2.png"
    image jack norm = "Chara/GG/norm.png"
    image jack smeh = "Chara/GG/smeh.png"
    image jack smeh2 = "Chara/GG/smeh2.png"
    image jack duma = "Chara/GG/duma.png"
    image jack udiv = "Chara/GG/udiv.png"
    image jack sad = "Chara/GG/sad.png"
    image jack zol = "Chara/GG/zol.png"
    image jack zolkapl = "Chara/GG/zolkapl.png"
    image jack hehe = "Chara/GG/hehe.png"
    image jack hehe2 = "Chara/GG/hehe2.png"
    
    image butler norm = "Chara/Butler/norm.png"
    
    image korol norm = "Chara/Korol/norm.png"
    image korol hvur = "Chara/Korol/hmur.png"
    image korol udiv = "Chara/Korol/udiv.png"
    
    image bankid hah = "Chara/Bandits/Bandkid_hah.png"
    image bankid norm = "Chara/Bandits/Bandkid_norm.png"
    image bangirl hah = "Chara/Bandits/Bandgirl_hah.png"
    image bangirl smile = "Chara/Bandits/Bandgirl_smile.png"
    image bangirl smile2 = "Chara/Bandits/Bandgirl_smile2.png"
    image bangirl ero = "Chara/Bandits/Bandgirl_ero.png"
    image bantop cool = "Chara/Bandits/Bandtop_cool.png"
    image bantop fight = "Chara/Bandits/Bandtop_fight.png"
    image bantop hah = "Chara/Bandits/Bandtop_hah.png"
    image bantop hmur = "Chara/Bandits/Bandtop_hmur.png"
    image bantop norm = "Chara/Bandits/Bandtop_norm.png"
    image bantop zlo = "Chara/Bandits/Bandtop_zlo.png"
    
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
    $ bangirl = Character(u'Красивая девушка', color="d24f4b")
    
#==============Головы персонажей Алинора=====================================
    $ bangirl_hah = Character(show_side_image=Image("Chara/Bandits/Bandgirl_hah_mini.png", xalign=0.0, yalign=1.0))
    $ bangirl_smile = Character(show_side_image=Image("Chara/Bandits/Bandgirl_smile_mini.png", xalign=0.0, yalign=1.0))
    $ bangirl_smile2 = Character(show_side_image=Image("Chara/Bandits/Bandgirl_smile2_mini.png", xalign=0.0, yalign=1.0))
    $ bankid_hah = Character(show_side_image=Image("Chara/Bandits/Bandkid_hah_mini.png", xalign=0.0, yalign=1.0))
    $ bankid_norm = Character(show_side_image=Image("Chara/Bandits/Bandkid_norm_mini.png", xalign=0.0, yalign=1.0))
    $ bantop_hah = Character(color="d7d4c4", show_side_image=Image("Chara/Bandits/Bandtop_hah_mini.png", xalign=0.0, yalign=1.0))
    $ bantop_cool = Character(color="d7d4c4", show_side_image=Image("Chara/Bandits/Bandtop_cool_mini.png", xalign=0.0, yalign=1.0))
    $ bantop_hmur = Character(color="d7d4c4", show_side_image=Image("Chara/Bandits/Bandtop_hmur_mini.png", xalign=0.0, yalign=1.0))
    $ bantop_norm = Character(color="d7d4c4", show_side_image=Image("Chara/Bandits/Bandtop_norm_mini.png", xalign=0.0, yalign=1.0))
    $ bantop_zlo = Character(color="d7d4c4", show_side_image=Image("Chara/Bandits/Bandtop_zlo_mini.png", xalign=0.0, yalign=1.0))
    $ butler = Character(show_side_image=Image("Chara/Butler/Butler_box.png", xalign=0.0, yalign=1.0))
    $ korol = Character(show_side_image=Image("Chara/Korol/Korol_box.png", xalign=0.0, yalign=1.0))
    $ man_voice = Character(show_side_image=Image("Chara/Man_voice.png", xalign=0.0, yalign=1.0))
    $ woman_voice = Character(show_side_image=Image("Chara/Woman_voice.png", xalign=0.0, yalign=1.0))
    $ driver1_duma = Character(show_side_image=Image("Chara/Train driver/duma_box.png", xalign=0.0, yalign=1.0))
    $ driver1_norm = Character(show_side_image=Image("Chara/Train driver/norm_box.png", xalign=0.0, yalign=1.0))
    $ driver1_shock = Character(show_side_image=Image("Chara/Train driver/shock_box.png", xalign=0.0, yalign=1.0))
    $ driver1_udiv = Character(show_side_image=Image("Chara/Train driver/udiv_box.png", xalign=0.0, yalign=1.0))
    $ driver1_udiv2 = Character(show_side_image=Image("Chara/Train driver/udiv2_box.png", xalign=0.0, yalign=1.0))
    
#==============Головы Джека=====================================
    $ j_auch = Character(show_side_image=Image("Chara/Mini GG/Auch.png", xalign=0.0, yalign=1.0))
    $ j_duma = Character(show_side_image=Image("Chara/Mini GG/Duma.png", xalign=0.0, yalign=1.0))
    $ j_hehe = Character(show_side_image=Image("Chara/Mini GG/Hehe.png", xalign=0.0, yalign=1.0))
    $ j_hehe2 = Character(show_side_image=Image("Chara/Mini GG/Hehe2.png", xalign=0.0, yalign=1.0))
    $ j_hehe3 = Character(show_side_image=Image("Chara/Mini GG/Hehe3.png", xalign=0.0, yalign=1.0))
    $ j_nepon = Character(show_side_image=Image("Chara/Mini GG/Nepon.png", xalign=0.0, yalign=1.0))
    $ j_nepon2 = Character(show_side_image=Image("Chara/Mini GG/Nepon2.png", xalign=0.0, yalign=1.0))
    $ j_nepon3 = Character(show_side_image=Image("Chara/Mini GG/Nepon3.png", xalign=0.0, yalign=1.0))
    $ j_neponsmile = Character(show_side_image=Image("Chara/Mini GG/Neponsmile.png", xalign=0.0, yalign=1.0))
    $ j_neponsmile2 = Character(show_side_image=Image("Chara/Mini GG/Neponsmile2.png", xalign=0.0, yalign=1.0))
    $ j_norm = Character(show_side_image=Image("Chara/Mini GG/Norm.png", xalign=0.0, yalign=1.0))
    $ j_out = Character(show_side_image=Image("Chara/Mini GG/Out.png", xalign=0.0, yalign=1.0))
    $ j_pohab = Character(show_side_image=Image("Chara/Mini GG/Pohab.png", xalign=0.0, yalign=1.0))
    $ j_pohab_close = Character(show_side_image=Image("Chara/Mini GG/Pohab_close.png", xalign=0.0, yalign=1.0))
    $ j_sad = Character(show_side_image=Image("Chara/Mini GG/Sad.png", xalign=0.0, yalign=1.0))
    $ j_sad2 = Character(show_side_image=Image("Chara/Mini GG/Sad2.png", xalign=0.0, yalign=1.0))
    $ j_serdit = Character(show_side_image=Image("Chara/Mini GG/Serdit.png", xalign=0.0, yalign=1.0))
    $ j_shock = Character(show_side_image=Image("Chara/Mini GG/Shock.png", xalign=0.0, yalign=1.0))
    $ j_shock2 = Character(show_side_image=Image("Chara/Mini GG/Shock2.png", xalign=0.0, yalign=1.0))
    $ j_smeh = Character(show_side_image=Image("Chara/Mini GG/Smeh.png", xalign=0.0, yalign=1.0))
    $ j_smeh2 = Character(show_side_image=Image("Chara/Mini GG/Smeh2.png", xalign=0.0, yalign=1.0))
    $ j_smile = Character(show_side_image=Image("Chara/Mini GG/Smile.png", xalign=0.0, yalign=1.0))
    $ j_smile2 = Character(show_side_image=Image("Chara/Mini GG/Smile2.png", xalign=0.0, yalign=1.0))
    $ j_smile3 = Character(show_side_image=Image("Chara/Mini GG/Smile3.png", xalign=0.0, yalign=1.0))
    $ j_smile4 = Character(show_side_image=Image("Chara/Mini GG/Smile4.png", xalign=0.0, yalign=1.0))
    $ j_smile4_blush = Character(show_side_image=Image("Chara/Mini GG/Smile4_blush.png", xalign=0.0, yalign=1.0))
    $ j_smile_close = Character(show_side_image=Image("Chara/Mini GG/Smile_close.png", xalign=0.0, yalign=1.0))
    $ j_smile_close2 = Character(show_side_image=Image("Chara/Mini GG/Smile_close2.png", xalign=0.0, yalign=1.0))
    $ j_smile_close3 = Character(show_side_image=Image("Chara/Mini GG/Smile_close3.png", xalign=0.0, yalign=1.0))
    $ j_zol = Character(show_side_image=Image("Chara/Mini GG/Zol.png", xalign=0.0, yalign=1.0))
    $ j_udiv = Character(show_side_image=Image("Chara/Mini GG/Udiv.png", xalign=0.0, yalign=1.0))
    $ j_zolkapl = Character(show_side_image=Image("Chara/Mini GG/Zolkapl.png", xalign=0.0, yalign=1.0))
    
    
#==============Переменные=====================================
    $ korol_dal_karta = False
    $ korol_dal_money = False
    $ korol_dal_dokument = False
    $ money_gold = 0 # Эта переменная покажет, сколько у вас золота.
    $ money_silver = 0 # Эта переменная покажет, сколько у вас серебра.
    $ money_bronz = 0 # Эта переменная покажет, сколько у вас бронзы.
    $ first_start = False # Эта переменная нужна для перехода на второй скрипт.
    $ ludzem = 1 # Эта переменная покажет, сколько стран вы уже открыли.
    $ strana = u"Алинор" # Эта переменная указывает, в какой стране вы находитесь.
    $ alinor_stolica = True # Эти переменные покажут, в каких местах вы уже побывали.
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
    scene expression location_image 
    
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
        
screen location_buttons():
    imagebutton:
           idle 'Images/menu.png'
           hover 'Images/menuakt.png'
           focus_mask True
           action Jump("button_menu")
       
    for i in range(buttons_quantity):
        imagebutton:
            idle button_name[i]
            hover button_hover[i]
            focus_mask True
            action goto_button(i+1)
            
    for i in range (len(random_today)):
        if random_today[i][1] == this_location:
            imagebutton:
                xpos random_today[i][2] ypos random_today[i][3]
                idle 'Images/'+random_today[i][0]+'.png'
                hover 'Images/'+random_today[i][0]+'_hover.png'
                focus_mask True
                action NullAction()
    #frame:
    #   ymaximum 26
    #   xmaximum 297 
    #   xpos 400 ypos 200
    #   bar:
    #       left_bar "Images/hp_full.png"
    #       right_bar "Images/hp_empty.png"
    #       thumb_offset 7
    #       thumb 'Images/lol.png'
    #       ymaximum 26
    #       xmaximum 297 
    #       value AnimatedValue(value=your_hp, range=max_hp, delay=1.0) 
    #       range max_hp
    #   text "[your_hp]/[max_hp]" xalign 0.5 yalign 0.5

            
            
    
label button_menu:
    call call_menu
    jump expression gotoarray[0]