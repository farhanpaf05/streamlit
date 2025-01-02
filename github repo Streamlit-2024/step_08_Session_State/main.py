import streamlit as st

st.title("Session State Basics")

st.write(f"Session State Object: {st.session_state}")

if "a_counter" not in st.session_state:
    st.session_state["a_counter"] = 0

if "radio_option" not in st.session_state:
    st.session_state["radio_option"] = "Nothing Selected"

if "option_text" not in st.session_state:
    st.session_state["option_text"] = "Please select an option."

if "boolean" not in st.session_state:
    st.session_state.boolean = False
st.write(st.session_state)

st.write("a_counter is:", st.session_state["a_counter"])
st.write("boolean is:", st.session_state.boolean)

for the_key in st.session_state.keys():
    st.write(the_key)

for the_values in st.session_state.values():
    st.write(the_values)

for item in st.session_state.items():
    st.write(item)

button = st.button("Update State")
st.write(f"before pressing button {st.session_state}")
if button:
    st.session_state["a_counter"] += 1
    st.session_state.boolean = not st.session_state.boolean
st.write(f"after pressing button {st.session_state}")


# Using Sessions with Widgets
def change_radio_option():
    if st.session_state["radio_option"] == "a":
        st.session_state.radio_option = "b"
        st.session_state["option_text"] = "You picked 'b' :heart:"
    elif st.session_state["radio_option"] == "b":
        st.session_state.radio_option = "c"
        st.session_state["option_text"] = "You picked 'c' :rocket:"
    else:
        st.session_state.radio_option = "a"
        st.session_state["option_text"] = "You picked 'a' :smile:"


def display_option():
    option = st.session_state.radio_option
    if option == "a":
        st.session_state["option_text"] = "You picked 'a' :smile:"
    elif option == "b":
        st.session_state["option_text"] = "You picked 'b' :heart:"
    elif option == "c":
        st.session_state["option_text"] = "You picked 'c' :rocket:"
    else:
        st.session_state["option_text"] = "Please select an option."


## works with all widgets!
number = st.slider("A number", 1, 10, key="slider")

st.write(st.session_state)

#  Using callbacks to set session state on_click and on_change
col1, col2 = st.columns(2)

option_names = ["Nothing Selected", "a", "b", "c"]

# Display the radio buttons and bind to session state

st.radio(
    "Pick an option",
    option_names,
    key="radio_option",
    on_change=display_option,
)
st.write(st.session_state["option_text"])


st.button("Next option", on_click=change_radio_option)

# Display the session state
st.write(st.session_state)
