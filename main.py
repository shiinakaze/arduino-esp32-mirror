import requests

def fetch_and_replace_urls():
    # 定义目标 URL 和替换规则
    url = "https://espressif.github.io/arduino-esp32/package_esp32_index.json"
    original = "https://github.com"
    replacement = "https://gh-proxy.com/github.com"
    output_file = "package_esp32_index.json"

    try:
        # 发送 HTTP 请求获取文件内容
        response = requests.get(url)
        response.raise_for_status()  # 检查 HTTP 错误

        # 执行字符串替换
        modified_content = response.text.replace(original, replacement)

        # 将修改后的内容写入新文件
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(modified_content)

        print(f"The file was successfully processed and saved as {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Network request failed: {e}")
    except Exception as e:
        print(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    fetch_and_replace_urls()
