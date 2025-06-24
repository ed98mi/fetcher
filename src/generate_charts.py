import json
import os
from datetime import datetime, timezone, timedelta

def to_persian_numerals(text):
    """
    Converts English numerals in a string to their Persian equivalent.
    It also handles floating-point numbers by converting the decimal point.
    """
    text = str(text)
    persian_numerals = '۰۱۲۳۴۵۶۷۸۹'
    english_numerals = '0123456789'
    
    # Use a unique placeholder for the decimal point to handle it separately
    text = text.replace('.', '[dot]')
    
    trans_table = str.maketrans(english_numerals, persian_numerals)
    persian_text = text.translate(trans_table)
    
    # Replace the placeholder with the standard Persian decimal separator
    return persian_text.replace('[dot]', '٫')


def format_persian_datetime(utc_iso_str):
    """
    Converts a UTC timestamp string in ISO format to a localized Persian 
    datetime string for the UTC+3:30 timezone.
    """
    # Return a default Persian string if the input is empty or not applicable
    if not utc_iso_str or utc_iso_str in ["N/A", "None"]:
        return "نامشخص" # "Unknown"

    try:
        # Standardize the UTC format by replacing 'Z'
        if utc_iso_str.endswith('Z'):
            utc_iso_str = utc_iso_str[:-1] + '+00:00'
        
        # Parse the ISO string into a datetime object
        dt_utc = datetime.fromisoformat(utc_iso_str)

        # If the parsed datetime is "naive" (has no timezone info), assume it's UTC
        if dt_utc.tzinfo is None:
            dt_utc = dt_utc.replace(tzinfo=timezone.utc)

        # Define the target timezone: UTC+3:30 (Iran Standard Time)
        iran_tz = timezone(timedelta(hours=3, minutes=30))

        # Convert the datetime object to the target timezone
        dt_iran = dt_utc.astimezone(iran_tz)

        # Format into a readable Persian string (YYYY/MM/DD Hour:Minute)
        formatted_time = dt_iran.strftime('%Y/%m/%d ساعت %H:%M')

        # Convert the numerical parts of the string to Persian numerals
        return to_persian_numerals(formatted_time)
    except (ValueError, TypeError):
        # Handle cases where the timestamp format is invalid
        return "فرمت نامعتبر" # "Invalid Format"

def generate_basic_svg(stats_data):
    width = 800
    height = len(stats_data['channels']) * 50 + 100
    
    svg = f'''<?xml version="1.0" encoding="UTF-8"?>
    <svg width="{width}" height="{height}" version="1.1" xmlns="http://www.w3.org/2000/svg">
    <style>
        .row {{ font: 14px Arial; fill: #64748b; }}
        .score {{ font: bold 14px Arial; fill: #64748b; }}
    </style>
    <text x="400" y="40" text-anchor="middle" font-size="20px" font-weight="bold" fill="#64748b">Channel Performance Overview</text>'''
    
    for idx, channel in enumerate(stats_data['channels']):
        y = 80 + (idx * 50)
        name = channel['url'].split('/')[-1]
        score = channel['metrics']['overall_score']
        success = (channel['metrics']['success_count'] / 
                  max(1, channel['metrics']['success_count'] + channel['metrics']['fail_count'])) * 100
        
        svg += f'<rect x="150" y="{y}" width="500" height="30" fill="#eee" rx="5"/>'
        
        width = min(500, 5 * score)
        color = '#22c55e' if score >= 70 else '#eab308' if score >= 50 else '#ef4444'
        svg += f'<rect x="150" y="{y}" width="{width}" height="30" fill="{color}" rx="5"/>'
        
        svg += f'''
        <text x="140" y="{y+20}" text-anchor="end" class="row">{name}</text>
        <text x="660" y="{y+20}" text-anchor="start" class="score">{score:.1f}% (S:{success:.0f}%)</text>'''
    
    svg += '</svg>'
    return svg

