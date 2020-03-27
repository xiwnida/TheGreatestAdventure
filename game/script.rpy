# Здесь будет скрипт вашей визуальной новеллы.

# Отсюда начинается игра.

label start:
    play music "Music/Alinor/Vash_dom.ogg"
    $ muzika = "Alinor_vash_dom"
    scene expression "Images/alinor/capital/jackHome.jpg" with fade
    
    #jump alinor_capital_plaza
        
    "Это был обычный день, такой же, как и все."
    "Вы сидели в кресле у камина и отдыхали, размышляя над тем, как бы завтра подзаработать."
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
    
    scene expression "Images/alinor/capital/jackHome.jpg"
    $jack = ["nepon", "belt"]
    show Jack at left with dissolve
    j "Ничего себе!"
    j "У короля ко мне какое то дело?"
    $jack = ["neponsmile", "head_belt"]
    j "Хе, неужели я настолько известен?"
    $jack = ["nepon", "normal"]
    j "Ладно, делать нечего, думай, не думай, идти придется."
    j "Надеюсь, мне не кинут какую то подставу..."
    hide Jack  with dissolve
    stop music
    
    scene black with dissolve
    $ renpy.pause (2.0)
    show naslutro with dissolve
    $ renpy.pause (4.0)
    hide naslutro with dissolve
    $ renpy.pause (1.0)
    
    scene expression "Images/alinor/capital/sad_dvorca.jpg" with dissolve
    play music "Music/Alinor/stolica.ogg"
    $ muzika = "Alinor_stolica"
    $ renpy.pause (1.0)
    
    $jack = ["norm", "belt"]
    show Jack at left with dissolve
    j "И вот я тут..."
    j "Всю ночь только и думал об этом, так и не смог уснуть..."
    j "Как было написано в свитке, кто то должен меня встретить."
    "Вы оглядываетесь по сторонам."
    $ renpy.pause (1.0)
    show butler norm at right with dissolve
    butler "Джек, верно?"
    $jack = ["neponsmile2", "belt"]
    j "Да, это я."
    butler "Замечательно."
    butler "Прошу за мной."
    
    scene black with fade
    $ renpy.pause (1.0)
    
    scene expression "Images/alinor/capital/koridor1.jpg"
    $jack = ["smile2", "normal"]
    show Jack at right
    show butler norm at left
    with fade
    j "{i}Ничего себе!{/i}"
    j "{i}Никогда не был во дворце.{/i}"
    j "{i}Тут так просторно...{/i}"
    
    scene black with fade
    $ renpy.pause (1.0)
    
    scene expression "Images/alinor/capital/kabinet1.jpg"
    $jack = ["norm", "normal"]
    show Jack at left
    show butler norm at right
    with fade
    butler "Подождите тут, я оповещу Его Величество, что вы прибыли."
    j "Понял."
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
    j "Это была честь для меня, Ваше Величество..."
    $jack[0] = 'neponsmile'
    j "{i}Ага, как будто я мог просто взять и не придти.{/i}"
    $jack = ["norm", "normal"]
    j "В послании вы писали о каком то деле ко мне, Ваше Величество?"
    korol "Да, именно так... Не будем вести разговор стоя, прошу, присаживайся."
    "Его Величество проследовал к одному из диванов, противоположному тому, где находились вы, и опустился на подушки."
    "Вы последовали его примеру."
    korol "Так вот... люди поговаривают, что ты отличный сыщик. Можешь найти практически любого человека или предмет. Это так?"
    $jack[0] = 'neponsmile'
    j "Нуу..."
    $jack = ["smeh", "head_belt"]
    j "Я бы не осмелился подтверждать столь хвалебные слухи..."
    j "Но, пожалуй, они вполне правдивы."
    $jack = ["smile2", "normal"]
    j "Прошу простить меня за наглость..."
    korol "Не стоит извинений."
    $jack[0] = 'smile'
    korol "Не буду ходить вокруг да около. Я хочу, чтобы ты кое что для меня добыл."
    $jack[0] = 'neponsmile'
    j "Ух ты... для вас лично, Ваше Величество?"
    korol "Именно так. И это крайне секретное дело. Поэтому я и говорю с тобой лично."
    $jack[0] = 'smile'
    j "Я весь во внимании."
    korol "Ты когда нибудь слышал о ягодах юности?"
    $jack[0] = 'duma'
    j "Совсем немного, Ваше Величество."
    j "Я знаю, что они способны омолодить того, кто их съест. И что они очень редки, и о них ходят лишь слухи, но никакой конкретной информации."
    korol "Верно. Мне известно ровно столько же."
    korol "Собственно, в наших краях мало кто знает больше."
    $jack[1] = 'belt'
    j "Рискну предположить, что вы хотите, чтобы я добыл их для вас?"
    korol "И снова верно. Именно это я и хочу тебе предложить."
    $jack = ['neponsmile', 'normal']
    korol "Воздержись от ответа на минуту. Я прекрасно понимаю, что мое предложение на грани невозможного."
    korol "Поэтому ты имеешь полное право отказаться. Не стоит беспокоится о последствиях."
    korol "Если ты решишь не браться за это дело, то волен свободно покинуть дворец."
    korol "Но если ты все же решишь взяться за работу, я гарантирую тебе по истине королевское вознаграждение в случае успеха."
    korol "Сможешь жить припеваючи до конца своей жизни. Да еще и детям наследство останется."
    korol "Так что подумай. Я тебя не тороплю."
    $jack = ['duma', 'mouth']
    j "{i}Хм. Предложение на миллион. С кучей трудностей и проблем, зато какие перспективы, ммм...{/i}"
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
    $jack[1] = 'normal'
    $jack[0] = 'neponsmile2'
    j "Простите, Ваше Величество, я все же откажусь."
    j "Это задание, вероятно, займет не один год. Да я и за границу наших земель не выбирался ни разу в своей жизни."
    j "Вашему покорному слуге по душе менее опасная работенка, но чтобы ее было побольше."
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
    $jack[1] = 'belt'
    $jack[0] = 'smeh2'
    j "Я согласен!"
    $jack[0] = 'smile'
    j "Я найду для вас ягоды юности, сколько бы времени это ни заняло."
    "После ваших слов король заметно повеселел."
    korol "Это очень радует."
    korol "Правда, я искренне надеюсь, что ты успеешь до того, как кто-нибудь сменит меня на троне..."
    korol "Кхм, ну, в прочем, не важно."
    $jack[1] = 'normal'
    j "Разрешите идти?"
    korol "Минутку, не торопись."
    korol "Энтузиазм - это замечательно, но путь до магических земель далек. Тебе потребуются средства... и кое что еще."
    "Его Величество поднялся с дивана, подошел к стоящему рядом столу и взял оттуда несколько предметов, после чего вернулся обратно."
    korol "Вот, взгляни."
    "Вы наклонились над столом."
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
        scene expression "Images/dalser.jpg" with fade
        $ renpy.pause (1.0)
        $jack[0] = 'smile2'
        show Jack with dissolve
        j "{i}О, вот это вещичка!{/i}"
        j "{i}Эта карта мне очень пригодится, учитывая, что мой путь теперь лежит на самый край света!{/i}"
        $ korol_dal_karta = True
        $ ludzem = 1
        hide Jack with dissolve
        scene koroldal with fade
        jump koroldal
    else:
        $jack = ['duma', 'belt']
        show Jack with dissolve
        j "{i}Я уже рассмотрел карту. Надо глянуть, что там еще.{/i}"
        hide Jack with dissolve
        jump koroldal
        
