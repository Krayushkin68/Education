def isfloat(number):
    try:
        float(number)
    except ValueError:
        return False
    return True


def replace_shwedish(text):
    # Need to specify right letters to replace
    sw_letters_dict = {'”': 'ö', '†': 'å', '„': 'ä', '™': 'Ö', 'Ћ': 'Ä', 'Џ': 'Å'}
    for old, new in sw_letters_dict.items():
        text = text.replace(old, new)
    return text


def reformat_file(input_filename, output_filename):
    with open(input_filename, 'rt', encoding='windows-1251') as f:
        data = f.read()

    # data = replace_shwedish(data)     # Can be enabled to replace incorrect letters
    data = data.splitlines()
    start_line = data[0]
    header = data[1].strip().split(',')

    data = data[2:]
    parsed_data = []
    for row in data:
        start_idx = 0
        row_elements = []
        while True:
            cur_idx = row.find(',', start_idx)
            if cur_idx != -1:
                if not row[start_idx:cur_idx].startswith('"'):
                    el = row[start_idx:cur_idx].strip('"')
                    el = el.replace('.', ',') if isfloat(el) else el
                    row_elements.append(el)
                    start_idx = cur_idx+1
                else:
                    quote_end_idx = row.find('",', start_idx)
                    el = row[start_idx+1:quote_end_idx].strip('"')
                    el = el.replace('.', ',') if isfloat(el) else el
                    row_elements.append(el)
                    start_idx = quote_end_idx+2
            else:
                el = row[start_idx:].strip('"')
                el = el.replace('.', ',') if isfloat(el) else el
                row_elements.append(el)
                break
        parsed_data.append(row_elements)

    with open(output_filename, 'wt', encoding='utf-8') as f:
        f.write(start_line+'\n')
        f.write('\t'.join(header)+'\n')
        for el in parsed_data:
            f.write('\t'.join(el)+'\n')


if __name__ == '__main__':
    reformat_file('From.txt', 'Output.txt')




