init:
    $inventory_active_mode='weapon'


screen inventory:
    button:
        background 'inventory/main.jpg'
        action NullAction()
        
    imagebutton:
        idle 'Inventory/cross.png'
        hover 'Inventory/cross_hover.png'
        focus_mask True
        action NullAction()
        
#Указатели====
        
    imagebutton:
        idle 'Inventory/pointer_up.png'
        hover'Inventory/pointer_up_hover.png'
        focus_mask True
        action NullAction()
    
    imagebutton:
        idle 'Inventory/pointer_down.png'
        hover'Inventory/pointer_down_hover.png'
        focus_mask True
        action NullAction()
        
#Кнопки действия=====
        
    imagebutton:
        idle 'Inventory/use_wear.png'
        hover 'Inventory/use_wear_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/use_eat.png'
        hover 'Inventory/use_eat_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/use_drink.png'
        hover 'Inventory/use_drink_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/use_look.png'
        hover 'Inventory/use_look_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/use_read.png'
        hover 'Inventory/use_read_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/item_down.png'
        focus_mask True
        action NullAction()
        
#Боковые кнопки=====

        
    imagebutton:
        idle 'Inventory/right_chara.png'
        hover 'Inventory/right_chara_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/right_inventory.png'
        hover 'Inventory/right_inventory_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/right_skills.png'
        hover 'Inventory/right_skills_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/right_journal.png'
        hover 'Inventory/right_journal_hover.png'
        focus_mask True
        action NullAction()
        
    imagebutton:
        idle 'Inventory/right_map.png'
        hover 'Inventory/right_map_hover.png'
        focus_mask True
        action NullAction()
        
#Иконки отделов=====
    hbox:
        xpos 730 ypos 30 xanchor 1.0
        imagebutton:
            idle 'Inventory/icon_sword.png'
            selected_idle 'Inventory/icon_sword_hover.png'
            selected_hover 'Inventory/icon_sword_hover.png'
            action [SelectedIf(inventory_active_mode=='weapon'), SetVariable('inventory_active_mode', 'weapon')]
            
        imagebutton:
            idle 'Inventory/icon_ring.png'
            selected_idle 'Inventory/icon_ring_hover.png'
            selected_hover 'Inventory/icon_ring_hover.png'
            action [SelectedIf(inventory_active_mode=='jeveler'), SetVariable('inventory_active_mode', 'jeveler')]

        imagebutton:
            idle 'Inventory/icon_bottle.png'
            selected_idle 'Inventory/icon_bottle_hover.png'
            selected_hover 'Inventory/icon_bottle_hover.png'
            action [SelectedIf(inventory_active_mode=='alchemy'), SetVariable('inventory_active_mode', 'alchemy')]

        imagebutton:
            idle 'Inventory/icon_bread.png'
            selected_idle 'Inventory/icon_bread_hover.png'
            selected_hover 'Inventory/icon_bread_hover.png'
            action [SelectedIf(inventory_active_mode=='food'), SetVariable('inventory_active_mode', 'food')]

        imagebutton:
            idle 'Inventory/icon_bone.png'
            selected_idle 'Inventory/icon_bone_hover.png'
            selected_hover 'Inventory/icon_bone_hover.png'
            action [SelectedIf(inventory_active_mode=='drop'), SetVariable('inventory_active_mode', 'drop')]

        imagebutton:
            idle 'Inventory/icon_paper.png'
            selected_idle 'Inventory/icon_paper_hover.png'
            selected_hover 'Inventory/icon_paper_hover.png'
            action [SelectedIf(inventory_active_mode=='paper'), SetVariable('inventory_active_mode', 'paper')]
