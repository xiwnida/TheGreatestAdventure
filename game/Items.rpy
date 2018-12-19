init python:
    class Item:
        def __init__(self, name, description, picture, icon, mode):
            self.name=name
            self.description=description
            self.picture='Items/'+str(picture)+'.png'
            self.icon='Icons/'+str(icon)+'.png'
            self.mode=mode
            
    class Food(Item):
        def __init__(self, name, description, picture, icon, mode):
            Item.__init__(self, name, description, picture, icon, mode)


            
    class Shop:
        def __init__(self, system_name, game_name, items):
            self.ststem_name=system_name
            self.game_name=game_name
            self.items=items
        
            self.weapon=[]
            self.jeveler=[]
            self.alchemy=[]
            self.food=[]
            self.drop=[]
            self.paper=[]
        
            self.buy_weapon=False
            self.buy_jeveler=False
            self.buy_alchemy=False
            self.buy_food=False
            self.buy_drop=False
            self.buy_paper=False
        
            self.sell_weapon=False
            self.sell_jeveler=False
            self.sell_alchemy=False
            self.sell_food=False
            self.sell_drop=False
            self.sell_paper=False
            
            self.sorting()
        
        def sorting(self):
            
            self.weapon, self.jeveler, self.alchemy, self.food, self.drop, self.paper=[],[],[],[],[],[]
            self.buy_weapon, self.buy_jeveler, self.buy_alchemy, self.buy_food, self.buy_drop, self.buy_paper=False, False, False, False, False, False
            
            for i in range(len(self.items)):
                var=(self.items[i])[0].mode
                if var=='weapon':
                    self.buy_weapon=True
                    self.weapon.append(self.items[i])
                if var=='jeveler':
                    self.buy_jeveler=True
                    self.jeveler.append(self.items[i])
                if var=='alchemy':
                    self.buy_alchemy=True
                    self.alchemy.append(self.items[i])
                if var=='food':
                    self.buy_food=True
                    self.food.append(self.items[i])
                if var=='drop':
                    self.buy_drop=True
                    self.drop.append(self.items[i])
                if var=='paper':
                    self.buy_paper=True
                    self.paper.append(self.items[i])


    amy_cake=Food("Клубничное пироженное", "Небольшое сладкое пироженное, украшенное клубникой \nВосстанавливает 1 здоровья", "amy_cake", "cake", 'food')
    amy_candies=Food("Кулек конфет", "Мешочек с вкусными желейными конфетами  \nВосстанавливает 1 здоровья", "amy_candies", "candy", 'food')

    amy_shop=Shop('amy_shop', 'Лавка кондитера', [[amy_cake, 8], [amy_candies, 2]])




init:
    image bitem dopusk = "Invent/Bitems/dopusk.png"
    image itemmenu1 = "Invent/itemmenu1.png"
    image bitem train_wife_foto = "Invent/Bitems/foto1.png"

label items_menu1:
    show itemmenu1 at right with easeinright
    return
 
label item_dopusk: # Допуск, данный нам королем.
    show bitem dopusk
    call items_menu1 from _call_items_menu1
    label .akt:
    $ result = renpy.imagemap("Invent/itemmenu1.png", "Invent/Itemmenu1akt.png", [
    (607, 127, 770, 194, "Информация"),
    (607, 224, 770, 291, "Использовать"),
    (607, 321, 770, 388, "Отмена")
    ])
    if result == "Информация":
        show jack smile at left with dissolve
        j_smile "Эту бумагу я получил от короля. Она позволяет мне некие привелегии в моих поисках."
        show jack smeh2 at left
        j_smeh2 "Потрясная вещичка!"
        hide jack with dissolve
        jump .akt
    if result == "Использовать":
        show jack serdit at left with dissolve
        j_serdit "Как мне ее использовать?! Сжечь что ли?" 
        j_serdit "Нетушки!"
        hide jack with dissolve
        jump .akt
    if result == "Отмена":
        hide bitem
        hide itemmenu1 with easeoutright
        jump inventakt
    
label item_train_wife_foto:
    show bitem train_wife_foto
    call items_menu1 from _call_items_menu1_1
    label .akt:
    $ result = renpy.imagemap("Invent/itemmenu1.png", "Invent/Itemmenu1akt.png", [
    (607, 127, 770, 194, "Информация"),
    (607, 224, 770, 291, "Использовать"),
    (607, 321, 770, 388, "Отмена")
    ])
    if result == "Информация":
        show jack smile at left with dissolve
        j_smile "Это фотография Миары - жены поездного проводника."
        j_smile "Я собираюсь отыскать ее, воссоединить семью, а заодно выбить себе бесплатный проезд!"
        hide jack with dissolve
        jump .akt
    if result == "Использовать":
        show jack nepon2 at left with dissolve
        j_nepon2 "Хммммм......."
        show jack duma at left with dissolve
        j_duma "Нет, я ее еще нигде не встречал."
        hide jack with dissolve
        jump .akt
    if result == "Отмена":
        hide bitem
        hide itemmenu1 with easeoutright
        jump inventakt
