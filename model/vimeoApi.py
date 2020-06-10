import vimeo

def vimeoFirst(a):
    client = vimeo.VimeoClient(
        token='1a028b267f6e92a4f90389b031d33b60',
        key='a591a007d8a09bc7fd57c50d325180224bdffa25',
        secret='4IWycSdPpr9m73k/5TTQF+WBUV631kUtK4EQETBVhzmweZXTiOZp7jYYSP3cEXrzSLfS2IrQh1lnVPevXvZPbyRJV3UKWYwfhzHr68nUHSHg+Srm3BvqOiPvc8gAjWH3'
    )
    res = client.get('/videos?query=cat')
    jsonData = res.json()
    return jsonData