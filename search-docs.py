import subprocess as sp
import webbrowser

searchEnginesMap = {}

def dd(data):
    print(data)
    exit()

def convertToString(contents) -> str :
    stringiFied = ""

    if isinstance(contents, dict):
        for content in contents:
            stringiFied += "{content} : {data} \n".format(content = content.title(), data = contents[content])
    else:
        for content in contents:
            stringiFied += content.title() + "\n"

    return stringiFied

def showRofiData(query: str, listData: str):
    status = sp.run(['rofi' ,'-dmenu', '-i', '-l', '20', '-p', query], stdout=sp.PIPE, input=listData, universal_newlines=True)

    # exit if none of the options are slelected
    if status.returncode != 0:
        exit()

    return status.stdout.replace('\n', '').strip(' ')

def getSearchEnginesKeys(searchEngines):
    out = ''
    for engine in searchEngines:

        # populate the map of seatchEngiens
        out += searchEngines[engine]["name"] + ' ' + engine + ':\n'

    return out

modes = ["search", "doc"]

# select the mode to work on
selected_mode = showRofiData("Select a mode", convertToString(modes))

searchEngines = {
    "go" : { "name": "google", "link": "https://www.google.com/search?q="},
    "bi" : { "name": "bing", "link": "https://www.bing.com/search?q="},
    "ya" : { "name": "yahoo", "link": "https://search.yahoo.com/search?p="},
    "dd" : { "name": "duckduckgo", "link": "https://www.duckduckgo.com/?q="},
    "ya" : { "name": "yandex", "link": "https://yandex.ru/yandsearch?text="},
    "gi" : { "name": "github", "link": "https://github.com/search?q="},
    "so" : { "name": "stackoverflow", "link": "http://stackoverflow.com/search?q="},
    "sy" : { "name": "symbolhound", "link": "http://symbolhound.com/?q="},
    "sc" : { "name": "searchcode", "link": "https://searchcode.com/?q="},
    "oh" : { "name": "openhub", "link": "https://www.openhub.net/p?ref=homepage&query="},
    "su" : { "name": "superuser", "link": "http://superuser.com/search?q="},
    "ab" : { "name": "askubuntu", "link": "http://askubuntu.com/search?q="},
    "imdb" : { "name": "imdb", "link": "http://www.imdb.com/find?ref_=nv_sr_fn&q="},
    "rt" : { "name": "rottentomatoes", "link": "https://www.rottentomatoes.com/search/?search="},
    "pb" : { "name": "piratebay", "link": "https://thepiratebay.org/search/"},
    "yt" : { "name": "youtube", "link": "https://www.youtube.com/results?search_query="},
    "vi" : { "name": "vimawesome", "link": "http://vimawesome.com/?q="},
}

