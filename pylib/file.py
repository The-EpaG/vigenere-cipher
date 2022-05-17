from io import FileIO
from typing import Any, Callable

class FileUtils:
    @staticmethod
    def openfile(
        filename:str,
        onDone:Callable[[FileIO], Any] | None = None,
        onError:Callable[[str], None] | None = None,
        mode:str='rb',
    ) -> Any:
        try: return onDone(open(filename, mode))
        except: onError('Can\'t open the file')
    
    @staticmethod
    def readfile(
        file:FileIO,
        onDone:Callable[[bytes], Any] | None = None,
        onError:Callable[[str], None] | None = None,
    ) -> Any:
        if not file.readable(): return onError('File not readable')

        try: return onDone(file.read())
        except: onError('Error while reading')
    
    staticmethod
    def writefile(
        file:FileIO,
        payload:bytes,
        onDone:Callable[[int], Any] | None = None,
        onError:Callable[[str], None] | None = None,
    ) -> Any:
        if not file.writable(): return onError('File not writable')

        try: return onDone(file.write(payload))
        except: onError('Error while writing')