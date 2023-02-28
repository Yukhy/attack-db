from mitreattack.stix20 import MitreAttackData
from settings import Session
from models.tactic import Tactic

def tactic():
    mitre_attack_data = MitreAttackData("/resources/enterprise-attack.json")
    tactics = mitre_attack_data.get_tactics(remove_revoked_deprecated=True)
    
    for row in tactics:
        record = Tactic()
        record.id = int(row.external_references[0].external_id.split("TA")[1])
        record.name = row.name
        record.description = row.description
        Session.add(record)
    Session.commit()
    Session.close()

if __name__ == "__main__":
    tactic()