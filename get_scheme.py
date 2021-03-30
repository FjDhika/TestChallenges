def get_scheme(html):
    arr = html.translate({ord(i):' ' for i in '</>'})
    arr = arr.split()
    result = []
    for i in arr:
        if '-' in i:
            scheme = i.split('-')
            result.append(scheme[1])
    return result
