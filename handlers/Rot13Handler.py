from Handler import Handler


class Rot13Handler(Handler):
    def do_rot13(self, text):
        upper_a_ascii = 65
        upper_z_ascii = 90
        lower_a_ascii = 97
        lower_z_ascii = 122
        output = ""

        for c in text:
            c = ord(c)

            if upper_a_ascii <= c <= upper_z_ascii:
                c += 13
                if c > upper_z_ascii:
                    c += upper_a_ascii - upper_z_ascii - 1
            elif lower_a_ascii <= c <= lower_z_ascii:
                c += 13
                if c > lower_z_ascii:
                    c += lower_a_ascii - lower_z_ascii - 1

            output += chr(c)

        return output
