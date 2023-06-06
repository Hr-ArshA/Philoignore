import os
import io
import re
import sys
import argparse

from Philoignore import __version__
from Philoignore.constants.informations import VERSION_INFO, APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION, INSTALLATION_GUIDE
from rich.console import Console
from importlib import resources
from pathlib import Path

parser = argparse.ArgumentParser(
    description=APPLICATION_DESCRIPTION + '\n\r\n\r' + INSTALLATION_GUIDE,
    epilog=EPILOG_DESCRIPTION,
    formatter_class=argparse.RawDescriptionHelpFormatter,
)

parser.add_argument(
    'entry',
    nargs='*',
    help='Technologies that you want the related files to be ignored',

)

parser.add_argument(
    '--version',
    action='version',
    version=VERSION_INFO.format(__version__),
)

parser.add_argument(
    '-o',
    '--output',
    type=str,
    help='The path where you want the output to be saved',
    metavar='',
)

def main():
    args = parser.parse_args()
    console = Console()

    if args:
        with console.status('Creating'):
            entry = args.entry
            list_of_all = list()
            main_text = "# Created by PhiloLearn\n\n"
            exist_list = list()
            with resources.open_text("Philoignore", 'files.txt') as file:
                this_file = file.read()
                list_of_all = this_file.split('\n')

            for e in entry:
                for i in list_of_all:
                    if re.findall(f'^{e}\..+', i) != []:
                        exist_list.append(re.findall(f'^{e}\..+', i)[0])


            for i in exist_list:
                with resources.open_text("Philoignore.templates", f'{i}') as f:
                    name_list = str(i).split('.')[:-1]
                    name = ('.').join(name_list)
                    
                    main_text += f"### {name.upper()} ###\n\n"
                    main_text += f.read()
                    main_text += "\n"


            if args.output:
                path = args.output
                with open(f'{args.output}/.gitignore', 'w') as file:
                    file.write(main_text)
            
            else:
                path = Path().cwd()
                with open(f'{path}/.gitignore', 'w') as file:
                    file.write(main_text)
                
            console.print(f'[bold yellow]gitignore[/] for {args.entry} was [bold yellow]created[/] in {path}!')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())