laravel_data = {
    "Release Notes" : "https://laravel.com/docs/8.x/releases",
    "Upgrade Guide" : "https://laravel.com/docs/8.x/upgrade",
    "Contribution Guide" : "https://laravel.com/docs/8.x/contributions",
    "Installation" : "https://laravel.com/docs/8.x/installation",
    "Configuration" : "https://laravel.com/docs/8.x/configuration",
    "Directory Structure" : "https://laravel.com/docs/8.x/structure",
    "Starter Kits" : "https://laravel.com/docs/8.x/starter-kits",
    "Deployment" : "https://laravel.com/docs/8.x/deployment",
    "Request Lifecycle" : "https://laravel.com/docs/8.x/lifecycle",
    "Service Container" : "https://laravel.com/docs/8.x/container",
    "Service Providers" : "https://laravel.com/docs/8.x/providers",
    "Facades" : "https://laravel.com/docs/8.x/facades",
    "Routing" : "https://laravel.com/docs/8.x/routing",
    "Middleware" : "https://laravel.com/docs/8.x/middleware",
    "CSRF Protection" : "https://laravel.com/docs/8.x/csrf",
    "Controllers" : "https://laravel.com/docs/8.x/controllers",
    "Requests" : "https://laravel.com/docs/8.x/requests",
    "Responses" : "https://laravel.com/docs/8.x/responses",
    "Views" : "https://laravel.com/docs/8.x/views",
    "Blade Templates" : "https://laravel.com/docs/8.x/blade",
    "URL Generation" : "https://laravel.com/docs/8.x/urls",
    "Session" : "https://laravel.com/docs/8.x/session",
    "Validation" : "https://laravel.com/docs/8.x/validation",
    "Error Handling" : "https://laravel.com/docs/8.x/errors",
    "Logging" : "https://laravel.com/docs/8.x/logging",
    "Artisan Console" : "https://laravel.com/docs/8.x/artisan",
    "Broadcasting" : "https://laravel.com/docs/8.x/broadcasting",
    "Cache" : "https://laravel.com/docs/8.x/cache",
    "Collections" : "https://laravel.com/docs/8.x/collections",
    "Compiling Assets" : "https://laravel.com/docs/8.x/mix",
    "Contracts" : "https://laravel.com/docs/8.x/contracts",
    "Events" : "https://laravel.com/docs/8.x/events",
    "File Storage" : "https://laravel.com/docs/8.x/filesystem",
    "Helpers" : "https://laravel.com/docs/8.x/helpers",
    "HTTP Client" : "https://laravel.com/docs/8.x/http-client",
    "Localization" : "https://laravel.com/docs/8.x/localization",
    "Mail" : "https://laravel.com/docs/8.x/mail",
    "Notifications" : "https://laravel.com/docs/8.x/notifications",
    "Package Development" : "https://laravel.com/docs/8.x/packages",
    "Queues" : "https://laravel.com/docs/8.x/queues",
    "Rate Limiting" : "https://laravel.com/docs/8.x/rate-limiting",
    "Task Scheduling" : "https://laravel.com/docs/8.x/scheduling",
    "Authentication" : "https://laravel.com/docs/8.x/authentication",
    "Authorization" : "https://laravel.com/docs/8.x/authorization",
    "Email Verification" : "https://laravel.com/docs/8.x/verification",
    "Encryption" : "https://laravel.com/docs/8.x/encryption",
    "Hashing" : "https://laravel.com/docs/8.x/hashing",
    "Password Reset" : "https://laravel.com/docs/8.x/passwords",
    "Database Started" : "https://laravel.com/docs/8.x/database",
    "Query Builder" : "https://laravel.com/docs/8.x/queries",
    "Pagination" : "https://laravel.com/docs/8.x/pagination",
    "Migrations" : "https://laravel.com/docs/8.x/migrations",
    "Seeding" : "https://laravel.com/docs/8.x/seeding",
    "Redis" : "https://laravel.com/docs/8.x/redis",
    "Eloquent" : "https://laravel.com/docs/8.x/eloquent",
    "Eloquent Relationships" : "https://laravel.com/docs/8.x/eloquent-relationships",
    "Eloquent Collections" : "https://laravel.com/docs/8.x/eloquent-collections",
    "Eloquent Mutators / Casts" : "https://laravel.com/docs/8.x/eloquent-mutators",
    "Eloquent API Resources" : "https://laravel.com/docs/8.x/eloquent-resources",
    "Eloquent Serialization" : "https://laravel.com/docs/8.x/eloquent-serialization",
    "Testing start" : "https://laravel.com/docs/8.x/testing",
    "HTTP Tests" : "https://laravel.com/docs/8.x/http-tests",
    "Console Tests" : "https://laravel.com/docs/8.x/console-tests",
    "Browser Tests" : "https://laravel.com/docs/8.x/dusk",
    "Database Test" : "https://laravel.com/docs/8.x/database-testing",
    "Mocking" : "https://laravel.com/docs/8.x/mocking",
    "Breeze" : "https://laravel.com/docs/8.x/starter-kits#laravel-breeze",
    "Cashier (Stripe)" : "https://laravel.com/docs/8.x/billing",
    "Cashier (Paddle)" : "https://laravel.com/docs/8.x/cashier-paddle",
    "Dusk" : "https://laravel.com/docs/8.x/dusk",
    "Envoy" : "https://laravel.com/docs/8.x/envoy",
    "Fortify" : "https://laravel.com/docs/8.x/fortify",
    "Homestead" : "https://laravel.com/docs/8.x/homestead",
    "Horizon" : "https://laravel.com/docs/8.x/horizon",
    "Jetstream" : "https://jetstream.laravel.com/",
    "Octane" : "https://laravel.com/docs/8.x/octane",
    "Passport" : "https://laravel.com/docs/8.x/passport",
    "Sail" : "https://laravel.com/docs/8.x/sail",
    "Sanctum" : "https://laravel.com/docs/8.x/sanctum",
    "Scout" : "https://laravel.com/docs/8.x/scout",
    "Socialite" : "https://laravel.com/docs/8.x/socialite",
    "Telescope" : "https://laravel.com/docs/8.x/telescope",
    "Valet" : "https://laravel.com/docs/8.x/valet",
    "API Documentation" : "https://laravel.com/api/8.x",
}

docList = {
    "Laravel" : laravel_data
}

data_sources = {
    "Search" : searchEngines,
    "Doc" : docList,
}

if selected_mode not in data_sources.keys():
    print("select a valid option")
    exit()

if selected_mode == 'Search':

    enteredQuery = showRofiData('Search >', getSearchEnginesKeys(searchEngines))

    # get the search key and searchEngine from the search query
    searchHash = enteredQuery.split(":")

    if searchHash[0] not in searchEngines.keys():
        engine = 'dd'
        searchQuery = searchHash[0]
    else:
        engine = searchHash[0]
        searchQuery = searchHash[1]

    webbrowser.open(searchEngines[engine]['link'] + searchQuery)
    exit()

elif selected_mode == 'Doc':
    step_2 = showRofiData('Search ' + selected_mode, convertToString(docList.keys()))

    # have a default value if nothing is selected in docs list
    if step_2 not in docList.keys():
        step_2 = 'Laravel'

    step_3 = showRofiData('Search ' + selected_mode, convertToString(docList[step_2]))

    doc_url = step_3.split(': ')

    webbrowser.open(doc_url[1])



