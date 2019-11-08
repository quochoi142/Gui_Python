
import yaml

with open("linux_low.yaml", 'r') as stream:
    try:
        x=yaml.safe_load(stream)
        print(yaml.safe_load(stream))
    except yaml.YAMLError as exc:
        print(exc)