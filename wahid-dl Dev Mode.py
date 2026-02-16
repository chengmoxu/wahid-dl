try:
    from packages.function import wahiddl_devmode
    wahiddl_devmode.devmode()
except:
    print ("不支援的平台或wahid-dl安裝不完整")
input()