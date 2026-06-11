
import ast, random, marshal, base64, bz2, zlib, lzma, time, sys, threading
from ast import *

# Lấy version Python
ver = f"{sys.version_info.major}.{sys.version_info.minor}"

from pystyle import *
banner = f"""
    [+] VER: 1.0 ORCA
    [+] Running with Python: {sys.version_info.major}.{sys.version_info.minor}
    ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠺⢿⣿⣿⣿⣿⣿⣿⣷⣦⣠⣤⣤⣤⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⣿⣿⣷⣄⠀⠀
    ⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⠀⠀⠀⣀⣿⣿⣿⣆⠀
    ⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄
    ⠀⠀⠀⠀⣾⣿⣿⡿⠋⠁⣀⣠⣬⣽⣿⣿⣿⣿⣿⣿⠿⠿⠿⠿⠿⠿⠿⠿⠟⠁
    ⠀⠀⠀⢀⣿⣿⡏⢀⣴⣿⠿⠛⠉⠉⠀⢸⣿⣿⠿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢸⣿⣿⢠⣾⡟⠁⠀⠀⠀⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⢸⣿⣿⣾⠏⠀⠀  > Author: Lisander
    ⠀⠀⠀⣸⣿⣿⣿⣀⠀⠀  > ['Github']['Callista/Zenobia']
    ⠀⢠⣾⣿⣿⣿⣿⣿⣷⣄⠀ > ['Youtube']['Minor/Zenobia']
    ⠀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣦ > ['Instagram']['No Use Instagram']
    ⢰⣿⡿⠛⠉⠀⠀⠀⠈⠙⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""
buitlins = ['__import__', 'abs', 'all', 'any', 'ascii', 'bin', 'breakpoint', 'callable', 'chr', 'compile', 'delattr', 'dir', 'divmod', 'eval', 'exec', 'format', 'getattr', 'globals', 'hasattr', 'hash', 'hex', 'id', 'input', 'isinstance', 'issubclass', 'iter', 'aiter', 'len', 'locals', 'max', 'min', 'next', 'anext', 'oct', 'ord', 'pow', 'print', 'repr', 'round', 'setattr', 'sorted', 'sum', 'vars', 'None', 'Ellipsis', 'NotImplemented', 'False', 'True', 'bool', 'memoryview', 'bytearray', 'bytes', 'classmethod', 'complex', 'dict', 'enumerate', 'filter', 'float', 'frozenset', 'property', 'int', 'list', 'map', 'object', 'range', 'reversed', 'set', 'slice', 'staticmethod', 'str', 'super', 'tuple', 'type', 'zip']
def Hiragana():
    ranges = list(range(0x3040, 0x30A0)) + list(range(0x30A0, 0x3100))
    return ''.join(random.choices([chr(i) for i in ranges if chr(i).isprintable() and chr(i).isidentifier()], k=11))

Meliodas, Elizabeth, Ban, King, Diane, Gowther, Merlin, Escanor, Hawk, Zeldris = [Hiragana() for _ in range(10)]
ver = str(sys.version_info.major)+'.'+str(sys.version_info.minor)
def rd():
    # return "_" + "".join(__import__("random").sample([str(i) for i in range(1, 20)], k=2))
    return ''.join(__import__('random').choices([chr(i) for i in range(0x4e00, 0x9fff)], k=3))

def rb():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))
anti = """
print(' ' * len('>> Running...'), end='\\r')

if str(__import__('sys').exit) != '<built-in function exit>':
    print('Hook hả con trai')
    __import__('sys').exit()

if str(print) != '<built-in function print>':
    print('Hook hả con trai')
    __import__('sys').exit()

if str(exec) != '<built-in function exec>':
    print('Hook hả con trai')
    __import__('sys').exit()

if str(input) != '<built-in function input>':
    print('Hook hả con trai')
    __import__('sys').exit()

if str(len) != '<built-in function len>':
    print('Hook hả con trai')
    __import__('sys').exit()

if str(__import__('marshal').loads) != '<built-in function loads>':
    print('Hook hả con trai')
    __import__('sys').exit()
if len(open(__file__, 'rb').read().splitlines()) != 55:
    print(">> Don't Edit This File")
    with open(__file__, "wb") as f:
        f.write(b'')
    __import__('sys').exit()
"""
antiglb = r"""
import inspect,sys,types,itertools,importlib,linecache,os,re,dis
from collections import namedtuple, OrderedDict
modulesbyfile = {}
_filesbymodname = {}
_Traceback = namedtuple('_Traceback', 'filename lineno function code_context index')
class Traceback(_Traceback):
    def __new__(cls, __memoryloader__, ___loadrunner__, function, ___occonbo__, ___um___, *, positions=None):
        __anhnguyencoder__ = super().__new__(cls, __memoryloader__, ___loadrunner__, function, ___occonbo__, ___um___)
        __anhnguyencoder__.positions = positions
        return __anhnguyencoder__
    def __repr__(self):
        return 'Traceback(__memoryloader__={!r}, ___loadrunner__={!r}, function={!r}, ___occonbo__={!r}, ___um___={!r}, positions={!r})'.format(self.__memoryloader__, self.___loadrunner__, self.function, self.___occonbo__, self.___um___, self.positions)
_FrameInfo = namedtuple('_FrameInfo', ('frame',) + Traceback._fields)
class FrameInfo(_FrameInfo):
    def __new__(cls, frame, filename, lineno, function, code_context, index, *, positions=None):
        __anhnguyencoder__ = super().__new__(cls, frame, filename, lineno, function, code_context, index)
        __anhnguyencoder__.positions = positions
        return __anhnguyencoder__
    def __repr__(self):
        return 'FrameInfo(frame={!r}, filename={!r}, lineno={!r}, function={!r}, code_context={!r}, index={!r}, positions={!r})'.format(self.frame, self.filename, self.lineno, self.function, self.code_context, self.index, self.positions)
def getabsfile(object, _filename=None):
    if _filename is None:
        _filename = getsourcefile(object) or getfile(object)
    return os.path.normcase(os.path.abspath(_filename))
