from settings import Session
from models.tactic import Tactic
from lib.scrape import Scrape

url = "https://attack.mitre.org/tactics/enterprise/"
df_tactics = Scrape(url).get_table_by_df()

for row in df_tactics.itertuples():
    record = Tactic()
    record.ta_id = row[1]
    record.name = row[2]
    record.description = row[3]
    Session.add(record)
Session.commit()
Session.close()