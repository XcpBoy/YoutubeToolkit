# ----------------------
# RESTRICCIONES Y CONFIGURACIÓN GLOBAL
# ----------------------

# 🚫 Canales bloqueados (no permitidos para búsqueda o descarga)
CHANNEL_BLACKLIST = [
    'Gothamchess', 'Brendan Miller', 'Adam Conover', 'Ordinary Things', 'Tri Line', 
    'kurzgesagt', 'Esquizofrenia Natural', 'Cordura Artificial', 'Adef', 'Artchad',
    'Half as interesting', 'Living Deadman', 'Casi Creativo', 'Jesse James West',
    'The Duck Stories', 'Super Eye Patch Wolf', 'Theorist', 'Batakotoons', 'PapaMeat',
    'OffendingEverybody', 'MeatCanyon', 'Dragoon', 'Adam Something', 'Professor Lando',
    'Wefere', 'SCA entreteinment', 'Factorio', 'Enchufe TV', 'Pipepino', 'Fzst',
    'Ricky tafollados', 'Ricky Tafolla', 'QuickLag', 'Triline', 'CircleToonsHD',
    'El ultimo TV nauta', 'Casually Explained', 'Nico Core', 'Sr.Pelo', 'BackGuy',
    'ManlyBadassHero', 'Gonzok', 'El mundo de zowl', 'Dross', 'Drossrank', 'T3rr0r',
    'Bismuth', 'Summoning Salt', 'Nostalfan', 'Dr. Nowhere', 'Joseju', 'Jeff Nippard',
    'LALITO RAMS', 'Ciencia de Sofa', 'Blue Jay', 'Sam O Nella', 'Lul Yeah',
    'JackScepticEye', 'Alpharad', 'Ludwig', 'Language Simp', 'Tu cosmopolis',
    'Missasinfonia', 'Theory', 'Solar Sands', 'EmpLemon', 'El plech', 
    'Lessons in Meme Culture', 'Asmongold', 'Frozen prime', 'Mr Beast', 'Meat Cannyon',
    'Papa Meat', 'Julio Di Esto', 'Doobus Goobus', 'AnzuTops 365', 'Sr Pelo', 
    'ssethtzeentach', 'Greg Doucette', 'Anzutops777', 'charnew', 'Beluga', 
    'Chilaclips Esquizitos', 'penguinz0', 'Markiplier', 'Haroo', '3huntleo', 
    'The game theorist', 'Majorkill', 'Wesshamer', 'Luetin', 'X shift', 'Fernanfloo',
    'JuegaGerman', 'El Rubius', 'Enchufe TV', 'Auron', 'AuronPlay', 'pChal', 
    'Alpharad', 'WolfeyVGC', 'Me dicen dai', 'Memenade', 'Missasinfonia',
    'Jaiden animations', 'the0dd1out', 'somethingelseyt', 'I did a thing', 
    'Tier Zoo', 'Tale foundry', 'Curious archive', 'Overly Sarcastic Prodductions',
    'BaityBait', 'HamonBeat', 'Javienator3000', 'Fitnico', 'Dibrah', 'Cookie', 
    'Waffle Time'
]

# 🚫 Palabras clave bloqueadas (filtra títulos o descripciones)
KEYWORD_BLACKLIST = [
    'Pokemon', 'syfr', 'purge', 'Magi ', 'Futurama', 'Million Monster Millitia',
    'Tower Defense', 'Overlord', 'Sinbad', 'Pokemusu', 'Franco Escamilla',
    'Dandadan', 'Manga', 'Anime', 'Creppypasta', 'OPM', 'One Punch Man', 'Smash',
    'Bloons', 'Kirby', 'Dragon Ball', 'Phineas', 'Gumball', 'FF', 'Final fantasy',
    'Deltarune', 'look outside ', 'Dead Cells', 'Hollow Knight', 'Death note',
    'Bloons TD6', 'Terraria', 'Comic', 'Hello Kitty', 'TCG', 'Speedrun',
    'Magic the gathering', 'Yu gi oh', 'Spiderman', 'Marvel', 'Noita', 'Dofus',
    'Mod', 'nuzlocke', 'Ludwig', 'Summoner', 'Friday Night Funkin', 'Warhammer',
    'meme', 'Minecraft', 'Silksong', 'videogame', 'roguelike', 'lore', 'FNAF',
    'fnf', 'Steel ball run', 'JoJo', 'Slay the spire', 'Slice and Dice', 'Defect',
    'challenge', 'Dead Internet Theory'
]

# ⚙️ Límites de descargas diarias por tipo
DOWNLOAD_LIMITS = {
    "video": 3,
    "audio": 5,
    "playlist": 7
}

# 📅 Restricción de día 
def check_day_restriction():
    """Permite ejecutar el script solo los domingos."""
    from datetime import datetime
    today = datetime.now().weekday()  # 0 = lunes ... 6 = domingo
    if today == 5 or today == 6:
        return 
    else: 
        print("🚫 Las funciones de búsqueda y descarga solo están disponibles los domingos.")
        exit(0)
