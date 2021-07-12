import config

if config.serializer == 'json':
    FILENAME = f'{config.filename}.json'
    file_access_mode = 't'
    from .json_ import FileError
    from .json_ import load
    from .json_ import dump
elif config.serializer == 'pickle':
    FILENAME = f'{config.filename}.pickle'
    file_access_mode = 'b'
    from .pickle_ import FileError
    from .pickle_ import load
    from .pickle_ import dump
elif config.serializer == 'csv':
    FILENAME = f'{config.filename}.csv'
    file_access_mode = 't'
    from .csv_ import FileError
    from .csv_ import load
    from .csv_ import dump
else:
    raise ImportError