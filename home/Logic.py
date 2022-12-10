import os


def RuTextToSlug(url):
    en = {
        'а': 'a', 'б': 'b', 'в': 'v',
        'г': 'g', 'д': 'd', 'е': 'e',
        'ё': 'e', 'ж': 'j', 'з': 'z',
        'и': 'i', 'й': 'i', 'к': 'k',
        'л': 'l', 'м': 'm', 'н': 'n',
        'о': 'o', 'п': 'p', 'р': 'r',
        'с': 's', 'т': 't', 'у': 'u',
        'ф': 'f', 'х': 'x', 'ц': 'c',
        'ч': 'ch', 'ш': 'sh', 'щ': 'sh',
        'ъ': '', 'ы': '', 'ь': '',
        'э': 'a', 'ю': 'u', 'я': 'a',
        "-": "-", "_": "-"
    }
    slug = ""
    url = url.replace(" ", "_").lower().replace("'", "").replace('"', '')


    for symbol in url:
        slug += en[symbol] if symbol in en else symbol
    return slug


def path_and_rename(instance, filename):
    slug = RuTextToSlug(instance.title)
    upload_to = 'preview_photo/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.pk:
        filename = '{}_{}.{}'.format(slug, instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(slug, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
