from mitreattack.stix20 import MitreAttackData


def main():
    mitre_attack_data = MitreAttackData("/resources/enterprise-attack.json")

    techniques = mitre_attack_data.get_techniques(remove_revoked_deprecated=True)
    id = "T1002"
    print(id.split("."))


if __name__ == "__main__":
    main()