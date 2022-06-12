import configparser
import os
import shutil
import logging

GAME_FOLDER = ["Skyrim Special Edition", "Fallout4"]

def init_logger():
    logging.basicConfig(
        filename='output.log', 
        filemode='w', 
        format='%(asctime)s - %(message)s'
    )

    logger = logging.getLogger()

    logger.setLevel(logging.DEBUG)

    return logger

logger = init_logger()

def get_config():
    logger.info("Reading config.ini...")
    filename = 'config.ini'

    config = configparser.ConfigParser()

    try:
        config.read(filename)
    except:
        logger.error("ERROR: Unable to locate or read config.ini")
        exit()

    return config

def get_cc_list(game_mode:int):
    logger.info("Trying to get list of creation club plugins...")
    loadorder_path = os.path.join(os.getenv("LOCALAPPDATA"), GAME_FOLDER[game_mode], "loadorder.txt")

    if not os.path.exists(loadorder_path):
        logger.error("ERROR: Unable to locate loadorder.txt")
        exit()

    with open(loadorder_path) as fp:
        cc_files = [s for s in fp.read().splitlines() if s.startswith("cc")]
        
        if len(cc_files) == 0:
            logger.info("No creation club plugins found.")
            exit()
        else:
            logger.info(f"Found {len(cc_files)} creation club plugins")

        return cc_files

def update_plugins_file(game_mode:int, cc_files:list):
    local_appdata = os.getenv("LOCALAPPDATA")
    folder = os.path.join(local_appdata, GAME_FOLDER[game_mode])

    if not os.path.exists(folder):
        logger.error(f"ERROR: Unable to locate \"{GAME_FOLDER[game_mode]}\" folder inside {local_appdata}")
        exit()

    plugins_file = os.path.join(folder, "plugins.txt")

    if not os.path.exists(plugins_file):
        logger.error("ERROR: Unable to find plugins.txt file")
        exit()

    backup_file = os.path.join(folder, "plugins_backup.txt")

    # Create a back up copy
    logger.info("Creating plugins.txt backup...")
    try:
        shutil.copyfile(plugins_file, backup_file)
        logger.info("Backup created")
    except Exception as e:
        logger.error("ERROR: Unable to create back up due to the following error")
        logger.error(e)

    # Update original plugins.txt
    logger.info("Updating plugins.txt...")
    with open(plugins_file) as fp:
        ls = fp.read().splitlines()
        for i in range(len(cc_files) - 1, -1, -1):
            logger.info(f"Adding {cc_files[i]}")
            ls.insert(0, "*" + cc_files[i])
    with open(plugins_file, "w") as f:
        for s in ls:
            f.write(s + "\n")

def main():
    config = get_config()

    game_mode = 0

    try:
        game_mode = int(config.get("SETTINGS", "Game"))
        if game_mode < 0 or game_mode > len(GAME_FOLDER) - 1:
            raise Exception("Invalid game specified")
    except Exception:
        logger.error("ERROR: Unable to determine game mode. This might be caused when the program was unable to find the property \"Game\" under \"[SETTINGS]\", or an invalid value was inserted.")
        exit()

    cc_files = get_cc_list(game_mode)
    update_plugins_file(game_mode, cc_files)

    logger.info("Process completed successfully")

if __name__ == '__main__':
    main()