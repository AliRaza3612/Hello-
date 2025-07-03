import streamlit as st

# Initialize calculator state
if 'display' not in st.session_state:
    st.session_state.display = "0"
if 'stored_value' not in st.session_state:
    st.session_state.stored_value = None
if 'current_operation' not in st.session_state:
    st.session_state.current_operation = None
if 'new_input' not in st.session_state:
    st.session_state.new_input = True


def update_display(value):
    """Handle button presses"""
    if value in '0123456789':
        if st.session_state.display == "0" or st.session_state.new_input:
            st.session_state.display = value
            st.session_state.new_input = False
        else:
            st.session_state.display += value
    elif value == '.':
        if '.' not in st.session_state.display:
            st.session_state.display += value
            st.session_state.new_input = False
    elif value == 'C':
        st.session_state.display = "0"
        st.session_state.stored_value = None
        st.session_state.current_operation = None
        st.session_state.new_input = True
    elif value in '+-*/':
        if st.session_state.stored_value is None:
            st.session_state.stored_value = float(st.session_state.display)
        else:
            calculate_result()
        st.session_state.current_operation = value
        st.session_state.new_input = True
    elif value == '=':
        calculate_result()


def calculate_result():
    """Perform the calculation"""
    try:
        if st.session_state.stored_value is not None and st.session_state.current_operation:
            num2 = float(st.session_state.display)

            if st.session_state.current_operation == '+':
                result = st.session_state.stored_value + num2
            elif st.session_state.current_operation == '-':
                result = st.session_state.stored_value - num2
            elif st.session_state.current_operation == '*':
                result = st.session_state.stored_value * num2
            elif st.session_state.current_operation == '/':
                result = st.session_state.stored_value / num2

            st.session_state.display = str(result)
            st.session_state.result = str(result)  # Update result field
            st.session_state.stored_value = None
            st.session_state.current_operation = None
            st.session_state.new_input = True
    except ZeroDivisionError:
        st.session_state.display = "Error"
        st.session_state.result = "Error"
        st.session_state.stored_value = None
        st.session_state.current_operation = None
    except:
        st.session_state.display = "Invalid"
        st.session_state.result = "Invalid"
        st.session_state.stored_value = None
        st.session_state.current_operation = None


def calculate_separately():
    """Handle separate calculate button press"""
    calculate_result()


# Calculator UI
st.title("Python Calculator")

# Display
st.text_input("",
              value=st.session_state.display,
              key="display_box",
              disabled=True,
              help="Calculation results appear here")

# Button layout
col1, col2, col3, col4 = st.columns(4)

# Custom CSS for buttons
st.markdown("""
<style>
    /* Base button styling for all buttons */
    div[data-testid="stButton"] > button {
        background-color: #0068c9 !important;
        color: white !important;
        font-weight: bold;
        width: 100%;
        margin: 5px 0;
        border: 2px solid white;
        font-size: 24px;
        font-family: Arial, "Segoe UI Symbol", "Noto Sans", Helvetica, Tahoma, sans-serif !important;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
        line-height: 50px;
    }
    
    /* Specific styling for plus button */
    button[aria-label="plus"]::before {
        content: "\\002B" !important; /* Unicode for + */
        font-size: 24px;
        color: white;
    }
    
    /* Hover effect */
    div[data-testid="stButton"] > button:hover {
        background-color: #004a8f !important;
    }
</style>
""", unsafe_allow_html=True)

with col1:
    st.button("7", on_click=update_display, args=("7",), key="btn7")
    st.button("4", on_click=update_display, args=("4",), key="btn4")
    st.button("1", on_click=update_display, args=("1",), key="btn1")
    st.button("0", on_click=update_display, args=("0",), key="btn0")

with col2:
    st.button("8", on_click=update_display, args=("8",), key="btn8")
    st.button("5", on_click=update_display, args=("5",), key="btn5")
    st.button("2", on_click=update_display, args=("2",), key="btn2")
    st.button(".", on_click=update_display, args=(".",), key="btn_dot")

with col3:
    st.button("9", on_click=update_display, args=("9",), key="btn9")
    st.button("6", on_click=update_display, args=("6",), key="btn6")
    st.button("3", on_click=update_display, args=("3",), key="btn3")
    st.button("=", on_click=update_display, args=("=",), key="btn_equal")

with col4:
    st.button("C", on_click=update_display, args=("C",), key="btn_clear")
    st.button("÷", on_click=update_display, args=("/",), key="btn_div")
    st.button("×", on_click=update_display, args=("*",), key="btn_mul")
    st.button("−", on_click=update_display, args=("-",), key="btn_sub")
    st.button("", on_click=update_display, args=("+",), key="btn_add", help="plus")

# Separate Calculate button
st.button("Calculate", on_click=calculate_separately, key="btn_calculate")

# Result display below Calculate button
st.text_input("Result",
              value=st.session_state.result,
              key="result_box",
              disabled=True,
              help="Final result appears here")
