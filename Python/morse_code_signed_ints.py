import pdb

class Morse:
    @staticmethod
    def toint(string):
        # Requires a signed int as the output and python doesn't support that out of the box
        if string[0] == '1':
            #negative
            string = ''.join('1' if char == '0' else '0' for char in string)
            return(-(int(string, 2) + 1))
        else:
            return int(string, 2)
    @staticmethod
    def tobin(value):
        # Convert signed int signed binary
        if value < 0:
            # Convert to 32 bit signed binary
            binary = '{0:b}'.format(value)[1:].zfill(32)
            # Flip bits
            signed_binary = ''.join('1' if bit == '0' else '0' for bit in binary)
            # Add one have to do this manually since python doesn't support out of box
            for index in range(len(signed_binary)-1,-1,-1):
                if signed_binary[index] == '1':
                    # Flip bit and carry 1 over
                    signed_binary = signed_binary[:index] + '0' + signed_binary[index+1:]
                else:
                    # Flip bit, addition is done
                    signed_binary = signed_binary[:index] + '1' + signed_binary[index+1:]
                    break
            return signed_binary
        else:
            return '{0:032b}'.format(value)

    @classmethod
    def encode(cls,message):
        string = '000'.join([cls.alpha[char] for char in list(message)])
        if len(string) % 32 != 0:
            string += '0'*(32-len(string)%32)
        return [cls.toint(string[index:index+32]) for index in range(0, len(string), 32)]

    @classmethod
    def decode(cls,array):
        # instantiate beta object if not already done
        if cls.beta is None:
            cls.beta = {cls.alpha[key]: key for key in cls.alpha.keys()}
        #convert array into binary representation
        binary = ''.join(cls.tobin(value) for value in array)
        #Strip all following 0s since they don't represent anything useful in morse code
        morse_code = binary.rstrip('0')
        # Replace seven 0s with a space
        morse_code = morse_code.replace('0000000', '000 000')
        return ''.join(cls.beta[code] if code != ' ' else ' ' for code in morse_code.split('000'))

    alpha={
    'A': '10111',
    'B': '111010101',
    'C': '11101011101',
    'D': '1110101',
    'E': '1',
    'F': '101011101',
    'G': '111011101',
    'H': '1010101',
    'I': '101',
    'J': '1011101110111',
    'K': '111010111',
    'L': '101110101',
    'M': '1110111',
    'N': '11101',
    'O': '11101110111',
    'P': '10111011101',
    'Q': '1110111010111',
    'R': '1011101',
    'S': '10101',
    'T': '111',
    'U': '1010111',
    'V': '101010111',
    'W': '101110111',
    'X': '11101010111',
    'Y': '1110101110111',
    'Z': '11101110101',
    '0': '1110111011101110111',
    '1': '10111011101110111',
    '2': '101011101110111',
    '3': '1010101110111',
    '4': '10101010111',
    '5': '101010101',
    '6': '11101010101',
    '7': '1110111010101',
    '8': '111011101110101',
    '9': '11101110111011101',
    '.': '10111010111010111',
    ',': '1110111010101110111',
    '?': '101011101110101',
    "'": '1011101110111011101',
    '!': '1110101110101110111',
    '/': '1110101011101',
    '(': '111010111011101',
    ')': '1110101110111010111',
    '&': '10111010101',
    ':': '11101110111010101',
    ';': '11101011101011101',
    '=': '1110101010111',
    '+': '1011101011101',
    '-': '111010101010111',
    '_': '10101110111010111',
    '"': '101110101011101',
    '$': '10101011101010111',
    '@': '10111011101011101',
    ' ': '0'}

    beta = None

if __name__ == '__main__':
    print(Morse.encode('HELLO WORLD'))
    print(Morse.decode([-1440552402, -1547992901, -1896993141, -1461059584]))
    print(Morse.encode('EEEEEEEIE'))
    print(Morse.decode([-2004318070,536870912]))
    # Edge case doesn't work
    pdb.set_trace()
    print(Morse.decode([-2147483648]))
    # Edge case doesn't work
