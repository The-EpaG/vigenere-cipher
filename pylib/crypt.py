from typing import Any, Callable


class VigenereCipher:
    @staticmethod
    def createKey(
        plainFile:bytes,
        keyFile:bytes,
    ) -> bytes:
        key:bytes = b''

        for i in range(len(plainFile)):
            key = b''.join([key, bytes([keyFile[i%len(keyFile)]])])
        return key
    
    @staticmethod
    def encode(
        plain:bytes,
        key:bytes,
        onDone:Callable[[bytes], Any] | None = None,
        onError:Callable[[str], None] | None = None,
    ) -> Any:
        if len(plain) != len(key): return onError('This is not a right key')

        encoded:bytes = b''
        for i in range(len(plain)):
            encoded = b''.join([encoded, bytes([(plain[i] + key[i]) % 256])])
            
        return onDone(encoded)

    @staticmethod
    def decode(
        encoded:bytes,
        key:bytes,
        onDone:Callable[[bytes], Any] | None = None,
        onError:Callable[[str], None] | None = None,
    ) -> Any:
        if len(encoded) != len(key): return onError('This is not a right key')

        plain:bytes = b''
        for i in range(len(encoded)):
            plain = b''.join([plain, bytes([(encoded[i] + (256 - key[i])) % 256])])
            
        return onDone(plain)
