import json
import os
import shutil
import sys
import re
# preparation
track_key = [
    "./Dumped/DATA/files/Race/Course/beginner_course","./Dumped/DATA/files/Race/Course/farm_course",
    "./Dumped/DATA/files/Race/Course/kinoko_course","./Dumped/DATA/files/Race/Course/factory_course",
    "./Dumped/DATA/files/Race/Course/castle_course","./Dumped/DATA/files/Race/Course/shopping_course",
    "./Dumped/DATA/files/Race/Course/boardcross_course","./Dumped/DATA/files/Race/Course/truck_course",
    "./Dumped/DATA/files/Race/Course/senior_course","./Dumped/DATA/files/Race/Course/water_course",
    "./Dumped/DATA/files/Race/Course/treehouse_course","./Dumped/DATA/files/Race/Course/volcano_course",
    "./Dumped/DATA/files/Race/Course/desert_course","./Dumped/DATA/files/Race/Course/ridgehighway_course",
    "./Dumped/DATA/files/Race/Course/koopa_course","./Dumped/DATA/files/Race/Course/rainbow_course",
    "./Dumped/DATA/files/Race/Course/old_peach_gc","./Dumped/DATA/files/Race/Course/old_falls_ds",
    "./Dumped/DATA/files/Race/Course/old_obake_sfc","./Dumped/DATA/files/Race/Course/old_mario_64",
    "./Dumped/DATA/files/Race/Course/old_sherbet_64","./Dumped/DATA/files/Race/Course/old_heyho_gba",
    "./Dumped/DATA/files/Race/Course/old_town_ds","./Dumped/DATA/files/Race/Course/old_waluigi_gc",
    "./Dumped/DATA/files/Race/Course/old_desert_ds","./Dumped/DATA/files/Race/Course/old_koopa_gba",
    "./Dumped/DATA/files/Race/Course/old_donkey_64","./Dumped/DATA/files/Race/Course/old_mario_gc",
    "./Dumped/DATA/files/Race/Course/old_mario_sfc","./Dumped/DATA/files/Race/Course/old_garden_ds",
    "./Dumped/DATA/files/Race/Course/old_donkey_gc","./Dumped/DATA/files/Race/Course/old_koopa_64"
    ]
minimap_dir = "./menu/minimap/game_image/timg/"
minimap_key = {
    "Mario":"mario","Luigi":"luigi","Peach":"peach","Yoshi":"yoshi",
    "Wario":"wario","Waluigi":"waluigi","Donkey Kong":"donkey","Bowser":"koopa",
    "Baby Mario":"baby_mario","Baby Peach":"baby_peach","Toad":"kinopio","Koopa Troopa":"noko",
    "Baby Luigi":"baby_luigi","Baby Daisy":"baby_daisy","Toadette":"kinopico","Dry Bones":"karon",
    "Daisy":"daisy","Birdo":"catherine","Diddy Kong":"didy","Bowser Jr.":"koopa_jr",
    "King Boo":"teresa","Rosalina":"roseta","Funky Kong":"fuky","Dry Bowser":"hone_koopa"
    }
cup_key = {
    "Mushroom Cup":"kinoko.thp","Flower Cup":"flower.thp","Star Cup":"star.thp",
    "Special Cup":"special.thp","Shell Cup":"koura.thp","Banana Cup":"banana.thp",
    "Leaf Cup":"konoha.thp","Lightning Cup":"lightning.thp"
}
music_key = [
    "n_circuit32_n","n_farm_n","n_kinoko_n","STRM_N_FACTORY_N",
    "n_circuit32_n","n_shopping32_n","n_snowboard32_n","STRM_N_TRUCK_N",
    "n_daisy32_n","STRM_N_WATER_N","n_maple_n","n_volcano32_n",
    "STRM_N_DESERT_N","STRM_N_RIDGEHIGHWAY_N","STRM_N_KOOPA_N","n_rainbow32_n",
    "r_gc_beach32_n","r_ds_jungle32_n","r_sfc_obake32_n","r_64_circuit32_n",
    "r_64_sherbet32_n","r_agb_beach32_n","r_ds_town32_n","r_gc_stadium32_n",
    "r_ds_desert32_n","r_agb_kuppa32_n","r_64_jungle32_n","r_gc_circuit32_n",
    "r_sfc_circuit32_n","r_ds_garden32_n","r_gc_mountain32_n","r_64_kuppa32_n",
]
music_key_f = [
    "n_circuit32_f","n_farm_f","n_kinoko_f","STRM_N_FACTORY_F",
    "n_circuit32_f","n_shopping32_f","n_snowboard32_f","STRM_N_TRUCK_F",
    "n_daisy32_f","STRM_N_WATER_F","n_maple_f","n_volcano32_f",
    "STRM_N_DESERT_F","STRM_N_RIDGEHIGHWAY_F","STRM_N_KOOPA_F","n_rainbow32_f",
    "r_gc_beach32_f","r_ds_jungle32_f","r_sfc_obake32_f","r_64_circuit32_f",
    "r_64_sherbet32_f","r_agb_beach32_f","r_ds_town32_f","r_gc_stadium32_f",
    "r_ds_desert32_f","r_agb_kuppa32_f","r_64_jungle32_f","r_gc_circuit32_f",
    "r_sfc_circuit32_f","r_ds_garden32_f","r_gc_mountain32_f","r_64_kuppa32_f",
]
print("dumping disk")
os.system(".\\bin\\wit EXTRACT .\\MarioKartWii.iso .\\Dumped --quiet")
with open("./mod/project.json","r") as read_project:
    project = json.loads(read_project.read())
