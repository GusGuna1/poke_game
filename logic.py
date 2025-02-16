import aiohttp  # A library for asynchronous HTTP requests
import random

class Pokemon:
    pokemons = {}
    # Object initialisation (constructor)
    def __init__(self, pokemon_trainer):
        self.pokemon_trainer = pokemon_trainer
        self.pokemon_number = random.randint(1, 1000)
        self.name = None
        self.img = None
        self.ability = None
        self.hp = random.randint(50,150)
        self.power = random.randint(30,175)
        if pokemon_trainer not in Pokemon.pokemons:
            Pokemon.pokemons[pokemon_trainer] = self
        else:
            self = Pokemon.pokemons[pokemon_trainer]
    
    async def attack(self, enemy):
        if isinstance(enemy, Wizard):  # Periksa apakah musuh adalah tipe data Penyihir (instance dari kelas Penyihir)
            kesempatan = random.randint(1,5)
            if kesempatan == 1:
                return "Pokemon penyihir menggunakan perisai dalam pertarungan"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Pertarungan @{self.pokemon_trainer} dengan @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"@{self.pokemon_trainer} menang melawan @{enemy.pokemon_trainer}!"

    async def get_name(self):
        # An asynchronous method to get the name of a pokémon via PokeAPI
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return data['forms'][0]['name']  # Returning a Pokémon's name
                else:
                    return "Pikachu"  # Return the default name if the request fails

    async def info(self):
        # A method that returns information about the pokémon
        if not self.name:
            self.name = await self.get_name()  # Retrieving a name if it has not yet been uploaded
            self.ability = await self.show_ability()
            
        return f"The name of your Pokémon: {self.name} HP: {self.hp} Power: {self.power} ability: {self.ability}"  # Returning the string with the Pokémon's name

    async def show_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    return random.choice([data['sprites']['front_default'], data['sprites']['front_shiny']]) # Returning a Pokémon's name
                else:
                    return "not found"  # Return the default name if the request fails
        # An asynchronous method to retrieve the URL of a pokémon image via PokeAPI

    async def show_ability(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'  # URL API for the request
        async with aiohttp.ClientSession() as session:  # Opening an HTTP session
            async with session.get(url) as response:  # Sending a GET request
                if response.status == 200:
                    data = await response.json()  # Receiving and decoding JSON response
                    skills = ""
                    for skill in data['abilities']:
                        skills += skill['name'] + " "
                    return skills # Returning a Pokémon's name
                else:
                    return "not found"
class Wizard(Pokemon):
    async def attack(self, enemy):
         await super().attack(enemy)

class Fighter(Pokemon):
    async def attack(self, enemy):
        kekuatan_super = random.randint(5,15)
        self.kekuatan += kekuatan_super
        hasil = await super().attack(enemy)
        self.kekuatan -= kekuatan_super
        return hasil + f"\nPetarung menggunakan serangan super dengan kekuatan:{kekuatan_super}"
    
# if __name__ == '__main__':
#     wizard = Wizard("username1")
#     fighter = Fighter("username2")

#     print(wizard.info())
#     print()
#     print(fighter.info())
#     print()
#     print(fighter.attack(wizard))
    
