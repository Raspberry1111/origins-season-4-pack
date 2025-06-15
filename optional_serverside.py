import glob

OPTIONAL_CONFIG = """

[option]
optional = true
default = false
description = "Not needed to join server, but needed if you want to play singleplayer"
"""

def confirm(message):
    answer = input(message + " [y/N]: ")
    return answer in ["y", "yes"]    

for file in glob.glob("mods/*.pw.toml"):
    with open(file, "r+") as f:
        content = f.read()
        if 'side = "server"' in content:
            if not confirm(f"{file} is serverside. Should I make it optional"):
                continue
        
            content = content.replace('side = "server"', 'side = "both"')
            content += OPTIONAL_CONFIG
            f.seek(0)
            f.write(content)
