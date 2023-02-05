from settings import Session
from models.tactic import Tactic
from models.technique import Technique
from models.reason import Reason
from lib.scrape import Scrape
import pandas as pd

df_tactics = Scrape("https://attack.mitre.org/tactics/enterprise/").get_table_by_df()
df_technique_group_by = pd.DataFrame(columns=["ID", "ID.1", "Name", "Description", "Tactic"])

for tactic_id in df_tactics["ID"]:
    url = "https://attack.mitre.org/tactics/" + tactic_id + "/"
    df_tmp = Scrape(url).get_table_by_df()
    df_tmp["Tactic"] = tactic_id
    df_technique_group_by = pd.concat([df_technique_group_by, df_tmp], axis=0)

df_reasons = df_technique_group_by[df_technique_group_by["ID.1"].str.startswith("T")]
df_reasons = df_reasons.drop(["ID.1", "Name", "Description"], axis=1)

tactic_id_pair = Tactic().get_id_pair_dict()
technique_id_pair = Technique().get_id_pair_dict()

for row in df_reasons.itertuples():
    record = Reason()
    record.tactic_id = tactic_id_pair[row[2]]
    record.technique_id = technique_id_pair[row[1]]
    Session.add(record)
Session.commit()
Session.close()