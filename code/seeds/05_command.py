from settings import Session
from models.technique import Technique
from models.subtechnique import Subtechnique
from models.command import Command
from lib.scrape import Scrape
import pandas as pd
import ruamel.yaml
import glob

def get_commands_by_df(file: str):
    yaml = ruamel.yaml.YAML()
    with open(file) as f:
        content = yaml.load(f)
    commands = list()
    for el in content["atomic_tests"]:
        try:
            command = el["executor"]["command"]
        except:
            command = None
        commands.append(command)
    df_commands = pd.DataFrame(commands, columns=["Commands"])
    return df_commands

technique_id_pair = Technique().get_id_pair_dict()
subtechnique_id_pair = Subtechnique().get_id_pair_dict() #{(st_id, technique_id):id} 

# atomicのDFを生成
file_lst = glob.glob("/resources/atomics/*")
df_atomics = pd.DataFrame(columns=["Commands", "t_id"])
for file in file_lst:
    full_t_id = file.split("/")[3].split(".yaml")[0]
    t_id = full_t_id.split(".")[0]
    try:
        st_id = full_t_id.split(".")[1]
    except IndexError:
        st_id = ""
    df_tmp = get_commands_by_df(file)
    df_tmp["t_id"] = t_id
    df_tmp["st_id"] = st_id
    df_atomics = pd.concat([df_atomics, df_tmp], axis=0)
df_atomics = df_atomics.dropna(subset=["Commands"])
df_atomics = df_atomics.sort_values("t_id")

for row in df_atomics.itertuples():
    record = Command()
    record.command = row[1]
    technique_id = technique_id_pair[row[2]]
    record.technique_id = technique_id
    if row[3] == "":
        record.subtechnique_id = None
    else:
        record.subtechnique_id = subtechnique_id_pair[row[3], technique_id]
    Session.add(record)
Session.commit()
Session.close()