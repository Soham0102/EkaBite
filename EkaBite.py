import streamlit as st
import torch
from transformers import pipeline


generator = pipeline("text-generation", model="gpt2")

st.title("✨ EkaBite – Your AI Recipe Companion")
st.write("Tell EkaBite what ingredients you have, and get simple recipe ideas using local AI.")

user_input = st.text_input("Enter Ingredients (e.g., rice, onion, paneer)")
cuisine_options = ["Any", "Indian", "Italian", "Mexican", "Chinese", "Thai", "Mediterranean"]
cuisine = st.selectbox("Select Preferred Cuisine", cuisine_options)
diet = st.text_input("Dietary Preferences (e.g., vegetarian, gluten-free)")

if st.button("Get Recipes from EkaBite"):
    if not user_input.strip():
        st.warning("Please enter some ingredients.")
    else:
        prompt = f"""Suggest a recipe using only these ingredients: {user_input}.
Cuisine: {cuisine if cuisine != "Any" else "any"}
Dietary preference: {diet if diet else "none"}

Provide the recipe title, ingredients, and steps in short.
"""

        output = generator(prompt, max_length=200, num_return_sequences=1)[0]["generated_text"]
        st.markdown("### 🍽️ Suggested Recipe")
        st.markdown(output)
