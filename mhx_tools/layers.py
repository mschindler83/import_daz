# SPDX-FileCopyrightText: 2016-2026, Thomas Larsson
#
# SPDX-License-Identifier: GPL-2.0-or-later

import bpy

#-------------------------------------------------------------
#   MHX Layers
#-------------------------------------------------------------

L_MAIN =    "Root"
L_SPINE =   "Spine"

L_LARMIK =  "IK Arm Left"
L_LARMFK =  "FK Arm Left"
L_LLEGIK =  "IK Leg Left"
L_LLEGFK =  "FK Leg Left"
L_LHAND =   "Hand Left"
L_LFINGER = "Fingers Left"
L_LARM2IK = "IK Arm 2 Left"
L_LLEG2IK = "IK Leg 2 Left"
L_LTOE =    "Toes Left"

L_RARMIK =  "IK Arm Right"
L_RARMFK =  "FK Arm Right"
L_RLEGIK =  "IK Leg Right"
L_RLEGFK =  "FK Leg Right"
L_RHAND =   "Hand Right"
L_RFINGER = "Fingers Right"
L_RARM2IK = "IK Arm 2 Right"
L_RLEG2IK = "IK Leg 2 Right"
L_RTOE =    "Toes Right"

L_FACE =    "Face"
L_TWEAK =   "Tweak"
L_HEAD =    "Head"
L_SPINE2 =  "Spine 2"
L_CUSTOM =  "Custom"
L_CUSTOM2 = "Custom 2"

L_HELP =    "Help"
L_HELP2 =   "Help 2"
L_HIDDEN =   "Hidden"
L_DEF =     "Deform"


MhxLayers = {
    L_MAIN :    "Root",
    L_SPINE :   "Spine",

    L_LARMIK :  "IK Arm Left",
    L_LARMFK :  "FK Arm Left",
    L_LLEGIK :  "IK Leg Left",
    L_LLEGFK :  "FK Leg Left",
    L_LHAND :   "Hand Left",
    L_LFINGER : "Fingers Left",
    L_LARM2IK : "IK Arm 2 Left",
    L_LLEG2IK : "IK Leg 2 Left",
    L_LTOE :    "Toes Left",

    L_RARMIK :  "IK Arm Right",
    L_RARMFK :  "FK Arm Right",
    L_RLEGIK :  "IK Leg Right",
    L_RLEGFK :  "FK Leg Right",
    L_RHAND :   "Hand Right",
    L_RFINGER : "Fingers Right",
    L_RARM2IK : "IK Arm 2 Right",
    L_RLEG2IK : "IK Leg 2 Right",
    L_RTOE :    "Toes Right",

    L_FACE :    "Face",
    L_TWEAK :   "Tweak",
    L_HEAD :    "Head",
    L_SPINE2 :  "Spine 2",
    L_CUSTOM :  "Custom",
    L_CUSTOM2 : "Custom 2",

    L_HELP :    "Help",
    L_HELP2 :   "Help 2",
    L_DEF :     "Deform",
}

#-------------------------------------------------------------
#   Mha features
#-------------------------------------------------------------

F_TONGUE = 1
F_FINGER = 2
F_IDPROPS = 4
F_SPINE = 8
F_SHAFT = 16
F_NECK = 32


