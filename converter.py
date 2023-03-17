"""
Temperature Converter - Command Line Solution
"""

import argparse

def converter(temp: float, unit: str, output: str) -> None:
    """
    Converts TEMP from UNIT to FORMAT

    Parameters
    ----------
    temp: float
    unit: str
    output: str
    """
    try:
        temp = float(temp)
    except ValueError as err:
        raise ValueError(f"Please enter a valid number -- {err}")

    unit = get_unit_input(unit)
    output = get_unit_input(output)

    temp = to_celsius(temp, unit)
    out = convert_temp(temp, output)
    print(out)
    return out


def get_unit_input(unit_input):
    unit_mapper = {'celsius': ['celsius', 'c', 'cel', 'cels'],
                   'fahrenheit': ['fahrenheit', 'f', 'fah', 'fahr'],
                   'kelvin': ['kelvin', 'k', 'kel', 'kelv']}

    if unit_input in unit_mapper['celsius']:
        unit = 'celsius'
    elif unit_input in unit_mapper['fahrenheit']:
        unit = 'fahrenheit'
    elif unit_input in unit_mapper['kelvin']:
        unit = 'kelvin'
    else:
        print('please enter a valid unit')
        return None
    return unit

def to_celsius(temp: float, unit) -> float:
    unit_mapper_input = {'celsius': lambda x: x,
                    'fahrenheit': lambda x: (x - 32) * 5/9,
                    'kelvin': lambda x: x - 273.15}

    return unit_mapper_input[unit](temp)

def convert_temp(temp: float, unit) -> float:
    unit_mapper_output = {'celsius': lambda x: x,
                   'fahrenheit': lambda x: (x * 9/5) + 32,
                   'kelvin': lambda x: x + 273.15}

    return unit_mapper_output[unit](temp)

def parser_command_line():
    parser = argparse.ArgumentParser(
        description= "Temperature Converter")
    parser.add_argument(
        '-u',
        '--unit',
        choices=['celsius', 'c', 'cel', 'cels', 'fahrenheit', 'f', 'fah', 'fahr', 'kelvin', 'k', 'kel', 'kelv'],
        default='celsius',
        help="input unit to convert"
    )
    parser.add_argument(
        '-o',
        '--output',
        choices=['celsius', 'c', 'cel', 'cels', 'fahrenheit', 'f', 'fah', 'fahr', 'kelvin', 'k', 'kel', 'kelv'],
        default='celsius',
        help="output unit to convert to"
    )
    parser.add_argument(
        'temp',
        help="temperature to be converted"
    )
    return parser

if __name__ == '__main__':
    parser = parser_command_line()
    args = parser.parse_args()

    # converter(50, 'c', 'f')
    converter(args.temp, args.unit, args.output)