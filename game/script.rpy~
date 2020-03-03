# Здесь будет скрипт вашей визуальной новеллы.

# Отсюда начинается игра.
label start:
    play music "Music/Alinor/Vash_dom.ogg"
    $ muzika = "Alinor_vash_dom"
    scene dom with fade
    
    jump alinor_capital_gorod
    
    #$ test5 = [["Chara/GG/nepon.png", j_smile, "Фраза номер 1"], ["Chara/GG/smile.png", j_smile, "Фраза номер 2"], ["Chara/GG/smile_close.png", j_smile_close, "Фраза номер 3"], 0]
    #$ test6=test5[0]
    #$ test7=0
    #while test6 !=0:
    #    show expression test6[0]
    #    $lol6 = test6[2]
    #    $lol7 = test6[1]
    #    lol7 "[lol6]"
    #    $ test7+=1
    #    $ test6=test5[test7]
        
    
    "Это был обычный день, такой же, как и все."
    "Вы сидели в кресле у камина и отдыхали, размышляя над тем, как бы завтра подзаработать."
    #show jack smile at left with dissolve
    $jack = ['smile', 'normal']
    show Jack at left with dissolve
    j "Ох, ну и удачно сегодня сложились дела!"
    $jack[0] = 'smileclose2'
    j "Если бы каждый день приносил столько денег, я бы работал без выходных!"
    $jack = ['serdit','belt']
    j "К сожалению, работа по контракту не всегда выходит удачной."
    $jack = ['smile', 'normal']
    j "Ну да ладно, подумаю об этом завтра."
    j "А сейчас, пожалуй, пора спать."
    
    play sound "Music/stuk_v_dver.mp3"
    $ renpy.pause (6.0)
    
    $jack = ['duma', 'mouth']
    j "Хм? Кто это может быть так поздно?"
    hide Jack with dissolve
    "Вы подошли к двери и открыли ее."
    "Снаружи оказался почтальон, который передал вам письмо."
    "Вернувшись в уютную комнату и усевшись на кресло, вы распечатали письмо, вчитываясь в аккуратные рукописные строчки."
    
    $ renpy.pause (1.0)
    scene svitok1 with dissolve
    $ result = renpy.imagemap("Images/svitok1.jpg", "Images/svitok1_karta.jpg", [
    (254, 218, 546, 343, "Развернуть свиток")
    ])
    if result == "Развернуть свиток":
        jump svitok1

label svitok1:

    scene svitok2 with dissolve
    $ result = renpy.imagemap("Images/svitok2.jpg", "Images/svitok2_karta.jpg", [
    (258, 112, 540, 516, "Убрать свиток")
    ])
    if result == "Убрать свиток":
        jump svitok2
