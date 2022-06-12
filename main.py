import configparser
import os
import shutil

GAME_FOLDER = ["Skyrim Special Edition", "Fallout4"]

def get_config():
    filename = 'config.ini'

    config = configparser.ConfigParser()
    config.read(filename)

    return config

def get_cc_list(game_mode:int):
    loadorder_path = os.path.join(os.getenv("LOCALAPPDATA"), GAME_FOLDER[game_mode], "loadorder.txt")
    with open(loadorder_path) as fp:
        cc_files = [s for s in fp.read().splitlines() if s.startswith("cc")]
        return cc_files

def update_plugins_file(game_mode:int, cc_files:list):
    folder = os.path.join(os.getenv("LOCALAPPDATA"), GAME_FOLDER[game_mode])
    plugins_file = os.path.join(folder, "plugins.txt")
    backup_file = os.path.join(folder, "plugins_backup.txt")

    # Create a back up copy
    shutil.copyfile(plugins_file, backup_file)

    # Update original plugins.txt
    with open(plugins_file) as fp:
        ls = fp.read().splitlines()
        for i in range(len(cc_files) - 1, -1, -1):
            ls.insert(0, "*" + cc_files[i])
    with open(plugins_file, "w") as f:
        for s in ls:
            f.write(s + "\n")

def main():
    config = get_config()
    game_mode = int(config.get("SETTINGS", "Game"))
    cc_files = get_cc_list(game_mode)
    update_plugins_file(game_mode, cc_files)

if __name__ == '__main__':
    main()