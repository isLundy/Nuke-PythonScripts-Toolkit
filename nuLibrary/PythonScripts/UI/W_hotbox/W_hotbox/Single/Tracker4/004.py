#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX
#
# NAME: Set to current frame
#
#----------------------------------------------------------------------------------------------------------

for node in nuke.selectedNodes():
    node.showControlPanel()
    
    for knob in node.allKnobs():
        if knob.label() == 'set to current frame':
            knob.execute()
    
    node.hideControlPanel()