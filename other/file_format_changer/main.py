import pyparsing as pp


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
    data = [[i.strip('"') for i in pp.commaSeparatedList.parseString(el.strip()).asList()] for el in data[2:]]
    data = [[i.replace('.', ',') if isfloat(i) else i for i in el] for el in data]

    with open(output_filename, 'wt', encoding='utf-8') as f:
        f.write(start_line+'\n')
        f.write('\t'.join(header)+'\n')
        for el in data:
            f.write('\t'.join(el))
            f.write('\n')


if __name__ == '__main__':
    reformat_file('NeedsToBeConverted.txt', 'Output.txt')
