import json
from channels.generic.websocket import AsyncWebsocketConsumer

class CharacterMoveConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # 這裡可以進行身份驗證等操作
        self.room_name = 'character_move'
        self.room_group_name = f'game_{self.room_name}'

        # 加入房間組
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # 離開房間組
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # 從後端發送消息給 WebSocket 客戶端
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        action = text_data_json['action']
        position = text_data_json['position']

        # 發送到前端
        await self.send(text_data=json.dumps({
            'action': action,
            'position': position
        }))
