import yaml


def load_config(config_path="pekobot-config.yaml"):
    with open(config_path) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)

    token = data["discord_token"]
    cogs = data["cogs"]

    return dict(discord_token=token, cogs=cogs)
