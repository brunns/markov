#!/usr/bin/env python
# encoding: utf-8
"""
Docstring...
"""
import codecs
import locale
import logging
import optparse
import os
import sys
import warnings
import os.path
import docx

__author__ = '$USER'
__version__="0.0"

script_name = os.path.basename(sys.argv[0])
usage = script_name + ' [options] args'
description = '''
Description of script...
'''

logger = logging.getLogger(script_name)

def main(*argv):
    options, script, args, help = get_options(argv)
    init_logger(options.verbosity)

    corpus = ''
    for arg in args:
        ext = os.path.splitext(arg)[-1]
        corpus += extract_functions.get(ext, unknown_extension)(arg)

    print corpus

def extract_docx(filename):
    logger.info("Adding %s", filename)
    document = docx.Document(filename)
    return " ".join(paragraph.text for paragraph in document.paragraphs)

def unknown_extension(filename):
    logger.warn("Unknown file type %s", filename)
    return ""

extract_functions = {
    ".docx": extract_docx
}

def get_options(argv):
    '''Get options and arguments from argv string.'''
    parser = optparse.OptionParser(usage=usage, version=__version__)
    parser.description=description
    parser.add_option("-v", "--verbosity", action="count", default=0,
        help="Specify up to three times to increase verbosity, i.e. -v to see warnings, -vv for information messages, or -vvv for debug messages.")

    # Script options here...

    options, args = parser.parse_args(list(argv))
    script, args = args[0], args[1:]
    return options, script, args, parser.format_help()

def init_logger(verbosity, stream=sys.stdout):
    '''Initialize logger and warnings according to verbosity argument.
    Verbosity levels of 0-3 supported.'''
    is_not_debug = verbosity <= 2
    level = [logging.ERROR, logging.WARNING, logging.INFO][verbosity] if is_not_debug else logging.DEBUG
    format = '%(message)s' if is_not_debug else '%(asctime)s %(levelname)-8s %(name)s %(module)s.py:%(funcName)s():%(lineno)d %(message)s'
    logging.basicConfig(level=level, format=format, stream=stream)
    if is_not_debug: warnings.filterwarnings('ignore')

def wrap_stream_for_tty(stream):
    if stream.isatty():
        # Configure locale from the user's environment settings.
        locale.setlocale(locale.LC_ALL, '')

        # Wrap stdout with an encoding-aware writer.
        lang, encoding = locale.getdefaultlocale()
        logger.debug('Streaming to tty with lang, encoding = %s, %s', lang, encoding)
        if encoding:
            return codecs.getwriter(encoding)(stream)
        else:
            logger.warn('No tty encoding found!')

    return stream

if __name__ == "__main__":
    sys.exit(main(*sys.argv))
