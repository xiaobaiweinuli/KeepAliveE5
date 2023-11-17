import os
from concurrent.futures import ThreadPoolExecutor

CONFIG_PATH = "./config"


def multip_accounts_task(fn):
    configs = []
    try:
        configs.extend(
            os.path.join(CONFIG_PATH, path) for path in os.listdir(CONFIG_PATH)
        )
    except Exception:
        pass

    if not configs:
        print("找不到設定檔案 請先進行註冊")
        exit(1)

    futures, pool = [], ThreadPoolExecutor(len(configs))
    futures.extend(pool.submit(fn, config) for config in configs)
    for future in futures:
        print(f'{future.result()}')