label svitok2:
    
    scene dom
    $jack = ["nepon", "belt"]
    show Jack at left with dissolve
    j "Ничего себе!"
    j "У короля ко мне какое то дело?"
    $jack = ["neponsmile", "head_belt"]
    j "Хе, неужели я настолько известен?"
    $jack = ["nepon", "normal"]
    j "Ладно, делать нечего, думай, не думай, идти придется."
    j "Надеюсь, мне не кинут какую то подставу..."
    hide Jack
    stop music
    
    scene black with dissolve
    $ renpy.pause (2.0)
    show naslutro with dissolve
    $ renpy.pause (4.0)
    hide naslutro with dissolve
    $ renpy.pause (1.0)
    
    scene sad dvorca with dissolve
    play music "Music/Alinor/stolica.ogg"
    $ muzika = "Alinor_stolica"
    $ renpy.pause (1.0)
    
    show jack norm at left with dissolve
    j_norm "И вот я тут..."
    j_norm "Всю ночь только и думал об этом, так и не смог уснуть..."
    j_norm "Как было написано в свитке, кто то должен меня встретить."
    "Вы оглядываетесь по сторонам."
    $ renpy.pause (1.0)
    show butler norm at right with dissolve
    butler "Джек, верно?"
    show jack neponsmile2 at left
    j_neponsmile2 "Да, это я."
    butler "Замечательно."
    butler "Прошу за мной."
    
    scene black with fade
    $ renpy.pause (1.0)
    
    scene koridor dvorca
    show jack smile2 at right
    show butler norm at left
    with fade
    j_smile2 "{i}Ничего себе!{/i}"
    j_smile2 "{i}Никогда не был во дворце.{/i}"
    j_smile2 "{i}Тут так просторно...{/i}"
    
    scene black with fade
    $ renpy.pause (1.0)
    
    scene kabinet dvorca
    show jack norm at left
    show butler norm at right
    with fade
    butler "Подождите тут, я оповещу Его Величество, что вы прибыли."
    j_norm "Понял."
    hide butler norm
    "Вы осторожно присели на диван, осматривая помещение."
    $ renpy.pause (1.0)
    show tenmin with dissolve
    $ renpy.pause (1.0)
    hide tenmin with dissolve
    $ renpy.pause (1.0)
    
    "Наконец дверь в кабинет отворилась снова."
    show korol norm at right with dissolve
    "Вы тут же подскочили на ноги."
    korol "Кхм. Я рад, что ты откликнулся на мое приглашение."
    j_norm "Это была честь для меня, Ваше Величество..."
    show jack neponsmile at left
    j_neponsmile "{i}Ага, как будто я мог просто взять и не придти.{/i}"
    show jack norm at left
    j_norm "В послании вы писали о каком то деле ко мне, Ваше Величество?"
    korol "Да, именно так... Не будем вести разговор стоя, прошу, присаживайся."
    "Его Величество проследовал к одному из диванов, противоположному тому, где находились вы, и опустился на подушки."
    "Вы последовали его примеру."
    korol "Так вот... люди поговаривают, что ты отличный сыщик. Можешь найти практически любого человека или предмет. Это так?"
    show jack neponsmile2 at left
    j_neponsmile2 "Нуу..."
    show jack smeh at left
    j_smeh "Я бы не осмелился подтверждать столь хвалебные слухи..."
    j_smeh "Но, пожалуй, они вполне правдивы."
    show jack smile2 at left
    j_smile2 "Прошу простить меня за наглость..."
    korol "Не стоит извинений."
    show jack smile at left
    korol "Не буду ходить вокруг да около. Я хочу, чтобы ты кое что для меня добыл."
    show jack neponsmile at left
    j_neponsmile "Ух ты... для вас лично, Ваше Величество?"
    korol "Именно так. И это крайне секретное дело. Поэтому я и говорю с тобой лично."
    show jack smile at left
    j_smile "Я весь во внимании."
    korol "Ты когда нибудь слышал о ягодах юности?"
    show jack duma at left
    j_duma "Совсем немного, Ваше Величество."
    j_duma "Я знаю, что они способны омолодить того, кто их съест. И что они очень редки, и о них ходят лишь слухи, но никакой конкретной информации."
    korol "Верно. Мне известно ровно столько же."
    korol "Собственно, в наших краях мало кто знает больше."
    j_duma "Рискну предположить, что вы хотите, чтобы я добыл их для вас?"
    korol "И снова верно. Именно это я и хочу тебе предложить."
    show jack neponsmile at left
    korol "Воздержись от ответа на минуту. Я прекрасно понимаю, что мое предложение на грани невозможного."
    korol "Поэтому ты имеешь полное право отказаться. Не стоит беспокоится о последствиях."
    korol "Если ты решишь не браться за это дело, то волен свободно покинуть дворец."
    korol "Но если ты все же решишь взяться за работу, я гарантирую тебе по истине королевское вознаграждение в случае успеха."
    korol "Сможешь жить припеваючи до конца своей жизни. Да еще и детям наследство останется."
    korol "Так что подумай. Я тебя не тороплю."
    show jack duma at left
    j_duma "{i}Хм. Предложение на миллион. С кучей трудностей и проблем, зато какие перспективы, ммм...{/i}"
    "Вы внимательно все обдумываете и решаете..."
    
    $ result = renpy.imagemap("Images/viborkorol.png", "Images/viborkorolkarta.png", [
    (185, 187, 620, 240, "Принять"),
    (185, 303, 615, 351, "Отклонить")
    ])
    if result == "Принять":
        jump prinyat
    elif result == "Отклонить":
        jump otklonit
    
