import streamlit as st
st.title("Manufacturing Troubleshooting Guide")

"""
Vista Search Engine
------------------
You fill in the questions and answers below.
Type a question -> get the answer.
"""
from rapidfuzz import fuzz
from Rigid1 import Rigid1
from Rigid2 import Rigid2
from Rigid4 import Rigid4
from R2R import R2R
from EFI1 import EFI1
from EFI2 import EFI2
from R2R_Cutter import R2R_Cutter
from Rigid1_Cutter import Rigid1_Cutter
from Rigid2_Cutter import Rigid2_Cutter
from Rigid4_Cutter import Rigid4_Cutter
from Eurolaser import Eurolaser

Rigid1()
Rigid2()
Rigid4()
R2R()
EFI1()
EFI2()
R2R_Cutter()
Rigid1_Cutter()
Rigid2_Cutter()
Rigid4_Cutter()
Eurolaser()












# ======================================================================
# FILL THIS UP  --  add as many question/answer pairs as you want
# ======================================================================
QA_DATA = {
    "color registration": "check vacuum level.",

     "colour registration": "check vacuum level.",

    "What causes color registration error?": "Substrate slip, low vacuum level, or mechanical misalignment.",

    "How do you fix color registration?": "Increase the vacuum level until the substrate is held flat and registration error is within tolerance.",

    "How do you fix colour registration?": "Increase the vacuum level until the substrate is held flat and registration error is within tolerance.",

    "What is the registration tolerance?": "0.70 mm is the acceptable misregistration limit.",

    "vacuum level": "5 for magnets, 10 for sheets",

    "What is the max vacuum level?": "10.",

    "What is the vacuum level for magnets?": "5.",

    "What is the vacuum level for foamboard?": "10.",

    "What is the vacuum level for lawnsign?": "10.",

    "What is the vacuum level for foamboards?": "10.",

    "What's the vacuum level for lawnsigns ?": "10.",

    "material slipping ": "Increase vacuum level",

    "Feeding issues ": "take the sheet out, and re-feed it. If the problem persists, call maintenance. ",



    "crooked sheet, skewed sheet": "Increase vacuum level, If the problem persists, call maintenance.",

    "banding, ink spray, missing ink":"short purge, dry wipe printheads",

    

    

    

    

    

    # <-- keep adding your own below this line
}






    