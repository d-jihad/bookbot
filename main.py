def gen_report(file: str) -> (int, dict[str, int]):
    words = file.lower().split()

    char_count = {}
    for c in ''.join(words):
        if c.isalpha():
            if c in char_count:
                char_count[c] += 1
            else:
                char_count[c] = 1

    char_count = sorted(char_count.items(), reverse=True, key=lambda x: x[1])
    return len(words), char_count


def write_report(filepath: str, words_count: int, char_count: dict[str, int]):
    print(f'--- Begin report of {filepath} ---')
    print(f'{words_count} words found in the document\n')

    for c, count in char_count:
        print(f'The {c} character was found {count} times')

    print('--- End report ---')


def main(argv: list[str]) -> int:
    filepath = argv[0]

    with open(filepath) as f:
        file_content = f.read()
        w_count, c_count = gen_report(file_content)
        write_report(filepath, w_count, c_count)

    return 0


if __name__ == '__main__':
    import sys

    sys.exit(main(sys.argv[1:]))