def getmodule(object, _filename=None):

    if ismodule(object):
        return object
    if hasattr(object, '__module__'):
        return sys.modules.get(object.__module__)
    if _filename is not None and _filename in modulesbyfile:
        return sys.modules.get(modulesbyfile[_filename])
    try:
        file = getabsfile(object, _filename)
    except (TypeError, FileNotFoundError):
        return None
    if file in modulesbyfile:
        return sys.modules.get(modulesbyfile[file])
    for modname, module in sys.modules.copy().items():
        if ismodule(module) and hasattr(module, '__file__'):
            f = module.__file__
            if f == _filesbymodname.get(modname, None):
                continue
            _filesbymodname[modname] = f
            f = getabsfile(module)
            modulesbyfile[f] = modulesbyfile[
                os.path.realpath(f)] = module.__name__
    if file in modulesbyfile:
        return sys.modules.get(modulesbyfile[file])
    main = sys.modules['__main__']
    if not hasattr(object, '__name__'):
        return None
    if hasattr(main, object.__name__):
        mainobject = getattr(main, object.__name__)
        if mainobject is object:
            return main
    builtin = sys.modules['builtins']
    if hasattr(builtin, object.__name__):
        builtinobject = getattr(builtin, object.__name__)
        if builtinobject is object:
            return builtin
def findsource(object):
    file = getsourcefile(object)
    if file:
        linecache.checkcache(file)
    else:
        file = getfile(object)
        if not (file.startswith('<') and file.endswith('>')):
            raise OSError('source code not available')

    module = getmodule(object, file)
    if module:
        lines = linecache.getlines(file, module.__dict__)
    else:
        lines = linecache.getlines(file)
    if not lines:
        raise OSError('could not get source code')

    if ismodule(object):
        return lines, 0

    if isclass(object):
        qualname = object.__qualname__
        source = ''.join(lines)
        tree = ast.parse(source)
        class_finder = _ClassFinder(qualname)
        try:
            class_finder.visit(tree)
        except ClassFoundException as e:
            line_number = e.args[0]
            return lines, line_number
        else:
            raise OSError('could not find class definition')

    if ismethod(object):
        object = object.__func__
    if isfunction(object):
        object = object.__code__
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        if not hasattr(object, 'co_firstlineno'):
            raise OSError('could not find function definition')
        lnum = object.co_firstlineno - 1
        pat = re.compile(r'^(\s*def\s)|(\s*async\s+def\s)|(.*(?<!\w)lambda(:|\s))|^(\s*@)')
        while lnum > 0:
            try:
                line = lines[lnum]
            except IndexError:
                raise OSError('lineno is out of bounds')
            if pat.match(line):
                break
            lnum = lnum - 1
        return lines, lnum
    raise OSError('could not find code object')
def iscode(object):
    return isinstance(object, types.CodeType)
def isframe(object):
    return isinstance(object, types.FrameType)
def ismodule(object):
    return isinstance(object, types.ModuleType)
def isclass(object):
    return isinstance(object, type)
def isfunction(object):
    return isinstance(object, types.FunctionType)
def ismethod(object):
    return isinstance(object, types.MethodType)
def getfile(object):
    if ismodule(object):
        if getattr(object, '__file__', None):
            return object.__file__
        raise TypeError('{!r} is a built-in module'.format(object))
    if isclass(object):
        if hasattr(object, '__module__'):
            module = sys.modules.get(object.__module__)
            if getattr(module, '__file__', None):
                return module.__file__
            if object.__module__ == '__main__':
                raise OSError('source code not available')
        raise TypeError('{!r} is a built-in class'.format(object))
    if ismethod(object):
        object = object.__func__
    if isfunction(object):
        object = object.__code__
    if istraceback(object):
        object = object.tb_frame
    if isframe(object):
        object = object.f_code
    if iscode(object):
        return object.co_filename
    raise TypeError('module, class, method, function, traceback, frame, or ''code object was expected, got {}'.format(type(object).__name__))

def getsourcefile(object):
    filename = getfile(object)
    all_bytecode_suffixes = importlib.machinery.DEBUG_BYTECODE_SUFFIXES[:]
    all_bytecode_suffixes += importlib.machinery.OPTIMIZED_BYTECODE_SUFFIXES[:]
    if any(filename.endswith(s) for s in all_bytecode_suffixes):
        filename = (os.path.splitext(filename)[0] +
                    importlib.machinery.SOURCE_SUFFIXES[0])
    elif any(filename.endswith(s) for s in
                 importlib.machinery.EXTENSION_SUFFIXES):
        return None
    if filename in linecache.cache:
        return filename
    if os.path.exists(filename):
        return filename
    module = getmodule(object, filename)
    if getattr(module, '__loader__', None) is not None:
        return filename
    elif getattr(getattr(module, "__spec__", None), "loader", None) is not None:
        return filename
def istraceback(object):
    return isinstance(object, types.TracebackType)
