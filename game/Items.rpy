init -22 python:
    class Item:
        def __init__(self, name, description, picture, icon, mode, price):
            self.name = name
            self.description = description
            self.picture = 'Items/'+str(picture)+'.png'
            self.icon = 'Icons/'+str(icon)+'.png'
            self.mode = mode
            self.price = price
            
    class Food(Item):
        def __init__(self, name, description, picture, icon, mode, price):
            Item.__init__(self, name, description, picture, icon, mode, price)
            
#=============ИНВЕНТАРЬ===================

    class Inventar:
        def __init__(self, items):
            self.items = items
        
            self.weapon = []
            self.jeveler = []
            self.alchemy = []
            self.food = []
            self.drop = []
            self.paper = []
            
            for item in self.items:
                getattr(self, item[0].mode).append(item)

                
        def addItem(self, item, quantity): 
            for i in getattr(self, item.mode):
                if i[0] == item:
                    i[1] += quantity
                    break
            else:
                getattr(self, item.mode).append([item, quantity])
                
                
        def delItem(self,item, quantity):
            for i in getattr(self, item.mode):
                if i[0] == item:
                    i[1] -= quantity
                    if i[1] == 0:
                        getattr(self, item.mode).remove(i)
                    break
                    
#=============МАГАЗИН===================

    class Shop:
        def __init__(self, game_name, items, weapon, jeveler, alchemy, food, drop, paper):
            self.game_name = game_name
            self.items = items
        
            self.weapon = []
            self.jeveler = []
            self.alchemy = []
            self.food = []
            self.drop = []
            self.paper = []
        
            self.sell_weapon = weapon
            self.sell_jeveler = jeveler
            self.sell_alchemy = alchemy
            self.sell_food = food
            self.sell_drop = drop
            self.sell_paper = paper
            
            self.itemPrice = 0
           
            for item in self.items:
                getattr(self, item[0].mode).append(item)
                    
        def addItem(self, item, quantity): 
            for i in getattr(self, item.mode):
                if i[0] == item:
                    i[1] += quantity
                    break
            else:
                getattr(self, item.mode).append([item, quantity])
                                
        def delItem(self,item, quantity):
            for i in getattr(self, item.mode):
                if i[0] == item:
                    i[1] -= quantity
                    if i[1] == 0:
                        getattr(self, item.mode).remove(i)
                    break
                    
                    
                    
        def getGold(self):
            return self.itemPrice//2000
            
        def getSilver(self):
            money_without_gold = self.itemPrice - (self.itemPrice//2000) * 2000
            return money_without_gold//100
            
        def getBronze(self):
            money_without_gold = self.itemPrice - (self.itemPrice//2000) * 2000
            return money_without_gold%100
                    
#=============КОШЕЛЕК===================
    class Wallet:
        def __init__(self):
            self.money = 0
            
        def addMoney(self, gold, silver, bronze):
            self.money += bronze + silver*100 + gold*2000
            
        def delMoney(self, gold, silver, bronze):
            self.money -= bronze + silver*100 + gold*2000
            if self.money < 0:
                self.money += bronze + silver*100 + gold*2000
                return False
                
        def getGold(self):
            return self.money//2000
            
        def getSilver(self):
            money_without_gold = self.money - (self.money//2000) * 2000
            return money_without_gold//100
            
        def getBronze(self):
            money_without_gold = self.money - (self.money//2000) * 2000
            return money_without_gold%100
            
    wallet = Wallet()
                
                
            


    amy_cake = Food("Клубничное пироженное", "Небольшое сладкое пироженное, украшенное клубникой \nВосстанавливает 1 здоровья", "amy_cake", "cake", 'food', [0, 0, 5])
    amy_candies = Food("Кулек конфет", "Мешочек с вкусными желейными конфетами  \nВосстанавливает 1 здоровья", "amy_candies", "candy", 'food', [0, 0, 19])

    alinor_amy_shop = Shop('Лавка кондитера', [[amy_cake, 18], [amy_candies, 22]], False, False, False, True, False, False) #weapon, jeveler, alchemy, food, drop, paper

    inventory = Inventar([[amy_cake, 8]])



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
        $jack = ['smile', 'normal']
        show Jack at left with dissolve
        j "Эту бумагу я получил от короля. Она позволяет мне некие привелегии в моих поисках."
        $jack = ['smeh2', 'belt']
        j "Потрясная вещичка!"
        hide Jack with dissolve
        jump .akt
    if result == "Использовать":
        $jack = ['serdit', 'belt']
        show Jack at left with dissolve
        j "Как мне ее использовать?! Сжечь что ли?" 
        j "Нетушки!"
        hide Jack with dissolve
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
        $jack = ['smile', 'normal']
        show Jack at left with dissolve
        j "Это фотография Миары - жены поездного проводника."
        j "Я собираюсь отыскать ее, воссоединить семью, а заодно выбить себе бесплатный проезд!"
        hide Jack with dissolve
        jump .akt
    if result == "Использовать":
        $jack = ['nepon2', 'head_belt']
        show Jack at left with dissolve
        j "Хммммм......."
        $jack = ['duma', 'belt']
        j "Нет, я ее еще нигде не встречал."
        hide Jack with dissolve
        jump .akt
    if result == "Отмена":
        hide bitem
        hide itemmenu1 with easeoutright
        jump inventakt
