try:
    from packages.function import wahiddl_audio
    wahiddl_audio.main()
except:
    print ("不支援的平台或wahid-dl安裝不完整")
input()