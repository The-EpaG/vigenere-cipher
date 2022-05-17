from typing import Any
from pylib.file import FileUtils, FileIO
from pylib.crypt import VigenereCipher

def onError(error:str):
    print(error)

def readFile(fileName:str) -> bytes:
    def onFileRead(payload:bytes) -> bytes:
        return payload

    def onOpenFileToRead(file:FileIO) -> bytes:
        return FileUtils.readfile(
            file=file,
            onDone=onFileRead,
            onError=onError,
        )
    
    return FileUtils.openfile(
        filename=fileName,
        onDone=onOpenFileToRead,
        onError=onError,
    )

def writeFile(filename:str, payload:bytes) -> int:
    def onFileWrite(byteWrited:int) -> int:
        return byteWrited

    def onOpenFileToWrite(file:FileIO) -> int:
        return FileUtils.writefile(
            file=file,
            payload=payload,
            onDone=onFileWrite,
            onError=onError,
        )

    return FileUtils.openfile(
        filename=filename,
        onDone= onOpenFileToWrite,
        onError=onError,
        mode='wb',
    )

def encode(plain:bytes, key:bytes):
    def onEncode(payload:bytes):
        return payload

    key = VigenereCipher.createKey(plain, key)

    return VigenereCipher.encode(
        plain=plain,
        key=key,
        onDone=onEncode,
        onError=onError,
    )

def decode(encoded:bytes, key:bytes):
    def onDecode(payload:bytes):
        return payload

    key = VigenereCipher.createKey(plain, key)

    return VigenereCipher.decode(
        encoded=encoded,
        key=key,
        onDone=onDecode,
        onError=onError,
    )

if __name__ == '__main__':
    # Key
    key:bytes = readFile('example/key.png')

    # Plain
    fileName = 'example/plain.png'
    plain:bytes = readFile(fileName)

    # Encode
    encoded:bytes = encode(
        plain=plain,
        key=key
    )

    # Save
    writeFile(
        filename=fileName + '.vgn',
        payload=encoded,
    )

    # Decode
    decoded:bytes = decode(
        encoded=encoded,
        key=key,
    )

    # Save
    writeFile(
        filename=fileName.replace('plain','out'),
        payload=decoded,
    )