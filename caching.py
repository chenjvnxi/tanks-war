def caching_fps(fps,settings):
    with open(file=settings.INI_FILE,mode="w",encoding="utf-8") as j_file:
        j_file.write(f"[fps]\n{fps}")