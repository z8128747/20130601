import logging

def test_log2():
    # 创建日志器
    logger=logging.getLogger('root')
    logger.setLevel(logging.INFO)
    # if not logging.StreamHandler():
        # # 需要控制台处理器
    sh=logging.StreamHandler()
    logger.addHandler(sh)
    # 创建格式器
    fmt='%(asctime)s %(filename)s %(funcName)s %(levelname)s %(message)s'
    fm=logging.Formatter(fmt)
    # # 保存在文件中 文件处理器
    sh.setFormatter(fm)

    fh=logging.FileHandler('log2.txt')
    logger.addHandler(fh)
    fh.setFormatter(fm)
    return logger

