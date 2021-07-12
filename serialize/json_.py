import json
import functools

FileError = json.JSONDecodeError

load = json.load
dump = functools.partial(json.dump, indent=4)