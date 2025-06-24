## Quick Access to Configs

You can directly access the latest configurations through this URL:
```
https://raw.githubusercontent.com/ed98mi/fetcher/refs/heads/main/configs/proxy_configs.txt
```
This project features advanced capabilities for proxy configuration management. The retrieved configurations are automatically converted to Sing-box format and stored in a separate JSON file. For each server, its geographical location is identified using the get location method, and the corresponding flag emoji and country name are automatically added to its tag. These features make proxy management and usage significantly more user-friendly and efficient.

Sing-box subscription link:
```
https://raw.githubusercontent.com/ed98mi/fetcher/refs/heads/main/configs/singbox_configs.json
```

## Channel and URL Performance

Below is the real-time performance statistics of the configured sources (Telegram channels and other URLs). This chart is automatically updated every hour.

### Quick Overview
<div align="center">
  <a href="assets/channel_stats_chart.svg">
    <img src="assets/channel_stats_chart.svg" alt="Source Performance Statistics" width="800">
  </a>
</div>

### Detailed Report
📊 [View Full Interactive Dashboard](https://htmlpreview.github.io/?https://github.com/ed98mi/fetcher/blob/main/assets/performance_report.html)

Each source is scored based on four key metrics:
- **Reliability Score (35%)**: Success rate in fetching and updating configurations.
- **Config Quality (25%)**: Ratio of valid configs to total fetched configurations.
- **Config Uniqueness (25%)**: Percentage of unique configs contributed.
- **Response Time (15%)**: Server response time and availability.

The overall score is calculated in real-time and updated hourly. Sources scoring below 30% are automatically disabled.

## Setup

1. Fork this repository.
2. Edit `src/config.py` and add your Telegram channels, SSCONF links or other URLs to the `SOURCE_URLS` list.
3. Enable GitHub Actions in your forked repository.
4. The configs will be automatically updated every hour in `configs/proxy_configs.txt`.

## Manual Setup

```bash
# Clone the repository
git clone https://github.com/4n0nymou3/multi-proxy-config-fetcher.git
cd multi-proxy-config-fetcher

# Install dependencies
pip install -r requirements.txt

# Run manually
python src/fetch_configs.py
```

## Configuration

Edit `src/config.py` to modify:
- Source list (Telegram channels, SSCONF links or URLs)
- Minimum/maximum configs per protocol
- Protocol ratios and balancing
- Maximum config age
- Output file location
- Supported protocols
- Request headers and timeouts

## Note for Forked Repositories

If you fork this repository, you need to manually enable GitHub Actions:
1. Go to `Settings > Actions` in your forked repository.
2. Select **Allow all actions and reusable workflows**.
3. Save the settings.

## Source Statistics

The project tracks comprehensive performance metrics of each source in `configs/channel_stats.json`:
- Overall performance score (0-100%)
- Success rate in fetching configurations
- Valid vs total configs ratio
- Unique config contribution
- Response time and reliability
- Source health status
