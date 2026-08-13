# ============================================
# 📘 CONNECTING TO AN API USING PYTHON
# ============================================

# API = Application Programming Interface
#
# An API allows one program to communicate with
# another program and request or send data.
#
# In this example, we use the PokeAPI to get
# information about a Pokémon.
#
# PokeAPI:
# https://pokeapi.co/
#
# We use the `requests` library to send an
# HTTP request to the API.


# ============================================
# 1️⃣ IMPORT REQUESTS
# ============================================

import requests


# ============================================
# 2️⃣ API BASE URL
# ============================================

base_url = "https://pokeapi.co/api/v2"


# ============================================
# 3️⃣ CREATE FUNCTION TO GET POKÉMON DATA
# ============================================

def get_pokemon_info(name):

    url = f"{base_url}/pokemon/{name}"

    response = requests.get(url)


    # ========================================
    # CHECK RESPONSE STATUS
    # ========================================

    if response.status_code == 200:

        # Convert JSON response into
        # a Python dictionary.
        pokemon_data = response.json()

        return pokemon_data

    else:
        print(f"Failed to retrieve data: {response.status_code}")


# ============================================
# 4️⃣ GET POKÉMON NAME
# ============================================

pokemon_name = "pikachu"

pokemon_info = get_pokemon_info(pokemon_name)


# ============================================
# 5️⃣ DISPLAY DATA
# ============================================

if pokemon_info:

    print(f"Name: {pokemon_info['name'].capitalize()}")
    print(f"Id: {pokemon_info['id']}")
    print(f"Height: {pokemon_info['height']}")
    print(f"Weight: {pokemon_info['weight']}")


# ============================================
# 📌 HOW IT WORKS
# ============================================

# Step 1:
# Import requests
#
# Step 2:
# Create the API URL
#
# Step 3:
# Send GET request using requests.get()
#
# Step 4:
# Check status_code
#
# Step 5:
# Convert JSON response into Python data
#
# Step 6:
# Access required information
#
#
# Flow:
#
# Python
#    ↓
# requests.get()
#    ↓
# PokeAPI
#    ↓
# JSON response
#    ↓
# response.json()
#    ↓
# Python dictionary
#    ↓
# Extract data


# ============================================
# 📌 IMPORTANT
# ============================================

# requests.get(url)
# → Sends a GET request to the API.
#
# response.status_code
# → Tells whether the request was successful.
#
# 200
# → Request successful.
#
# response.json()
# → Converts JSON response into Python
#   dictionary/list.
#
# API endpoint:
#
# /pokemon/pikachu
#
# → Requests information about Pikachu.
#
#
# Common HTTP status codes:
#
# 200 → Success
# 404 → Not Found
# 500 → Server Error
#
#
# Remember:
#
# API → Allows applications to communicate
# requests → Sends HTTP requests
# JSON → Common format for API data
# status_code → Shows request result
# ============================================