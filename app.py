import streamlit as st
import base64
import pandas as pd
import requests
import json
import random
from pymongo import MongoClient
import pymongo
# import  03-HTML-API import pokemon-api //Users//arun._.appulingam//Data223/Python//03-HTML-API//pokemon-api.ipynb

from pymongo.mongo_client import MongoClient


uri = "mongodb+srv://arunsparta01:G0rillas13@arun02.dzu4giz.mongodb.net/?retryWrites=true&w=majority"


# Create a new client and connect to the server
client = MongoClient(uri)

db = client["pokemon_battle"]
matches = db["matches"]

# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)

st.set_page_config(page_title="My Webpage", page_icon= "tada", layout= "wide")

st.sidebar.write("---")
st.image('/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/International_Pokémon_logo.svg.png')
original_title = '<h3 style="text-align:center; color:black; font-size: 90px;">BATTLE GAME</h3>'
st.markdown(original_title, unsafe_allow_html=True)
st.write('---')

st.sidebar.markdown("<h2 style='text-align: center;font-size: 40px'>All Pokémon names:</h2>",unsafe_allow_html= True)
st.sidebar.write("---")

def get_pokemon_details(id):

    response= requests.get(f'https://pokeapi.co/api/v2/pokemon/{id}')
    pokemon_data=response.json()
    id=pokemon_data['id']
    name=pokemon_data['name']

    # to retieve the base stat of HP and its value together
    for key in pokemon_data['stats']:

        for value in key.items():
            if key['stat']['name'] == 'hp':
                HP = key['base_stat']
            elif key['stat']['name'] == 'attack':
                attack = key['base_stat']
            elif key['stat']['name'] == 'defense':
                defense = key['base_stat']


        types=[t['type']['name']for t in pokemon_data['types']]

    pokemon_details={'id':id, 'name':name, 'HP': HP, 'attack': attack, 'defense': defense, 'types':types}
    return pokemon_details

def get_random_pokemon_id():
    return random.randint(1,1010)

