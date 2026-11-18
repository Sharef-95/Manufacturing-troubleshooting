
import streamlit as st

from pathlib import Path


# Set website background to white

st.markdown("""
    <style>

        /* White background */
        .stApp {
            background-color: #FFFFFF;
        }
        /*  header color */
        [data-testid="stHeader"] {
            background-color: #00FFFF;
        }

        /*  sidebar color */
        [data-testid="stSidebar"] {
            background-color: #00FFFF;
        }

        /* Black text */
        .stApp p,
        .stApp h1,
        .stApp h2,
        .stApp h3 {
            color: #000000;
        }

        /* Font sizes */
        h1 {
            font-size: 26px !important;
        }

        h2 {
            font-size: 23px !important;
        }

        h3 {
            font-size: 30px !important;
        }

        .stApp p {
            font-size: 14px !important;
        }

        .stTextInput input {
            font-size: 14px !important;
        }

    </style>
""", unsafe_allow_html=True)



# Logo location
BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "assets" / "logo.png"


col1, col2 = st.columns([1, 5])

with col1:
    st.image(str(LOGO_PATH), width=100)

with col2:
    st.title("Manufacturing Troubleshooting")

"""
Vista Search Engine
------------------

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


    "What causes color registration error?": "Substrate slip, low vacuum level, or mechanical misalignment.",


    "How do you fix colour registration?": "Increase the vacuum level until the substrate is held flat and registration error is within tolerance.",

    "What is the registration tolerance?": "0.70 mm is the acceptable misregistration limit.",

    "vacuum level": "5 for magnets, 10 for sheets",


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






    