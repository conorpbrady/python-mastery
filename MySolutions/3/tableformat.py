

def print_table(obj_list, headers):
    columns = len(headers)
    header_lines = ['---------']
    format_string = '%10s '

    print(format_string * columns % tuple(headers))
    print(format_string * columns % tuple(header_lines * columns))
    for obj in obj_list:
        record = []
        format_spec = ''
        for header in headers:
            attr = getattr(obj, header)
            format_spec += '%10'
            if isinstance(attr, str):
                format_spec += 's'
            elif isinstance(attr, int):
                format_spec += 'd'
            elif isinstance(attr, float):
                format_spec += '.2f'
            format_spec += ' '
            record.append(getattr(obj, header))
        print(format_spec % tuple(record))
