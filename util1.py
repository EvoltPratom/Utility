import os
import json
import shutil

def find_duplicates(folder_path, rm_dup=False):
    '''
    folder_path   : path of a folder to find duplicates in
    rm_dup        : Boolean for removing duplicates

    returns a dict of duplicates

    Should recursively traverse everyfolder and find duplicates
    '''
    print(folder_path)

    dup = {}
    for root, dire, files in os.walk(folder_path):
        # print(root)

        for file in files:
            # print(os.path.join(root, file))
            if file not in dup:
                dup[file] = 0
            if file in dup:
                dup[file] += 1
                if rm_dup and dup[file] > 1:
                    print(f"Removing duplicate file{os.path.join(root,file)}")
                    os.remove(os.path.join(root, file))
    y = dup.copy()
    for i in y:
        if y[i] == 1:
            dup.pop(i)

    # print(dup)
    return dup


def organize(folder_path=None, config=None):
    '''
    Organizes the folder following the config
    Config:
    can be a dict obj or a json file
        eg   :
            {
                "Images":"img,jpg,png",
                "MyMedia":"mp4,mp3,m4a"
            }
    '''

    if folder_path is None:
        folder_path = os.getcwd()
    if config is None:
        config = r"D:\pyfiles\pyutils\test.json"

    # load config file as json
    if isinstance(config, str):
        with open(config, 'r') as json_file:
            config = json.loads(json_file.read())

    # make folder as in config if doesn't exist
    for fol in config:
        if not os.path.exists(os.path.join(folder_path, fol)):
            os.mkdir(os.path.join(folder_path, fol))

    #make a duplicates folder to keep all the duplicates if it doesn't exist
    if not os.path.exists(os.path.join(folder_path, "Duplicatess")):
        os.mkdir(os.path.join(folder_path, "Duplicatess"))

    # only work on files, ignore if folder
    for each_thing in os.listdir(folder_path):
        if os.path.isdir(os.path.join(folder_path, each_thing)):
            # print("folder")
            continue

        extn = each_thing.split(".")[-1]

        for i in config:
            if extn.lower() in config[i].split(","):
                # the file extention is in config and this file should be moved to folder " i "
                print(f"Moving {each_thing} into {i}")
                try:
                    shutil.move(os.path.join(folder_path, each_thing),
                                os.path.join(folder_path, i))
                except Exception as e:
                    print(e)
                    print(f"Moving {each_thing} to Duplicatess")
                    shutil.move(os.path.join(folder_path, each_thing),"Duplicatess")


def traverse_recursively(a_path: str = None) -> dict:

    if a_path == None:
        a_path = os.getcwd()

    filedict = {}
    filedict[a_path] = []
    os.chdir(a_path)
    for file in os.listdir():
        if os.path.isfile(file):
            filedict[a_path].append(file)

        else:
        # a folder
            filedict[a_path].append(traverse_recursively(file))
            #change dir back to the previous folder
            os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))
    return filedict


def flatten(source:str|None = None, dest:str|None =None):
    # print(source,dest)
    """
    Flattens the folder's contents

    """

    if source == None:
        source = os.getcwd()
    if dest == None:
        dest = source


    os.chdir(source)
    folders = (list(filter(os.path.isdir,os.listdir())))
    print(folders)
    for folder in folders:
        os.chdir(folder)
        for afile in os.listdir():
            if os.path.isdir(afile):
                #flatten this a file
                flatten(afile,dest)
            try:
                shutil.move(afile,dest)
            except Exception as e:
                print(e)

        os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))

    os.chdir(os.path.normpath(os.getcwd() + os.sep + os.pardir))


