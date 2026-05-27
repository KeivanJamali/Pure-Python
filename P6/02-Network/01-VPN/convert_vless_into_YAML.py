import urllib.parse
import yaml

CLASH_TEMPLATE = {
    "mode": "Global",
    "port": 7890,
    "proxies": [],
    "proxy-groups": [],
    "rules": []
}

def parse_vless_link(link: str):
    assert link.startswith("vless://")

    # Remove scheme
    body = link[len("vless://"):]
    
    # Split name
    if "#" in body:
        body, name = body.split("#", 1)
        name = urllib.parse.unquote(name)
    else:
        name = "VLESS"

    # Parse userinfo and query
    parsed = urllib.parse.urlparse("vless://" + body)

    uuid = parsed.username
    server = parsed.hostname
    port = parsed.port

    params = urllib.parse.parse_qs(parsed.query)

    # Helper to get single value
    def get(key, default=""):
        return params.get(key, [default])[0]

    proxy = {
        "name": name,
        "type": "vless",
        "server": server,
        "port": port,
        "uuid": uuid,
        "udp": True,
    }

    network = get("type", "tcp")
    proxy["network"] = network

    security = get("security", "")

    # ---- TLS / Reality ----
    if security in ("tls", "reality"):
        proxy["tls"] = True

    sni = get("sni")
    if sni:
        proxy["servername"] = sni

    fp = get("fp")
    if fp:
        proxy["client-fingerprint"] = fp

    flow = get("flow")
    if flow:
        proxy["flow"] = flow

    # ---- Reality specific ----
    if security == "reality":
        proxy["reality-opts"] = {
            "public-key": get("pbk"),
            "short-id": ""
        }

    # ---- WebSocket specific ----
    if network == "ws":
        ws_opts = {}

        path = get("path")
        if path:
            ws_opts["path"] = urllib.parse.unquote(path)

        host = get("host") or get("sni")
        if host:
            ws_opts["headers"] = {"Host": host}

        if ws_opts:
            proxy["ws-opts"] = ws_opts

    # Optional ip-version
    proxy.setdefault("tcp-opts", {})
    proxy["tcp-opts"]["ip-version"] = "dual"

    return proxy


def convert_vless_list(vless_links):
    clash = CLASH_TEMPLATE.copy()
    proxies = []

    for link in vless_links:
        link = link.strip()
        if not link:
            continue
        proxy = parse_vless_link(link)
        proxies.append(proxy)

    clash["proxies"] = proxies
    return clash


if __name__ == "__main__":
    # Example input: read from file
    folder_path = "/Users/keivanjamali/Projects/Pure-Python/P6/02-Network/01-VPN/"
    with open(folder_path + "vless.txt", "r", encoding="utf-8") as f:
        vless_links = f.readlines()

    clash_config = convert_vless_list(vless_links)

    with open(folder_path + "clash.yaml", "w", encoding="utf-8") as f:
        yaml.dump(clash_config, f, allow_unicode=True, sort_keys=False)

    print("Generated clash.yaml successfully.")
