import streamlit as st

QA_DATA = { 
"Drying Issues":"Call maintenance",
"Lois Sensor Issue":"Call maintenance",
"Vacuum Issues":"adgust vacuum to the desired setting for the media\n\n"
"for decals adjust the vacuum setting between 3-5. ",

"frozen":"Restart DURST app",
"Banding":"step 1: wet wipe all printheads\n\n"
"step 2: short purge all printheads.\n\n"
"step 3: Dry wipe all printheads.\n\n"
"if banding is still present after wiping, call your supervisor/PC",

"Computer Frozen":"Restart DURST program.",
"Door Issues": "open door, re-close gently.",
"Initialization Issues":"step 1: go printer tab \n\n"
    "step 2:click initialize Sledge\n\n"
    "step 3 click initilize printer"
    "if it's still not initilizing, restart the machine.",
"Missing Nozzles":"wet wipe all printheads\n\n"
"step 2: short purge all printheads.\n\n"
"step 3: Dry wipe all printheads.\n\n"
"if nozzles are still missing, call your supervisor",
"Purge Tub Error":"open purge tub, re-close gently.",
"Registration Issues":"Check vacuum setting",
"UV Issues":"on printer tab, turn UV lamp off, and turn it back on.\n\n"
"if it doesn't work restart the machine\n\n"
"if it still not worling after restarting the machine, call maintenance.",
"Blurry Barcodes":"Check vacuum settings\n\n"
"adgust vacuum to the desired setting for the media\n\n"
"for decals adjust the vacuum setting between 3-5. ",

"Communication Issues":"restart the machine\n\n"
"if you still have communciation issues after restrating the machine, call maintenance.",
"Head Crash":"on printer tab. Click initilize printer.",
"Ink Leak":"Call maintenance.",
"Jam":"Check vacuum settings\n\n"
"adgust vacuum to the desired setting for the media\n\n"
"for decals adjust the vacuum setting between 3-5.",

"Loading Issues":"",
"Sledge Control Unit Error":"on printer tab. Click initilize sledge.",
"Sledge Error":"on printer tab. Click initilize sledge.",
"Front To Back Registration":"Insure vacuum level is at 10\n\n"
"When loading the back: Make sure the sheet is positioned to the left side of the machine.\n\n"
"When loading the front: Make sure the sheet is positioned to the right side of the machine.\n\n"
"if you still having front and back registration issues, call maintenance.",
"Crash Sensor Triggered":"restart the machine.",
"Purgetub Open Error":"open purge tub, re-close gently.",
"White Nozzles Missing Not Matching Master":"step 1: short purge spot colours only.\n\n"
"Step2: Dry wipe white printheads only.\n\n"
"if nozzles are not matching Master still, call for your supervisor/PC.",
"Feeding Error":"Check feeding switch is on\n\n."
    " The switch is located at the bottom-left of the front end of the machine.",

"Ink System Air Leak":"call maintenance.",
"Broken Spindles":"call maintenance.",
"Print Skew":"Check vacuum settings.",
"UV Lamps Not Turning On":"on printer tab, turn UV lamp off, and turn back on.\n\n"
    "if UV lamp is still not working, restart the machine.",
"Ink Spots":"step 1: wet wipe all printheads\n\n"
"step 2: short purge all printheads.\n\n"
"step 3: Dry wipe all printheads.\n\n"
"if ink spots are still present after wiping, call your supervisor/PC",
"Ink Overspray":"step 1: wet wipe all printheads\n\n"
"step 2: short purge all printheads.\n\n"
"step 3: Dry wipe all printheads.\n\n"
"if overspray is still present after wiping, call your supervisor/PC",
"Print Off Center":"call maintenance.",
"Ink Water Mark":"call maintenance.",
"Error In Checking Printhead Ink Tanks":"Left up ink waste lever, and close down gently.\n\n"
"if error isn't cleared, call maintenance.",
"Missing Nozzles Causing Banding":"call maintenance.",
"Failed To Control Continuous Feeder Error":"Check feeding switch is on\n\n."
    " The switch is located at the bottom-left of the front end of the machine.",
"UV Lamps Won't Heat Up":"Restart the machine.\n\n"
"if still not working, call maintenance.",
"Unable To Switch Off The Head Voltage Error":"call maintenance.",
"Ink Not Registering":"call your supervisor/PC.",
"Rabbit Scanner Not Working":"call maintenance.",
"Reading Image File Failed":"call maintenance.",
"Print Head Carriage":"on printer tab. Click initilize sledge.",
    "Feeding Unit Error": "Check feeding switch is on. The sitch is located at the bottom-left of the front end of the machine.",
"Unable To Scan Ink In":"restart the machine.",
"Ink Marks On Foam Boards":"call maintenance.",
"No Heating Up":"restart the machine.",
"Ink Heating Taking Long Time":"restart the machine.",
"Failed To Set Jet Straighten Pulse":"call maintenance.",
"Sheets Skewed":"Increase vacuum level to 10.",
"Failed Initialization":"restart the machine.",
"Vacuum System Reference Not Found":"call maintenance.",
"Media Crashing On First Off":"Check vacuum settings.",
"Crashed On First Off":"Check vacuum settings.",
"Sheet Not Moving Into Belt":"call maintenance.",
"E-stop Pressed":"call maintenance.",
"Ink Smearing":"call maintenance.",
"Belt Scraping":"Call maintenance.",
"Ink Marks On Lawn Signs":"call maintenance.",
"Keeps Jamming For Paper":"Jamming first-off paper: Increase the vacuum.\n\n"
"Jamming on decals: Adjust the vacuum level between 3-5"
}


def get_answer(question: str) -> str:
    """Return the answer for a question (case-insensitive, ignores extra spaces)."""
    q = question.strip().lower()

    for stored_q, stored_a in QA_DATA.items():
        if stored_q.strip().lower() == q:
            return stored_a

    # optional: partial match when no exact match is found
    for stored_q, stored_a in QA_DATA.items():
        if q in stored_q.strip().lower():
            return stored_a

    return "Sorry, I don't have an answer for that question yet."

def Rigid4_Cutter():
    Search = st.text_input("Rigid4 Cutter",
key="Rigid4_Cutter")

    if Search:
        answer = get_answer(Rigid4_Cutter)
        if answer.startswith("sorry"):
         st.warning(answer)
    
        else:
            st.success(answer)