label otklonit:
    show jack neponsmile2 at left
    j_neponsmile2 "Простите, Ваше Величество, я все же откажусь."
    j_neponsmile "Это задание, вероятно, займет не один год. Да я и за границу наших земель не выбирался ни разу в своей жизни."
    j_neponsmile "Вашему покорному слуге по душе менее опасная работенка, но чтобы ее было побольше."
    korol "Вот как."
    korol "Не буду лгать, я надеялся, что ты согласишься. Но ничего не поделаешь, это твой выбор."
    korol "Счастливо, Джек. Мой дворецкий проводит тебя до ворот."
    hide korol norm with dissolve
    $ renpy.pause (1.0)
    scene black with fade
    show konec1 with dissolve
    $ renpy.pause (3.0)
    hide konec1 with dissolve
    show konec2 with dissolve
    $ renpy.pause (3.0)
    hide konec2 with dissolve
    show konec3 with dissolve
    $ renpy.pause (2.0)


label prinyat:
    show jack smeh2 at left
    j_smeh2 "Я согласен!"
    show jack smile at left
    j_smile "Я найду для вас ягоды юности, сколько бы времени это ни заняло."
    "После ваших слов король заметно повеселел."
    korol "Это очень радует."
    korol "Правда, я искренне надеюсь, что ты успеешь до того, как кто-нибудь сменит меня на троне..."
    korol "Кхм, ну, в прочем, не важно."
    j_smile "Разрешите идти?"
    korol "Минутку, не торопись."
    korol "Энтузиазм - это замечательно, но путь до магических земель далек. Тебе потребуются средства... и кое что еще."
    "Его Величество поднялся с дивана, подошел к стоящему рядом столу и взял оттуда несколько предметов, после чего вернулся обратно."
    korol "Вот, взгляни."
    "Вы наклонились над столом."
    hide jack smile
    scene koroldal 
    with fade
label koroldal:
    if korol_dal_karta:
        if korol_dal_dokument:
            if korol_dal_money:
                jump koroldal1

    $ result = renpy.imagemap("Images/koroldal.jpg", "Images/koroldalakt.jpg", [
    (61, 110, 375, 372, "Карта"),
    (486, 124, 689, 320, "Допуск"),
    (349, 384, 498, 536, "Деньги")
    ])
    if result == "Карта":
        jump koroldalkarta
    elif result == "Допуск":
        jump koroldaldopusk
    elif result == "Деньги":
        jump koroldalmoney
        
label koroldalkarta:
    if korol_dal_karta == False:
        scene kartadalser with fade
        $ renpy.pause (1.0)
        show jack smile2 with dissolve
        j_smile2 "{i}О, вот это вещичка!{/i}"
        j_smile2 "{i}Эта карта мне очень пригодится, учитывая, что мой путь теперь лежит на самый край света!{/i}"
        $ korol_dal_karta = True
        $ ludzem = 1
        hide jack smile2
        scene koroldal with fade
        jump koroldal
    else:
        show jack duma with dissolve
        j_duma "{i}Я уже рассмотрел карту. Надо глянуть, что там еще.{/i}"
        hide jack duma
        jump koroldal
        
label koroldaldopusk:
    if korol_dal_dokument == False:
        scene dopusk with fade
        $ result = renpy.imagemap("Images/dopusk.jpg", "Images/dopuskakt.jpg", [
        (185, 80, 596, 516, "Свернуть")
        ])
        if result == "Свернуть":
            scene koroldal with fade
            show jack smeh2 with dissolve
            j_smeh2 "{i}Вот это да!{/i}"
            j_smeh2 "{i}С такой бумагой путешествовать по Людским Землям будет весьма удобно!{/i}"
            $ korol_dal_dokument = True
            hide jack smeh2
            jump koroldal
    else:
        show jack duma with dissolve
        j_duma "{i}Я уже рассмотрел королевский допуск. Надо глянуть, что там еще.{/i}"
        hide jack duma
        jump koroldal
        