label koroldaldopusk:
    if korol_dal_dokument == False:
        scene dopusk with fade
        $ result = renpy.imagemap("Images/dopusk.jpg", "Images/dopuskakt.jpg", [
        (185, 80, 596, 516, "Свернуть")
        ])
        if result == "Свернуть":
            scene koroldal with fade
            $jack = ['smeh2', 'belt']
            show Jack with dissolve
            j "{i}Вот это да!{/i}"
            j "{i}С такой бумагой путешествовать по Людским Землям будет весьма удобно!{/i}"
            $ korol_dal_dokument = True
            hide Jack with dissolve
            jump koroldal
    else:
        $jack = ['duma', 'belt']
        show Jack with dissolve
        j "{i}Я уже рассмотрел королевский допуск. Надо глянуть, что там еще.{/i}"
        hide Jack with dissolve
        jump koroldal
        
label koroldalmoney:
    if korol_dal_money == False:
        "Вы проверяете кошелек."
        "Внутри оказывается большая горсть монет."
        $jack = ['udiv', 'head_belt']
        show Jack with dissolve
        j "{i}Да тут на вскидку не меньше трех сотен монет!!!{/i}"
        j "{i}Я такой суммы не то, что в руках не держал, даже не видел никогда!{/i}"
        j "{i}Вот это спонсирование, ничего не скажешь!{/i}"
        hide Jack with dissolve
        $ korol_dal_money = True
        jump koroldal
    else:
        $jack = ['duma', 'belt']
        show Jack with dissolve
        j "{i}Я уже рассмотрел кошелек. Надо глянуть, что там еще.{/i}"
        hide Jack with dissolve
        jump koroldal
        
