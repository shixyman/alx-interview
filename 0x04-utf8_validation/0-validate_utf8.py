#!/usr/bin/python3


def validUTF8(data):
    Variable to keep track of the number
    of bytes remaining for the current character
    remaining_bytes = 0

    for byte in data:
        Check if the byte is a continuation byte (starts with '10')
        if byte >> 6 == 0b10:
            If there are no bytes remaining, or the byte
            is not a valid continuation byte, return False
            if remaining_bytes == 0:
                return False
            Decrement the count of remaining bytes
            remaining_bytes -= 1
        else:
            If there are remaining bytes, it means a new character
            has started before completing the previous one
            if remaining_bytes > 0:
                return False

            Determine the number of bytes for the current character
            if byte >> 7 == 0b0:
                Single-byte character
                remaining_bytes = 0
            elif byte >> 5 == 0b110:
                Two-byte character
                remaining_bytes = 1
            elif byte >> 4 == 0b1110:
                Three-byte character
                remaining_bytes = 2
            elif byte >> 3 == 0b11110:
                Four-byte character
                remaining_bytes = 3
            else:
                Invalid starting byte
                return False

    If there are remaining bytes, it means a character is not complete
    if remaining_bytes > 0:
        return False

    All checks passed, the data represents a valid UTF-8 encoding
    return True


# def validUTF8(data):
#     # Number of bytes in the current UTF-8 character
#     num_bytes = 0

#     for byte in data:
#         # Check the most significant bit (MSB) of the current byte
#         if num_bytes == 0:
#             # If the MSB is 0, it's a single-byte character
#             if (byte >> 7) == 0b0:
#                 continue
#             # If the MSB is 1, count the number of
#             # leading 1s to determine the number of bytes in the character
#             elif (byte >> 5) == 0b110:
#                 num_bytes = 1
#             elif (byte >> 4) == 0b1110:
#                 num_bytes = 2
#             elif (byte >> 3) == 0b11110:
#                 num_bytes = 3
#             else:
#                 return False
#         else:
#             # Check if the current byte starts with 10 (continuation byte)
#             if (byte >> 6) != 0b10:
#                 return False

#             num_bytes -= 1

#     # If there are remaining bytes, it's an invalid encoding
#     return num_bytes == 0
