import utils.common as cm
import common.doc_sources as ds
import common.search_engines as search_engines
import webbrowser

def run():
    modes = ["search", "doc"]

# select the mode to work on
    selected_mode = cm.showRofiData("Select a mode", cm.convertToString(modes))


    docList = ds.sources

    data_sources = {
        "Search" : search_engines.engines,
        "Doc" : docList,
    }

    if selected_mode not in data_sources.keys():
        print("select a valid option")
        exit()

    if selected_mode == 'Search':

        enteredQuery = cm.showRofiData('Search >', cm.getSearchEnginesKeys(search_engines.engines))

        # get the search key and searchEngine from the search query
        searchHash = enteredQuery.split(":", 1)

        if searchHash[0] not in search_engines.engines.keys():
            engine = 'dd'
            searchQuery = enteredQuery
        else:
            engine = searchHash[0]
            searchQuery = searchHash[1]

        webbrowser.open(search_engines.engines[engine]['link'] + searchQuery)
        exit()

    elif selected_mode == 'Doc':
        step_2 = cm.showRofiData('Search ' + selected_mode, cm.convertToString(docList.keys()))

        # have a default value if nothing is selected in docs list
        if step_2 not in docList.keys():
            step_2 = 'Laravel'

        step_3 = cm.showRofiData('Search ' + selected_mode, cm.convertToString(docList[step_2]))

        doc_url = step_3.split(': ')

        webbrowser.open(doc_url[1])
