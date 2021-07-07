sample = "cvpbPGS{arkg_gvzr_V'yy_gel_2_ebhaqf_bs_ebg13_GYpXOHqX}"


def decrypt(sample: str):
    for x in sample:
        print(get_alpha_by_offset(x, 13), end="")


lower_alpha = []
capital_alpha = []
a_index = ord('a')
A_index = ord('A')
alpha_length = 26

for i in range(alpha_length):
    lower_alpha.append(i + a_index)
    capital_alpha.append(i + A_index)


def is_alpha(alpha: str) -> bool:
    if (ord(alpha) >= a_index and ord(alpha) < a_index + alpha_length) \
            or (ord(alpha) >= A_index and ord(alpha) < A_index + alpha_length):
        return True
    return False


def is_lower(alpha: str) -> bool:
    if ord(alpha) >= a_index and ord(alpha) < a_index + alpha_length:
        return True
    return False


def get_alpha_by_offset(alpha: str, offset: int) -> str:
    if len(alpha) > 1:
        return ""
    if not is_alpha(alpha):
        return alpha
    if is_lower(alpha):
        index = alpha2index_in_alphabet_table(alpha)
        decrypt_index = (index + offset) % alpha_length
        return int2alpha(decrypt_index + a_index)
    index = alpha2index_in_alphabet_table(alpha)
    decrypt_index = (index + offset) % alpha_length
    return int2alpha(decrypt_index + A_index)


def alpha2index_in_alphabet_table(alpha: str) -> int:
    index = ord(alpha)
    if index >= a_index and index < a_index + alpha_length:
        return index - a_index
    if index >= A_index and index <= A_index + alpha_length:
        return index - A_index
    return -1


def int2alpha(index: int) -> str:
    return chr(index)

decrypt(sample)
