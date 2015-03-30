from parse import make_copy, parse


data = [
    'cz.txt',
    'da.txt',
    'de.txt',
    'es.txt',
    'fi.txt',
    'fr.txt',
    'it.txt',
    'nl.txt',
    'pl.txt',
    'ru.txt',
    'sv.txt',
]

for source in data:
    full = 'full_file_' + source
    make_copy(source, full, add_english=True, remove_same=False)
    # make_copy(full, source, add_english=False, remove_same=True)