label koroldal1:
    $ item1 = True
    $ wallet.addMoney(300, 0, 0)
    $ items.append("item_dopusk")
    scene expression "Images/alinor/capital/kabinet1.jpg"
    $jack = ['smile', 'normal']
    show Jack at left
    show korol norm at right
    with fade
    korol "С этим тебе будет легче путешествовать."
    j "Полностью согласен!"
    korol "Ну, вот теперь, пожалуй, все."
    korol "У тебя есть какие то вопросы ко мне?"
    $jack = ['duma', 'mouth']
    j "Хмм... да, наверное, нет."
    $jack = ['smile', 'normal']
    j "Все четко и ясно."
    "Король кивнул."
    korol "В таком случае, до встречи, Джек. Как я могу догадываться, не скорой. Но, надеюсь, она состоится."
    $jack = ['smile', 'belt_forward']
    j "Я приложу все силы к тому, чтобы так оно и было!"
    $ renpy.pause (1.0)
    hide korol norm with dissolve
    scene black with fade
    $ renpy.pause (1.0)
    scene expression "Images/alinor/capital/sad_dvorca.jpg"
    $jack = ['smile', 'belt']
    show Jack at left
    show butler norm at right
    with fade
    butler "Вот мы и у выхода."
    butler "Всего доброго."
    hide butler norm with dissolve
    $jack[0] = 'smeh2'
    j "Пока!"
    $jack[0] = 'smile'
    j "{i}Ну, мне тоже пора.{/i}"
    $addChara(buttler_alinor, "Алинор", "Аранкар")
    $addChara(korol_alinor, "Алинор", "Аранкар")
    $buttler_alinor.name = "???"
    $buttler_alinor.reputation = 1
    $korol_alinor.name = "Джулио Третий"
    $korol_alinor.reputation = 5
    $korol_alinor.info.append("Не хочет терять престол.")
    $prolog_text = False
    scene black with fade
    $ renpy.pause (1.0)
    
    
    
