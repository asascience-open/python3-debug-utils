# python3-debug-utils
Debugging utility modules for Python 3 code.

## Installing
```bash
pip install git+https://github.com/asascience-open/python3-debug-utils@v1.0.0#egg=python3-debug-utils
```
## Provides
The following modules are provided:

### `funcinternals`

Provides deep introspection of function internal state at runtime; dumps to log file or terminal.
Supports displaying images in-line on supported frame-buffer terminals like iTerm2 and xterm.

Basic import:
```python
from funcinternals.txt import debug_text as dbg
```
For the ability to display PIL image objects in a supported terminal, you should:
```bash
pip install -r funcinternals/img/requirements.txt
```
then:
```python
from funcinternals.img import debug_visual as dbg
```
#### Using `funcinternals`
After importing as above, you can use the library as follows.
To inspect the state of one object, pass its name as a string:
```python
def my_func():
    lst = [1, 2, 3, 4]

    dct = {
        "foo": "bar",
        "baz": "qux",
        "list": lst
    }
    dbg.debug('dct')  # like this
    var = "http://example.com"

    return
```
Which, when placed in a file called `test.py` and called, will print:
```sh
-------------------------------------------------- ( debug called from: my_func @ test.py:11 ) --------------------------------------------------

<class 'dict'>
dct =
baz: qux
foo: bar
list: [1, 2, 3, 4]
```

Or to inspect the state of all function locals at a given point, do:
```python
def my_func():
    lst = [1, 2, 3, 4]

    dct = {
        "foo": "bar",
        "baz": "qux",
        "list": lst
    }
    var = "http://example.com"

    dbg.inspect()  # like this
    return
```
Which similarly will print:
```sh
-------------------------------------------------- ( debug called from: my_func @ test.py:14 ) --------------------------------------------------

<class 'list'>
lst = [1, 2, 3, 4]

-------------------------------------------------- ( debug called from: my_func @ test.py:14 ) --------------------------------------------------

<class 'dict'>
dct =
baz: qux
foo: bar
list: [1, 2, 3, 4]

-------------------------------------------------- ( debug called from: my_func @ test.py:14 ) --------------------------------------------------

<class 'str'>
var = 'http://example.com'
```
