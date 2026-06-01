try:
    from packages.function import wahiddl_tool
    wahiddl_tool.main() #from packages.function import the 'wahiddl_tool' and execute its function main()
except:
    print("執行終止：經使用者終止，或為不支援的平台、wahid-dl安裝不完整或程式發生問題")