#==================Ворота в сад======================
label alinor_capital_palaceGate_prolog:  
    $ location("alinor_capital_palaceGate_prolog", "alinor_stolica")
    if prolog_text == False:
        show Jack with dissolve
        "{i}Информация для справки.{/i}"
        "{i}У вас есть доступ к рюкзаку и карте. Для этого необходимо открыть меню, нажав на его краюшек в верхнем правом углу.{/i}"
        "{i}В рюкзаке хранятся все ваши вещи, которые вы будете получать по ходу путешествия.{/i}"
        "{i}Кроме того, в нем можно посмотреть, сколько у вас на данный момент монет (кошелек), узнать, у кого и какие задания вы взяли (блокнот), и проверить дату и ваше состояние (календарь).{/i}"
        "{i}Карта позволит вам узнать, где вы находитесь в данный момент, и в целом свериться с обстановкой.{/i}"
        $jack[0] = 'smeh2'
        j "Такие дела!"
        $jack[0] = 'smile'
        j "Между прочим, сейчас неплохо было бы сходить домой, собрать пару походных комплектов одежды."
        hide Jack with dissolve
        $ prolog_text = True
    $ buttons(['alinor_capital_garden_prolog' , 'alinor_capital_plaza_prolog'])
    jump alinor_capital_palaceGate_prolog

label alinor_capital_garden_prolog:
    $jack[0] = 'smile'
    show Jack at left with dissolve
    j "Сейчас мне незачем возвращаться."
    j "Я приду сюда, когда вернусь из своего путешествия с ягодами юности!"
    hide Jack with dissolve
    $ no_fade = True
    jump alinor_capital_palaceGate_prolog


#==================Главная улица столицы======================
label alinor_capital_plaza_prolog:
    $ location("alinor_capital_plaza_prolog", "alinor_stolica")
    $buttons(['alinor_capital_pereulok_prolog' , 'alinor_capital_palaceGate_prolog'])
jump alinor_capital_plaza_prolog

#==================Переулок======================
label alinor_capital_pereulok_prolog:
    $ location("alinor_capital_pereulok_prolog", "alinor_stolica")
    $buttons(['alinor_capital_tradingArea_prolog' , 'alinor_capital_plaza_prolog'])
jump alinor_capital_pereulok_prolog

#==================Торговая площадь======================
label alinor_capital_tradingArea_prolog: 
    $ location("alinor_capital_tradingArea_prolog", "alinor_stolica")
    $buttons(['alinor_capital_streetHome_prolog' , 'alinor_capital_pereulok_prolog'])
jump alinor_capital_tradingArea_prolog

#==================Улица где дом Джека======================
label alinor_capital_streetHome_prolog:
    $ location("alinor_capital_streetHome_prolog", "alinor_stolica")
    $buttons(['alinor_capital_jackHome_prolog' , 'alinor_capital_tradingArea_prolog'])
jump alinor_capital_streetHome_prolog

#==================Дом Джека======================
label alinor_capital_jackHome_prolog:
    $ location("alinor_capital_jackHome_prolog", "alinor_vash_dom", True)
    $buttons(['alinor_capital_jackBedroom_prolog' , 'alinor_capital_streetHome_prolog'], True)
jump alinor_capital_jackHome_prolog

#==================Спальня======================
label alinor_capital_jackBedroom_prolog:
    scene expression "Images/alinor/capital/jackBedroom.jpg"
    if no_fade == False:
       with fade
    
