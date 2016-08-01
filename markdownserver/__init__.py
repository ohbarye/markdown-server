from bottle import route,run,template,static_file
from markdown_converter import MarkdownConverter
from env import *
import os

converter = MarkdownConverter()

@route('/<resource>')
def gfmize(resource):

    html_file_name = os.path.basename(converter.convert(resource))
    return static_file(os.path.join(html_dir, html_file_name), root=root_path)

def main():
    run(host=ms_host,port=ms_port,debug=ms_debug,reloader=ms_reloader)

if __name__ == '__main__':
    main()
