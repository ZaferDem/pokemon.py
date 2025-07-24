import aiohttp
import random

class Pokemon:
    pokemons = {}

    def __init__ (self, pokemon_trainer):
        self.pokemon_trainer=pokemon_trainer
        self.pokemon_number= random.randint(1,1300)
        self.name = None
        self.img = None
        self.attack = None
        self.defense= None
        self.hp = None

    async def get_name(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["forms"][0]["name"]
                else:
                    return "Pikachu"
                
    async def show_img(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                if response.status == 200:
                    data = await response.json()
                    return data["sprites"]["front_default"]
                else:
                    return None
                

        
    async def fetch_stats(self):
            stats = {"attack": 0, "defense": 0, "hp": 0}
            url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"   
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        data = await response.json()
                        for stat in data["stats"]:
                            name = stat["stat"]["name"]
                            if name == "attack":
                                stats["attack"] = stat["base_stat"] 
                            elif name == "defense":
                                stats["defense"] = stat["base_stat"] 
                            elif name == "hp":
                                stats["hp"] = stat["base_stat"]            
        
            return stats 
    
    async def set_stats(self):
        stats = await self.fetch_stats                
        self.attack =stats["attack"]
        self.hp =stats["hp"]
        self.defense = stats["defense"]
        print(stats)


    async def attack(self, enemy):
        if isinstance(enemy):
            if enemy.hp > self.attack:
                enemy.hp -= self.attack
                return f"Pokemon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ne saldırdı\n@{enemy.pokemon_trainer}'nin sağlık durumu şimdi {enemy.hp}"
            else:
                enemy.hp = 0
                return f"Pokemon eğitmeni @{self.pokemon_trainer} @{enemy.pokemon_trainer}'ni yendi"
            


        