label koroldalmoney:
    if korol_dal_money == False:
        "Вы проверяете кошелек."
        "Внутри оказывается большая горсть монет."
        show jack udiv with dissolve
        j_udiv "{i}Да тут на вскидку не меньше трех сотен монет!!!{/i}"
        j_udiv "{i}Я такой суммы не то, что в руках не держал, даже не видел никогда!{/i}"
        j_udiv "{i}Вот это спонсирование, ничего не скажешь!{/i}"
        hide jack udiv
        $ korol_dal_money = True
        jump koroldal
    else:
        show jack duma with dissolve
        j_duma "{i}Я уже рассмотрел кошелек. Надо глянуть, что там еще.{/i}"
        hide jack duma
        jump koroldal
        
label koroldal1:
    $ item1 = True
    $ wallet.addMoney(300, 0, 0)
    $ items.append("item_dopusk")
    scene kabinet dvorca
    show jack smile at left
    show korol norm at right
    with fade
    korol "С этим тебе будет легче путешествовать."
    j_smile "Полностью согласен!"
    korol "Ну, вот теперь, пожалуй, все."
    korol "У тебя есть какие то вопросы ко мне?"
    show jack duma at left
    j_duma "Хмм... да, наверное, нет."
    show jack smile at left
    j_smile "Все четко и ясно."
    "Король кивнул."
    korol "В таком случае, до встречи, Джек. Как я могу догадываться, не скорой. Но, надеюсь, она состоится."
    j_smile "Я приложу все силы к тому, чтобы так оно и было!"
    $ renpy.pause (1.0)
    hide korol norm with dissolve
    scene black with fade
    $ renpy.pause (1.0)
    scene sad dvorca
    show jack smile at left
    show butler norm at right
    with fade
    butler "Вот мы и у выхода."
    butler "Всего доброго."
    hide butler norm with dissolve
    show jack smeh2 at left
    j_smeh2 "Пока!"
    show jack smile at left
    j_smile "{i}Ну, мне тоже пора.{/i}"
    scene black with fade
    $ renpy.pause (1.0)
    
    
#==================Ворота в сад======================
label alinor_vorota_dvorca1:  
    $ location("Alinor", "vorota", "alinor_stolica")
    if first_start == False:
        show jack smile with dissolve
        "{i}Информация для справки.{/i}"
        "{i}У вас есть доступ к рюкзаку и карте. Для этого необходимо открыть меню, нажав на его краюшек в верхнем правом углу.{/i}"
        "{i}В рюкзаке хранятся все ваши вещи, которые вы будете получать по ходу путешествия.{/i}"
        "{i}Кроме того, в нем можно посмотреть, сколько у вас на данный момент монет (кошелек), узнать, у кого и какие задания вы взяли (блокнот), и проверить дату и ваше состояние (календарь).{/i}"
        "{i}Карта позволит вам узнать, где вы находитесь в данный момент, и в целом свериться с обстановкой.{/i}"
        call time2 from _call_time2
        show jack smeh2
        j_smeh2 "Такие дела!"
        show jack smile
        j_smile "Между прочим, сейчас неплохо было бы сходить домой, собрать пару походных комплектов одежды."
        hide jack smile with dissolve
        $ first_start = True
    $ buttons('vorota', ['alinor_vorota_dvorca1' , 'alinor_vorota_dvorca1.garden' , 'alinor_glavn_ul1'])
    jump alinor_vorota_dvorca1

    label .garden:
        show jack smile at left with dissolve
        j_smile "Сейчас мне незачем возвращаться."
        j_smile "Я приду сюда, когда вернусь из своего путешествия с ягодами юности!"
        hide jack smile with dissolve
        $ no_fade = True
        jump alinor_vorota_dvorca1


#==================Главная улица столицы======================
label alinor_glavn_ul1:
    $ location("Alinor", "ul_plaza", "alinor_stolica")
    $buttons('ul_plaza', ['alinor_glavn_ul1' , 'alinor_pereulok1' , 'alinor_vorota_dvorca1'])
jump alinor_glavn_ul1

#==================Переулок======================
label alinor_pereulok1:
    $ location("Alinor", "pereulok", "alinor_stolica")
    $buttons('pereulok', ['alinor_pereulok1' , 'alinor_gorod1' , 'alinor_glavn_ul1'])
jump alinor_pereulok1

#==================Торговая площадь======================
label alinor_gorod1: 
    $ location("Alinor", "trading_area", "alinor_stolica")
    $buttons('trading_area', ['alinor_gorod1' , 'alinor_ul_dom1' , 'alinor_pereulok1'])
