import streamlit as st

QA_DATA = { 
    
"Drying Issues":"",
"Lois Sensor Issue":"",
"Blurry Barcodes":"",
"Encoder Issue":"",
"Feeding Multiple Sheets":"",
"Banding":"",
"Computer Frozen":"",
"Door Issues":"",
"Initialization Issues":"",
"Communication Issues":"",
"Head Crash":"",
"Ink Leak":"",
"Jam":"",
"Loading Issues":"",
"Registration Issues":"",
"UV Issues":"",
"Vacuum Issues":"",
"Other issues shown":"",
"UV Lamp Failure":"",
"Banding in the Firstoff":"",
"Missing Nozzles":"",
"Printhead Ink Tank Error":"",
"Continuous Feeder Issues":"",
"Media Could Not Load Error":"",
"UV Lamps":"",
"Ink Spots":"",
"Water Marks Ink Seeming Lawn":"",
"Rub Marks":"",
"Maintenance Cycle Needed Error":"",
"Computer Frozen":"",
"Failed To Control Continuous Feeder":"",
"Air Fitting Leaking":"",
"Missing Nozzles New Master":"",
"Master Nozzle Sign Off":"",
"Ink Smearing":"",
"UV Lamp Failure One and 2":"",
"Ink Not Heating":"",
"Failing To Load First Off Paper":"",
"Printing Main Sheet":"",
"Single Figs":"",
"Feeding Issues":"",
"Light Cyan Ink Not Filling":"",
"Missing Yellow Nozzles":"",
"Found Bolt On Magnet When Pulled Out":"",
"Restart Press Is Requested":"",
"Shut Down":"",
"Nozzle Test":"",
"Press Will Not Restart":"",
"Black Markings On Roll Off":"",
"M/C4 Component Error":"",
"Pink Lines Around Product":"",
"Lines Through Grey Images":"",
"Yellow Nozzles Missing":"",
"Piece Of Magnet Stuck Inside":"",
"Printing Program Has No Options For Printing":"",
"Won't Load First Off Paper":"",
"Loose Screw":"",
"Air Hose":"",
"Purge Tub Error":"",
"Paper Jammed In Press":"",
"Power Outage":"",
"Weekly Maintenance Notification":"",
"Curing Issues":"",
"Making Loud Noise":"",
"Test":"",
"Outage":"",
"Sledge Will Not Initialize":"",

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

def Rigid2_Cutter():
    Search = st.text_input("Rigid2 Cutter")

    if Search:
        answer = get_answer(Rigid2_Cutter)
        if answer.startswith("sorry"):
         st.warning(answer)
    
        else:
            st.success(answer)