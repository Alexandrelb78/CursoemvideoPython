import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print ('O SITE PUDIM NÃO ESTÁ ACESSÍVEL NO MOMENTO')
else:
    print ('CONSEQUI ACESSAR O SITE OCM SUCESSO!!!')