jump alinor_gorod1

#==================Улица где дом Джека======================
label alinor_ul_dom1:
    $ location("Alinor", "ul_dom", "alinor_stolica")
    $buttons('ul_dom', ['alinor_ul_dom1' , 'alinor_vash_dom1' , 'alinor_gorod1'])
jump alinor_ul_dom1

#==================Дом Джека======================
label alinor_vash_dom1:
    $ location("Alinor", "dom", "alinor_vash_dom", True)
    $buttons('dom', ['alinor_vash_dom1' , 'alinor_dom_spal1' , 'alinor_ul_dom1'], True)
jump alinor_vash_dom1

#==================Спальня======================
label alinor_dom_spal1:
    scene alinor domspal
    if no_fade == False:
       with fade
    
label alinor_dom_spal10:
    $ result = renpy.imagemap("Images/Alinor/domspal.png", "Images/Alinor/domspalakt.png", [
    (705, 1, 731, 38, "Меню"),
    (224, 525, 629, 599, "В гостиную"),
    (500, 241, 750, 458, "Лечь на кровать"),
    (208, 53, 344, 398, "Собраться в путешествие"),
    (40, 235, 204, 327, "Осмотреть книги")
    ])
    if result == "Меню":
        call call_menu from _call_call_menu
    elif result == "В гостиную":
        if sobrat_veshi == True:
            if vzat_blank == True:
                if lech_na_krovat == True:
                    show jack smeh2 with dissolve
                    j_smeh2 "В путь!"
                    jump alinor_vash_dom2
                else:
                    show jack neponsmile2 with dissolve
                    j_neponsmile2 "Я ухожу так надолго... хочу еще чуть чуть побыть в своей комнате."
                    hide jack neponsmile2 with dissolve
                    jump alinor_dom_spal10
            else:
                show jack neponsmile2 with dissolve
                j_neponsmile2 "Прежде, чем уйти, я хочу осмотреться, может стоит взять что-нибудь еще?."
                hide jack neponsmile2 with dissolve
                jump alinor_dom_spal10
        else:
            show jack neponsmile2 with dissolve
            j_neponsmile2 "Прежде, чем уйти, мне нужно собраться в путешествие."
            hide jack neponsmile2 with dissolve
            jump alinor_dom_spal10
    if result == "Лечь на кровать":
        if lech_na_krovat == False:
            show jack hehe2 with dissolve
            j_hehe2 "Ох, моя любимая мягкая кровать. Я прощаюсь с тобой надолго..."
            show jack smile close
            j_smile_close "..."
            j_smile_close "Надо полежать на ней напоследок."
            hide jack smile close with dissolve
            "Вы ложитесь на свою кровать и валяетесь на мягком покрывале."
            "Вы лежите...{w} лежите......{w} лежите......."
            "................"
            scene black with fade
            $ renpy.pause (4.0, hard=True)
            scene alinor domspal 
            show jack zolkapl
            with vpunch
            j_zolkapl "Я УСНУЛ!!!"
            j_zolkapl "КАКОЙ СЕЙЧАС ГОД?!"
            call time2 from _call_time2_1
            show jack serdit
            $ renpy.pause (1.0)
            j_serdit "Солнце уже садится..."
            j_serdit "Это все из за того, что я не спал сегодня ночью."
            j_serdit "Делать нечего, нужно выходить прямо сейчас, чтобы не терять больше времени!"
            hide jack serdit with dissolve
            $ lech_na_krovat = True
            $ day_time='zakat'
            jump alinor_dom_spal10
        else:
            show jack serdit with dissolve
            j_serdit "Хватит лежать!"
            hide jack serdit with dissolve
            jump alinor_dom_spal10
    if result == "Собраться в путешествие":
        if sobrat_veshi == False:
            show jack smile with dissolve
            j_smile "Пожалуй, надену сразу одежду поудобней, возьму пару комплектов запасной..."
            show jack smeh
            j_smeh "...и носки! Много носков!"
            hide jack smeh with dissolve
            "Вы роетесь в шкафу, укладывая в рюкзак необходимые вещи."
            show jack smeh2 with dissolve
            j_smeh2 "Отлично! Теперь хоть на Северный Полюс!"
            hide jack smeh2 with dissolve
            $ sobrat_veshi = True
            jump alinor_dom_spal10
        else:
            show jack smile with dissolve
            j_smile "Я уже взял из шкафа все необходимое. Нет необходимости снова туда лезть."
            hide jack smile with dissolve
            jump alinor_dom_spal10
    if result == "Осмотреть книги":
        if vzat_blank == False:
            show jack smile with dissolve
            j_smile "Хм, может взять с собой книжку?"
            j_smile "Хотя, я их уже все прочитал."
            show jack smile2
            j_smile2 "Опа, а это же моя записная книжка, в которую я записывал с кем и какой у меня контракт."
            j_smile2 "Вот ее будет полезно прихватить."
            j_smile2 "Ну ка, сейчас заодно и продолжим..."
            show jack smeh
            j_smeh "Алинор... столица... нужно найти для Его Величества ягоды юности... обещана королевская награда..."
            j_smeh "Замечательно!"
            if sobrat_veshi == True:
                show jack smile with dissolve
                j_smile "Ну, пожалуй, можно отправляться."
                hide jack smile with dissolve
            else:
                hide jack smeh with dissolve
            $ vzat_blank = True
            jump alinor_dom_spal10
        else:
            show jack smile with dissolve
            j_smile "Или все же взять книжку..."
            j_smile "Все же нет."
            hide jack smile with dissolve
            jump alinor_dom_spal10
