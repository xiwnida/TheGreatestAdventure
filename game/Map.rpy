init:
    $mapMode = "all"
    $mapIslands = False
    $mapMagic = False
    $mapAlinor = False
    
label callMap:
    call screen Map
    $ no_fade = True
    jump expression this_location

screen Map:
    button:
        xpos -1 ypos -1
        background "Map/bg.jpg"
        action NullAction()
        
    button:
        xpos -1 ypos -1
        background "Map/substrate.png"
        action NullAction()
    
    if mapMode == "all":
        button:
            xpos -1 ypos -1
            background "Map/allMap.png"
            action NullAction()
            
        imagebutton:
            idle "Map/People.png"
            hover "Map/PeopleAkt.png"
            focus_mask True
            action SetVariable("mapMode", "PeopleLands")
            
        imagebutton:
            insensitive "Map/IslandsGray.png"
            idle "Map/Islands.png"
            hover "Map/IslandsAkt.png"
            focus_mask True
            action [NullAction(), SensitiveIf(mapIslands)]
            
        imagebutton:
            insensitive "Map/MagicGray.png"
            idle "Map/MagicGray.png"
            hover "Map/MagicAkt.png"
            focus_mask True
            action [NullAction(), SensitiveIf(mapMagic)]
            
        imagebutton:
            idle "Map/back.png"
            hover "Map/backAkt.png"
            focus_mask True
            action [SetVariable("mapMode", "all"), Return()]
            
            
            
    elif mapMode == "PeopleLands":
        button:
            xpos -1 ypos -1
            background "Map/PeopleLands/map.png"
            action NullAction()
    
        imagebutton:
            idle "Map/back.png"
            hover "Map/backAkt.png"
            focus_mask True
            action SetVariable("mapMode", "all")
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/Alinor.png"
            hover "Map/PeopleLands/AlinorAkt.png"
            action [SensitiveIf(mapAlinor == False), SetVariable("mapAlinor", True)]
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/1.png"
            hover "Map/PeopleLands/1.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/2.png"
            hover "Map/PeopleLands/2.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/3.png"
            hover "Map/PeopleLands/3.png"
            action NullAction()
        
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/4.png"
            hover "Map/PeopleLands/4.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/5.png"
            hover "Map/PeopleLands/5.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/6.png"
            hover "Map/PeopleLands/6.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/7.png"
            hover "Map/PeopleLands/7.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/8.png"
            hover "Map/PeopleLands/8.png"
            action NullAction()
            
        imagebutton:
            focus_mask True
            idle "Map/PeopleLands/9.png"
            hover "Map/PeopleLands/9.png"
            action NullAction()
            
            
    #Места Алинора
        imagebutton:
            focus_mask True
            insensitive "Map/Null.png"
            idle "Map/PeopleLands/Alinor/Capital.png"
            hover "Map/PeopleLands/Alinor/Capital.png"
            action [SensitiveIf(mapAlinor), SetVariable("mapMode", "all"), SetVariable("no_fade", True), Jump("alinor_capital_plaza")]
            
        imagebutton:
            idle "Map/back.png"
            hover "Map/backAkt.png"
            focus_mask True
            action SetVariable("mapAlinor", False)
    
