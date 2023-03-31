from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return "Welcome to the Pokedex!"

@app.route('/pokemon')
def pokemon():
    pokemon = {
        "name": "Pikachu",
        "number": "025",
        "type": "Electric",
        "description": "Pikachu is an Electric-type Pokémon that evolves from Pichu when leveled up with high friendship and evolves into Raichu when exposed to a Thunder Stone.",
        "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/25.png"
    }
    return render_template("pokemon.html", pokemon=pokemon)

@app.route('/static/<path:path>')
def serve_css(path):
    return send_from_directory('/static/css/', path)
