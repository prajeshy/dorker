import argparse
import urllib.parse
import webbrowser

dork_options = [
    ("Publicaly Exposed Documents", "ext:doc | ext:docx | ext:odt | ext:rtf | ext:sxw | ext:psw | ext:ppt | ext:pptx | ext:pps | ext:csv"),
    ("Directory Listing Vulnerability", "intitle:index.of"),
    ("Configuration Files Exposed", "ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini | ext:env"),
    ("Database Files Exposed", "ext:sql | ext:dbf | ext:mdb"),
    ("Log Files Exposed", "ext:log"),
    ("Backup & Old Files", "ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup"),
    ("Login Pages", '(inurl:login | inurl:signin | intitle:Login | intitle:"sign in" | inurl:auth)'),
    ("SQL Errors", '(intext:"sql syntax near" | intext:"syntax error has occurred" | intext:"incorrect syntax near" | intext:"unexpected end of SQL command" | intext:"Warning: mysql_connect()" | intext:"Warning: mysql_query()" | intext:"Warning: pg_connect()")'),
    ("PHP errors", '("PHP Parse error" | "PHP Warning" | "PHP Error")'),
    ("PHP info()", '(ext:php intitle:phpinfo "published by the PHP Group")'),
    ("Search Pasting Sites", '(site:pastebin.com | site:paste2.org | site:pastehtml.com | site:slexy.org | site:snipplr.com | site:snipt.net | site:textsnip.com | site:bitpaste.app | site:justpaste.it | site:heypasteit.com | site:hastebin.com | site:dpaste.org | site:dpaste.com | site:codepad.org | site:jsitor.com | site:codepen.io | site:jsfiddle.net | site:dotnetfiddle.net | site:phpfiddle.org | site:ide.geeksforgeeks.org | site:repl.it | site:ideone.com | site:paste.debian.net | site:paste.org | site:paste.org.ru | site:codebeautify.org  | site:codeshare.io | site:trello.com)'),
    ("Search Github & Gitlab", '(site:github.com | site:gitlab.com)'),
    ("Stackoverflow", "site:stackoverflow.com"),
    ("Sign Up Pages", '(inurl:signup | inurl:register | intitle:Signup)'),
    ("Find Subdomains", ""),
    ("Find Sub - Subdomains", "")
]


def search(search_input, selected_option):
    selected_dork = dork_options[selected_option - 1][1]

    if 1 <= selected_option <= 10:
        search_query = f"site:{search_input} {selected_dork}"
    elif 15 <= selected_option <= 16:
        search_query = f"site:{'*.' * (selected_option - 15)}{search_input}"
    else:
        search_query = f'{selected_dork} "{search_input}"'

    encoded_query = urllib.parse.quote(search_query)
    search_url = f"https://www.google.com/search?q={encoded_query}"
    webbrowser.open_new_tab(search_url)


def main():
    parser = argparse.ArgumentParser(description="Google Dork Search Tool")
    parser.add_argument("search_input", help="Enter your search term")
    parser.add_argument("selected_option", type=int, choices=range(1, len(dork_options) + 1), help="Select an option by entering its number")

    args = parser.parse_args()

    search(args.search_input, args.selected_option)


if __name__ == "__main__":
    main()