def _get_code_position(code, instruction_index):
    if instruction_index < 0:
        return (None, None, None, None)
    positions_gen = code.co_positions()
    return next(itertools.islice(positions_gen, instruction_index // 2, None))
def _get_code_position_from_tb(tb):
    code, instruction_index = (tb.tb_frame.f_code, tb.tb_lasti)
    return _get_code_position(code, instruction_index)
def getframeinfo(frame, context=1):
    if istraceback(frame):
        positions = _get_code_position_from_tb(frame)
        lineno = frame.tb_lineno
        frame = frame.tb_frame
    else:
        lineno = frame.f_lineno
        positions = _get_code_position(frame.f_code, frame.f_lasti)
    if positions[0] is None:
        frame, *positions = (frame, lineno, *positions[1:])
    else:
        frame, *positions = (frame, *positions)
    lineno = positions[0]
    if not isframe(frame):
        raise TypeError('{!r} is not a frame or traceback object'.format(frame))
    filename = getsourcefile(frame) or getfile(frame)
    if context > 0:
        start = lineno - 1 - context // 2
        try:
            lines, lnum = findsource(frame)
        except OSError:
            lines = index = None
        else:
            start = max(0, min(start, len(lines) - context))
            lines = lines[start:start + context]
            index = lineno - 1 - start
    else:
        lines = index = None
    return Traceback(filename, lineno, frame.f_code.co_name, lines, index, positions=dis.Positions(*positions))
def __loader__(frame, context=1):
    framelist = []
    while frame:
        traceback_info = getframeinfo(frame, context)
        frameinfo = (frame,) + traceback_info
        framelist.append(FrameInfo(*frameinfo, positions=traceback_info.positions))
        frame = frame.f_back
    return framelist
def stack(context=1):
    return __loader__(sys._getframe(1), context)
def __finally__(__ngauroido__: bytes):
    h = 2166136261
    for b in __ngauroido__:
        h ^= b
        h *= 16777619
        h &= 0xffffffff
    return h

def __ngauroicacem__(code):
    return (code.co_code, code.co_consts, code.co_names, code.co_varnames, code.co_freevars, code.co_cellvars)

def flatten(__ngauroido__):
    if isinstance(__ngauroido__, (list, tuple)):
        return b''.join(flatten(x) for x in __ngauroido__)
    elif isinstance(__ngauroido__, bytes):
        return __ngauroido__

    elif isinstance(__ngauroido__, str):
        return __ngauroido__.encode('utf-8')
    elif isinstance(__ngauroido__, int):
        return __ngauroido__.to_bytes(8, 'little', signed=True)
    elif __ngauroido__ is None:
        return b'N'
    elif isinstance(__ngauroido__, float):
        import struct
        return struct.pack('<d', __ngauroido__)
    elif isinstance(__ngauroido__, bool):
        return b'T' if __ngauroido__ else b'F'
    elif isinstance(__ngauroido__, type(Ellipsis)):
        return b'E'
    elif isinstance(__ngauroido__, complex):
        import struct
        return struct.pack('<dd', __ngauroido__.real, __ngauroido__.imag)
    elif isinstance(__ngauroido__, type((lambda: 1).__code__)):
        return flatten(__ngauroicacem__(__ngauroido__))
    else:
        return str(__ngauroido__).encode('utf-8')
def __loader1__(code_obj):
    __mmbeo__ = __ngauroicacem__(code_obj)
    __ok__ = flatten(__mmbeo__)
    return __finally__(__ok__)
"""
class RenameVars(ast.NodeTransformer):
    def __init__(self):
        self.map = {}
        self.scope_stack = []

    def _new(self):
        return rb()

    def visit_FunctionDef(self, node):
        local_map = {}
        self.scope_stack.append(local_map)

        for arg in node.args.args:
            new = self._new()
            local_map[arg.arg] = new
            arg.arg = new

        self.generic_visit(node)
        self.scope_stack.pop()
        return node

    def visit_Lambda(self, node):
        local_map = {}
        self.scope_stack.append(local_map)
        for arg in node.args.args:
            new = self._new()
            local_map[arg.arg] = new
            arg.arg = new
        self.generic_visit(node)
        self.scope_stack.pop()
        return node

    def visit_Name(self, node):
        if isinstance(node.ctx, (ast.Store, ast.Load)):
            if node.id in buitlins:
                return node

            for scope in reversed(self.scope_stack):
                if node.id in scope:
                    node.id = scope[node.id]
                    return node

            if node.id not in self.map:
                self.map[node.id] = self._new()
            node.id = self.map[node.id]

        return node
def antibypass():

    def anti(s: str, kkk=69):

        def f(n):
            a, b = (n & 240, n & 15)
            return f'(({a + 10000000000000000000000000}) >>  ({b + 100000000000000000000000000000000000}))' if n > 15 else str(n)
        fx = [f(ord(c) ^ kkk) for c in s]
        mm = ', '.join(fx)
        return f"""((lambda __Anhnguyencoder__: __Anhnguyencoder__(*[__dat__('Biet Dzai Roi',{mm})]))(lambda *__occak__: ((lambda __thknqu__, __Anhnguyencoder__:__Anhnguyencoder__().join([*map(lambda n: __Anhnguyencoder__().format((n ^ 64)), __Anhnguyencoder__)]))(lambda: getattr(''.__class__, '__add__')('__Anhnguyencoder__', ''),lambda: "__CONCAC__"))))"""
    junk_code = []
    for i in range(100):
        junk_code.append(f'\ndef _junk{i}():\n    x = {random.randint(1000, 9999)}\n    for n in range(50):\n        x ^= (n << {i % 5})\n    return x\n')
    fake_flow = []
    for i in range(100):
        fake_flow.append(f'\ntry:\n    if ({i} * {i}) % 5 == ({i * i}) % 5:\n        _junk{i % 10}()\nexcept:\n    pass\n')

    def __spam_marshal_runtime__():
        junk_src = 'x=' + str(random.randint(10 ** 50, 10 ** 60))
        junk_ast = ast.parse(junk_src)
        junk_ast = ast.fix_missing_locations(junk_ast)
        blob = marshal.dumps(compile(junk_ast, '<FoNixA>', 'exec'))
        try:
            marshal.loads(blob)
        except:
            pass
        return '0'
    import ast
    def spam_marshal_runtime():
        src = "x='X'*2000000"
        tree = ast.parse(src)
        ast.fix_missing_locations(tree)
        cd = compile(ast.unparse(tree), '<FoNixA>', 'exec')
        blob = marshal.dumps(cd)
        try:
            marshal.loads(blob)
        except:
            pass
        return '0'

    def anti_decompile():
        for _ in range(100):
            __spam_marshal_runtime__()
            spam_marshal_runtime()
        return '0'

    def mutate_consts():
        import random
        co = mutate_consts.__code__
        junk = bytes((random.randint(0, 255) for _ in range(100)))
        mutate_consts.__code__ = co.replace(co_consts=co.co_consts + (junk,))
        return '0'
    c = spam_marshal_runtime() + mutate_consts() + anti_decompile() + __spam_marshal_runtime__()

    def _anti():
        def rb():
            return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))
        d = rb()
        antipycdc = ''
        for i in range(100):
            antipycdc += f"__Anhnguyencoder__(__Anhnguyencoder__(__Anhnguyencoder__(__Anhnguyencoder__(__Anhnguyencoder__(__Anhnguyencoder__('{d}')))))),"
        antipycdc = "try:anhnguyen=[" + antipycdc + c + "]\nexcept:pass"
        text = f"""
{''.join(junk_code)}
def __CTEVCLDZAI__(__chanankdi__):
    return __chanankdi__
try:pass
except:pass
finally:pass
{antipycdc}
{''.join(fake_flow)}
finally:int(2011-2011)
        """
        return f"""
try:
    def __ctevcldz__(__ok__):return "__ANTI-DECOMPILER__"
    {anti("__Anhnguyencoder__")}
except:pass
else:pass
finally:pass
{text}"""

    return _anti()

antidec = f"""
{antibypass()}
"""
obf_var = r"""
import inspect, sys

def __var_chaos__():
    f = inspect.currentframe().f_back
    fid = id(f)
    globals()[str(fid)] = f.f_lineno ^ fid

    c = 0
    for _ in range(3):
        c += 1
        globals()['_'+('_'*c)] = c << 3

    class _X: pass
    a = _X(); b = _X()
    globals()[str(id(a))] = id(b)
    globals()[str(id(b))] = id(a)

    def _ls_():
        x = 1
        locals()[str(x)] = x << 4
        x = 2
        locals()[str(x)] = x << 5
        return x
    _ls_()
    if sys.gettrace():
        for i in range(1500):
            globals()[str(id(i))] = None

__var_chaos__()
"""
antidec1 = r"""
import os, sys, shutil, zlib, importlib.abc, importlib.util

duoi = ".py__anhnguyencoder___"

def encode_file(src, dst):
    with open(src, "rb") as f:
        data = f.read()
    enc = zlib.compress(data)
    with open(dst, "wb") as f:
        f.write(enc)

def ensure_local_requests():
    try:
        import requests
        src_root = os.path.dirname(requests.__file__)
    except:
        return
    dst_root = os.path.join(os.path.dirname(__file__), "requests")
    if os.path.exists(dst_root):
        return

    for root, dirs, files in os.walk(src_root):
        rel = os.path.relpath(root, src_root)
        dst_dir = os.path.join(dst_root, rel)
        os.makedirs(dst_dir, exist_ok=True)

        for file in files:
            if file.endswith(".py"):
                src_file = os.path.join(root, file)
                dst_file = os.path.join(dst_dir, file + duoi)
                encode_file(src_file, dst_file)
            elif not file.endswith((".pyc", ".pyo")):
                shutil.copy2(os.path.join(root, file), os.path.join(dst_dir, file))
class EncLoader(importlib.abc.Loader):
    def __init__(self, path):
        self.path = path
    def create_module(self, spec):
        return None
    def exec_module(self, module):
        with open(self.path, "rb") as f:
            data = zlib.compress(f.read())
        code = compile(data, self.path, "exec")
        exec(code, module.__dict__)

class EncFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if not fullname.startswith("requests"):
            return None

        base = os.path.join(os.path.dirname(__file__), *fullname.split("."))
        file_path = base + duoi
        init_path = os.path.join(base, "__init__.py" + duoi)

        if os.path.isfile(file_path):
            return importlib.util.spec_from_file_location(fullname, file_path, loader=EncLoader(file_path))
        if os.path.isfile(init_path):
            return importlib.util.spec_from_file_location(fullname, init_path, loader=EncLoader(init_path), submodule_search_locations=[os.path.dirname(init_path)])
        return None

ensure_local_requests()
sys.meta_path.insert(0, EncFinder())

p = getattr(__import__('ctypes'), ''.join(['pyt','honapi']))
r = getattr(p, ''.join(['PyMarshal_','ReadObjectFromString']))
e = getattr(p, ''.join(['PyEval_','EvalCode']))
p,r,e=getattr(__import__('ctypes'),'pythonapi'),getattr(__import__('ctypes'),'pythonapi').PyMarshal_ReadObjectFromString,getattr(__import__('ctypes'),'pythonapi').PyEval_EvalCode;[setattr(f,a,v)for f,a,v in[(r,'restype',__import__('ctypes').py_object),(r,'argtypes',[__import__('ctypes').c_char_p,__import__('ctypes').c_long]),(e,'restype',__import__('ctypes').py_object),(e,'argtypes',[__import__('ctypes').py_object]*3)]]
"""
class Flatten(ast.NodeTransformer):

    def visit_FunctionDef(self, node):
        if len(node.body) < 2:
            return node
        state = rb()
        cases = []
        for i, stmt in enumerate(node.body):
            cases.append(ast.If(test=ast.Compare(left=ast.Name(state, ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(i)]), body=[stmt, ast.Assign(targets=[ast.Name(state, ast.Store())], value=ast.Constant(i + 1))], orelse=[]))
        node.body = [ast.Assign(targets=[ast.Name(state, ast.Store())], value=ast.Constant(0)), ast.While(test=ast.Constant(True), body=cases + [ast.Break()], orelse=[])]
        return node

class ConstHide(ast.NodeTransformer):
    def visit_Constant(self, node):
        if isinstance(node.value, str) and len(node.value) > 3:
            parts = [node.value[i:i+2] for i in range(0, len(node.value), 2)]
            return ast.Call(
                func=ast.Attribute(value=ast.Constant(''), attr='join', ctx=ast.Load()),
                args=[ast.List(elts=[ast.Constant(p) for p in parts], ctx=ast.Load())],
                keywords=[]
            )
        if isinstance(node.value, int) and node.value > 9:
            a = random.randint(2, 9)
            b = node.value ^ a
            return ast.BinOp(ast.Constant(b), ast.BitXor(), ast.Constant(a))
        return node

class FakeLogic(ast.NodeTransformer):

    def wrap(self, real):
        flag = rb()
        return [ast.Assign(targets=[ast.Name(flag, ast.Store())], value=ast.Constant(True)), ast.If(test=ast.Name(flag, ast.Load()), body=[real], orelse=[])]

    def visit_Module(self, node):
        new_body = []
        for stmt in node.body:
            new_body.extend(self.wrap(stmt))
        node.body = new_body
        return node

    def visit_FunctionDef(self, node):
        new_body = []
        for stmt in node.body:
            new_body.extend(self.wrap(stmt))
        node.body = new_body
        return node

class ASTFormat(ast.NodeTransformer):

    def visit_Expr(self, node):
        return ast.Expr(value=ast.Call(func=ast.Lambda(args=ast.arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=node.value), args=[], keywords=[]))

    def visit_Assign(self, node):
        node.value = ast.BinOp(left=ast.BinOp(left=node.value, op=ast.Add(), right=ast.Constant(0)), op=ast.Sub(), right=ast.Constant(0))
        return node

    def visit_If(self, node):
        self.generic_visit(node)
        node.test = ast.BoolOp(op=ast.And(), values=[ast.Constant(True), node.test])
        return node

    def visit_While(self, node):
        self.generic_visit(node)
        node.test = ast.BoolOp(op=ast.Or(), values=[node.test, ast.Constant(False)])
        return node

    def visit_Return(self, node):
        if node.value:
            node.value = ast.BinOp(node.value, ast.Add(), ast.Constant(0))
        return node
def _moreobf(node_or_tree):
    import random

    def rd():
        return str(random.randint(0x1E000000000, 0x7E000000000))

    def junk(en, max_value):
        cases = []
        line = max_value + 1
        for i in range(random.randint(1, 5)):
            case_name = "__"+rd()
            case_body = [
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=line)]
                    ), 
                    body=[
                        ast.Assign(
                            targets=[ast.Name(id=case_name)], 
                            value=ast.Constant(value=random.randint(0xFFFFF, 0xFFFFFFFFFFFF)), 
                            lineno=None
                        )
                    ], 
                    orelse=[]
                )
            ]
            cases.extend(case_body)
            line += 1
        return cases

    def bl(body):
        var = "__"+rd()
        en = "__"+rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id='MemoryError'), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        
        for i in body:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        
        tb[1].handlers[0].body.extend(junk(en, len(body) + 1))
        
        node = ast.Assign(
            targets=[ast.Name(id=var)], 
            value=ast.Constant(value=0), 
            lineno=None
        )
        
        return [node] + tb

    def _bl(node):
        olb = node.body
        var = "__"+rd()
        en = "__"+rd()

        tb = [
            ast.AugAssign(
                target=ast.Name(id=var), 
                op=ast.Add(), 
                value=ast.Constant(value=1)
            ),
            ast.Try(
                body=[
                    ast.Raise(
                        exc=ast.Call(func=ast.Name(id='MemoryError'), 
                                     args=[ast.Name(id=var)], 
                                     keywords=[])
                    )
                ],
                handlers=[
                    ast.ExceptHandler(
                        type=ast.Name(id='MemoryError'), 
                        name=en, 
                        body=[]
                    )
                ],
                orelse=[],
                finalbody=[]
            )
        ]
        for i in olb:
            tb[1].handlers[0].body.append(
                ast.If(
                    test=ast.Compare(
                        left=ast.Subscript(
                            value=ast.Attribute(
                                value=ast.Name(id=en), 
                                attr='args'
                            ), 
                            slice=ast.Constant(value=0)
                        ), 
                        ops=[ast.Eq()], 
                        comparators=[ast.Constant(value=1)]
                    ), 
                    body=[i], 
                    orelse=[]
                )
            )
        tb[1].handlers[0].body.extend(junk(en, len(olb) + 1))
        node.body = [
            ast.Assign(
                targets=[ast.Name(id=var)], 
                value=ast.Constant(value=0), 
                lineno=None
            )
        ] + tb
        return node

    # ===== THÊM XỬ LÝ CHO NODE ĐƠN =====
    # Nếu là module (có body)
    if hasattr(node_or_tree, 'body') and isinstance(node_or_tree.body, list):
        tree = node_or_tree
        nb = []
        for node in tree.body:
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                nb.append(_bl(node))
            elif isinstance(node, (ast.Assign, ast.AugAssign, ast.AnnAssign)):
                nb.extend(bl([node]))
            elif isinstance(node, ast.Expr):
                nb.extend(bl([node]))
            else:
                nb.append(node)
        tree.body = nb
        return tree
    else:
        # Nếu là node đơn (câu lệnh không có body)
        return node_or_tree
class junk1(ast.NodeTransformer):
    def visit(self, node):
        # Duyệt con trước
        node = self.generic_visit(node)
        
        # Xử lý tất cả các block lệnh
        for field in ('body', 'orelse', 'finalbody'):
            if hasattr(node, field) and isinstance(getattr(node, field), list):
                block = getattr(node, field)
                new_block = []
                for stmt in block:
                    result = _moreobf(stmt)
                    if isinstance(result, list):
                        new_block.extend(result)
                    else:
                        new_block.append(result)
                setattr(node, field, new_block)
        
        # Xử lý handlers của Try
        if hasattr(node, 'handlers'):
            new_handlers = []
            for handler in node.handlers:
                if hasattr(handler, 'body') and isinstance(handler.body, list):
                    new_body = []
                    for stmt in handler.body:
                        result = _moreobf(stmt)
                        if isinstance(result, list):
                            new_body.extend(result)
                        else:
                            new_body.append(result)
                    handler.body = new_body
                new_handlers.append(handler)
            node.handlers = new_handlers
        
        return node

class AntiSafeVarSpam(ast.NodeTransformer):

    def visit_Module(self, node):
        junk = []
        for i in range(25):
            junk_name = rb()
            junk.append(ast.Assign(targets=[ast.Name(junk_name, ast.Store())], value=ast.BinOp(ast.Constant(i), ast.BitXor(), ast.Constant(123456))))
        node.body = junk + node.body
        return node

class AntiSafeNoise(ast.NodeTransformer):

    def visit_Module(self, node):
        noise = []
        for _ in range(15):
            flag = rb()
            noise.append(ast.Assign(targets=[ast.Name(flag, ast.Store())], value=ast.Constant(True)))
            noise.append(ast.If(test=ast.Name(flag, ast.Load()), body=[ast.Pass()], orelse=[]))
        node.body = noise + node.body
        return node

conconlak = {'__file__', 'filename', 'path', 'p1', 'p2', 'p3', 'p4', 'inspect', 'os', 'sys', 'Path', 'open', 'compile', 'pydc', '__import__', 'exec'}

class Vars(ast.NodeTransformer):

    def __init__(self):
        self.scope_stack = []

    def _new(self):
        return rb()

    def visit_FunctionDef(self, node):
        local_map = {}
        self.scope_stack.append(local_map)
        for arg in node.args.args:
            if arg.arg not in conconlak:
                new = self._new()
                local_map[arg.arg] = new
                arg.arg = new
        self.generic_visit(node)
        self.scope_stack.pop()
        return node

    def visit_Lambda(self, node):
        local_map = {}
        self.scope_stack.append(local_map)
        for arg in node.args.args:
            if arg.arg not in conconlak:
                new = self._new()
                local_map[arg.arg] = new
                arg.arg = new
        self.generic_visit(node)
        self.scope_stack.pop()
        return node

    def visit_Name(self, node):
        if node.id in buitlins:
            return node
        if node.id in conconlak:
            return node
        for scope in reversed(self.scope_stack):
            if node.id in scope:
                node.id = scope[node.id]
                return node
        return node

def ast_lol(code: str):
    code = ast.parse(code)

    meo = AntiSafeVarSpam().visit(code)
    code = AntiSafeNoise().visit(meo)
    code = Vars().visit(code)
    
    ast.fix_missing_locations(code)
    return ast.unparse(code)

d_var = r"""
def __dyn_set__(k, v):
    globals()[k] = v

def __dyn_get__(k):
    return globals().get(k)

_k0 = 'x' * 5
_k1 = 'y' * 5

__dyn_set__(_k0, 123456)
__dyn_set__(_k1, __dyn_get__(_k0) ^ 0)
"""
def var_con_cak():
    return ''.join(random.choices([chr(i) for i in range(44032, 55204) if chr(i).isprintable() and chr(i).isidentifier()], k=11))
v = var_con_cak()
args = var_con_cak()
kwds = var_con_cak()
d = var_con_cak()
k = var_con_cak()
c = var_con_cak()
arg_ = var_con_cak()
s = var_con_cak()
def _args(name):
    return ast.arguments(
        posonlyargs=[],
        args=[ast.arg(arg=name)],
        vararg=None,
        kwonlyargs=[],
        kw_defaults=[],
        kwarg=None,
        defaults=[]
    )
antipycdc = ''
for i in range(1000):
    antipycdc += f"你器(你器(你器(你器(你器(你器('')))))),"
antipycdc = "try:Anhnguyencoder=[" + antipycdc + "]\nexcept:pass"
ANTI_PYCDC = f"""
def 你器(你):
    return 你
try:pass
except:pass
finally:pass
{antipycdc}
finally:int(2011-2111)
"""
def obfstr(s):
    lst=[ord(i) for i in s]; v=var_con_cak()
    lam3=ast.Lambda(
        args=_args(var_con_cak()),
        body=ast.Call(
            func=ast.Attribute(
                value=ast.Call(ast.Name('str',ast.Load()),[],[]),
                attr="join", ctx=ast.Load()
            ),
            args=[ast.GeneratorExp(
                elt=ast.Call(ast.Name("chr",ast.Load()),[ast.Name(v,ast.Load())],[]),
                generators=[ast.comprehension(
                    target=ast.Name(v,ast.Store()),
                    iter=ast.List([ast.Constant(x) for x in lst],ast.Load()),
                    ifs=[], is_async=0
                )]
            )],
            keywords=[]
        )
    )
    lam2=ast.Lambda(_args(var_con_cak()),
        ast.Call(lam3,[ast.Constant("Lisender")],[]))
    lam1=ast.Lambda(_args(var_con_cak()),
        ast.Call(lam2,[ast.Constant("Lisender")],[]))
    return ast.Call(lam1,[ast.Constant("Lisender")],[])

def obfint(i):
    haha=2010-i
    lam3=ast.Lambda(_args(var_con_cak()),
        ast.Call(ast.Name("int",ast.Load()),
            [ast.BinOp(ast.Constant(2010),ast.Sub(),ast.Constant(haha))],[]))
    lam2=ast.Lambda(_args(var_con_cak()),
        ast.Call(lam3,[ast.Constant("Lisender")],[]))
    lam1=ast.Lambda(_args(var_con_cak()),
        ast.Call(lam2,[ast.Constant("Lisender")],[]))
    return ast.Call(lam1,[ast.Constant("Lisender")],[])

def joinstr(f):
    if not isinstance(f, ast.JoinedStr):
        return f
    vl = []
    for i in f.values:
        if isinstance(i, ast.Constant):
            vl.append(i)
        elif isinstance(i, ast.FormattedValue):
            value_expr = i.value
            if i.conversion == 115:
                value_expr = Call(func=Name(id='str', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 114:
                value_expr = Call(func=Name(id='repr', ctx=Load()), args=[value_expr], keywords=[])
            elif i.conversion == 97:
                value_expr = Call(func=Name(id='ascii', ctx=Load()), args=[value_expr], keywords=[])
            if i.format_spec:
                if isinstance(i.format_spec, ast.JoinedStr):
                    spec_expr = joinstr(i.format_spec)
                elif isinstance(i.format_spec, ast.Constant):
                    spec_expr = i.format_spec
                elif isinstance(i.format_spec, ast.FormattedValue):
                    spec_parts = []
                    spec_value = i.format_spec.value
                    if i.format_spec.conversion == 115:
                        spec_value = Call(func=Name(id='str', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 114:
                        spec_value = Call(func=Name(id='repr', ctx=Load()), args=[spec_value], keywords=[])
                    elif i.format_spec.conversion == 97:
                        spec_value = Call(func=Name(id='ascii', ctx=Load()), args=[spec_value], keywords=[])
                    spec_expr = spec_value
                else:
                    spec_expr = i.format_spec
                value_expr = Call(func=Name(id='format', ctx=Load()), args=[value_expr, spec_expr], keywords=[])
            elif i.conversion == -1:
                value_expr = Call(func=Name(id='str', ctx=Load()), args=[value_expr], keywords=[])
            vl.append(value_expr)
        elif hasattr(i, 'values') and isinstance(i, ast.JoinedStr):
            vl.append(joinstr(i))
        else:
            vl.append(Call(func=Name(id='str', ctx=Load()), args=[i], keywords=[]))
    if not vl:
        return Constant(value='')
    if len(vl) == 1 and isinstance(vl[0], ast.Constant):
        return vl[0]
    return Call(func=Attribute(value=Constant(value=''), attr='join', ctx=Load()), args=[Tuple(elts=vl, ctx=Load())], keywords=[])
class A(ast.NodeTransformer):
    __slots__ = ()
    def visit_Module(self, node):
        self.generic_visit(node)
        node.body = [n for n in node.body if not (isinstance(n, ast.Expr) and isinstance(n.value, ast.Constant) and isinstance(n.value.value, str))]
        return node
    visit_FunctionDef = visit_Module
    visit_AsyncFunctionDef = visit_Module
    visit_ClassDef = visit_Module

class obf(ast.NodeTransformer):

    def visit_Constant(self, node):
        if isinstance(node.value, str):
            node = obfstr(node.value)
        elif isinstance(node.value, int):
            node = obfint(node.value)
        return node
def gen_jcode(code):
    men = var_con_cak()
    trinhdeptrai = var_con_cak()
    quadeptrai = var_con_cak()
    return [Assign(targets=[Name(id=trinhdeptrai, ctx=Store())], value=Constant(value=men), lineno=0), Assign(targets=[Name(id=quadeptrai, ctx=Store())], value=Constant(value=True), lineno=0), If(test=BoolOp(op=And(), values=[Compare(left=Name(id=trinhdeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value=men)]), Compare(left=Name(id=quadeptrai, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=True)])]), body=[Expr(value=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Constant(value='dit me may')))], orelse=[If(test=BoolOp(op=And(), values=[Compare(left=Name(id=trinhdeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value=men)]), Compare(left=Name(id=quadeptrai, ctx=Load()), ops=[NotEq()], comparators=[Constant(value=False)])]), body=[Try(body=[Expr(value=Tuple(elts=[BinOp(left=Constant(value=1), op=Div(), right=Constant(value=0)), BinOp(left=Constant(value=123), op=Div(), right=Constant(value=0)), BinOp(left=Constant(value=12312321312), op=Div(), right=Constant(value=0))], ctx=Load()))], handlers=[ExceptHandler(body=[code])], orelse=[], finalbody=[])], orelse=[If(test=BoolOp(op=Or(), values=[Compare(left=Name(id=trinhdeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value='gay')]), Compare(left=Name(id=quadeptrai, ctx=Load()), ops=[Eq()], comparators=[Constant(value=False)])]), body=[Expr(value=Call(func=Lambda(args=arguments(posonlyargs=[], args=[], kwonlyargs=[], kw_defaults=[], defaults=[]), body=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='cai lon cha nha may')], keywords=[])), args=[], keywords=[]))], orelse=[While(test=Constant(value=True), body=[Pass()], orelse=[]), Expr(value=Call(func=Name(id='print', ctx=Load()), args=[Constant(value='cai dit thang cha may')], keywords=[]))])])])]
class junk(ast.NodeTransformer):

    def visit_Module(self, node):
        for i, j in enumerate(node.body):
            if isinstance(j, (ast.FunctionDef, ast.ClassDef)):
                self.visit(j)
            node.body[i] = [gen_jcode(j)]
        return node

    def visit_FunctionDef(self, node):
        for i, j in enumerate(node.body):
            node.body[i] = [gen_jcode(j)]
        return node

    def visit_ClassDef(self, node):
        for i, j in enumerate(node.body):
            node.body[i] = [gen_jcode(j)]
        return node
class cv(ast.NodeTransformer):

    def visit_JoinedStr(self, node):
        node = joinstr(node)
        return node
class hide1(ast.NodeTransformer):
    targets = set(buitlins) | {'exec', 'eval'}

    def _get_builtin(self, name, use_eval=False):
        core = ast.Call(func=ast.Name('getattr', ast.Load()), args=[ast.Call(func=ast.Name('__import__', ast.Load()), args=[ast.Constant('builtins')], keywords=[]), ast.Constant(name)], keywords=[])
        if use_eval:
            return ast.Call(func=ast.Name('eval', ast.Load()), args=[core], keywords=[])
        return core

    def visit_Call(self, node):
        self.generic_visit(node)
        if isinstance(node.func, ast.Name) and node.func.id in self.targets:
            node.func = self._get_builtin(node.func.id, use_eval=node.func.id in {'exec', 'eval'})
        return node

    def visit_Attribute(self, node):
        self.generic_visit(node)
        if isinstance(node.value, ast.Name) and node.value.id in {'builtins', '__builtins__'} and (node.attr in self.targets):
            return self._get_builtin(node.attr, use_eval=node.attr in {'exec', 'eval'})
        return node

    def visit_Name(self, node):
        if node.id in buitlins:
            node = Call(func=Name(id='getattr', ctx=Load()), args=[Call(func=Name(id='AnhNguyenCoder', ctx=Load()), args=[Constant(value='builtins')], keywords=[]), Constant(value=node.id)], keywords=[])
        return node
def moreobf1(src: str) -> str:
    tree = ast.parse(src)

    def rd():
        return '__x0_' + ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=5))
        
    def wrap_stmt(stmt):
        state = rd()
        err = rd()
        assign = ast.Assign(targets=[ast.Name(state, ast.Store())], value=ast.Constant(0))
        try_block = ast.Try(body=[ast.Raise(exc=ast.Call(func=ast.Name('MemoryError', ast.Load()), args=[ast.Name(state, ast.Load())], keywords=[]))], handlers=[ast.ExceptHandler(type=ast.Name('MemoryError', ast.Load()), name=err, body=[ast.If(test=ast.Compare(left=ast.Subscript(value=ast.Attribute(value=ast.Name(err, ast.Load()), attr='args', ctx=ast.Load()), slice=ast.Constant(0), ctx=ast.Load()), ops=[ast.Eq()], comparators=[ast.Constant(0)]), body=[stmt], orelse=[])])], orelse=[], finalbody=[])
        return [assign, try_block]
    new_body = []
    for node in tree.body:
        if isinstance(node, (ast.Assign, ast.Expr, ast.AugAssign)):
            new_body.extend(wrap_stmt(node))
        elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            node.body = sum([wrap_stmt(n) for n in node.body], [])
            new_body.append(node)
        else:
            new_body.append(node)
    tree.body = new_body
    ast.fix_missing_locations(tree)
    return tree

def strin(text, xor_range=(10000, 99999)):
    byte_data = text.encode('utf8') if isinstance(text, str) else text
    parts = []
    for i, byte in enumerate(byte_data):
        xor_val = random.randint(xor_range[0], xor_range[1])
        encoded = byte ^ xor_val
        lambda_name = c
        parts.append(f"(lambda {lambda_name}: {lambda_name} ^ {xor_val})({encoded})")
    if not parts:
        return "bytes([]).decode('utf8')"
    return f"bytes([{', '.join(parts)}]).decode('utf8')"
VIP_ANTI = '\nif len(globals()) != 100:\n    globals()["_HOOK_CAI_LON_"]=("TrinhNguyen0611") * 1\n    exit()\nif __import__(\'os\').environ.get("HTTP_TOOLKIT_ACTIVE") == "true":\n    globals()["_HOOK_CAI_LON_"]=("TrinhNguyen0611") * 1\n    exit()\nfor ev in ["SSL_CERT_FILE", "NODE_EXTRA_CA_CERTS", "PATH"]:\n    if ev in __import__(\'os\').environ and "httptoolkit" in __import__(\'os\').environ[ev].lower():\n        globals()["_HOOK_CAI_LON_"]=("TrinhNguyen0611") * 1\n        exit()\nfor px in ["HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy"]:\n    if px in __import__(\'os\').environ and "127.0.0.1:8000" in __import__(\'os\').environ[px]:\n        globals()["_HOOK_CAI_LON_"]=("TrinhNguyen0611") * 1\n        exit()\ntry:\n    h = requests.get("https://example.com", timeout=5).headers\n    if any("HTTP-Toolkit" in h.get(x, "") for x in ["Server", "Via", "X-Powered-By"]):\n        globals()["_HOOK_CAI_LON_"]=("TrinhNguyen0611") * 1\n        exit()\nexcept:\n    pass\n'
Lisander = 'Lisander'
BattleBank = f"""#!/usr/bin/python3
# -*- coding: utf-8 -*-
__OBF__ = ('LisanderPremium')[(lambda : 0 << 2009 << 0)()]
__OWN__ = "Lisander & Percival & Dorian"
__USR__ = "LisanderIsTheBest - Main - Requests Protected"
__PY__ = "{sys.version_info.major}.{sys.version_info.minor}"
__GLB__ = (lambda Lisander: (lambda Lisander: (lambda: {random.randint(500,3000)} - (lambda: {random.randint(100,1000)})() - (lambda: Lisander)() + (lambda: {random.randint(1,100)})())())({Lisander}))(2000)
__CMT__ = "Don't Read This Code Because You Will Be Dizzy By My Magic!"
__WARN__={{
"_VN_": "Obfuscator được tạo ra nhằm bảo vệ mã nguồn, tuy nhiên nó cũng có thể bị các thành phần xấu lợi dụng để che giấu mã độc, botnet, keylogger, v.v. Hãy thận trọng khi chạy. Nếu bạn chạy, owner sẽ không chịu trách nhiệm!",
"_EN_": "This obfuscator is created to protect code, so it may also be abused by malicious actors to hide malware, botnets, keyloggers, etc. Please be cautious when running it. If you run it anyway, the owner takes no responsibility!",
}}

class ObsidianObfuscate(object):
    def __init__(self):
        if str(__import__("sys").version_info.major)+"."+str(__import__("sys").version_info.minor) != "{ver}":
            print(f'>> Your Python Version Is {{str(__import__("sys").version_info.major)+"."+str(__import__("sys").version_info.minor)}}.\\n>> Please Install Python {ver} To Run This File!')
            __import__('sys').exit()
        else:
            print('>> Running...', end='\\r')
    def __call__(self, *{args}, **{kwds}):
        global Super, BatMan, Spdier, Ender_Pearl, Crystal, Herobrine, Notch, Gapple, Shulker, Lava, Elytra, Water
        globals()['Super'] = eval({strin('eval')})
        globals()['BatMan'] = Super({strin('str')})
        globals()['Spdier'] = Super({strin('bytes')})
        globals()['Notch'] = Super({strin('dict')})
        globals()['Gapple'] = Super({strin('zip')})
        globals()['Shulker'] = {strin('LisanderPremium')}
        globals()['Lava'] = {strin("AnBoMayDi")}
        globals()['Elytra'] = Notch(Gapple(Shulker, Lava))
        globals()['Ender_Pearl'] = Super({strin('__import__')})
        globals()['Crystal'] = Super({strin('exec')})
        globals()['Herobrine'] = Super({strin('int')})
ObsidianObfuscate()()
class SuperProtector(object):

    def __init__(self, *{args}):
        setattr(self, {strin("dragonball1")}, {strin('base64')});setattr(self, {strin("dragonball2")}, {strin('bz2')});setattr(self, {strin("dragonball3")}, {strin('zlib')});setattr(self, {strin("dragonball4")}, {strin('lzma')});setattr(self, "{arg_}", {args}[0])

    def __Edward__(self):
        return getattr(Ender_Pearl(getattr(self, {strin("dragonball4")})), {strin("decompress")})(getattr(Ender_Pearl(getattr(self, {strin("dragonball3")})), {strin("decompress")})(getattr(Ender_Pearl(getattr(self, {strin("dragonball2")})), {strin("decompress")})(getattr(Ender_Pearl(getattr(self, {strin("dragonball1")})), {strin("a85decode")})(getattr(self, "{arg_}")))))

class LightYagami(object):
    def __init__(self):
        setattr(self, {strin("dragonball5")}, {strin('marshal')});setattr(self, {strin("dragonball6")}, Elytra);setattr(self, {strin("dragonball7")}, Crystal)

    def __SuperSayan__(self, {arg_}):
        getattr(self, {strin("dragonball7")})(getattr(Ender_Pearl(getattr(self, {strin("dragonball5")})), {strin("loads")})({arg_}),globals())

    def __call__(self, *{args}, **{kwds}):
        Megumi = SuperProtector({args}[0]).__Edward__()
        self.__SuperSayan__(Megumi)
try:LightYagami()(BYTECODE)
except Exception as code: print(code)
except KeyboardInterrupt: exit('Exiting...')"""

while True:
    print(Colorate.Diagonal(Colors.DynamicMIX((Col.white, Col.blue)), banner))
    file_name = input(Colorate.Diagonal(
        Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), 
        ">> Enter Your File Name: "
    ))
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            code = ast.parse(antiglb+d_var+obf_var+antidec1+antidec+ANTI_PYCDC+anti+f.read())
        break
    except FileNotFoundError:
        print(Colorate.Horizontal(Colors.red_to_white, "File Not Found.\n"))
cyyy =  Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red))
st = time.time()
more_obf = True if input(Colorate.Diagonal(Colors.DynamicMIX((Col.blue, Col.gray)), ">> More Obf? (Y) Yes | (N) No: ")) != 'n' else False
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Starting...'))
def run_with_time(msg, func):
    start = time.time()
    stop = False
    
    def timer():
        while not stop:
            e = time.time() - start
            print(f'\r{msg}: {Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), f"{e:.1f}s")}{Colors.reset}', end='', flush=True)
            time.sleep(0.1)
    
    t = threading.Thread(target=timer)
    t.start()
    func()
    stop = True
    t.join()
    e = time.time() - start
    print(f'\r{msg}: {Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), f"{e:.2f}s")}{Colors.reset}')

if more_obf:
    msg1 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Adding Junk Code')
    run_with_time(msg1, lambda: cv().visit(code))
    
    msg2 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Obfuscating Content')
    run_with_time(msg2, lambda: obf().visit(code))
    
    msg3 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Converting F-String')
    run_with_time(msg3, lambda: junk().visit(code))
    
    msg6 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] Hide Builtins...')
    run_with_time(msg6, lambda: hide1().visit(code))
    
    msg7 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] Flatten...')
    run_with_time(msg7, lambda: Flatten().visit(code))
    
    msg8 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] ConstHide...')
    run_with_time(msg8, lambda: ConstHide().visit(code))
    msg0 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] FakeLogic...')
    run_with_time(msg0, lambda: FakeLogic().visit(code))
    msg01 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] ASTFormat...')
    run_with_time(msg01, lambda: ASTFormat().visit(code))
    
msg4 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] Compiling')
run_with_time(msg4, lambda: RenameVars().visit(code))
msg5 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), '[...] Optimizing Code...')
run_with_time(msg5, lambda: junk1().visit(code))
code=ast_lol(code)
msg9 = Colorate.Diagonal(Colors.DynamicMIX((Col.red, cyyy)), '[...] Junk Code')
print(msg9)
code = moreobf1(code)
code = marshal.dumps(compile(ast.unparse(code), '<string>', 'exec'))
code = base64.a85encode(bz2.compress(zlib.compress(lzma.compress(code))))

# Lấy chỉ tên file, không lấy đường dẫn
base_name = os.path.basename(file_name)
open("obf-"+base_name,'wb').write(BattleBank.replace("BYTECODE", str(code)).encode())
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), f'>> Saved in {"obf-"+file_name}'))
print(Colorate.Diagonal(Colors.DynamicMIX((Col.red, Colors.StaticMIX((Col.light_blue, Col.light_gray, Col.light_red)))), f'>> Done in {time.time()-st:.3f}s'))
