encoded = """
   !!junk-77!! | [3::DW::ok] | [xx::DRSC::bad] |
   [1::NFFU::ok] | ##nothing## | [5::TQI_QNGWFWD::ok] |
   [2::OG::ok] | [4::XLI::ok] | [7::WT7::bad] |
   [6::GZ_7_VS::ok] | [99::IGNORE_ME::bad] | %%noise%%
"""

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

parts = encoded.split("|")
decoded_parts = []

for part in parts:
    part = part.strip()
    if not part.startswith("["):
        continue

    inside = part[1:-1]
    pieces = inside.split("::")

    if len(pieces) != 3:
        continue

    status = pieces[2]
    if status != "ok":
        continue

    num = int(pieces[0])
    text = pieces[1]

    decoded = ""
    for ch in text:
        if ch in alphabet:
            old_index = alphabet.index(ch)
            decoded = decoded + alphabet[old_index - num]
        else:
            decoded = decoded + ch

    # the underscore was used as a space in the hidden message
    decoded = decoded.replace("_", " ")

    decoded_parts.append((num, decoded))

decoded_parts.sort()

final_message = ""
for num, decoded in decoded_parts:
    final_message = final_message + decoded + " "

final_message = final_message.strip()
print(final_message)
