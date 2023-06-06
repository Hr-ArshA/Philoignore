import os
import re
import sys
import argparse

from Philoignore import __version__
from Philoignore.constants.informations import VERSION_INFO, APPLICATION_DESCRIPTION, EPILOG_DESCRIPTION, INSTALLATION_GUIDE
from rich.console import Console

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
            entry = str(args.entry[0]).split()
            list_of_all = list()
            main_text = "# Created by PhiloLearn\n\n"
            exist_list = list()
            with open('files.txt', 'r') as file:
                this_file = file.read()
                list_of_all = this_file.split('\n')

            for e in entry:
                for i in list_of_all:
                    new_e = e[0].upper() + e[1:]
                    if re.findall(f'^{e}\..+', i) != []:
                        exist_list.append(re.findall(f'^{e}\..+', i)[0])
                    
                    elif re.findall(f'^{new_e}\..+', i) != []:
                        exist_list.append(re.findall(f'^{new_e}\..+', i)[0])
            

            for i in exist_list:
                with open(f'templates/{i}') as f:
                    name_list = str(i).split('.')[:-1]
                    name = ('.').join(name_list)
                    main_text += f"\t### {name.upper()} ###\n\n"
                    main_text += f.read()

                    main_text += "\n"


            if args.output:
                path = args.output
                with open(f'{args.output}/.gitignore', 'w') as file:
                    file.write(main_text)
            
            else:
                path = os.getenv('HOME')
                try:
                    os.mkdir(f'{path}/Philoignore')
                except:
                    pass

                with open(f'{path}/Philoignore/.gitignore', 'w') as file:
                    file.write(main_text)

            print_list = list()
            for i in str(args.entry[0]).split():
                # print(i)
                print_list.append(f"[bold #01bc30]{i}[/]")
                
            console.print(f'[bold yellow]gitignore[/] for \[{(", ".join(print_list))}] was [bold yellow]created[/] in {path}!')
    
    return 0


if __name__ == '__main__':
    sys.exit(main())