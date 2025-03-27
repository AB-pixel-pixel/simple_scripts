#!/bin/bash

MAX_RETRIES=20
RETRY_COUNT=0

while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
    echo "尝试第 $((RETRY_COUNT + 1)) 次下载..."
    ollama pull llama3.1:70b
    EXIT_CODE=$?

    if [ $EXIT_CODE -eq 0 ]; then
        echo "下载成功！"
        exit 0
    else
        echo "下载失败，错误代码: $EXIT_CODE"
        ((RETRY_COUNT++))
        echo "剩余重试次数: $((MAX_RETRIES - RETRY_COUNT))"
        
        # 等待一段时间再重试，防止频繁请求
        sleep 5
    fi
done

echo "超过最大重试次数，下载失败。"
exit 1