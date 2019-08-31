import yaml

config = yaml.load(open("config.yaml"))
print(config.get("host"))