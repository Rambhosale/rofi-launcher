import utils.common as cm
import common.doc_sources as ds
import common.search_engines as search_engines
import webbrowser

def run():
    modes = ["search", "doc"]

    # select the mode to work on
    selected_mode = cm.launch_rofi("Select a mode", cm.convert_dict_to_options(modes))

    docList = ds.sources

    data_sources = {
        "Search" : search_engines.engines,
        "Doc" : docList,
    }

    if selected_mode == 'Doc':
        step_2 = cm.launch_rofi('Search ' + selected_mode, cm.convert_dict_to_options(docList.keys()))

        # have a default value if nothing is selected in docs list
        if step_2 not in docList.keys():
            step_2 = 'Laravel'

        step_3 = cm.launch_rofi('Search ' + selected_mode, cm.convert_dict_to_options(docList[step_2]))

        doc_url = step_3.split(': ')
        url = doc_url[1].replace('{version}', '10.x')

        webbrowser.open(url)
        exit()
    else:

        if selected_mode in data_sources.keys():
            enteredQuery = cm.launch_rofi('Search >', cm.get_search_engines_keys(search_engines.engines))
        else:
            enteredQuery = selected_mode

        # get the search key and searchEngine from the search query
        searchHash = enteredQuery.split(":", 1)

        if searchHash[0] not in search_engines.engines.keys():
            engine = 'dd'
            searchQuery = enteredQuery
        else:
            engine = searchHash[0]
            searchQuery = searchHash[1]

        webbrowser.open(search_engines.engines[engine]['link'] + searchQuery)

