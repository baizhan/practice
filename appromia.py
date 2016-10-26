SUFFIXES={1000:['KB','MB','GB','TB','TB','PB','EB','ZB','YB'],
          1024:['KIB','MIB','GIB','TIB','PIB','EIB','ZIB','YIB']}
def approximate_size(size,a_kilobyte_is_1024_bytes=True):
    if size<0:
        raise ValueError('number must be non-negative')
    multiple=1024 if a_kilobyte_is_1024_bytes else 1000
    for suffix in SUFFIXES[multiple]:
        size=size/multiple
        if size<multiple:
            return '{0:.1f} {1}'.format(size,suffix)
    raise ValueError('number too large')
if __name__=='__main__':
    print(approximate_size(1000000000000000000000000000000,False))
    print(approximate_size(1000000000000))
