Python 3.8.6 (tags/v3.8.6:db45529, Sep 23 2020, 15:37:30) [MSC v.1927 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> myDictionary = { 'index1': 1, 'index2': 2, 'index3':355}
>>> myDictionary
{'index1': 1, 'index2': 2, 'index3': 355}
>>> myDictionary{'index2'}
SyntaxError: invalid syntax
>>> myDictionary[index2]
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    myDictionary[index2]
NameError: name 'index2' is not defined
>>> myDictionary[index2]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    myDictionary[index2]
NameError: name 'index2' is not defined
>>> myDictionary[index3]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    myDictionary[index3]
NameError: name 'index3' is not defined
>>> print(index2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(index2)
NameError: name 'index2' is not defined
>>> dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_12345': ('fname': 'Brandon', 'lname': 'Lyon', 'phone': '126-123-476') }
SyntaxError: invalid syntax
>>> dic_users = {'em_1234': {'fname': 'Bob', 'lname': 'Smith', 'phone': '123-456-7890'}, 'em_12345': ('fname' : 'Brandon', 'lname': 'Lyon', 'phone': '126-123-476') }
SyntaxError: invalid syntax
>>> 
================================ RESTART: Shell ================================
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> myDictionary = {'index': 1,'index2': 2,'index3': 355}
>>> myDictionary['index2']
2
>>> dic_users = {'em_1234': {'fname': 'Bob','lname': 'Smith','phone': '123-456-7890'}, 'em12345': {'fname': 'Mary', 'lname': 'Jones', 'phone': '543-093-3048'} }
>>> print(dic_users['em_12345'])
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print(dic_users['em_12345'])
KeyError: 'em_12345'
>>> print(dic_users['em12345'])
{'fname': 'Mary', 'lname': 'Jones', 'phone': '543-093-3048'}
>>> print(dic_users['em12345']['phone'])
543-093-3048
>>> print('User: () ()\nPhone: ()'.format(dic_users['em12345']['fname'],dic_users['em12345']['lname'],dic_users['em12345']['phone']))
User: () ()
Phone: ()
>>> 
================================ RESTART: Shell ================================
>>> carDict = {'brand': 'subaru', 'modle': 'wrx', 'year': '2009'}
>>> x = carDict.get('brand')
>>> print(x)
subaru
>>> carDict.update({'year': '2021'})
>>> car2Dict = {'car1': {'modle': 'wrx', 'year': '2009'}, 'car2' : {'modle': 'sti', 'year': '2020'},'car3': {'modle': 'outback', 'year': '2005'} }
>>> newCar = dict.fromkeys(carDict, car2Dict)
>>> print(newCar)
{'brand': {'car1': {'modle': 'wrx', 'year': '2009'}, 'car2': {'modle': 'sti', 'year': '2020'}, 'car3': {'modle': 'outback', 'year': '2005'}}, 'modle': {'car1': {'modle': 'wrx', 'year': '2009'}, 'car2': {'modle': 'sti', 'year': '2020'}, 'car3': {'modle': 'outback', 'year': '2005'}}, 'year': {'car1': {'modle': 'wrx', 'year': '2009'}, 'car2': {'modle': 'sti', 'year': '2020'}, 'car3': {'modle': 'outback', 'year': '2005'}}}
>>> 
>>> 
================================ RESTART: Shell ================================
>>> motors = ['EJ-255', 'rotrary', 'k24', 'Ls']
>>> x = 10
>>> print(type(x))
<class 'int'>
>>> help
Type help() for interactive help, or help(object) for help about object.
>>> help()

Welcome to Python 3.8's help utility!

If this is your first time using Python, you should definitely check out
the tutorial on the Internet at https://docs.python.org/3.8/tutorial/.

Enter the name of any module, keyword, or topic to get help on writing
Python programs and using Python modules.  To quit this help utility and
return to the interpreter, just type "quit".

To get a list of available modules, keywords, symbols, or topics, type
"modules", "keywords", "symbols", or "topics".  Each module also comes
with a one-line summary of what it does; to list the modules whose name
or summary contain a given string such as "spam", type "modules spam".

help> modules

Please wait a moment while I gather a list of all available modules...


Warning (from warnings module):
  File "C:\Users\lyonb\AppData\Local\Programs\Python\Python38-32\lib\site-packages\setuptools\distutils_patch.py", line 25
    warnings.warn(
UserWarning: Distutils was imported before Setuptools. This usage is discouraged and may exhibit undesirable behaviors or errors. Please use Setuptools' objects directly or at least import Setuptools first.
__future__          asyncio             history             sched
__main__            asyncore            hmac                scrolledlist
_abc                atexit              html                search
_ast                audioop             http                searchbase
_asyncio            autocomplete        hyperparser         searchengine
_bisect             autocomplete_w      idle                secrets
_blake2             autoexpand          idle_test           select
_bootlocale         base64              idlelib             selectors
_bz2                bdb                 imaplib             setuptools
_codecs             binascii            imghdr              shelve
_codecs_cn          binhex              imp                 shlex
_codecs_hk          bisect              importlib           shutil
_codecs_iso2022     browser             inspect             sidebar
_codecs_jp          builtins            io                  signal
_codecs_kr          bz2                 iomenu              site
_codecs_tw          cProfile            ipaddress           smtpd
_collections        calendar            itertools           smtplib
_collections_abc    calltip             json                sndhdr
_compat_pickle      calltip_w           keyword             socket
_compression        cgi                 lib2to3             socketserver
_contextvars        cgitb               linecache           sqlite3
_csv                chunk               locale              squeezer
_ctypes             cmath               logging             sre_compile
_ctypes_test        cmd                 lzma                sre_constants
_datetime           code                macosx              sre_parse
_decimal            codecontext         mailbox             ssl
_dummy_thread       codecs              mailcap             stackviewer
_elementtree        codeop              mainmenu            stat
_functools          collections         marshal             statistics
_hashlib            colorizer           math                statusbar
_heapq              colorsys            mimetypes           string
_imp                compileall          mmap                stringprep
_io                 concurrent          modulefinder        struct
_json               config              msilib              subprocess
_locale             config_key          msvcrt              sunau
_lsprof             configdialog        multicall           symbol
_lzma               configparser        multiprocessing     symtable
_markupbase         contextlib          netrc               sys
_md5                contextvars         nntplib             sysconfig
_msi                copy                nt                  tabnanny
_multibytecodec     copyreg             ntpath              tarfile
_multiprocessing    crypt               nturl2path          telnetlib
_opcode             csv                 numbers             tempfile
_operator           ctypes              opcode              test
_osx_support        curses              operator            textview
_overlapped         dataclasses         optparse            textwrap
_pickle             datetime            os                  this
_py_abc             dbm                 outwin              threading
_pydecimal          debugger            parenmatch          time
_pyio               debugger_r          parser              timeit
_queue              debugobj            pathbrowser         tkinter
_random             debugobj_r          pathlib             token
_sha1               decimal             pdb                 tokenize
_sha256             delegator           percolator          tooltip
_sha3               difflib             pickle              trace
_sha512             dis                 pickletools         traceback
_signal             distutils           pip                 tracemalloc
_sitebuiltins       doctest             pipes               tree
_socket             dummy_threading     pkg_resources       tty
_sqlite3            dynoption           pkgutil             turtle
_sre                easy_install        platform            turtledemo
_ssl                editor              plistlib            types
_stat               email               poplib              typing
_statistics         encodings           posixpath           undo
_string             ensurepip           pprint              unicodedata
_strptime           enum                profile             unittest
_struct             errno               pstats              urllib
_symtable           faulthandler        pty                 uu
_testbuffer         filecmp             py_compile          uuid
_testcapi           fileinput           pyclbr              venv
_testconsole        filelist            pydoc               warnings
_testimportmultiple fnmatch             pydoc_data          wave
_testmultiphase     format              pyexpat             weakref
_thread             formatter           pyparse             webbrowser
_threading_local    fractions           pyshell             window
_tkinter            ftplib              python 276          winreg
_tracemalloc        functools           query               winsound
_warnings           gc                  queue               wsgiref
_weakref            genericpath         quopri              xdrlib
_weakrefset         getopt              random              xml
_winapi             getpass             re                  xmlrpc
_xxsubinterpreters  gettext             redirector          xxsubtype
abc                 glob                replace             zipapp
aifc                grep                reprlib             zipfile
antigravity         gzip                rlcompleter         zipimport
argparse            hashlib             rpc                 zlib
array               heapq               run                 zoomheight
ast                 help                runpy               zzdummy
asynchat            help_about          runscript           

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose name or summary contain the string "spam".

help> quit

You are now leaving help and returning to the Python interpreter.
If you want to ask for help on a particular object directly from the
interpreter, you can type "help(object)".  Executing "help('string')"
has the same effect as typing a particular string at the help> prompt.
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> import math
>>> math.floor(3.5)
3
>>> 
>>> 
= RESTART: C:/Users/lyonb/OneDrive/myProjects/Python Stuff/Python-Projects/printnum.py
45
>>> 
================================ RESTART: Shell ================================
>>> import datetime
>>> 
>>> x = datetime.datetime.now()
>>> print(x)
2020-11-25 20:17:51.527581
>>> 