try:
    from packages.function import wahiddl_devmode
    wahiddl_devmode.devmode()
except:
    print("執行終止：經使用者終止，或為不支援的平台、wahid-dl安裝不完整或程式發生問題")