label alinor_dom_spal10:
    $ result = renpy.imagemap("Images/Alinor/domspal.png", "Images/Alinor/domspalakt.png", [
    (224, 525, 629, 599, "В гостиную"),
    (500, 241, 750, 458, "Лечь на кровать"),
    (208, 53, 344, 398, "Собраться в путешествие"),
    (40, 235, 204, 327, "Осмотреть книги")
    ])
    if result == "В гостиную":
        if sobrat_veshi == True:
            if vzat_blank == True:
                if lech_na_krovat == True:
                    $jack = ['smeh2', 'belt']
                    show Jack with dissolve
                    j "В путь!"
                    jump alinor_capital_jackHome_prolog2
                else:
                    $jack = ['neponsmile2', 'normal']
                    show Jack with dissolve
                    j "Я ухожу так надолго... хочу еще чуть чуть побыть в своей комнате."
                    hide Jack with dissolve
                    jump alinor_dom_spal10
            else:
                $jack = ['neponsmile2', 'belt']
                show Jack with dissolve
                j "Прежде, чем уйти, я хочу осмотреться, может стоит взять что-нибудь еще?."
                hide Jack with dissolve
                jump alinor_dom_spal10
        else:
            $jack = ['neponsmile2', 'belt']
            show Jack with dissolve
            j "Прежде, чем уйти, мне нужно собраться в путешествие."
            hide Jack with dissolve
            jump alinor_dom_spal10
    if result == "Лечь на кровать":
        if lech_na_krovat == False:
            $jack = ['hehe2', 'normal']
            show Jack with dissolve
            j "Ох, моя любимая мягкая кровать. Я прощаюсь с тобой надолго..."
            $jack = ['smileclose', 'head_belt']
            j "..."
            j "Надо полежать на ней напоследок."
            hide Jack with dissolve
            "Вы ложитесь на свою кровать и валяетесь на мягком покрывале."
            "Вы лежите...{w} лежите......{w} лежите......."
            "................"
            scene black with fade
            $ renpy.pause (4.0, hard=True)
            scene expression "Images/alinor/capital/jackBedroom.jpg"
            $jack = ['zolkapl', 'belt']
            show Jack 
            with vpunch
            j "Я УСНУЛ!!!"
            j "КАКОЙ СЕЙЧАС ГОД?!"
            $jack[0] = 'serdit'
            $ renpy.pause (1.0)
            j "Солнце уже садится..."
            $energy = 10
            j "Это все из за того, что я не спал сегодня ночью."
            j "Делать нечего, нужно выходить прямо сейчас, чтобы не терять больше времени!"
            hide Jack with dissolve
            $ lech_na_krovat = True
            jump alinor_dom_spal10
        else:
            $jack = ['serdit', 'belt']
            show Jack with dissolve
            j "Хватит лежать!"
            hide Jack with dissolve
            jump alinor_dom_spal10
    if result == "Собраться в путешествие":
        if sobrat_veshi == False:
            $jack = ['smile', 'normal']
            show Jack with dissolve
            j "Пожалуй, надену сразу одежду поудобней, возьму пару комплектов запасной..."
            $jack = ['smeh', 'belt']
            j "...и носки! Много носков!"
            hide Jack with dissolve
            "Вы роетесь в шкафу, укладывая в рюкзак необходимые вещи."
            $jack[0] = 'smeh2'
            show Jack with dissolve
            j "Отлично! Теперь хоть на Северный Полюс!"
            hide Jack with dissolve
            $ sobrat_veshi = True
            jump alinor_dom_spal10
        else:
            $jack = ['smile', 'normal']
            show Jack with dissolve
            j "Я уже взял из шкафа все необходимое. Нет необходимости снова туда лезть."
            hide Jack with dissolve
            jump alinor_dom_spal10
    if result == "Осмотреть книги":
        if vzat_blank == False:
            $jack = ['smile', 'normal']
            show Jack with dissolve
            j "Хм, может взять с собой книжку?"
            j "Хотя, я их уже все прочитал."
            $jack[0] = 'smile2'
            j "Опа, а это же моя записная книжка, в которую я записывал с кем и какой у меня контракт."
            j "Вот ее будет полезно прихватить."
            j "Ну ка, сейчас заодно и продолжим..."
            $jack = ['smeh', 'belt']
            j "Алинор... столица... нужно найти для Его Величества ягоды юности... обещана королевская награда..."
            j "Замечательно!"
            if sobrat_veshi == True:
                $jack = ['smile', 'belt']
                show Jack with dissolve
                j "Ну, пожалуй, можно отправляться."
                hide Jack with dissolve
            else:
                hide Jack with dissolve
            $ vzat_blank = True
            jump alinor_dom_spal10
        else:
            $jack = ['smile', 'normal']
            show Jack with dissolve
            j "Или все же взять книжку..."
            j "Все же нет."
            hide Jack with dissolve
            jump alinor_dom_spal10
jump alinor_capital_jackBedroom_prolog

