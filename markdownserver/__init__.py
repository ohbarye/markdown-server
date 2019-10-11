from __future__ import absolute_import
from bottle import route, run, static_file
from .markdown_converter import MarkdownConverter
from .env import root_path, ms_host, ms_port, ms_debug
import os

converter = MarkdownConverter()


@route(r'/<resource:re:.*\.md>')
def gfmize(resource):
    if resource == 'favicon.ico':
        return ''

    html_file_name = os.path.basename(converter.convert(resource))
    if '/' in resource:
        html_file_name = '/'.join(resource.split('/')[:-1]) + \
            '/' + html_file_name
    return static_file(os.path.join('resources/html',
                                    html_file_name),
                       root=root_path)


def main():
    run(host=ms_host,
        port=ms_port,
        debug=ms_debug,
        reloader=False)


if __name__ == '__main__':
    main()
