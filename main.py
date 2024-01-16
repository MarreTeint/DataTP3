# Import des modules nécessaires
import VideoGames_pb2  # Le module généré à partir de VideoGames.proto
import Util_pb2       # Le module généré à partir de Util.proto


def create_game_collection():
    # Création d'une collection de jeux vidéo
    game_collection = VideoGames_pb2.GameCollection()

    # Ajout de jeux vidéo à la collection
    fifa_2020 = game_collection.games.add()
    fifa_2020.name = "FIFA 2020"
    fifa_2020.game_type.append(VideoGames_pb2.GameType.SPORTS)

    monkey_island = game_collection.games.add()
    monkey_island.name = "Monkey Island"
    monkey_island.game_type.append(VideoGames_pb2.GameType.ADVENTURE)
    monkey_island.date_purchase.GetCurrentTime()

    vroum = game_collection.games.add()
    vroum.name = "Vroum"
    vroum.game_type.extend([VideoGames_pb2.GameType.RACING, VideoGames_pb2.GameType.SPORTS])
    vroum.date_purchase.GetCurrentTime()

    # Ajout de parties jouées pour le jeu "Vroum"
    play1 = vroum.game_plays.add()
    play1.date_play.day = 30
    play1.date_play.month = 5
    play1.date_play.year = 2018
    play1.minutes_played = 125

    play2 = vroum.game_plays.add()
    play2.date_play.day = 2
    play2.date_play.month = 6
    play2.date_play.year = 2018
    play2.minutes_played = 45

    return game_collection

def save_collection_to_file(game_collection, filename):
    # Sérialisation de la collection de jeux et sauvegarde dans un fichier
    with open(filename, "wb") as f:
        f.write(game_collection.SerializeToString())

def load_collection_from_file(filename):
    # Chargement d'une collection de jeux depuis un fichier
    game_collection = VideoGames_pb2.GameCollection()
    with open(filename, "rb") as f:
        game_collection.ParseFromString(f.read())
    return game_collection

def add_play_to_game(game_collection, game_name, date_play, minutes_played):
    # Ajout d'une nouvelle partie à un jeu existant dans la collection
    for game in game_collection.games:
        if game.name == game_name:
            new_play = game.game_plays.add()
            new_play.date_play.CopyFrom(date_play)
            new_play.minutes_played = minutes_played
            return

def main():
    # Création de la collection de jeux
    my_game_collection = create_game_collection()

    # Affichage de la collection avant sauvegarde
    print("Collection avant sauvegarde :")
    print(my_game_collection)

    # Sauvegarde de la collection dans un fichier
    save_collection_to_file(my_game_collection, "game_collection.dat")

    # Chargement de la collection depuis le fichier
    loaded_collection = load_collection_from_file("game_collection.dat")

    # Ajout d'une nouvelle partie au jeu "FIFA 2020"
    new_play_date = Util_pb2.Date()
    new_play_date.day = 1
    new_play_date.month = 1
    new_play_date.year = 2022
    add_play_to_game(loaded_collection, "FIFA 2020", new_play_date, 60)

    # Affichage de la collection après modification
    print("\nCollection après modification :")
    print(loaded_collection)

if __name__ == "__main__":
    main()
