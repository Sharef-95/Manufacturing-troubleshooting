from spellchecker import SpellChecker
from rapidfuzz import fuzz
import streamlit as st

spell = SpellChecker()

QA_DATA = { 


"Drying Issues": "Call maintenance.",

"Lois Sensor Issue": "Call maintenance.",

"Vacuum Issues": "Adjust the vacuum to the desired setting for the media.\n\n"
"For decals, adjust the vacuum setting between 3 and 5.",

"frozen": "Restart the DURST app.",

"Banding": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"If banding is still present after wiping, call your supervisor/PC.",

"Computer Frozen": "Restart the DURST program.",

"Door Issues": "Open the door and re-close it gently.",

"Initialization Issues": "Step 1: Go to the Printer tab.\n\n"
"Step 2: Click Initialize Sledge.\n\n"
"Step 3: Click Initialize Printer.\n\n"
"If it still does not initialize, restart the machine.",

"Missing Nozzles": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"If nozzles are still missing, call your supervisor.",

"Purge Tub Error": "Open the purge tub and re-close it gently.",

"Registration Issues": "Check the vacuum setting.",

"UV Issues": "Go to the Printer tab, turn the UV lamp off, and turn it back on.\n\n"
"If it doesn't work, restart the machine.\n\n"
"If it is still not working after restarting the machine, call maintenance.",

"Blurry Barcodes": "Check the vacuum settings.\n\n"
"Adjust the vacuum to the desired setting for the media.\n\n"
"For decals, adjust the vacuum setting between 3 and 5.",

"Communication Issues": "Restart the machine.\n\n"
"If you still have communication issues after restarting the machine, call maintenance.",

"Head Crash": "Go to the Printer tab and click Initialize Printer.",

"Ink Leak": "Call maintenance.",

"Jam": "Check the vacuum settings.\n\n"
"Adjust the vacuum to the desired setting for the media.\n\n"
"For decals, adjust the vacuum setting between 3 and 5.",

"Loading Issues": "Call maintenance.",

"Sledge Control Unit Error": "Go to the Printer tab and click Initialize Sledge.",

"Sledge Error": "Go to the Printer tab and click Initialize Sledge.",

"Front To Back Registration": "Ensure the vacuum level is set to 10.\n\n"
"When loading the back: Make sure the sheet is positioned to the left side of the machine.\n\n"
"When loading the front: Make sure the sheet is positioned to the right side of the machine.\n\n"
"If you are still having front-to-back registration issues, call maintenance.",

"Crash Sensor Triggered": "Restart the machine.",

"Purgetub Open Error": "Open the purge tub and re-close it gently.",

"White Nozzles Missing Not Matching Master": "Step 1: Perform a short purge on spot colours only.\n\n"
"Step 2: Dry-wipe the white printheads only.\n\n"
"If the nozzles still do not match the Master, call your supervisor/PC.",

"Feeding Error": "Check that the feeding switch is on.\n\n"
"The switch is located at the bottom-left of the front end of the machine.",

"Ink System Air Leak": "Call maintenance.",

"Broken Spindles": "Call maintenance.",

"Print Skew": "Check the vacuum settings.",

"UV Lamps Not Turning On": "Go to the Printer tab, turn the UV lamp off, and turn it back on.\n\n"
"If the UV lamp is still not working, restart the machine.",

"Ink Spots": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"If ink spots are still present after wiping, call your supervisor/PC.",

"Ink Overspray": "Step 1: Wet-wipe all printheads.\n\n"
"Step 2: Perform a short purge on all printheads.\n\n"
"Step 3: Dry-wipe all printheads.\n\n"
"If overspray is still present after wiping, call your supervisor/PC.",

"Print Off Center": "Call maintenance.",

"Ink Water Mark": "Call maintenance.",

"Error In Checking Printhead Ink Tanks": "Lift up the ink waste lever and close it down gently.\n\n"
"If the error isn't cleared, call maintenance.",

"Missing Nozzles Causing Banding": "Call maintenance.",

"Failed To Control Continuous Feeder Error": "Check that the feeding switch is on.\n\n"
"The switch is located at the bottom-left of the front end of the machine.",

"UV Lamps Won't Heat Up": "Restart the machine.\n\n"
"If it is still not working, call maintenance.",

"Unable To Switch Off The Head Voltage Error": "Call maintenance.",

"Ink Not Registering": "Call your supervisor/PC.",

"Rabbit Scanner Not Working": "Call maintenance.",

"Reading Image File Failed": "Call maintenance.",

"Print Head Carriage": "Go to the Printer tab and click Initialize Sledge.",

"Feeding Unit Error": "Check that the feeding switch is on. The switch is located at the bottom-left of the front end of the machine.",

"Unable To Scan Ink In": "Restart the machine.",

"Ink Marks On Foam Boards": "Call maintenance.",

"No Heating Up": "Restart the machine.",

"Ink Heating Taking Long Time": "Restart the machine.",

"Failed To Set Jet Straighten Pulse": "Call maintenance.",

"Sheets Skewed": "Increase the vacuum level to 10.",

"Failed Initialization": "Restart the machine.",

"Vacuum System Reference Not Found": "Call maintenance.",

"Media Crashing On First Off": "Check the vacuum settings.",

"Crashed On First Off": "Check the vacuum settings.",

"Sheet Not Moving Into Belt": "Call maintenance.",

"E-stop Pressed": "Call maintenance.",

"Ink Smearing": "Call maintenance.",

"Belt Scraping": "Call maintenance.",

"Ink Marks On Lawn Signs": "Call maintenance.",

"Keeps Jamming For Paper": "If jamming occurs on first-off paper: Increase the vacuum.\n\n"
"If jamming occurs on decals: Adjust the vacuum level between 3 and 5."
}


def correct_spelling(text):
    words = text.split()
    corrected_words = []

    for word in words:
        corrected = spell.correction(word)
        corrected_words.append(corrected if corrected else word)

    return " ".join(corrected_words)

def get_answer(question: str) -> str:
    question = correct_spelling(question)

    q = question.strip().lower()

    for stored_q, stored_a in QA_DATA.items():
        if stored_q.strip().lower() == q:
            return stored_a
    best_score = 0
    best_answer = None

    # optional: partial match when no exact match is found
    for stored_q, stored_a in QA_DATA.items():
        score = fuzz.token_set_ratio(q,stored_q.strip().lower())
        if score > best_score:
            best_score = score
            best_answer = stored_a

    if best_score >= 45:
        return best_answer

    return "Sorry, I don't have an answer for that question yet."

def Rigid4():
    Search = st.text_input("Rigid 4",
key="Rigid4")

    if Search:
     answer = get_answer(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)
            