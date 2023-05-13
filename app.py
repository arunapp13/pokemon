import streamlit as st
import base64
import pandas as pd
import requests
import json
import random

# import  03-HTML-API import pokemon-api //Users//arun._.appulingam//Data223/Python//03-HTML-API//pokemon-api.ipynb

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


    # Grass type Attack modifier

    if 'grass' in p1_types and 'fire' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2
    elif 'grass' in p1_types and 'water' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2
    elif 'grass' in p1_types and 'electric' in p2_types:
        p2_attack = p2_attack / 2

    elif 'grass' in p1_types and 'grass' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack / 2

    elif 'grass' in p1_types and 'ice' in p2_types:
        p2_attack = p2_attack * 2

        # no attack modifier needed
    elif 'grass' in  p1_types and 'poison' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2

    elif 'grass' in p1_types and 'ground' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2

    elif 'grass' in p1_types and 'flying' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2

        # no attack modifier needed
    elif 'grass' in p1_types and 'bug' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2

    elif 'grass' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack * 2

        # no attack modifier needed
    elif 'grass' in p1_types and 'dragon' in p2_types:
        p1_attack = p1_attack / 2

        # no attack modifier needed
    elif 'grass' in p1_types and 'steel' in p2_types:
        p1_attack = p1_attack / 2


 # Normal type Attack modifier
        # no attack modifier needed
    if 'normal' in p1_types and 'fighting' in p2_types:
        p2_attack = p2_attack * 2

    elif 'normal' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack / 2

    elif 'normal' in p1_types and 'ghost' in p2_types:
        p1_attack = 0
        p2_attack = 0

        # no attack modifier needed
    elif 'normal' in p1_types and 'steel' in p2_types:
        p1_attack = p1_attack / 2


# Fire type Attack modifier
    if 'fire' in p1_types and 'fire' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack / 2

    elif 'fire' in p1_types and 'water' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2

    elif 'fire' in p1_types and 'grass' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2

    elif 'fire' in p1_types and 'ice' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2

        # no attack modifier needed
    elif 'fire' in p1_types and 'ground' in p2_types:
        p2_attack = p2_attack * 2

        # no attack modifier needed
    elif 'fire' in p1_types and 'bug' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2

    elif 'fire' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2

        # no attack modifier needed
    elif 'fire' in p1_types and 'dragon' in p2_types:
        p1_attack = p1_attack / 2

        # no attack modifier needed
    elif 'fire' in p1_types and 'steel' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2
    elif 'fire' in p1_types and 'fairy' in p2_types:
        p2_attack = p2_attack / 2


# Water type Attack modifier
    if 'water' in p1_types and 'water' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack / 2

    elif 'water' in p1_types and 'electric' in p2_types:
         p2_attack = p2_attack * 2

    elif 'water' in p1_types and 'ice' in p2_types:
         p2_attack = p2_attack / 2

    elif 'water' in p1_types and 'grass' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2

    elif 'water' in p1_types and 'fire' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2

    elif 'water' in p1_types and 'ground' in p2_types:
        p1_attack = p1_attack * 2

    elif 'water' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack * 2

        # no attack modifier needed
    elif 'water' in p1_types and 'dragon' in p2_types:
        p1_attack = p1_attack / 2

        # no attack modifier needed
    elif 'water' in p1_types and 'steel' in p2_types:
        p2_attack = p2_attack / 2


# Electric type Attack modifier
    if 'electric' in p1_types and 'electric' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack / 2

    elif 'electric' in p1_types and 'grass' in p2_types:
        p1_attack = p1_attack / 2

    elif 'electric' in p1_types and 'water' in p2_types:
         p1_attack = p1_attack * 2

    elif 'electric' in p1_types and 'ground' in p2_types:
        p1_attack = 0
        p2_attack = p2_attack * 2

    elif 'electric' in p1_types and 'flying' in p2_types:
        p1_attack = p1_attack * 2
        p2_attack = p2_attack / 2

    elif 'electric' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack * 2

        # no attack modifier needed
    elif 'electric' in p1_types and 'steel' in p2_types:
        p2_attack = p2_attack / 2



# Ice type Attack modifier
    if 'ice' in p1_types and 'ice' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack / 2

    if 'ice' in p1_types and 'fire' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2
    elif 'ice' in p1_types and 'water' in p2_types:
        p1_attack = p1_attack / 2
        # no attack modifier needed
    elif 'ice' in p1_types and 'ground' in p2_types:
        p1_attack = p1_attack * 2

    elif 'ice' in p1_types and 'grass' in p2_types:
        p1_attack = p1_attack * 2

    elif 'ice' in p1_types and 'fighting' in p2_types:
        p1_attack = p1_attack * 2

    elif 'ice' in p1_types and 'rock' in p2_types:
        p2_attack = p2_attack * 2

        # no attack modifier needed
    elif 'ice' in p1_types and 'dragon' in p2_types:
        p1_attack = p1_attack * 2

        # no attack modifier needed
    elif 'ice' in p1_types and 'steel' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2


