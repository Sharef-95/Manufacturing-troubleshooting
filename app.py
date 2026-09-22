import streamlit as st
st.title("Manufacturing Troubleshooting Guide")



"""
Simple Q&A Program
------------------
You fill in the questions and answers below.
Type a question -> get the answer.
"""

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

Search = st.text_input("Search")
if Search:
    answer = get_answer(Search)
    if answer.startswith("sorry"):
        st.warning(answer)
    
    else:
            st.success(answer)



    