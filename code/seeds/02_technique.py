from settings import Session
from models.technique import Technique
from lib.scrape import Scrape

url = "https://attack.mitre.org/techniques/enterprise/"
df_techniques = Scrape(url).get_table_by_df()
df_parent_techniques = df_techniques[df_techniques["ID.1"].str.startswith("T")]
df_parent_techniques = df_parent_techniques.drop("ID.1", axis=1)

create_table = Technique()
for row in df_parent_techniques.itertuples():
    record = Technique()
    record.t_id = row[1]
    record.name = row[2]
    record.description = row[3]
    Session.add(record)
Session.commit()
Session.close()