#==================Дом Джека======================
label alinor_capital_jackHome_prolog2:
    $ location("alinor_capital_jackHome_prolog2", "alinor_vash_dom", True)
    $buttons(['alinor_capital_jackBedroom_prolog' , 'alinor_capital_streetHome_prolog2'], True)
jump alinor_capital_jackHome_prolog2

#==================Улица где дом Джека======================
label alinor_capital_streetHome_prolog2:
    $ location("alinor_capital_streetHome_prolog2", "alinor_stolica")
    $buttons(['alinor_capital_jackHome_prolog2' , 'alinor_capital_tradingArea_prolog2'])
jump alinor_capital_streetHome_prolog2

#==================Торговая площадь======================
label alinor_capital_tradingArea_prolog2: 
    $ location("alinor_capital_tradingArea_prolog2", "alinor_stolica")
    $buttons(['alinor_capital_streetHome_prolog2' , 'alinor_capital_vokzal_prolog'])
jump alinor_capital_tradingArea_prolog2

#==================Ночной вокзал. Ограбление======================
label alinor_capital_vokzal_prolog:

    scene expression "Images/Vok/voknoch.jpg"
    show vokname_alinornight
    with fade
    play music "Music/Alinor/Vok_night.ogg"
        
    $jack = ['smile', 'normal']
    show Jack with dissolve
    j "А вот и наш замечательный вокзал! Никогда не бывал тут ночью."
    $jack =[ 'smileclose3', 'belt']
    j "Но не важно!"
    j "Во имя славы и денег! Время отправляться в путь!"
    hide Jack with dissolve
    "С предвкушением славного путешествия, вы направляетесь к вагону проводника, чтобы обзавестись билетом."
    stop music fadeout 0.5
    play music "Music/Alinor/Ograblenie.ogg"
    extend "\n...но не тут то было."
    woman_voice "Эй, братишка!"
    $jack = ['nepon', 'normal']
    j "А? Что?"
    show bangirl smile with dissolve
    bangirl_smile "Здравствуй. Едешь куда-то?"
    $jack[0] = 'pohab'
    j "{i}Ооо, какая красотка!{/i}"
    $jack[1] = 'head'
    extend "\n{i}Может она хочет поехать со мной путешествовать по миру?"
    $jack = ['smile', 'normal']
    j "А то! Я отправляюсь в далекое путешествие."
    extend "\nНо не просто так."
    $jack[0] = 'smile3'
    j "Скажу тебе по секрету, я выполняю секретную миссию короля."
    bangirl_smile "Звучит очень интригующе..."
    show bangirl smile2
    bangirl_smile2 "Звучит очень интригующе...{fast} Не откажешь ли ты мне в толике подробностей?"
    $jack[0] = 'pohabclose'
    j "Ох, это {i}очень{/i} секретная миссия, мне не дозволено говорить о ней. Она настолько важная, что за успешное выполнение король пообещал мне большую награду! И гонорар для выполнения дал!"
    $jack[0] = 'smile3brush'
    j "Однако... может я смогу рассказать про мою миссию, если ты составишь мне компанию в поездке."
    bangirl_smile2 "Какое прелестное предложение..."
    "Неожиданно вы слышите звук шагов."
    show bantop hah at right with dissolve
    bantop_hah "Действительно, прелестное."
    show bankid norm at left with dissolve
    bankid_norm "Может быть нам всем согласиться на него, хах?"
    $jack[0] = 'serdit'
    j "Эй, а вы еще кто такие?"
    show bantop hah at right
    bantop_hah "Ха-ха. Догадайся с одного раза."
    $jack[0] = 'nepon2'
    j "Ммм... непонятные парни странноватого вида, которые просто проходили мимо, и прямо сейчас собираются идти дальше?"
    show bankid hah at left 
    show bantop hmur at right 
    bankid_hah "Хорошая попытка. Но не прокатит."
    bantop_hmur "Так что ты там говорил про гонорар, который дал тебе король?"
    j "Кхм..."
    $jack[0] = 'nepon3'
    j "Ничего. Я все нагнал."
    show bangirl hah 
    bangirl_hah "Ладно, хватит уже, не ломайся. Просто давай сюда свое золотишко, и разойдемся друзьями."
    $jack[0] = 'serdit'
    j "{i}Так! Это тот самый час, когда мужчина должен быть мужчиной!{/i}"
    extend "{i}Я не могу дать им забрать мои кровные деньжата! Придется сражаться!{/i}"
    $jack[0] = 'zol'
    j "Значит так! Если вы сейчас же не..."
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
    
    man_voice "рень..."
    man_voice "Парень! Эй, парень!"
    $jack[0] = 'nepon2'
    j "А...Что за фигня?"
    scene expression "Images/Vok/voknoch.jpg"
    show vokname_alinornight
    show driver1 shock
    with fade
    play music "Music/Alinor/vok_night.ogg" fadein 1.0
    driver1_shock "Слава богу, ты жив. Ты в порядке, парень?"
    $jack[0] = 'norm'
    j "Хммм... вроде да."
    show driver1 norm
    driver1_norm "Хорошо."
    extend "\nЕсли тебе нужна какая то помощь..."
    $jack[0] = 'smile'
    j "Спасибо, но я действительно в порядке. Будет достаточно, если вы просто продадите мне билет, я ведь все таки собирался в путеше..."
    $jack[0] = 'shock'
    j "А!"
    show driver1 udiv2
    $jack[0] = 'shock2'
    j "Минуточку!"
    "Вы резко спохватываетесь и проверяете свой рюкзак на наличие мешочка с золотом."
    $jack[0] = 'zol'
    j "Нету!!!"
    show driver1 udiv
    driver1_udiv "Кажется, вас ограбили?"
    j "Не кажется!"
    extend "\nМеня ограбили! Вот наглецы!"
    $wallet.delMoney(299, 12, 57)
    $jack[0] = 'serdit'
    j "Ну и как мне теперь ехать на край света без единого гроша в кармане?"
    $jack[0] = 'nepon2'
    j "..."
    j "Вы меня зайцем не пропустите?"
    show driver1 norm
    driver1_norm "Меня тогда уволят."
    $jack[0] = 'sad'
    j "{i}Эх. Ну и попал. Не пойду же я обратно к королю с рассказом о том, что меня ограбили.{/i}"
    j "{i}А от задания отказываться совсем не вариант, да и не хочу я.{/i}"
    $jack[0] = 'norm'
    j "{i}Придется где нибудь заработать.{/i}"
    j "{i}В конце концов, не впервой же, просто найду какой нибудь контракт. Уж это я умею.{/i}"
    driver1_norm "Что делать будешь, парень?"
    $jack[0] = 'smile'
    j "Заработаю деньжат, что же еще!"
    show driver1 duma
    driver1_duma "Ничего себе, быстрая смена настроения."
    $jack[0] = 'smeh2'
    j "Это мой стиль жизни!"
    $jack[0] = 'smile'
    j "В общем так, мистер проводник, расскажите мне о расценках вашей компании."
    show driver1 norm
    driver1_norm "Ну, как ты наверняка знаешь, поезд ездит только по столицам стран Людских Земель."
    driver1_norm "Поездка в соседнюю страну будет стоить два золотых. Соответственно, чем дальше место назначения, тем дороже будет проезд."
    driver1_norm "Как то так."
    $jack[0] = 'serdit'
    j "{i}Дофига!{/i}"
    j "{i}Когда я ездил на дилижансах, самое дорогое, что с меня сдирали, было семь серебрушек!{/i}"
    $jack[0] = 'duma'
    j "{i}С тем гонораром проблем бы не было. Но если я буду искать деньги сам, то на это может уйти много времени.{/i}"
    $jack[0] = 'nepon2'
    j "{i}Хочу халявы!{/i}"
    j "..."
    $jack[0] = 'nepon'
    j "{i}Хм, а если попробовать...{/i}"
    $jack[0] = 'smileclose3'
    j "Мистер проводник, а вот этот документ никак не поможет сбросить цену?"
    "Вы достаете допуск, данный вам королем."
    "Он не имеет никакого отношения к скидкам в поезде, но вы не теряете надежды."
    j "Я работаю на короля, как вы видете, моя миссия подразумевает много странствий, то есть, другими словами, мне нужно ездить из города в город по {i}государственным{/i} причинам."
    driver1_norm "Хммм..."
    $jack[0] = 'smileclose'
    j "{i}Ну же, соглашайся, иначе я разорюсь.{/i}"
    driver1_norm "Что ж, это резонно. Я поговорю с начальником, и думаю, что он согласится на скидку. Попробую выбить для тебя 50 процентов, то есть, будет достаточно одного золотого."
    $jack[0] = 'zol'
    j "{i}Дофига! В смысле, дофига скинул!{/i}"
    j "..."
    $jack[0] = 'smileclose'
    j "Я вам очень признателен, спасибо."
    driver1_norm "Ага. Слушай, парень..."
    "Неожиданно проводник смотрит на вас очень внимательно."
    $jack[0] = 'nepon'
    j "Да?"
    show driver1 duma
    driver1_duma "Ты же местный, так? Не поможешь мне с одной бедой? А я отблагодарю, оплачу за тебя проезд куда угодно."
    $jack[0] = 'norm'
    j "Так, так. Что за беда?"
    driver1_duma "Жена у меня пропала."
    driver1_duma "Мы то с ней родом из соседней страны, Вейлена, но неделю назад она поехала со мной на поезде в Алинор, пошла прогуляться по столице, и не вернулась обратно."
    driver1_duma "Я искал ее несколько дней, но так и не смог найти. А дома меня ждет дочь, поэтому мне приходится вернуться..."
    show driver1 norm
    driver1_norm "Я, конечно, обязательно приеду снова, быть может она уже будет ждать меня тут, на вокзале..."
    driver1_norm "Но может быть ты все таки смог бы ее поискать?"
    $jack[0] = 'sad'
    j "Ох... Это действительно ужасно, я сожалею вашему горю, мистер."
    $jack[0] = 'norm'
    j "И я обязательно вам помогу. По правде, я всю жизнь работаю сыщиком, так что поиски людей для меня не впервой."
    j "У вас есть фотография жены?"
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
    $jack[0] = 'smile'
    j "Не беспокойтесь, мистер проводник, я отыщу ее для вас."
    driver1_norm "Спасибо тебе, парень. Ну ладно, в таком случае, еще увидимся. Я пойду, мне нужно осмотреть поезд перед отправлением."
    j "Да, доброй ночи вам."
    hide driver1 norm with dissolve
    j "{i}А я пойду ка, досплю уж до утра. А то гулять по ночам у меня, похоже, надолго желание отбилось.{/i}"
    scene black with dissolve
    $renpy.pause (3.0)
    $ in_home = True
    $ energy = 100
    $addChara(bandit_girl_alinor, "Алинор", "Аранкар")
    $addChara(bandit_kid_alinor, "Алинор", "Аранкар")
    $addChara(bandit_man_alinor, "Алинор", "Аранкар")
    $bandit_girl_alinor.name = "???"
    $bandit_kid_alinor.name = "???"
    $bandit_man_alinor.name = "???"
    $bandit_girl_alinor.reputation = -1
    $bandit_kid_alinor.reputation = -1
    $bandit_man_alinor.reputation = -1 
    $addChara(driver1_alinor, "Вейлен", "Сильвенар")
    $addChara(miara_alinor, "Вейлен", "Сильвенар")
    $driver1_alinor.reputation = 11
    $driver1_alinor.info.append("Семья: жена и дочь.")
    $miara_alinor.info.append("Семья: муж и дочь.")
    $first_start = False
    jump alinor_capital_jackBedroom