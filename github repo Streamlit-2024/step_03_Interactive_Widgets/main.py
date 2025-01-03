import streamlit as st

# Title
st.title("Streamlit Interactive Widget Examples")

# Button
st.button("Hello World")

# if st.button("Click Me"):
#     st.write("Button clicked!")

# Checkbox
# checkbox_state = st.checkbox("Check me to enable something")
# if checkbox_state:
#     st.write("Checkbox is checked!")

# # Radio button
# radio_selection = st.radio("Choose an option:", ["NLP", "CV", "DL", "ML"])
# st.write("You selected:", radio_selection)

# # Selectbox
# selectbox_selection = st.selectbox("Choose an item:", ["NLP", "CV", "DL", "ML"])
# st.write("You selected:", selectbox_selection)

# # Multiselect
# multiselect_selection = st.multiselect(
#     "Choose multiple items:", ["NLP", "CV", "DL", "ML"]
# )
# st.write("You selected:", multiselect_selection)

# # Slider
# slider_value = st.slider("Select a value:", min_value=0, max_value=10, value=0, step=3)
# st.write("Slider value:", slider_value)

# # Slider with custom values
# select_slider_value = st.select_slider(
#     "Select a value:", options=["Hello", "World", False, 6, 3, 2, "NLP"]
# )

# st.write("Selected slider value:", select_slider_value)