tracks = project["tracks"]
try:
    os.remove("./"+project["export"]+".iso")
except:
    print("skipping removal of: "+project["export"]+".iso")
try:
    shutil.rmtree("./menu/")
except:
    print("skipping removal of: menu")
# add tracks
for track in list(tracks):
    track_data=tracks[track]
    try:
        print("adding file: "+track+".szs")
        shutil.copyfile("./mod/tracks/"+track+".szs",track_key[track_data["slot"]]+".szs")
        shutil.copyfile("./mod/tracks/"+track+".szs",track_key[track_data["slot"]]+"_d.szs")
    except:
        print("couldn't add file: "+track+".szs")
# rename tracks
ui_location = "./Dumped/DATA/files/Scene/UI/"
try:
    shutil.rmtree("./rename/")
except:
    print("failed to remove: rename")
try:
    shutil.rmtree("./menu/")
except:
    print("failed to remove: menu")
try:
    shutil.rmtree("./sfx/")
except:
    print("failed to remove: sfx")
for dir in ["./rename/","./rename/SZS/","./rename/BMG/","./menu","./menu/driver", 
            "./menu/image","./menu/minimap/","./menu/single/","./menu/multi/",
            "./sfx/"
            ]:
    try:
        os.mkdir(dir)
    except:
        print("[FATAL] couldn't create SZS temp dir: "+dir)
        sys.exit(1)
os.system(".\\bin\\wszst x -a "+ui_location+"Award_"+project["region"]+".szs"+" -D ./rename/SZS/ -o --quiet")
with open("./rename/SZS/message/Common.bmg.txt","r") as read_bmg:
    replace_bmg = read_bmg.read().splitlines()
print("renaming tracks")
replace = project["names"]["tracks"]
for track in list(replace):
    for line in range(12,52):
        if(not re.search(r"^.*= "+track,replace_bmg[line]) == None):
            replace_bmg[line] = re.sub(track,replace[track],replace_bmg[line])
print("renaming players")
replace = project["names"]["players"]
for player in list(replace):
    for line in range(66,96):
        if(not re.search(r"^.*= "+player,replace_bmg[line]) == None):
            replace_bmg[line] = re.sub(player,replace[player],replace_bmg[line])
with open("./rename/BMG/Common.txt", "w") as export_bmg:
    export_bmg.writelines((line+"\n" for line in replace_bmg))
os.system(".\\bin\\wszst patch "+ui_location+"*_?.szs --patch-bmg \"replace=./rename/BMG/Common.txt\" --quiet")
# add players/karts
print("adding \"allkarts\"")
allkart_dir = "./mod/karts/allkart/"
allkarts = os.listdir(allkart_dir)
for allkart in allkarts:
    shutil.copyfile(allkart_dir+allkart,"./Dumped/DATA/files/Scene/Model/Kart/"+allkart)
    print("added allkart: "+allkart)
for kart in project["karts"]:
    print("adding player: "+kart)
    karts = os.listdir("./mod/karts/"+kart+"/")
    for kart_part in karts:
        shutil.copyfile("./mod/karts/"+kart+"/"+kart_part,"./Dumped/DATA/files/Race/Kart/"+kart_part)
print("adding menu models")
menus = os.listdir("./mod/karts/menu/")
print("dumping Driver.szs")
os.system(".\\bin\\wszst EXTRACT ./Dumped/DATA/files/Scene/Model/Driver.szs -D ./menu/driver -o --quiet")
print("patching Driver.szs")
for menu in menus:
    shutil.copyfile("./mod/karts/menu/"+menu,"./menu/driver/"+menu)