def attack_mod(p1, p2):

    type_modifiers = {
        'normal': {'normal':1,'fire': 1, 'water': 1, 'electric': 1,'grass': 1, 'ice': 1,'fighting':1, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':1, 'bug': 1, 'rock': 0.5,'ghost':0, 'dragon': 1,'dark':1, 'steel': 0.5,'fairy':1},
        'fire': {'normal':1,'fire': 0.5, 'water': 0.5, 'electric': 1,'grass': 2, 'ice': 2,'fighting':1, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':1, 'bug': 2, 'rock': 0.5,'ghost':1, 'dragon': 0.5,'dark':1, 'steel': 2,'fairy':1},
        'water': {'normal':1,'fire': 2, 'water': 0.5, 'electric': 1,'grass': 0.5, 'ice': 1,'fighting':1, 'poison': 1, 'ground': 2, 'flying': 1,'psychic':1, 'bug': 1, 'rock': 2,'ghost':1, 'dragon': 0.5,'dark':1, 'steel': 1,'fairy':1},
        'electric': {'normal':1,'fire': 1, 'water': 2, 'electric': 0.5,'grass': 0.5, 'ice': 1,'fighting':1, 'poison': 0.5, 'ground': 0, 'flying': 2,'psychic':1, 'bug': 1, 'rock': 1,'ghost':1, 'dragon': 0.5,'dark':1, 'steel': 1,'fairy':1},
        'grass': {'normal':1,'fire': 0.5, 'water': 2, 'electric': 1,'grass': 1, 'ice': 1,'fighting':1, 'poison': 0.5, 'ground': 2, 'flying': 0.5,'psychic':1, 'bug': 1, 'rock': 2,'ghost':1, 'dragon': 0.5,'dark':1, 'steel': 0.5,'fairy':1},
        'ice': {'normal':1,'fire': 0.5, 'water': 0.5, 'electric': 1,'grass': 2, 'ice': 0.5,'fighting':1, 'poison': 1, 'ground': 2, 'flying': 0.5,'psychic':1, 'bug': 1, 'rock': 2,'ghost':1, 'dragon': 0.5,'dark':1, 'steel': 0.5,'fairy':1},
        'fighting': {'normal':2,'fire': 1, 'water': 1, 'electric': 1,'grass': 1, 'ice': 2,'fighting':1, 'poison': 0.5, 'ground': 1, 'flying': 0.5,'psychic':0.5, 'bug': 0.5, 'rock': 2,'ghost':0, 'dragon': 1,'dark':2, 'steel': 2,'fairy':0.5},
        'poison': {'normal':1,'fire': 1, 'water': 1, 'electric': 1,'grass': 2, 'ice': 1,'fighting':1, 'poison': 0.5, 'ground': 0.5, 'flying': 1,'psychic':1, 'bug': 1, 'rock': 0.5,'ghost':0.5, 'dragon': 1,'dark':1, 'steel': 0,'fairy':2},
        'ground': {'normal':1,'fire': 2, 'water': 1, 'electric': 2,'grass': 0.5, 'ice': 1,'fighting':1, 'poison': 2, 'ground': 1, 'flying': 0,'psychic':1, 'bug': 0.5, 'rock': 2,'ghost':1, 'dragon': 1,'dark':1, 'steel': 2,'fairy':1},
        'flying': {'normal':1,'fire': 1, 'water': 1, 'electric': 0.5,'grass': 2, 'ice': 1,'fighting':2, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':1, 'bug': 2, 'rock': 0.5,'ghost':1, 'dragon': 1,'dark':1, 'steel': 0.5,'fairy':1},
        'psychic': {'normal':1,'fire': 1, 'water': 1, 'electric': 1,'grass': 1, 'ice': 1,'fighting':2, 'poison': 2, 'ground': 1, 'flying': 1,'psychic':0.5, 'bug': 1, 'rock': 1,'ghost':1, 'dragon': 1,'dark':0, 'steel': 0.5,'fairy':1},
        'bug': {'normal':1,'fire': 0.5, 'water': 1, 'electric': 1,'grass': 2, 'ice': 1,'fighting':0.5, 'poison': 0.5, 'ground': 1, 'flying': 0.5,'psychic':2, 'bug': 1, 'rock': 1,'ghost':0.5, 'dragon': 1,'dark':2, 'steel': 0.5,'fairy':0.5},
        'rock': {'normal':1,'fire': 2, 'water': 1, 'electric': 1,'grass': 1, 'ice': 2,'fighting':0.5, 'poison': 1, 'ground': 0.5, 'flying': 2,'psychic':1, 'bug': 2, 'rock': 1,'ghost':1, 'dragon': 1,'dark':1, 'steel': 0.5,'fairy':1},
        'ghost': {'normal':0,'fire': 1, 'water': 1, 'electric': 1,'grass': 1, 'ice': 1,'fighting':1, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':2, 'bug': 1, 'rock': 1,'ghost':2, 'dragon': 1,'dark':0.5, 'steel': 1,'fairy':1},
        'dragon': {'normal':1,'fire': 1, 'water': 1, 'electric': 1,'grass': 1, 'ice': 1,'fighting':1, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':1, 'bug': 1, 'rock': 1,'ghost':1, 'dragon': 2,'dark':1, 'steel': 0.5,'fairy':0},
        'dark': {'normal':1,'fire': 1, 'water': 1, 'electric': 1,'grass': 1, 'ice': 1,'fighting':0.5, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':2, 'bug': 1, 'rock': 1,'ghost':2, 'dragon': 1,'dark':0.5, 'steel': 1,'fairy':0.5},
        'steel': {'normal':1,'fire': 0.5, 'water': 0.5, 'electric': 0.5,'grass': 1, 'ice': 2,'fighting':1, 'poison': 1, 'ground': 1, 'flying': 1,'psychic':1, 'bug': 1, 'rock': 2,'ghost':1, 'dragon': 1,'dark':1, 'steel': 0.5,'fairy':2},
        'fairy': {'normal':1,'fire': 0.5, 'water': 1, 'electric': 1,'grass': 1, 'ice': 1,'fighting':2, 'poison': 0.5, 'ground': 1, 'flying': 1,'psychic':1, 'bug': 1, 'rock': 1,'ghost':1, 'dragon': 2,'dark':2, 'steel': 0.5,'fairy':1},

    }

    p1_name = p1.get('name')
    p2_name = p2.get('name')

    p1_id = p1.get('id')
    p2_id = p2.get('id')

    p1_types = p1.get('types')
    p2_types = p2.get('types')

    p1_attack = p1.get('attack')
    p2_attack = p2.get('attack')

    p1_hp = p1.get('HP')
    p2_hp = p2.get('HP')

    p1_defense = p1.get('defense')
    p2_defense = p2.get('defense')

    for p1_type in p1_types:
        for p2_type in p2_types:
            if p1_type in type_modifiers and p2_type in type_modifiers:
                p1_attack = p1_attack * type_modifiers[p1_type][p2_type]
                p2_attack = p2_attack * type_modifiers[p2_type][p1_type]

    p1['attack'] = p1_attack
    p2['attack'] = p2_attack

    p1 = {'id': p1_id, 'name': p1_name, 'attack': p1_attack, 'HP': p1_hp, 'defense': p1_defense, 'type': p1_types }
    p2 = {'id': p2_id, 'name': p2_name, 'attack': p2_attack, 'HP': p2_hp, 'defense': p2_defense, 'type': p2_types }

    return p1, p2

# # Functions needed to run the main driver code
# def get_pokemon_id(name):
#     response= db.pokemon.find({'name': {'$eq':{name}}},{'id':1})
#     pokemon_data=response.json()
#     id=pokemon_data['id']
#     return id

# def pokenames_id():
#     # get the pokemon names from the mongodb database
#     pokemon = db.pokemon.find({},{'name':1})

#     return pokemon
def one_or_two():
    return random.randint(1,2)
# # Battle

def battle(pokemon_1,pokemon_2):

    battle_result = {
        "pokemon_1": pokemon_1["name"],
        "pokemon_2": pokemon_2["name"],
        "winner": "",
    }

    # p1_win = 0
    # p2_win = 0

    pokemon_2['health'] = pokemon_2['HP'] + pokemon_2['defense']
    pokemon_1['health'] = pokemon_1['HP'] + pokemon_1['defense']


    if pokemon_1['name'] == 'ditto':
        pokemon_1 = pokemon_2
        st.write(f"#### Wait! Ditto has changed into {pokemon_2['name']}! The same pokemon are battling it out!")
        st.write('---')
    elif pokemon_2['name'] == 'ditto':
        pokemon_2 = pokemon_1
        st.write(f"#### Wait! Ditto has changed into {pokemon_1['name']}! The same pokemon are battling it out!")
        st.write("---")

    if pokemon_1['attack'] == 0 and pokemon_2['attack'] == 0:
        st.write(f'##### Attacks are ineffective. The match is a draw.')
        battle_result['winner'] = 'No Contest'

    else:
        p1_or_p2 = one_or_two()
        if p1_or_p2 == 1:
            st.write(f"## Player 1 goes first!")
            st.write('---')

            while pokemon_1['health'] > 0 and pokemon_2['health'] > 0:
                pokemon_2['health'] = pokemon_2['health'] - pokemon_1['attack']
                if pokemon_2['health'] > 0:
                    output = f"{pokemon_2['name'].capitalize()} has {pokemon_2['health']}HP left!"
                    label = f"{pokemon_1['name'].capitalize()} has attacked {pokemon_2['name']} "
                    st.write(f"##### {label}!")
                    st.write(f'### {output}')
                    st.write("---")
                elif pokemon_2['health'] <= 0:
                    label = f"{pokemon_1['name'].capitalize()} has attacked {pokemon_2['name']} "
                    st.write(f"##### {label}!")
                    output = pokemon_2['name'] + ' is on 0HP and therefore unable to battle.'
                    st.write(f'### {output}')
                    st.write(f'# {pokemon_1["name"].upper()} WINS!')
                    break


                pokemon_1['health'] = pokemon_1['health'] - pokemon_2['attack']
                if pokemon_1['health'] > 0:
                    output = f"{pokemon_1['name'].capitalize()} has {pokemon_1['health']}HP left!"
                    label = f"{pokemon_2['name'].capitalize()} has attacked {pokemon_1['name']} "
                    st.write(f"##### {label}!")
                    st.write(f'### {output}')
                    st.write("---")
                elif pokemon_1['health'] <= 0:
                    output = pokemon_1['name'] + ' is on 0HP and therefore unable to battle.'
                    label = f"{pokemon_2['name'].capitalize()} has attacked {pokemon_1['name']} "
                    st.write(f"##### {label}!")
                    st.write(f'### {output}')
                    st.write(f'# {pokemon_2["name"].upper()} WINS!')
                    break

        elif p1_or_p2 == 2:
            st.write(f"## Player 2 goes first!")
            st.write('---')

            while pokemon_1['health'] > 0 and pokemon_2['health'] > 0:
                pokemon_1['health'] = pokemon_1['health'] - pokemon_2['attack']
                if pokemon_1['health'] > 0:
                    output = f"{pokemon_1['name'].capitalize()} has {pokemon_1['health']}HP left!"
                    label = f"{pokemon_2['name'].capitalize()} has attacked {pokemon_1['name']} "
                    st.write(f"##### {label}!")
                    st.write(f'### {output}')
                    st.write("---")
                elif pokemon_1['health'] <= 0:
                    output = pokemon_1['name'] + ' is on 0HP and therefore unable to battle.'
                    label = f"{pokemon_2['name'].capitalize()} has attacked {pokemon_1['name']} "
                    st.write(f"##### {label}!")
                    st.write(f'### {output}')
                    st.write(f'# {pokemon_2["name"].upper()} WINS!')
                    break



                pokemon_2['health'] = pokemon_2['health'] - pokemon_1['attack']
                if pokemon_2['health'] > 0:
                    output = f"{pokemon_2['name'].capitalize()} has {pokemon_2['health']}HP left!"
                    label = f"{pokemon_1['name'].capitalize()} has attacked {pokemon_2['name']} "
                    st.write(f"##### {label}!")
                    st.write(f'### {output}')
                    st.write("---")
                elif pokemon_2['health'] <= 0:
                    label = f"{pokemon_1['name'].capitalize()} has attacked {pokemon_2['name']} "
                    st.write(f"##### {label}!")
                    output = pokemon_2['name'] + ' is on 0HP and therefore unable to battle.'
                    st.write(f'### {output}')
                    st.write(f'# {pokemon_1["name"].upper()} WINS!')
                    break

        #     battle_result["log"].append({
        #         "pokemon_1_health": pokemon_1["health"],
        #         "pokemon_2_health": pokemon_2["health"]
        #     })

        if pokemon_1["health"] <= 0:
            battle_result["winner"] = pokemon_2["name"]
        else:
            battle_result["winner"] = pokemon_1["name"]

    matches.insert_one(battle_result)

    # print('-------------------------------------------------------')
    # print('End of game!')



def pokenames_id():
    response_2 = requests.get("https://pokeapi.co/api/v2/pokemon?limit=100000&offset=0")

    response_dict_2 = response_2.json()

    results = response_dict_2['results']

    names = []

    for items in results:
        names.append(items['name'])
        # print(items['name'])

    pokemon = pd.DataFrame(names)
    pokemon.index += 1
    pokemon.columns =['Names']
    pokemon.insert(1, 'id', range(1, 1 + len(pokemon)))

    return pokemon
print(pokenames_id())
df = pokenames_id()


gen_1 = df.loc[1:151]
gen_1 = gen_1.drop('id', axis=1)
gen_2 = df.loc[152:251]
gen_2 = gen_2.drop('id', axis=1)
gen_3 = df.loc[252:386]
gen_3 = gen_3.drop('id', axis=1)
gen_4 = df.loc[387:493]
gen_4 = gen_4.drop('id', axis=1)
gen_5 = df.loc[494:649]
gen_5 = gen_5.drop('id', axis=1)
gen_6 = df.loc[650:721]
gen_6 = gen_6.drop('id', axis=1)
gen_7 = df.loc[722:809]
gen_7 = gen_7.drop('id', axis=1)
gen_8 = df.loc[810:905]
gen_8 = gen_8.drop('id', axis=1)
gen_9 = df.loc[906:1010]
gen_9 = gen_9.drop('id', axis=1)

st.sidebar.write("**Generation I**")
st.sidebar.dataframe(gen_1)
st.sidebar.write("---")

st.sidebar.write("**Generation II**")
st.sidebar.dataframe(gen_2)
st.sidebar.write("---")

st.sidebar.write("**Generation III**")
st.sidebar.dataframe(gen_3)
st.sidebar.write("---")

st.sidebar.write("**Generation IV**")
st.sidebar.dataframe(gen_4)
st.sidebar.write("---")

st.sidebar.write("**Generation V**")
st.sidebar.dataframe(gen_5)
st.sidebar.write("---")

st.sidebar.write("**Generation VI**")
st.sidebar.dataframe(gen_6)
st.sidebar.write("---")

st.sidebar.write("**Generation VII**")
st.sidebar.dataframe(gen_7)
st.sidebar.write("---")

st.sidebar.write("**Generation VIII**")
st.sidebar.dataframe(gen_8)
st.sidebar.write("---")

st.sidebar.write("**Generation IX**")
st.sidebar.dataframe(gen_9)
st.sidebar.write("---")


# x = st.sidebar.text_input('Who is your favourite Pokémon:',0,5)
# z = st.sidebar.button("Submit")

with st.container():
    col_1,col_2,col_3 = st.columns(3)
    with col_1:
        file = open("/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/7dab25c7b14a249bbc4790176883d1c5_w200.gif", 'rb')
        contents = file.read()
        data_url = base64.b64encode(contents).decode('utf-8-sig')
        file.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)
    with col_2:

        st.markdown("<h3 style='text-align: center;font-size: 40px'>About the game:</h3>",unsafe_allow_html= True)
        st.write("**• This game is a Pokémon battle, which consists of a 1-player mode or 2-player mode.**")
        st.write("**• The Pokémon will take it in turns to battle it out using their attacks until one Pokémon \
                loses all their HP.**")
        st.write("**• Once their is a winner, the game will end.**")
        st.write("**• LETS GET INTO THE GAME!**")

    with col_3:
        file = open("/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/rayquaza.gif", 'rb')
        contents = file.read()
        data_url = base64.b64encode(contents).decode('utf-8-sig')
        file.close()
        st.markdown(f'<img src="data:image/gif;base64,{data_url}">',unsafe_allow_html = True)

st.write('---')
# tab1,tab2,tab3 = st.tabs(['Welcome to the battle!','Instructions.','Exit...'])

# Function to get attack modifiers

option = st.radio(
        "**Would you like to play?**",
        key="visibility",
        options=["Yes!", "Instructions", "Archive", "No"])

st.write('---')
if option == "Yes!":
    st.write("**Let's get into the game!**")

    with st.container():
        split1,split2,split3 = st.columns(3)

        with split1:
            op = st.selectbox(
            "**Select the mode:**",
            ("1-Player Mode", "2-Player Mode"))

            if op == "1-Player Mode":
                with split2:
                    st.tabs(["1-Player Mode"])
                    st.write("###### This is one-player mode, where you will be facing a randomly selected Pokémon.")
                    st.write("###### Choose wisely!")
                    with split3:
                        st.image('/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/greninja.png')

            if op == "2-Player Mode":
                with split2:
                    st.tabs(["2-Player Mode"])
                    st.write("###### This is two-player mode. Each player select your Pokémon!")
                    st.write("###### Choose wisely!")
                    with split3:
                        st.image("/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/lucario_x_infernap.png")

        # Indentation fix here
        st.write("---")

        p1_random = get_random_pokemon_id()
        cpu_random = get_random_pokemon_id()
        p2_random = get_random_pokemon_id()

        if op == "1-Player Mode":
            p1_name = st.text_input("**Enter your Pokémon name:**")
            form = st.form("form", clear_on_submit=True)
            submit = form.form_submit_button("Submit Now", disabled=False)

            if submit and p1_name in df['Names'].values:
                index = df.loc[df['Names'].values == p1_name]
                id_1 = index['id'].values[0]
                st.write(f"###### Your pokemon name is: {p1_name}. Your Pokémon ID is: {id_1}")
                p1 = get_pokemon_details(id_1)
                p2 = get_pokemon_details(cpu_random)
                st.write(f"###### Your opponent's Pokémon ID is: {cpu_random}.")
                pokemon_1, pokemon_2 = attack_mod(p1,p2)
                st.write('---')
                data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
                st.dataframe(data)
                st.write(f'---')
                st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
                st.write(f'---')
                bat = (battle(pokemon_1,pokemon_2))
                st.write(bat)
                st.write(f'---')

            elif submit and p1_name not in df['Names'].values:
                st.write("###### This Pokémon is not in the Pokédex. Randomly generating a Pokémon.")
                st.write(f"###### Your Pokémon ID is: {p1_random}.")
                p1 = get_pokemon_details(p1_random)
                p2 = get_pokemon_details(cpu_random)
                st.write(f"###### Your opponent's Pokémon ID is: {cpu_random}.")
                pokemon_1, pokemon_2 = attack_mod(p1,p2)
                st.write('---')
                data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
                st.dataframe(data)
                st.write(f'---')
                st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
                st.write(f'---')
                bat = (battle(pokemon_1,pokemon_2))
                st.write(bat)
                st.write(f'---')

            else:
                st.warning("Please enter a valid Pokémon name.")

        if op == "2-Player Mode":
            with st.container():
                c1,c2 = st.columns(2)
                with c1:
                    p1_name = st.text_input("**Player 1! Enter your Pokémon name:**")

                with c2:
                    p2_name = st.text_input("**Player 2! Enter your Pokémon name:**")

            form2 = st.form("form2", clear_on_submit=True)
            submit2 = form2.form_submit_button("Submit Now", disabled=False)

            if submit2 and p1_name in df['Names'].values and p2_name in df['Names'].values:
                index = df.loc[df['Names'].values == p1_name]
                id_1 = index['id'].values[0]
                st.write(f"###### Your Pokémon name is: {p1_name}. Your Pokémon ID is: {id_1}")
                p1 = get_pokemon_details(id_1)
                index2 = df.loc[df['Names'].values == p2_name]
                id_2 = index2['id'].values[0]
                st.write(f"###### Your Pokémon name is: {p2_name}. Your Pokémon ID is: {id_2}")
                p2 = get_pokemon_details(id_2)
                pokemon_1, pokemon_2 = attack_mod(p1,p2)
                st.write('---')
                data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
                st.dataframe(data)
                st.write(f'---')
                st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
                st.write(f'---')
                bat = (battle(pokemon_1,pokemon_2))
                st.write(bat)
                st.write(f'---')

            elif submit2 and p1_name not in df['Names'].values and p2_name in df['Names'].values:
                st.write("###### Player 1 Pokémon is not in the Pokédex. Randomly generating a Pokémon.")
                st.write(f"###### Player 1 Pokémon ID is: {p1_random}.")
                p1 = get_pokemon_details(p1_random)
                index2 = df.loc[df['Names'].values == p2_name]
                id_2 = index2['id'].values[0]
                st.write(f"###### Player 2 Pokémon name is: {p2_name}. Your Pokémon ID is: {id_2}")
                p2 = get_pokemon_details(id_2)
                pokemon_1, pokemon_2 = attack_mod(p1,p2)
                st.write('---')
                data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
                st.dataframe(data)
                st.write(f'---')
                st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
                st.write(f'---')
                bat = (battle(pokemon_1,pokemon_2))
                st.write(bat)
                st.write(f'---')

            elif submit2 and p1_name in df['Names'].values and p2_name not in df['Names'].values:
                index = df.loc[df['Names'].values == p1_name]
                id_1 = index['id'].values[0]
                st.write(f"###### Your Pokémon name is: {p1_name}. Your Pokémon ID is: {id_1}")
                p1 = get_pokemon_details(id_1)
                st.write("###### Player 2 Pokémon is not in the Pokédex. Randomly generating a Pokémon.")
                st.write(f"###### Your Pokémon ID is: {p2_random}.")
                p2 = get_pokemon_details(p2_random)
                pokemon_1, pokemon_2 = attack_mod(p1,p2)
                st.write('---')
                data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
                st.dataframe(data)
                st.write(f'---')
                st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
                st.write(f'---')
                bat = (battle(pokemon_1,pokemon_2))
                st.write(bat)
                st.write(f'---')

            elif submit2 and p1_name not in df['Names'].values and p2_name not in df['Names'].values:
                st.write("###### Player 1 Pokémon is not in the Pokédex. Randomly generating a Pokémon.")
                st.write(f"###### Player 1 Pokémon ID is: {p1_random}.")
                p1 = get_pokemon_details(p1_random)
                st.write("###### Player 2 Pokémon is not in the Pokédex. Randomly generating a Pokémon.")
                st.write(f"###### Your Pokémon ID is: {p2_random}.")
                p2 = get_pokemon_details(p2_random)
                pokemon_1, pokemon_2 = attack_mod(p1,p2)
                st.write('---')
                data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
                st.dataframe(data)
                st.write(f'---')
                st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
                st.write(f'---')
                bat = (battle(pokemon_1,pokemon_2))
                st.write(bat)
                st.write(f'---')
            else:
                st.warning("Please enter a valid Pokémon name.")

            # pokemon_1, pokemon_2 = attack_mod(p1,p2)
            # st.write('---')
            # data = pd.DataFrame([pokemon_1,pokemon_2],index=['Pokémon 1','Pokémon 2'])
            # st.dataframe(data)
            # st.write(f'---')
            # st.markdown("<h1 style='text-align: center;font-size: 50px'>FIGHT!</h1>",unsafe_allow_html= True)
            # st.write(f'---')
            # bat = (battle(pokemon_1,pokemon_2))
            # st.write(bat)
            # st.write(f'---')

if option == "Instructions":
    with st.container():
        tab1,tab2 = st.tabs(['Main Instructions','Pokemon Types'])
        with tab1:
            h1,h2 = st.columns(2)
            with h2:
                st.write("## Let's go through the instructions:")
                st.write("##### • Firstly, you will select a 1-player or 2-player mode.")
                st.write("##### • Then, you will type in the Pokémon of your choice. If your Pokémon is not typed in correctly, then it will be randomly generated.")
                st.write("##### • Finally, the two Pokémon will battle it out until one loses all their HP, leaving other victorious!")
                st.write("##### • Remember, a Pokémon with higher HP does not necessarily mean the win! The types, attacks and defense all come into play as well!")
                st.write("##### • So choose wisely!!!")
                st.write("##### • You now ready for the battle?")
            with h1:
                st.image("/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/blastoise_50.png")
        with tab2:
            cl1,cl2 = st.columns(2)
            with cl1:
                st.write('## Pokémon Types')
                st.write('##### • Each Pokémon has at least one type. This will affect their attacks during combat.')
                st.write('##### • A Pokémon can have two types, which might work to their (dis)advantage!')
                st.write('---')
                type = {'Multiplier':['x2','x1/2','0','x1'],'Effect':['Double Damage','Half Damage','No Damage','No Effect']}
                df3 = pd.DataFrame(type)
                df4 = df3.set_index('Multiplier')
                st.dataframe(df4)
            with cl2:
                st.image('/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/PokemonTypes.webp')

if option == "Archive":
    st.markdown("<h2 style='text-align: center;font-size: 40px'>Here is data on the previous matches that have happened:</h2>",unsafe_allow_html= True)
    st.write("---")

    def archive():
    # Retrieve all battle documents from the collection
        battles = matches.find()

        # Print each battle's details

        battles = matches.find().sort("_id", pymongo.DESCENDING)

    # Display each battle result on the Streamlit website
        for battle_result in battles:
            st.write("###### Pokemon 1:", battle_result["pokemon_1"])
            st.write("###### Pokemon 2:", battle_result["pokemon_2"])
            st.write("#### Winner:", battle_result["winner"])


            # for log in battle["log"]:

            #     st.write("Pokemon 1 HP:", log["pokemon_1_health"])
            #     str.write("Pokemon 2 HP:", log["pokemon_2_health"])

            st.write("---")

    archive()

if option == "No":
    st.markdown("<h3 style='text-align: center;font-size: 40px'>GAME OVER!</h2>",unsafe_allow_html= True)
    st.markdown("<h3 style='text-align: center;font-size: 40px'>Thanks for playing!</h2>",unsafe_allow_html= True)
