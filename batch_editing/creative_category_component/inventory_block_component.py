import json, os

#User input:
input_file = r'' + str(input("File/folder pathway (String):\n")).replace("\"", "")
input_category = str(input("What category do you want the blocks to be in? (String) (Press ENTER for \"Construction\"):\n"))
input_category = "Construction" if input_category == "" else input_category
    
#File/folder handling:
if input_file.endswith(".json"):
    files = tuple([os.path.basename(input_file)])
    folder = str(os.path.dirname(input_file)) + "\\"
else:
    try:
        folder = input_file
        files = tuple(filter(lambda fn: fn.endswith(".json"), os.listdir(folder)))
        folder = folder + "\\" if not folder.endswith("\\") else folder
    except:
        files = None
        print("Make sure you've specified an existing .json file or folder!")
        input("Press ENTER to exit...")   

if files != None and len(files) == 0:
    files = None
    print("No files found in selected folder.")
    input("Press ENTER to exit...")

#Operation:
if files != None:
    for filename in files:
        filepath = folder + filename
        print(filepath + ":")
        try:
            with open(filepath) as f:
                data = json.load(f)
            data["minecraft:block"]["components"]["minecraft:creative_category"] = {}
            data["minecraft:block"]["components"]["minecraft:creative_category"]["category"] = input_category
            with open(filepath, "w") as f:
                json.dump(data, f, indent=2)
            print("Sucessfully added \"minecraft:creative_category\" component.")
        except Exception as error:
            if type(error) == json.decoder.JSONDecodeError:
                print("Invalid json format! (Might be caused by comments in the file...)")
            elif type(error) == KeyError:
                print(f"No {error} component found!")
            else:
                print("Unknown error!")
    input("Press ENTER to exit...")