os.system(".\\bin\\wszst CREATE ./menu/driver/ -D ./menu/Driver.szs -o --quiet")
shutil.copyfile("./menu/Driver.szs","./Dumped/DATA/files/Scene/Model/Driver.szs")
# edit UI
print("dumping minimap UI")
os.system(".\\bin\\wszst EXTRACT ./Dumped/DATA/files/Scene/UI/Race.szs -D ./menu/minimap/ -o --quiet")
for minimap in list(project["UI"]["minimap"]):
    print("adding UI: "+minimap)
    os.system(".\\bin\\wimgt ENCODE ./mod/ui/"+minimap+".png -d ./menu/image/"+minimap+".tpl --quiet -o")
    shutil.copyfile("./menu/image/"+minimap+".tpl","./menu/minimap/game_image/timg/st_"+minimap_key[project["UI"]["minimap"][minimap]]+"_32x32.tpl")
print("patching minimap UI")
os.system(".\\bin\\wszst CREATE ./menu/minimap/ -D ./menu/Race.szs -o --quiet")
shutil.copyfile("./menu/Race.szs","./Dumped/DATA/files/Scene/UI/Race.szs")
minimap_key["Funky Kong"] = "funky"
print("dumping MenuSingle.szs")
os.system(".\\bin\\wszst EXTRACT ./Dumped/DATA/files/Scene/UI/MenuSingle.szs -D ./menu/single/ -o --quiet")
for player_icon in list(project["UI"]["players"]):
    print("adding MenuSingle UI: "+player_icon)
    os.system(".\\bin\\wimgt ENCODE ./mod/ui/"+player_icon+".png -d ./menu/image/"+player_icon+".tpl --quiet -o")
    shutil.copyfile("./menu/image/"+player_icon+".tpl","./menu/single/button/timg/tt_"+minimap_key[project["UI"]["players"][player_icon]]+"_64x64.tpl")
print("patching MenuSingle UI")
os.system(".\\bin\\wszst CREATE ./menu/single/ -D ./menu/MenuSingle.szs -o --quiet")
shutil.copyfile("./menu/MenuSingle.szs","./Dumped/DATA/files/Scene/UI/MenuSingle.szs")
print("dumping MenuMulti.szs")
os.system(".\\bin\\wszst EXTRACT ./Dumped/DATA/files/Scene/UI/MenuMulti.szs -D ./menu/multi/ -o --quiet")
for player_icon in list(project["UI"]["players"]):
    print("adding MenuMulti UI: "+player_icon)
    os.system(".\\bin\\wimgt ENCODE ./mod/ui/"+player_icon+".png -d ./menu/image/"+player_icon+".tpl --quiet -o")
    shutil.copyfile("./menu/image/"+player_icon+".tpl","./menu/multi/button/timg/tt_"+minimap_key[project["UI"]["players"][player_icon]]+"_64x64.tpl")
print("patching MenuMulti UI")
os.system(".\\bin\\wszst CREATE ./menu/multi/ -D ./menu/MenuMulti.szs -o --quiet")
shutil.copyfile("./menu/MenuMulti.szs","./Dumped/DATA/files/Scene/UI/MenuMulti.szs")
print("patching cup previews")
for cup in list(project["UI"]["preview"]):
    print("adding cup preview: "+cup)
    shutil.copyfile("./mod/ui/"+cup+".thp","./Dumped/DATA/files/thp/course/"+cup_key[project["UI"]["preview"][cup]])
# edit music
print("dumping music")
for music in music_key:
    shutil.copyfile("./Dumped/DATA/files/sound/strm/"+music+".brstm","./sfx/"+music+".brstm")
for music in music_key_f:
    shutil.copyfile("./Dumped/DATA/files/sound/strm/"+music+".brstm","./sfx/"+music+".brstm")
for track in list(tracks):
    print("adding music slot: "+str(tracks[track]["music"])+" to track: "+track)
    shutil.copyfile("./sfx/"+music_key[tracks[track]["music"]]+".brstm","./Dumped/DATA/files/sound/strm/"+music_key[tracks[track]["slot"]]+".brstm")
    shutil.copyfile("./sfx/"+music_key_f[tracks[track]["music"]]+".brstm","./Dumped/DATA/files/sound/strm/"+music_key_f[tracks[track]["slot"]]+".brstm")
# patch iso
print("patching disk image")
os.system(".\\bin\\wit copy Dumped ./"+project["export"]+".iso --quiet")
# clean directory
print("cleaning up")
for remove in ["rename","menu","Dumped","sfx"]:
    try:
        shutil.rmtree("./"+remove+"/")
    except:
        print("failed to remove: "+remove)