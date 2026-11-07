
import streamlit as st

st.set_page_config(
    page_title="SmartCalc",
    page_icon="🧮",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background-color: #17191f;
    color: white;
}

h1 {
    text-align: center;
    color: white;
}

.result {
    background: #292d36;
    color: white;
    padding: 25px;
    border-radius: 15px;
    text-align: right;
    font-size: 35px;
    margin-bottom: 15px;
    overflow-wrap: anywhere;
}

div.stButton > button {
    width: 100%;
    height: 65px;
    border-radius: 15px;
    font-size: 23px;
    font-weight: bold;
}

/* Keep four calculator buttons in each row on phones */
@media (max-width: 768px) {
    div[data-testid="stHorizontalBlock"] {
        flex-direction: row !important;
        flex-wrap: nowrap !important;
        gap: 6px !important;
    }

    div[data-testid="column"] {
        width: 25% !important;
        min-width: 0 !important;
        flex: 1 1 25% !important;
    }

    div.stButton > button {
        min-width: 0 !important;
        padding: 0 2px !important;
        height: 55px !important;
        font-size: clamp(15px, 4vw, 22px) !important;
    }

    .result {
        font-size: 30px;
        padding: 20px;
    }
}
</style>
""", unsafe_allow_html=True)

st.title("🧮 SmartCalc")

if "display" not in st.session_state:
    st.session_state.display = "0"
if "first" not in st.session_state:
    st.session_state.first = None
if "operator" not in st.session_state:
    st.session_state.operator = None
if "new_number" not in st.session_state:
    st.session_state.new_number = False

def press(value):
    s = st.session_state

    if value.isdigit() or value == ".":
        if s.new_number:
            s.display = "0" if value == "." else value
            s.new_number = False
        elif value == ".":
            if "." not in s.display:
                s.display += "."
        else:
            s.display = value if s.display == "0" else s.display + value

    elif value in ["+", "−", "×", "÷"]:
        s.first = float(s.display)
        s.operator = value
        s.new_number = True

    elif value == "=":
        if s.first is not None and s.operator:
            a = s.first
            b = float(s.display)
            op = s.operator

            if op == "+":
                result = a + b
            elif op == "−":
                result = a - b
            elif op == "×":
                result = a * b
            else:
                if b == 0:
                    s.display = "Error"
                    s.first = None
                    s.operator = None
                    s.new_number = True
                    return
                result = a / b

            s.display = str(round(result, 8))
            s.first = None
            s.operator = None
            s.new_number = True

    elif value == "AC":
        s.display = "0"
        s.first = None
        s.operator = None
        s.new_number = False

    elif value == "±":
        if s.display != "0" and s.display != "Error":
            s.display = str(-float(s.display))

    elif value == "%":
        if s.display != "Error":
            s.display = str(float(s.display) / 100)

st.markdown(
    f'<div class="result">{st.session_state.display}</div>',
    unsafe_allow_html=True
)

buttons = [
    ["AC", "±", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
    ["0", ".", "00", "="]
]

for row_index, row in enumerate(buttons):
    cols = st.columns(4, gap="small")

    for col_index, value in enumerate(row):
        with cols[col_index]:
            if st.button(value, key=f"btn_{row_index}_{col_index}"):
                if value == "00":
                    press("0")
                    press("0")
                else:
                    press(value)
                st.rerun()
