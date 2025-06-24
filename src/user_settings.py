# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
    "https://raw.githubusercontent.com/valid7996/Gozargah/refs/heads/main/Gozargah_Sub",
    "https://raw.githubusercontent.com/soroushmirzaei/telegram-configs-collector/main/channels/protocols/hysteria",
    "https://raw.githubusercontent.com/10ium/V2Hub3/main/Split/Normal/vless",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mci/sub_4.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_1.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_2.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_3.txt",
    "https://raw.githubusercontent.com/mahsanet/MahsaFreeConfig/refs/heads/main/mtn/sub_4.txt",
    "https://raw.githubusercontent.com/kayhgng/v2raykayh/refs/heads/main/kayhgngcollectorv3v2ray_ss",
    "https://raw.githubusercontent.com/Aristaproject/AristaSub/refs/heads/main/Arista4.txt",
    "https://raw.githubusercontent.com/Aristaproject/AristaSub/refs/heads/main/Arista7.txt",
    "https://raw.githubusercontent.com/Aristaproject/AristaSub/refs/heads/main/Arista8.txt",
    "https://raw.githubusercontent.com/iPsycho1/ss-config-updater/refs/heads/main/configs.txt",
    "https://xb.inekokkk.com/amei/0c230a6f6a95c9a9d3cdada708c9b1cb",
    "https://raw.githubusercontent.com/10ium/HiN-VPN/refs/heads/main/subscription/normal/ss",
    "https://raw.githubusercontent.com/10ium/HiN-VPN/refs/heads/main/subscription/normal/vless",
    "https://raw.githubusercontent.com/10ium/V2rayCollectorLite/refs/heads/main/vless_iran.txt",
    "https://raw.githubusercontent.com/10ium/V2rayCollectorLite/refs/heads/main/ss_iran.txt",

    "https://t.me/s/v2rayfree",
    "https://t.me/s/PrivateVPNs",
    "https://t.me/s/meli_proxyy",
    "https://t.me/s/DirectVPN",
    "https://t.me/s/shadowproxy66",
    "https://t.me/s/outline_vpn",
    "https://t.me/s/lrnbymaa",
    "https://t.me/s/v2rayngn",
    "https://t.me/s/v2raying",
    "https://t.me/s/fastkanfig",
    "https://t.me/s/hope_net",
    "https://t.me/s/freeiranianv2rey",
    "https://t.me/s/noforcedheaven",
    "https://t.me/s/vpnstable",
    "https://t.me/s/orange_vpns",
    "https://t.me/s/isvvpn",
    "https://t.me/s/grizzlyvpn",
    "https://t.me/s/v2source",
    "https://t.me/s/arv2ray",
    "https://t.me/s/configfa",
    "https://t.me/s/xsfilternet",
    "https://t.me/s/wirevpnguard",
    "https://t.me/s/lonup_m",
    "https://t.me/s/v2ray_free_conf",
    "https://t.me/s/privatevpns",
    "https://t.me/s/ip_cf_config",
    "https://t.me/s/viproxys",
    "https://t.me/s/redfree8",
    "https://t.me/s/xrovpn",
    "https://t.me/s/viturey",
    "https://t.me/s/freedom_guard_net",
    "https://t.me/s/v2box_free",
    "https://t.me/s/vpnaloo",
    "https://t.me/s/slamvpn",
    "https://t.me/s/vpn_solve",
    "https://t.me/s/ahwazigamingshop",
    "https://t.me/s/v2ray_vpn_ir",
    "https://t.me/s/asrnovin_ir",
    "https://t.me/s/capoit",
    "https://t.me/s/conectvpn10",
    "https://t.me/s/ar14n24b",
    "https://t.me/s/xixv2ray",
    "https://t.me/s/movie10_oficial",
    "https://t.me/s/mbtiuniverse",
    "https://t.me/s/FreeV2rays",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 300

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": False,
    "ss://": True,
    "trojan://": False,
    "tuic://": False,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 2
