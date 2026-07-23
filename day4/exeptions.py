def functionName(level):
    if level < 1:
        raise Exception("Invalid level! %s" % level)
    else:
        print(">")

functionName(5)
functionName(0)
