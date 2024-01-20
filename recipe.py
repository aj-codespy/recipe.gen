import streamlit as st
import requests

#Title
st.title("Recipe Generator App")

# User input for the dish
dish_name = st.text_input("Enter a dish name:")

# Button for generation
if st.button("Generate Recipe"):
    # Meal DB API endpoint for recipe generation
    api_endpoint = "https://www.themealdb.com/api/json/v1/1/search.php"

    # Parameters for the API request
    params = {"s": dish_name}

    # Making the API request
    response = requests.get(api_endpoint, params=params)
    data = response.json()

    # Checking if the API request was successful
    if data["meals"]:
        # Displaying the recipe details
        meal = data["meals"][0]
        st.subheader(f"Recipe for {dish_name}:")
        st.write(f"**Category:** {meal['strCategory']}")
        st.write(f"**Instructions:** {meal['strInstructions']}")
    else:
        st.warning(f"No recipe found for {dish_name}. Please try another dish.")
