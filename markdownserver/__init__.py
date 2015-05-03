from bottle import route,run,template,static_file
from md_to_html import MarkdownConverter
from env import *

converter = MarkdownConverter()

@route('/<resource>')
def gfmize(resource):

    html_file_name = converter.convert(resource)
    return static_file(html_file_name, root=ms_root)

def main():
    run(host=ms_host,port=ms_port,debug=ms_debug,reloader=ms_reloader)

if __name__ == '__main__':
    run(host=ms_host,port=ms_port,debug=ms_debug,reloader=ms_reloader)
