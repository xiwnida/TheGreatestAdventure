init python:
    
    
    def location(city, loca, music, inside=False): #Название города, название фона, время суток, название музыки
        global location_image
        global day_time
        if not inside:
            location_image = "Images/"+str(city)+"/"+str(loca)+"_"+str(day_time)+".jpg"
        else:
            location_image = "Images/"+str(city)+"/"+str(loca)+".jpg"
        global muz
        muz=music
        
        
    def buttons(name, quantity, goto_array): # Дописать закатные кнопки
        global button_name
        global button_hover
        global buttons_quantity
        global gotoarray
        button_name=[]
        button_hover=[]
        buttons_quantity=quantity
        gotoarray=goto_array
        for i in range(quantity):
            button_name.append("Images/Alinor/"+str(name)+str(i+1)+".png")
            button_hover.append("Images/Alinor/"+str(name)+str(i+1)+"akt.png")

init:

#=====================Фоны=====================================
    image dom = "Images/Alinor/dom_gamestart.jpg"
    image sad dvorca = "Images/Alinor/sad_dvorca.jpg"
    image koridor dvorca = "Images/Alinor/koridor1.jpg"
    image kabinet dvorca = "Images/Alinor/kabinet1.jpg"
    image kabinet dvorca1 = "Images/Alinor/kabinet2.jpg"
    image sad dvorca1 = "Images/Alinor/sad_dvorca1.jpg"
    image vorota dvorca = "Images/Alinor/vorota_day.jpg"
    image vorota dvorca zakat = "Images/Alinor/vorota_zakat.jpg"
    image alinor stolploshad = "Images/Alinor/ul2_day.jpg"
    image alinor stolploshadzakat = "Images/Alinor/ul2_zakat.jpg"
    image alinor ulvashdom = "Images/Alinor/ul1_day.jpg"
    image alinor ulvashdomzakat = "Images/Alinor/ul1_zakat.jpg"
    image alinor glavul = "Images/Alinor/ul3_day.jpg"
    image alinor vashdom = "Images/Alinor/dom1.jpg"
    image alinor domspal = "Images/Alinor/dom_spal.jpg"
    image alinor pereulok = "Images/Alinor/ul_day.jpg"
    image alinor pereulokzakat = "Images/Alinor/ul4_zakat.jpg"
    image alinor cerkov = "Images/Alinor/cerkov_day.jpg"
    image alinor cerkovzakat = "Images/Alinor/cerkov_zakat.jpg"
    
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
    $ muz = "Nope" # Эта переменная нужна, чтобы задать музыку в локации.
    $ muzika = "Nope" #  А эта переменная нужна, чтобы запустить ее.
    $ muz_title = "Nope" # Эта переменная хранит адреса музыки.
    $ event = "Nope" # Эта переменная отвечает за одноразовые события.
    $ no_fade = False # Эта переменная нужна, чтобы после отключения меню не сработал fade эффект (ох, костыли!)
    $ scene_p = "Nope" # Эта переменная нужна, чтобы показать нужную сцену перед иммедж картой
    $ day_time = "day" # Эта переменная нужна, чтобы включить закатную сцену вечером
    
    $ gotoarray = [] # Этот массив нужен для переадресации с кнопок на нужные лейблы
    $ buttons_quantity = 0 # В эту переменную на каждой локе заносится количество кнопок
    $ button_name = [] # Массив с иддл-именами кнопок
    $ button_hover = [] # Массив с ховер-именами кнопок
    
    $location_image=''

#==============Колл. Показывает изображение, чье название собрано функцией location====================
    
label location:
    show expression location_image 

    if muz=="alinor_stolica":
        $ muz_title = "Music/Alinor/stolica.ogg"
    elif muz=="Alinor_vash_dom":
        $ muz_title= "Music/Alinor/Vash_dom.ogg"
        
    if not no_fade:
        with fade
    else:
        $ no_fade = False
    
    if muzika == muz: #Если играющая музыка равна новой музыке
        pass
    else:
        play music muz_title
        $ muzika = muz
    return

#=========================
        
screen imagebutton_example(): #ПРОВЕРКА-------СДЕЛАТЬ WHILE В ЭКРАНЕ. И СДЕЛАТЬ ССЫЛКИ НА ЛЕЙБЛЫ В ПЕРЕМЕННЫХ, ДЛЯ ЭТОГО ОТРЕДАЧИТЬ ФУНКЦИЮ
    imagebutton:
           idle 'Images/menu.png'
           hover 'Images/menuakt.png'
           focus_mask True
           action Jump("button_menu")
            
    if buttons_quantity>0:
        imagebutton:
            idle button_name[0]
            hover button_hover[0]
            focus_mask True
            action Jump("button_one")
            
    if buttons_quantity>1:
        imagebutton:
            idle button_name[1]
            hover button_hover[1]
            focus_mask True
            action Jump("button_two")
            
    if buttons_quantity>2:
        imagebutton:
            idle button_name[2]
            hover button_hover[2]
            focus_mask True
            action Jump("button_three")
            
    if buttons_quantity>3:
        imagebutton:
            idle button_name[3]
            hover button_hover[3]
            focus_mask True
            action Jump("button_four")
            
    if buttons_quantity>4:
        imagebutton:
            idle button_name[4]
            hover button_hover[4]
            focus_mask True
            action Jump("button_five")
            
    if buttons_quantity>5:
        imagebutton:
            idle button_name[5]
            hover button_hover[5]
            focus_mask True
            action Jump("button_six")
            
    
label button_menu:
    call call_menu
    jump expression gotoarray[0]
label button_one:
    jump expression gotoarray[0]+gotoarray[1]
label button_two:
    jump expression gotoarray[0]+gotoarray[2]
label button_three:
    jump expression gotoarray[0]+gotoarray[3]
label button_four:
    jump expression gotoarray[0]+gotoarray[4]
label button_five:
    jump expression gotoarray[0]+gotoarray[5]
label button_six:
    jump expression gotoarray[0]+gotoarray[6]