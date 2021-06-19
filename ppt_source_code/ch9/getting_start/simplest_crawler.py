# -*- coding: utf-8 -*-

# simplest_crawler.py
import urllib.request as ur

# 利用urllib.request.urlopen()方法直接处理某个网页链接字符串
# crawl:['krɔlər]
link="https://www.doc88.com/p-771373021982.html"
print("begin to crawl..")
# set a variable:response to reference to the result of the ur.urlopen() ;the type is Any
response = ur.urlopen(link)
'''def urlopen(url: Union[str, Request],
            data: Optional[bytes] = ...,
            timeout: Optional[float] = ...,
            *,
            cafile: Optional[str] = ...,
            capath: Optional[str] = ...,
            cadefault: bool = ...,
            context: Optional[SSLContext] = ...) -> Any
    Open the URL url, which can be either a string or a Request object.

    data must be an object specifying additional data to be sent to the server, or None if no such data is needed. See Request for details.
    urllib.request module uses HTTP/1.1 and includes a "Connection:close" header in its HTTP requests.
    The optional timeout parameter specifies a timeout in seconds for blocking operations like the connection attempt (if not specified, the global default timeout setting will be used). This only works for HTTP, HTTPS and FTP connections.
    If context is specified, it must be a ssl.SSLContext instance describing the various SSL options. See HTTPSConnection for more details.
    The optional cafile and capath parameters specify a set of trusted CA certificates for HTTPS requests. cafile should point to a single file containing a bundle of CA certificates, whereas capath should point to a directory of hashed certificate files. More information can be found in ssl.SSLContext.load_verify_locations().
    The cadefault parameter is ignored.
    This function always returns an object which can work as a context manager and has the properties url, headers, and status. See urllib.response.addinfourl for more detail on these properties.
    For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse object slightly modified. In addition to the three new methods above, the msg attribute contains the same information as the reason attribute — the reason phrase returned by the server — instead of the response headers as it is specified in the documentation for HTTPResponse.
    For FTP, file, and data URLs and requests explicitly handled by legacy URLopener and FancyURLopener classes, this function returns a urllib.response.addinfourl object.
    Note that None may be returned if no handler handles the request (though the default installed global OpenerDirector uses UnknownHandler to ensure this never happens).
    In addition, if proxy settings are detected (for example, when a *_proxy environment variable like http_proxy is set), ProxyHandler is default installed and makes sure the requests are handled through the proxy.'''
print(response)
# use the read method to read the content of the response.
html = response.read().decode("gbk","ignore") #type Any
print("打印html内容：")
# print(html)
with open("doc.html","w") as fos:
    fos.write(str(html))