# Fighting type Attack modifier
    if 'fighting' in p1_types and 'normal' in p2_types:
        p1_attack = p1_attack * 2
    elif 'fighting' in p1_types and 'ice' in p2_types:
        p2_attack = p2_attack * 2
        # no attack modifier needed
    elif 'fighting' in p1_types and 'ground' in p2_types:
        p1_attack = p1_attack * 2
    elif 'fighting' in p1_types and 'poison' in p2_types:
        p1_attack = p1_attack / 2
    elif 'fighting' in p1_types and 'flying' in p2_types:
        p1_attack = p1_attack / 2
    elif 'fighting' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack * 2
        # no attack modifier needed
    elif 'fighting' in p1_types and 'dragon' in p2_types:
        p1_attack = p1_attack / 2
        # no attack modifier needed
    elif 'fighting' in p1_types and 'steel' in p2_types:
        p2_attack = p2_attack / 2

# Poison type Attack modifier
    if 'poison' in  p1_types and 'poison' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack / 2
        # no attack modifier needed
    elif 'poison' in p1_types and 'ground' in p2_types:
        p1_attack = p1_attack / 2
        p2_attack = p2_attack * 2
    elif 'poison' in p1_types and 'flying' in p2_types:
        p1_attack = p1_attack / 2
        # no attack modifier needed
    elif 'poison' in p1_types and 'pychic' in p2_types:
        p2_attack = p2_attack * 2
        # no attack modifier needed
    elif 'poison' in p1_types and 'bug' in p2_types:
        p2_attack = p2_attack / 2
    elif 'poison' in p1_types and 'rock' in p2_types:
        p1_attack = p1_attack / 2

    elif 'poison' in p1_types and 'ghost' in p2_types:
        p1_attack = p1_attack / 2
        # no attack modifier needed
    elif 'poison' in p1_types and 'dragon' in p2_types:
        pass
    elif 'poison' in p1_types and 'dark' in p2_types:
        pass
        # no attack modifier needed
    elif 'poison' in p1_types and 'steel' in p2_types:
        p1_attack = 0
    elif 'poison' in p1_types and 'fairy' in p2_types:
        pass


    p1 = {'id': p1_id, 'name': p1_name, 'attack': p1_attack, 'HP': p1_hp, 'defense': p1_defense, 'type': p1_types }
    p2 = {'id': p2_id, 'name': p2_name, 'attack': p2_attack, 'HP': p2_hp, 'defense': p2_defense, 'type': p2_types }
    # package p1 and p2 into dictionaries exactly like the input dictionaries

    return p1, p2

# # Battle

def battle(pokemon_1,pokemon_2):

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

    else:
        while pokemon_1['health'] > 0 and pokemon_2['health'] > 0:
            pokemon_2['health'] = pokemon_2['health'] - pokemon_1['attack']
            if pokemon_2['health'] > 0:
                output = f"{pokemon_2['name'].capitalize()} has {pokemon_2['health']}HP left!"
                st.write(f'**{output}**')
            elif pokemon_2['health'] <= 0:
                output = pokemon_2['name'] + ' is on 0HP and therefore unable to battle.'
                st.write(f'**{output}**')
                st.write(f'#### {pokemon_1["name"].upper()} WINS!')
                break


            pokemon_1['health'] = pokemon_1['health'] - pokemon_2['attack']
            if pokemon_1['health'] > 0:
                output = f"{pokemon_1['name'].capitalize()} has {pokemon_1['health']}HP left!"
                st.write(f'**{output}**')
            elif pokemon_1['health'] <= 0:
                output = pokemon_1['name'] + ' is on 0HP and therefore unable to battle.'
                st.write(f'**{output}**')
                st.write(f'#### {pokemon_2["name"].upper()} WINS!')
                break

    # print('-------------------------------------------------------')
    # print('End of game!')


# all_pokemon = []
# for i in range(1, 1011):
#     details = get_pokemon_details(i)
#     all_pokemon.append(details)

# # Pandas DataFrame from the dictionary "pokemon_quick_details"
# df = pd.DataFrame(all_pokemon)
# df.index += 1

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
        options=["Yes!", "Instructions", "No"])

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
                st.write('##### • Each Pokémon has at least one type. This will affect them during combat.')
                st.write('##### • A Pokémon can have two types, which might work to their (dis)advantage!')
                st.write('---')
                type = {'Colour':['green','red','black','white'],'Damage':['x2','x1/2','0','x1']}
                df3 = pd.DataFrame(type)
                df4 = df3.set_index('Colour')
                st.dataframe(df4)
            # with cl2:
                # st.image('/Users/arun._.appulingam/Data223/Python/03-HTML-API/pictures/types.png')

if option == "No":
    st.markdown("<h3 style='text-align: center;font-size: 40px'>GAME OVER!</h2>",unsafe_allow_html= True)
    st.markdown("<h3 style='text-align: center;font-size: 40px'>Thanks for playing!</h2>",unsafe_allow_html= True)
