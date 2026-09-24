import streamlit as st

QA_DATA = { 
    "p1": "sol1",
    "p2": "sol2",
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