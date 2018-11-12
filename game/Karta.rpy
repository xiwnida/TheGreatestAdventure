init:
    # Изображения
    image kartadalser = "Karta/dalser.jpg"
    image dallud = "Karta/dallud.jpg"
    image lud1 = "Karta/Lud/lud1.jpg"
    image lud3 = "Karta/Lud/lud3.png"

    
    # Названия
    # Алинор
    image alinor stolica = "Karta/Lud/Alinor/stolica.png"
    
    
label karta:
    scene dallud with fade
    $ result = renpy.imagemap("Karta/dallud.jpg", "Karta/dalludakt.jpg", [
    (30, 158, 359, 388, "Людские земли"),
    (697, 557, 799, 599, "Назад")
    ])
    if result == "Людские земли":
        jump lud
    if result == "Назад":
        return
        
# Блок для Людских Земель.        
        
label lud:
    scene lud1 with fade        
label lud1:
    if ludzem == 1:                # Указать страны, в которые можно поехать
        $ result = renpy.imagemap("Karta/Lud/lud1.jpg", "Karta/Lud/lud1akt.jpg", [
        (101, 422, 205, 516, "Алинор"),
        (697, 557, 799, 599, "Назад")
        ])
        if result == "Алинор":
            jump alinor_menu
        if result == "Назад":
            jump karta
            
            
    # Указать открытые названия   
    
label alinor_menu:            
    if strana == u"Алинор": 
        if alinor_stolica == True:
            show alinor stolica

            

        
            
    # Переход по местам в Алиноре
    
   
label alinor_menu2:    
    $ result = renpy.imagemap("Karta/Lud/lud3.png", "Karta/Lud/lud2.png", [
    (96, 434, 109, 444, "Столица"),
    (31, 414, 92, 426, "Столица"),
    (697, 557, 799, 599, "Назад")
    ])
    if result == "Столица":
        jump alinor_gorod
    if result == "Назад":
        jump lud1
    
    
    

