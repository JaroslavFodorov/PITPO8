class Track:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class PlaylistManager:
    def __init__(self):
        self.playlist = []
        self.playlist_name = ""

    def create_playlist(self):
        self.playlist_name = input("Введите название плейлиста: ")

    def add_track_to_playlist(self, track):
        self.playlist.append(track)

    def display_playlist(self):
        if not self.playlist:
            print("Playlist is empty.")
        else:
            print(f"Playlist '{self.playlist_name}':")
            for idx, track in enumerate(self.playlist, start=1):
                print(f"{idx}. {track.title} - {track.artist} [{track.duration}]")

# Пример использования
if __name__ == "__main__":
    # Создаем менеджер плейлиста
    playlist_manager = PlaylistManager()

    # Создаем плейлист
    playlist_manager.create_playlist()

    while True:
        print("\nМеню:")
        print("1. Добавить трек в плейлист")
        print("2. Показать плейлист")
        print("3. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название трека: ")
            artist = input("Введите исполнителя трека: ")
            duration = input("Введите продолжительность трека (в формате минут:секунды): ")
            track = Track(title, artist, duration)
            playlist_manager.add_track_to_playlist(track)
            print("Трек добавлен в плейлист.")
        elif choice == "2":
            playlist_manager.display_playlist()
        elif choice == "3":
            break
        else:
            print("Некорректный выбор. Пожалуйста, введите номер действия из меню.")
