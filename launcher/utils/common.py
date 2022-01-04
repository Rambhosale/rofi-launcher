import subprocess as sp

def dd(data):
    print(data)
    exit()

def convert_dict_to_options(contents) -> str :
    stringiFied = ""

    if isinstance(contents, dict):
        for content in contents:
            stringiFied += "{content} : {data} \n".format(content = content.title(), data = contents[content])
    else:
        for content in contents:
            stringiFied += content.title() + "\n"

    return stringiFied

def launch_rofi(query: str, listData: str):
    status = sp.run(['rofi' ,'-dmenu', '-i', '-l', '20', '-p', query], stdout=sp.PIPE, input=listData, universal_newlines=True)

    # exit if none of the options are slelected
    if status.returncode != 0:
        exit()

    return status.stdout.replace('\n', '').strip(' ')

def get_search_engines_keys(searchEngines):
    out = ''
    for engine in searchEngines:

        # populate the map of seatchEngiens
        out += searchEngines[engine]["name"] + ' ' + engine + ':\n'

    return out
