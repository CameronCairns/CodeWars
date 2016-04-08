def decodeBits(bits):
	# find timeunit by finding shortest repeat of 0 or 1
    # first convert repeat sequences of 0 into a number representing
    # that sequence length.
    # Remove leading and terminal 0s as they are meaningless
    bits = bits.strip('0')
    zero_bitstring = bits.replace('1', ' ')
    one_bitstring = bits.replace('0', ' ')
    # test sequence isn't all 1s
    for length in range(len(bits), 0, -1):
      # attempt to replace a string entirely made of 0s down to a string made of one 0
      zero_bitstring = zero_bitstring.replace('0'*length, str(length))
    for length in range(len(bits), 0, -1):
      # attempt to replace a string entirely made of 0s down to a string made of one 0
      one_bitstring = one_bitstring.replace('1'*length, str(length))
    time_unit = min([int(length) for length in zero_bitstring.split() if length != ''] +
    				[int(length) for length in one_bitstring.split() if length != ''])
    # Now that we know the time unit, decode the message
    return bits.replace('1'*3*time_unit, '-').replace('1'*time_unit, '.').replace(
    	'0'*7*time_unit, '   ').replace('0'*3*time_unit, ' ').replace('0'*time_unit, '')

def decodeMorse(morseCode):
    return ''.join([MORSE_CODE[code]
	               if code != '|'
    	           else code
        	       for code
            	   in morseCode.replace('   ', ' | ').split()]).replace('|', ' ')
