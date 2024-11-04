######################################################################################################################################
#  ______________________________   ___________________________ _______________  ____________ ___________.____     
#\_   ___ \______   \_   _____/  /  _  \__    ___/\_   _____/ \_   _____/\   \/  /\_   ___ \\_   _____/|    |    
#/    \  \/|       _/|    __)_  /  /_\  \|    |    |    __)_   |    __)_  \     / /    \  \/ |    __)_ |    |    
#\     \___|    |   \|        \/    |    \    |    |        \  |        \ /     \ \     \____|        \|    |___ 
# \______  /____|_  /_______  /\____|__  /____|   /_______  / /_______  //___/\  \ \______  /_______  /|_______ \
#        \/       \/        \/         \/                 \/          \/       \_/        \/        \/         \/
#######################################################################################################################################
#@felzosqrt
################################################

import json
import pandas as pd
import json

# Load fresh JSON from ROOT
with open(r"movie_data", "r") as file:
    data = json.load(file)


# check for Key
# check JSON struc or check JSONFORMATEEXML structure oversight 
if 'edges' in data['data']['advancedTitleSearch']:
    edges = data['data']['advancedTitleSearch']['edges']

    # extract "node" files into list of dict
    # (we have edges/node)
    nodes = [edge['node'] for edge in edges]

    # json to dataframe
    df = pd.json_normalize(nodes)

    # dataframe to excel
    df.to_excel("all_nodes_data.xlsx", index=False)

    print("Die Excel-Datei 'all_nodes_data.xlsx' wurde erfolgreich erstellt.")
else:
    print("Der Key 'edges' doesnt exists in 'advancedTitleSearch'")