"""
这是claude code帮我写的↓↓我一点也不会
自动把 Git 代理同步到当前 Windows 系统代理端口。
以后 git push 连不上就跑一下这个脚本。
"""
import subprocess
import winreg


def get_system_proxy():
    """从 Windows 注册表读取系统代理地址"""
    key = winreg.OpenKey(
        winreg.HKEY_CURRENT_USER,
        r"Software\Microsoft\Windows\CurrentVersion\Internet Settings",
    )
    enabled, _ = winreg.QueryValueEx(key, "ProxyEnable")
    if not enabled:
        return None
    server, _ = winreg.QueryValueEx(key, "ProxyServer")
    winreg.CloseKey(key)
    return server  # 比如 "127.0.0.1:18804"


def sync():
    proxy = get_system_proxy()
    if proxy is None:
        print("[X] 系统代理未开启，需要先打开代理软件")
        return

    url = f"http://{proxy}"
    subprocess.run(["git", "config", "--global", "http.proxy", url], check=True)
    subprocess.run(["git", "config", "--global", "https.proxy", url], check=True)
    print(f"[OK] Git 代理已同步到 {url}")


if __name__ == "__main__":
    sync()
