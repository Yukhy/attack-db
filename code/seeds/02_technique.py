from mitreattack.stix20 import MitreAttackData
from settings import Session
from models.technique import Technique

def technique():
    mitre_attack_data = MitreAttackData("/resources/enterprise-attack.json")
    techniques = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)
    
    for row in techniques:
        record = Technique()
        external_id = row.external_references[0].external_id
        if "." in external_id:
            id_lst = external_id.split(".")
            record.id = int(id_lst[0].split("T")[1])
            record.sub_id = int(id_lst[1])
        else:
            record.id = int(external_id.split("T")[1])
            record.sub_id = None
        record.name = row.name
        record.description = row.description
        Session.add(record)
    Session.commit()
    Session.close()

if __name__ == "__main__":
    technique()