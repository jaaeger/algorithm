class Solution:
    def encode(self, strings):
        delimeter = "|"
        string = ""
        for word in strings:
            string += "{count}{delimeter}{word}".format(
                count=len(word), delimeter=delimeter, word=word
            )
        return string

    def decode(self, string):
        delimeter = "|"
        result = []
        last_char_pos = 0
        string_len = len(string)
        while last_char_pos < string_len:
            num_pos = last_char_pos
            while string[num_pos] != delimeter:
                num_pos += 1
            word_len = int(string[last_char_pos:num_pos])
            word_start = num_pos+1
            word_end = word_start + word_len
            word = string[word_start:word_end]

            result.append(word)
            last_char_pos = word_end

        return result