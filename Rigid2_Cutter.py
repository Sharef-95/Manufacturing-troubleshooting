from spellchecker import SpellChecker
from rapidfuzz import fuzz, process
import streamlit as st

spell = SpellChecker()
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


def correct_spelling(text):
    words = text.split()
    corrected_words = []

    for word in words:
        corrected = spell.correction(word)
        corrected_words.append(corrected if corrected else word)

    return " ".join(corrected_words)


def smart_search(question: str) -> str:
    question = correct_spelling(question)

    q = question.strip().lower()
    q = q.replace("problems","issues")
    q = q.replace("problem","issue")

    # Words that usually don't help identify the actual issue
    stop_words = {
        "what", "whats", "what's", "is", "the", "a", "an",
        "for", "to", "of", "do", "i", "have", "how",
        "can", "my", "me", "please", "tell", "about",
        "level", "setting","machine",
    }

    # Get important words from the user's question
    q_words = {
        word.strip(".,?!")
        for word in q.split()
        if word.strip(".,?!") not in stop_words
    }

    best_score = 0
    best_answer = None

    for stored_q, stored_a in QA_DATA.items():

        stored = stored_q.strip().lower()

        stored_words = {
            word.strip(".,?!")
            for word in stored.split()
            if word.strip(".,?!") not in stop_words
        }

        # Count important words that appear in both questions
        matching_words = q_words.intersection(stored_words)

        keyword_score = len(matching_words)

        # Fuzzy similarity
        fuzzy_score = fuzz.token_set_ratio(q, stored)

        # Combine keyword matching + fuzzy matching
        score = (keyword_score * 20) + fuzzy_score

        if score > best_score:
            best_score = score
            best_answer = stored_a

    if best_answer and best_score >= 45:
        return best_answer

    return "Sorry, I don't have an answer for that question yet."

def Rigid2_Cutter():
    Search = st.text_input("Rigid 2 Cutter",
key="Rigid2_Cutter")

    if Search:
     answer = smart_search(Search)

     if answer.lower().startswith("sorry"):
        st.warning(answer)
     else:
        st.success(answer)
            