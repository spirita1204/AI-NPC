# AI村民

✅ **專案構想**

- **設計 2D 地圖與物件**：定義每個地點（如牆壁、商店等）的座標系統。
- **NPC 行為與任務系統**：建立 NPC 狀態機，並根據時間或其他條件生成每日任務。
- **地圖交互與路徑規劃**：實現路徑尋路演算法，讓 NPC 能夠在地圖上自由移動。
- **聊天系統整合**：設計玩家與 NPC 之間的互動指令，讓玩家能夠直接控制 NPC。
- **測試與優化**：測試 NPC 行為的正確性和流暢度，優化移動和任務生成的邏輯。

---

✅ **專案技術**

### **1. 項目架構與後端技術**

| **後端** | **Django**：用於處理聊天系統、任務生成和管理 NPC 行為。 |
| --- | --- |
| **資料庫** | **SQLite** 或 **MySQL**：用於存儲 NPC 設定、任務腳本和 NPC 狀態。
**MongoDB**（如果需要更靈活的結構化數據）. |
| **API 與聊天系統** | • **GPT-3**（或 GPT-4）API：生成日常任務、進行對話、解析玩家指令並指派給 NPC。
• [**Socket.io**](http://socket.io/)：實現即時聊天功能，讓玩家可以與 NPC 互動。 |

---

**2. 人工智能與 NPC 行為控制**

| **狀態機** | **Finite State Machine (FSM)**：用於建模 NPC 的狀態與行為（如等待、移動、互動等）。
**Task Scheduler**：生成每日任務，並根據任務進行行為調度 |
| --- | --- |
| **NPC 任務生成** | **規則引擎**（如 **Drools** 或 **Prolog**）：根據設置的規則來生成任務（例如“早上去超市”）。
**隨機生成系統**：基於規則和時間生成動態任務，增強遊戲性 |

---

### **3. 人工聊天系統與指令解析**

| **自然語言處理 (NLP)** |  **GPT-3/4**：用於解析玩家指令，理解指令並生成合理的 NPC 行為。
**spaCy** 或 **NLTK**：用於文本處理，提取指令中的關鍵資訊（例如 NPC 名稱、地點）。 |
| --- | --- |
| **聊天引擎** | **Dialogflow**（Google）：用於構建聊天機器人，處理複雜的對話流和指令解析。
**Rasa**：開源對話式 AI 平台，可用於構建自定義聊天機器人。 |
| **用戶交互接口** | **Telegram Bot API** 或 **Discord Bot API**：用於在聊天平台中與玩家互動，接收指令並回應。 |

---

### **4. 前端技術與遊戲引擎**

| **遊戲引擎** | UnrealEngine：渲染 2D 地圖和物體，控制 NPC 行為。 |
| --- | --- |

---

✅ **專案進度**

[ To-Do](To-Do%201b0cfc67a80e81b58849e88014bba105.csv)

✅ 專案素材,圖示

UE素材: Paper ZD

- ✅ 資料表
    
    ### **1. NPC 資料表 (`npc`)**
    
    這個資料表記錄所有 NPC 的基本資訊。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | npc_id | INT | NPC 唯一識別 ID |
    | name | VARCHAR | NPC 名稱 |
    | description | TEXT | NPC 描述 |
    | current_task | INT | 當前任務 ID（指向 `tasks` 資料表） |
    | status | VARCHAR | NPC 狀態（例如：待命、移動中、執行任務） |
    | position_x | INT | NPC 在地圖上的 X 座標 |
    | position_y | INT | NPC 在地圖上的 Y 座標 |
    | last_active | DATETIME | 上次執行任務的時間 |
    
    ---
    
    ### **2. 任務資料表 (`tasks`)**
    
    這個資料表記錄所有可分配的任務，包括每日任務和隨機任務。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | task_id | INT | 任務唯一識別 ID |
    | task_name | VARCHAR | 任務名稱 |
    | description | TEXT | 任務描述 |
    | task_type | VARCHAR | 任務類型（如日常、隨機、特殊） |
    | start_time | DATETIME | 任務開始時間 |
    | end_time | DATETIME | 任務結束時間 |
    | is_completed | BOOLEAN | 任務是否完成 |
    
    ---
    
    ### **3. 任務日程表 (`npc_task_schedule`)**
    
    這個資料表記錄每個 NPC 每天需要執行的任務安排，類似日程表。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | npc_id | INT | NPC ID（指向 `npc` 資料表） |
    | task_id | INT | 任務 ID（指向 `tasks` 資料表） |
    | date | DATE | 執行的日期 |
    | time_slot | VARCHAR | 任務執行時間段（如：早上、中午、晚上） |
    
    ---
    
    ### **4. 地圖資料表 (`map`)**
    
    這個資料表記錄遊戲中的 2D 地圖資訊，每個位置對應不同的物件。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | position_id | INT | 位置唯一識別 ID |
    | x_coordinate | INT | X 座標 |
    | y_coordinate | INT | Y 座標 |
    | object_type | VARCHAR | 物件類型（牆壁、商店、飲料店等） |
    | object_name | VARCHAR | 物件名稱（如牆、超市、飲料店等） |
    
    ---
    
    ### **5. NPC 路徑資料表 (`npc_path`)**
    
    這個資料表記錄 NPC 移動的路徑，讓 NPC 能夠根據路徑規劃自動移動。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | path_id | INT | 路徑唯一識別 ID |
    | npc_id | INT | NPC ID（指向 `npc` 資料表） |
    | start_position | INT | 起始位置（對應 `map` 資料表中的位置 ID） |
    | end_position | INT | 終點位置（對應 `map` 資料表中的位置 ID） |
    | status | VARCHAR | 路徑狀態（如：未完成、完成） |
    
    ---
    
    ### **6. NPC 與物件互動記錄資料表 (`npc_interaction`)**
    
    這個資料表記錄 NPC 與物體的互動，例如與商店互動、與飲料機互動等。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | interaction_id | INT | 互動記錄唯一識別 ID |
    | npc_id | INT | NPC ID（指向 `npc` 資料表） |
    | object_id | INT | 物件 ID（指向 `map` 資料表） |
    | action | VARCHAR | 互動行為（如：購物、吃東西等） |
    | timestamp | DATETIME | 互動時間 |
    
    ---
    
    ### **7. 玩家指令資料表 (`player_commands`)**
    
    如果你有人工聊天系統，這個資料表可以記錄玩家的指令並對應到 NPC 行為。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | command_id | INT | 指令唯一識別 ID |
    | player_id | INT | 玩家 ID（如果有玩家資料表） |
    | command_text | TEXT | 玩家輸入的指令 |
    | npc_id | INT | 被指定的 NPC ID（可選） |
    | command_time | DATETIME | 指令執行時間 |
    | status | VARCHAR | 指令狀態（如：待執行、已執行） |
    
    ---
    
    ### **8. 任務完成記錄資料表 (`task_completion`)**
    
    這個資料表記錄 NPC 完成的任務和狀態。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | completion_id | INT | 任務完成唯一識別 ID |
    | npc_id | INT | NPC ID（指向 `npc` 資料表） |
    | task_id | INT | 任務 ID（指向 `tasks` 資料表） |
    | completion_time | DATETIME | 任務完成時間 |
    | status | VARCHAR | 任務狀態（如：完成、未完成） |
    
    ---
    
    ### **9. NPC 等級與經驗資料表 (`npc_experience`)**
    
    這個資料表記錄 NPC 的經驗值和等級，用來控制 NPC 成長。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | npc_id | INT | NPC ID（指向 `npc` 資料表） |
    | experience | INT | NPC 經驗值 |
    | level | INT | NPC 等級 |
    | last_level_up | DATETIME | 上次升級時間 |
    
    ---
    
    ### **10. 日誌資料表 (`logs`)**
    
    記錄遊戲中發生的重要事件或錯誤日誌。
    
    | 欄位名稱 | 資料型態 | 說明 |
    | --- | --- | --- |
    | log_id | INT | 日誌唯一識別 ID |
    | log_type | VARCHAR | 日誌類型（如：錯誤、警告、訊息） |
    | log_message | TEXT | 日誌訊息 |
    | timestamp | DATETIME | 日誌時間 |

```bash
python manage.py runserver                     # 啟動server
python manage.py runserver --noreload
pipreqs --force --encoding=utf-8               # 複寫套件資源版本
pip install -r requirements.txt                # 安裝對應版本套件
daphne AI_NPC_Backend.asgi:application -p 8080 # daphne server 8080
python manage.py test api                      # 執行測試腳本
python manage.py migrate   
```