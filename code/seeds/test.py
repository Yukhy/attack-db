from mitreattack.stix20 import MitreAttackData
from models.tactic import Tactic
from models.technique import Technique

def main():
    
    mitre_attack_data = MitreAttackData("/resources/enterprise-attack.json")
    techniques = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)

    for technique in techniques:
        parent_tactics = list()
        for kill_chain_phase in technique.kill_chain_phases:
            parent_tactics.append(kill_chain_phase["phase_name"])

        technique_id = Technique.get_id_by_name(technique.name)
        for tactic in parent_tactics:
            tactic_name = tactic.replace("-", " ") # ex.) "privilege-escalation" -> "privilege escalation"
            print(Tactic.get_id_by_name(tactic_name))

if __name__ == "__main__":
    main()