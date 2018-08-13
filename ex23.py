import sys
script, encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()
    if line:  # checks whether the line has something in it.
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)
        # whoa whoa. What? So. It calls itself again after getting through one
        # line.
        # Why doesn't it read itself backwards?
        # I get why it doesn't run infinitely, but I don't get why it doesn't
        # run backwards. I guess because of the order it encounters the 
        # print statements is forwards. Like. It prints before it returns.
        # Returning goes "deeper", but that's not what we see. that's just
        # how we move the script to the next line.
        


def print_line(line, encoding, errors):
    next_lang = line.strip()  # wow, is this removing whitespace? OHH it's
    # removing the encoding of \n cuz of course that needs to be encoded.
    raw_bytes = next_lang.encode(encoding, errors=errors)
    # so we encode it into  utf-8
    cooked_string = raw_bytes.decode(encoding, errors=errors)
    # and then we decode THAT and we get the original text back.
    print(raw_bytes, "<===>", cooked_string)


languages = open("test.txt", encoding="utf-8")

main(languages, encoding, error)

'''
 a byte is 8 bits
 that's 00000001
 each of those is a bit
 bytes encode numbers (some are more than 8 bit)
 and numbers encode letters.

 ASCII is the American Standard Code for Information Interchange.
 Unicode is hopefully a "universal encoding" of all languages, not just
 english
 unicode is 32-bit.
 apparently, very common characters are actaully encoded in 8 bits, or 16
 if they're a bit less common. We really break out the 32-bit unicode when
 we need to do something relatively uncommon. Like.... accent marks?
 This is because we take up 32 whole bits per character in that case.
 That's 4 bytes! 32/8 = 4. That means that if it was all 32 bit, a thousand
 character text document would be 4000 bytes, which is 4kb, or .004Mb!
 what a catastrophe.

 UTF-8 Means Unicode Transformation Format 8 Bits.
 converts unicode to bytes, which are bits, which are electrical impulses.

 bytes are just numbers. You give them meaning by decoding them.
 Decode Bytes, Encode Strings. DBES. If you have bytes, and you need a string,
 decode it.
'''