jump alinor_dom_spal1

#==================Дом Джека======================
label alinor_vash_dom2:
    $ location("Alinor", "dom", "alinor_vash_dom", True)
    $buttons('dom', ['alinor_vash_dom1' , 'alinor_dom_spal1' , 'alinor_ul_dom2'], True)
jump alinor_vash_dom2

#==================Улица где дом Джека======================
label alinor_ul_dom2:
    $ location("Alinor", "ul_dom", "alinor_stolica")
    $buttons('ul_dom', ['alinor_ul_dom1' , 'alinor_vash_dom2' , 'alinor_gorod2'])
jump alinor_ul_dom2

#==================Торговая площадь======================
label alinor_gorod2: 
    $ location("Alinor", "trading_area", "alinor_stolica")
    $buttons('ograb', ['alinor_gorod1' , 'alinor_ul_dom2' , 'vokzal_night_ograb'])
jump alinor_gorod2

#==================Ночной вокзал. Ограбление======================
label vokzal_night_ograb:

    scene voknight
    show vokname_alinornight
    with fade
    play music "Music/Alinor/Vok_night.ogg"
        
    show jack smile with dissolve
    j_smile "А вот и наш замечательный вокзал! Никогда не бывал тут ночью."
    show jack smile close3
    j_smile_close3 "Но не важно!"
    j_smile_close3 "Во имя славы и денег! Время отправляться в путь!"
    hide jack smile close3 with dissolve
    "С предвкушением славного путешествия, вы направляетесь к вагону проводника, чтобы обзавестись билетом."
    stop music fadeout 0.5
    play music "Music/Alinor/Ograblenie.ogg"
    extend "\n...но не тут то было."
    woman_voice "Эй, братишка!"
    j_nepon "А? Что?"
    show bangirl smile with dissolve
    bangirl_smile "Здравствуй. Едешь куда-то?"
    j_pohab "{i}Ооо, какая красотка!{/i}"
    extend "\n{i}Может она хочет поехать со мной путешествовать по миру?"
    j_smile "А то! Я отправляюсь в далекое путешествие."
    extend "\nНо не просто так."
    j_smile3 "Скажу тебе по секрету, я выполняю секретную миссию короля."
    bangirl_smile "Звучит очень интригующе..."
    show bangirl smile2
    bangirl_smile2 "Звучит очень интригующе...{fast} Не откажешь ли ты мне в толике подробностей?"
    j_pohab_close "Ох, это {i}очень{/i} секретная миссия, мне не дозволено говорить о ней. Она настолько важная, что за успешное выполнение король пообещал мне большую награду! И гонорар для выполнения дал!"
    j_smile4_blush "Однако... может я смогу рассказать про мою миссию, если ты составишь мне компанию в поездке."
    bangirl_smile2 "Какое прелестное предложение..."
    "Неожиданно вы слышите звук шагов."
    show bantop hah at right with dissolve
    bantop_hah "Действительно, прелестное."
    show bankid norm at left with dissolve
    bankid_norm "Может быть нам всем согласиться на него, хах?"
    j_serdit "Эй, а вы еще кто такие?"
    show bantop hah at right
    bantop_hah "Ха-ха. Догадайся с одного раза."
    j_nepon2 "Ммм... непонятные парни странноватого вида, которые просто проходили мимо, и прямо сейчас собираются идти дальше?"
    show bankid hah at left 
    show bantop hmur at right 
    bankid_hah "Хорошая попытка. Но не прокатит."
    bantop_hmur "Так что ты там говорил про гонорар, который дал тебе король?"
    j_nepon2 "Кхм..."
    j_nepon3 "Ничего. Я все нагнал."
    show bangirl hah 
    bangirl_hah "Ладно, хватит уже, не ломайся. Просто давай сюда свое золотишко, и разойдемся друзьями."
    j_serdit "{i}Так! Это тот самый час, когда мужчина должен быть мужчиной!{/i}"
    extend "{i}Я не могу дать им забрать мои кровные деньжата! Придется сражаться!{/i}"
    j_zol "Значит так! Если вы сейчас же не..."
    stop music fadeout 1.0
    show bantop cool at right
    bantop_cool "А, надоело мне в игрушки играть."
    play sound "Music/Punch.wav"
    show bantop fight at right with vpunch
    $ renpy.pause (1.0)
    play sound "Music/fall_body.wav"
    scene black with fade
    $ renpy.pause (3.0)
    show ograblenie with dissolve
    $ renpy.pause (1.5)
    hide ograblenie with dissolve
    
    call time2 from _call_time2_2
    
    man_voice "рень..."
    man_voice "Парень! Эй, парень!"
    j_nepon2 "А...Что за фигня?"
    scene voknight
    show vokname_alinornight
    show driver1 shock
    with fade
    play music "Music/Alinor/vok_night.ogg" fadein 1.0
    driver1_shock "Слава богу, ты жив. Ты в порядке, парень?"
    j_norm "Хммм... вроде да."
    show driver1 norm
    driver1_norm "Хорошо."
    extend "\nЕсли тебе нужна какая то помощь..."
    j_smile "Спасибо, но я действительно в порядке. Будет достаточно, если вы просто продадите мне билет, я ведь все таки собирался в путеше..."
    j_shock "А!"
    show driver1 udiv2
    j_shock2 "Минуточку!"
    "Вы резко спохватываетесь и проверяете свой рюкзак на наличие мешочка с золотом."
    j_zol "Нету!!!"
    show driver1 udiv
    driver1_udiv "Кажется, вас ограбили?"
    j_zol "Не кажется!"
    extend "\nМеня ограбили! Вот наглецы!"
    $wallet.delMoney(298, 0, 57)
    j_serdit "Ну и как мне теперь ехать на край света без единого гроша в кармане?"
    j_nepon2 "..."
    j_nepon2 "Вы меня зайцем не пропустите?"
    show driver1 norm
    driver1_norm "Меня тогда уволят."
    j_sad "{i}Эх. Ну и попал. Не пойду же я обратно к королю с рассказом о том, что меня ограбили.{/i}"
    j_sad "\n{i}А от задания отказываться совсем не вариант, да и не хочу я.{/i}"
    j_norm "{i}Придется где нибудь заработать.{/i}"
    j_duma "{i}В конце концов, не впервой же, просто найду какой нибудь контракт. Уж это я умею.{/i}"
    driver1_norm "Что делать будешь, парень?"
    j_smile "Заработаю деньжат, что же еще!"
    show driver1 duma
    driver1_duma "Ничего себе, быстрая смена настроения."
    j_smeh2 "Это мой стиль жизни!"
    j_smile "В общем так, мистер проводник, расскажите мне о расценках вашей компании."
    show driver1 norm
    driver1_norm "Ну, как ты наверняка знаешь, поезд ездит только по столицам стран Людских Земель."
    driver1_norm "Поездка в соседнюю страну будет стоить два золотых. Соответственно, чем дальше место назначения, тем дороже будет проезд."
    driver1_norm "Как то так."
    j_serdit "{i}Дофига!{/i}"
    j_serdit "{i}Когда я ездил на дилижансах, самое дорогое, что с меня сдирали, было семь серебрушек!{/i}"
    j_duma "{i}С тем гонораром проблем бы не было. Но если я буду искать деньги сам, то на это может уйти много времени.{/i}"
    j_nepon2 "{i}Хочу халявы!{/i}"
    j_nepon2 "..."
    j_nepon "{i}Хм, а если попробовать...{/i}"
    j_smile_close3 "Мистер проводник, а вот этот документ никак не поможет сбросить цену?"
    "Вы достаете допуск, данный вам королем."
    "Он не имеет никакого отношения к скидкам в поезде, но вы не теряете надежды."
    j_smile_close3 "Я работаю на короля, как вы видете, моя миссия подразумевает много странствий, то есть, другими словами, мне нужно ездить из города в город по {i}государственным{/i} причинам."
    driver1_norm "Хммм..."
    j_smile_close "{i}Ну же, соглашайся, иначе я разорюсь.{/i}"
    driver1_norm "Что ж, это резонно. Я поговорю с начальником, и думаю, что он согласится на скидку. Попробую выбить для тебя 50 процентов, то есть, будет достаточно одного золотого."
    j_zol "{i}Дофига! В смысле, дофига скинул!{/i}"
    j_zol "..."
    j_smile_close "Я вам очень признателен, спасибо."
    driver1_norm "Ага. Слушай, парень..."
    "Неожиданно проводник смотрит на вас очень внимательно."
    j_nepon "Да?"
    show driver1 duma
    driver1_duma "Ты же местный, так? Не поможешь мне с одной бедой? А я отблагодарю, оплачу за тебя проезд куда угодно."
    j_norm "Так, так. Что за беда?"
    driver1_duma "Жена у меня пропала."
    driver1_duma "Мы то с ней родом из соседней страны, Вейлена, но неделю назад она поехала со мной на поезде в Алинор, пошла прогуляться по столице, и не вернулась обратно."
    driver1_duma "Я искал ее несколько дней, но так и не смог найти. А дома меня ждет дочь, поэтому мне приходится вернуться..."
    show driver1 norm
    driver1_norm "Я, конечно, обязательно приеду снова, быть может она уже будет ждать меня тут, на вокзале..."
    driver1_norm "Но может быть ты все таки смог бы ее поискать?"
    j_sad "Ох... Это действительно ужасно, я сожалею вашему горю, мистер."
    j_norm "И я обязательно вам помогу. По правде, я всю жизнь работаю сыщиком, так что поиски людей для меня не впервой."
    j_norm "У вас есть фотография жены?"
    show driver1 shock
    driver1_shock "Да ну! Неужели небеса улыбнулись мне?! Как я рад, что встретил тебя, парень!"
    show driver1 udiv2
    driver1_udiv2 "Я буду надеется на тебя. Найди мою Миару, прошу. Вот ее фотография, я всегда ношу ее с собой."
    "Проводник вытащил из за пазухи небольшую фотокарточку и протянул вам."
    show bitem train_wife_foto with dissolve
    $ items.append("item_train_wife_foto")
    $ renpy.pause (1)
    "Вы рассматриваете фотографию, но женщина на ней вам, к сожалению, не знакома. Вы убираете фото в рюкзак."
    show driver1 norm
    hide bitem train_wife_foto with dissolve
    j_smile "Не беспокойтесь, мистер проводник, я отыщу ее для вас."
    driver1_norm "Спасибо тебе, парень. Ну ладно, в таком случае, еще увидимся. Я пойду, мне нужно осмотреть поезд перед отправлением."
    j_smile "Да, доброй ночи вам."
    hide driver1 norm with dissolve
    j_smile "{i}А я пойду ка, досплю уж до утра. А то гулять по ночам у меня, похоже, надолго желание отбилось.{/i}"
    scene black with dissolve
    $renpy.pause (3.0)
    $ in_home = True
    $ day_time='day'
    jump alinor_capital_dom_spal