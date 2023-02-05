import glob

seeding_files = glob.glob("seeds/*.py")
for seeding_file in seeding_files:
    if seeding_file != "seeds/__main__.py":
        with open(seeding_file, "r") as f:
            script = f.read()
            exec(script)
        print(f"seeded: {seeding_file}")