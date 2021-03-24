import os
import sys
import re 
from urllib.parse import quote
import webbrowser



def import_to_things(path):
    log = open(path, "r").read()
    split_string = log.split('\n')

    for i in split_string:
        check_for_box = re.search("^\[].*$", i)

        if check_for_box:
            formatted = format(check_for_box.group(0)).replace('[]', '')
            jsoned = '[{"type":"to-do","attributes":{"title":"' + formatted + '"}}]'
            encoded = 'things:///json?data=' + quote(jsoned, safe='')
            webbrowser.open(encoded, new=0, autoraise=True)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        path = os.path.expanduser(sys.argv[1])
    else:
        # paste path to note here 
        path = os.path.expanduser("~/Desktop/vault/test_doc.md")

    import_to_things(path)

