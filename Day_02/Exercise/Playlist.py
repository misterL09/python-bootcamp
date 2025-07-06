import json
def add(song, inner_playlist):
    """Add song to playlist"""
    inner_playlist.append(song)

def remove(song, inner_playlist):
    """Remove song from playlist (if there)"""
    if song not in inner_playlist:
        print("Already remove")
    else:
        inner_playlist.remove(song)

def play(inner_playlist):
    """Print the first song in the playlist (if any) and remove"""
    song = inner_playlist.pop(0)
    print("Now Playing...",song)

def show_all(inner_playlist):
    message = "Here are your play list"
    print(f"{message:=^10}")
    for all_list in inner_playlist:
        print(all_list)
    """Print all contents in the playlist"""

def save(inner_playlist, filepath):
    """Save current playlist to filepath"""
    with open(filepath, 'w') as file:
        json.dump(inner_playlist, file, indent = 4)

def load(filepath) -> list[str]:
    """Load a new playlist from filepath and return it"""
    with open(filepath, 'r') as file:
        return json.load(file)


def playlist_app():
    """
    While user doesn’t want to stop, keep asking for command
    then do the task requested
    """
    playlist =[]
    start_process = False
    while not start_process:
        input_command = input("Enter Command:")
        list_command = ('add','remove','play','show_all','save','load','stop')
        if input_command not in list_command:
            print("not in the list of command")
        else:
            match input_command:
                case "stop":
                    start_process = True
                case "add":
                    new_song = input("Enter new song: ")
                    add(new_song,playlist)
                case "remove":
                    remove_song = input("Enter remove song: ")
                    remove(remove_song,playlist)
                case "play":
                    play(playlist)
                case "show_all":
                    show_all(playlist)
                case  "save":
                    filename = input("Enter filename: ")
                    save(playlist,filename)
                case "load":
                    load_file = input("Enter load list: ")
                    print('loading playlist...')
                    playlist = load(load_file)

playlist_app()