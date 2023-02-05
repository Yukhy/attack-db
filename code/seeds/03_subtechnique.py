from settings import Session
from models.technique import Technique
from models.subtechnique import Subtechnique
from lib.scrape import Scrape

url = "https://attack.mitre.org/techniques/enterprise/"
df_techniques = Scrape(url).get_table_by_df()
df_techniques = df_techniques.fillna(method="ffill")
df_subtechniques = df_techniques[df_techniques["ID.1"].str.startswith(".")]

technique_id_pair = Technique().get_id_pair_dict()

for row in df_subtechniques.itertuples():
    record = Subtechnique()
    record.st_id = row[2].split(".")[1]
    record.name = row[3]
    record.description = row[4]
    record.technique_id = technique_id_pair[row[1]]
    Session.add(record)
Session.commit()
Session.close()