def generate_html_report(stats_data):
    """
    Generates a complete HTML report with all data localized into Persian.
    """
    # --- Pre-calculate statistics to keep the HTML string clean ---
    total_channels = len(stats_data.get('channels', []))
    active_channels = sum(1 for c in stats_data.get('channels', []) if c.get('enabled'))
    total_valid_configs = sum(c.get('metrics', {}).get('valid_configs', 0) for c in stats_data.get('channels', []))
    
    avg_success_rate = 0
    avg_response_time = 0
    if total_channels > 0:
        # Calculate average success rate
        total_success_rate_sum = sum(
            (c.get('metrics', {}).get('success_count', 0) / 
             max(1, c.get('metrics', {}).get('success_count', 0) + c.get('metrics', {}).get('fail_count', 0))) * 100 
            for c in stats_data.get('channels', [])
        )
        avg_success_rate = total_success_rate_sum / total_channels
        
        # Calculate average response time
        avg_response_time = sum(c.get('metrics', {}).get('avg_response_time', 0) for c in stats_data.get('channels', [])) / total_channels

    # Format the main timestamp for the report
    last_updated_persian = format_persian_datetime(stats_data.get('timestamp'))

    # --- Start building the HTML document ---
    # Added lang="fa" and dir="rtl" for proper Persian layout.
    # Added a Persian font (Vazirmatn) for better readability.
    html = f'''<!DOCTYPE html>
    <html lang="fa" dir="rtl">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>گزارش عملکرد کانال‌ها</title>
        <link href="https://cdnjs.cloudflare.com/ajax/libs/tailwindcss/2.2.19/tailwind.min.css" rel="stylesheet">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Vazirmatn:wght@400;700&display=swap');
            body {{ font-family: 'Vazirmatn', sans-serif; }}
        </style>
    </head>
    <body class="bg-gradient-to-br from-gray-50 to-gray-100 min-h-screen">
        <div class="max-w-7xl mx-auto p-4 sm:p-6 lg:p-8">
            <header class="bg-white rounded-lg shadow-lg p-6 mb-8">
                <h1 class="text-3xl font-bold text-gray-900 text-center">داشبورد عملکرد کانال‌های پروکسی</h1>
                <p class="text-center text-gray-600 mt-2">آخرین بروزرسانی: {last_updated_persian}</p>
            </header>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8 text-center">
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">کانال‌های فعال</h3>
                    <div class="text-3xl font-bold text-blue-600">
                        {to_persian_numerals(active_channels)}
                        <span class="text-sm font-normal text-gray-500">/ {to_persian_numerals(total_channels)}</span>
                    </div>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">مجموع کانفیگ‌های معتبر</h3>
                    <div class="text-3xl font-bold text-green-600">
                        {to_persian_numerals(total_valid_configs)}
                    </div>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">میانگین درصد موفقیت</h3>
                    <div class="text-3xl font-bold text-yellow-600">
                        %{to_persian_numerals(f"{avg_success_rate:.1f}")}
                    </div>
                </div>
                <div class="bg-white rounded-lg shadow-lg p-6">
                    <h3 class="text-lg font-semibold text-gray-700 mb-4">میانگین زمان پاسخ</h3>
                    <div class="text-3xl font-bold text-purple-600">
                        {to_persian_numerals(f"{avg_response_time:.2f}")} ثانیه
                    </div>
                </div>
            </div>

            <div class="bg-white rounded-lg shadow-lg p-6 mb-8">
                <h3 class="text-xl font-semibold text-gray-800 mb-6">آمار دقیق کانال‌ها</h3>
                <div class="overflow-x-auto">
                    <table class="min-w-full divide-y divide-gray-200">
                        <thead class="bg-gray-50">
                            <tr>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">کانال</th>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">وضعیت</th>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">امتیاز</th>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">درصد موفقیت</th>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">زمان پاسخ</th>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">معتبر/کل</th>
                                <th class="px-6 py-3 text-right text-xs font-medium text-gray-500 uppercase tracking-wider">آخرین موفقیت</th>
                            </tr>
                        </thead>
                        <tbody class="bg-white divide-y divide-gray-200">'''

    # Sort channels by overall score in descending order
    sorted_channels = sorted(stats_data.get('channels', []), key=lambda x: x.get('metrics', {}).get('overall_score', 0), reverse=True)
    
    for channel in sorted_channels:
        metrics = channel.get('metrics', {})
        success_count = metrics.get('success_count', 0)
        fail_count = metrics.get('fail_count', 0)
        overall_score = metrics.get('overall_score', 0)
        
        success_rate = (success_count / max(1, success_count + fail_count)) * 100
        
        status_color = 'green' if channel.get('enabled') else 'red'
        score_color = 'green' if overall_score >= 70 else 'yellow' if overall_score >= 50 else 'red'
        status_text = 'فعال' if channel.get('enabled') else 'غیرفعال' # Active/Inactive
        
        last_success_persian = format_persian_datetime(metrics.get('last_success'))

        html += f'''
                            <tr>
                                <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900" style="direction: ltr; text-align: left;">
                                    {channel.get('url', 'N/A').split('/')[-1]}
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-{status_color}-100 text-{status_color}-800">
                                        {status_text}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap">
                                    <span class="px-2 inline-flex text-xs leading-5 font-semibold rounded-full bg-{score_color}-100 text-{score_color}-800">
                                        %{to_persian_numerals(f"{overall_score:.1f}")}
                                    </span>
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    %{to_persian_numerals(f"{success_rate:.1f}")}
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {to_persian_numerals(f"{metrics.get('avg_response_time', 0):.2f}")} ثانیه
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {to_persian_numerals(metrics.get('valid_configs', 0))}/{to_persian_numerals(metrics.get('total_configs', 0))}
                                </td>
                                <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
                                    {last_success_persian}
                                </td>
                            </tr>'''

    html += '''
                        </tbody>
                    </table>
                </div>
            </div>
            <footer class="text-center text-gray-500 text-sm py-4">
                <p>ساخته شده با ❤️</p>
            </footer>
        </div>
    </body>
    </html>'''
    
    return html

def main():
    """
    Main function to read stats, generate the report, and save it to a file.
    """
    try:
        # Open the JSON file containing the statistics
        with open('configs/channel_stats.json', 'r', encoding='utf-8') as f:
            stats_data = json.load(f)
        
        # Ensure the output directory exists
        os.makedirs('assets', exist_ok=True)


        svg_content = generate_basic_svg(stats_data)
        with open('assets/channel_stats_chart.svg', 'w', encoding='utf-8') as f:
            f.write(svg_content)
    
        # Generate the HTML content
        html_content = generate_html_report(stats_data)
        
        # Write the generated HTML to a file
        with open('assets/performance_report.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("Successfully generated Persian performance report!")
        
    except FileNotFoundError:
        print("Error: 'configs/channel_stats.json' not found. Please ensure the file exists.")
    except json.JSONDecodeError:
        print("Error: Could not decode JSON from 'configs/channel_stats.json'. The file may be corrupt.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")

if __name__ == '__main__':
    main()
