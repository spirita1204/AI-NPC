from django.apps import AppConfig
import asyncio
from .mcp import main

class McpAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mcp_app'

    def ready(self):    
        # 當應用啟動時，自動執行 MCP 客戶端初始化
        self.run_mcp_client_on_startup()

    def run_mcp_client_on_startup(self):
        """在Django啟動時，執行 MCP 客戶端的邏輯"""
        asyncio.run(main())
