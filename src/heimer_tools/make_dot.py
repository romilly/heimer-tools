import sys

from heimer_tools.convert import convert


def main():
    if 3 != len(sys.argv):
        print('usage localise_assets <alz-file> <dot-file>')
        sys.exit(1)
    alz_file = sys.argv[1]
    dot_file = sys.argv[2]
    print('converting %s to %s' % (alz_file, dot_file))
    dot_data = convert(alz_file)
    with open(dot_file, 'w') as dotf:
        dotf.write(dot_data)

if __name__ == '__main__':
    main()
