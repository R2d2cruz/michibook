import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import AnonymousUser

from .models import Maullido, MaullidoReaction

class MaullidoConsumer(AsyncWebsocketConsumer):
    group_name = "maullidos"

    async def connect(self):
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        try:
            data = json.loads(text_data)
        except Exception:
            return 

        maullido_id = data.get("maullido_id")
        action = data.get("action")
        user = self.scope.get("user")

        if not user or isinstance(user, AnonymousUser) or user.is_anonymous:
            await self.send(json.dumps({"error": "authentication required"}))
            return

        valid_choices = dict(MaullidoReaction.REACTION_CHOICES)
        if action not in valid_choices:
            await self.send(json.dumps({"error": "invalid action"}))
            return

        reactions = await sync_to_async(self._processReaction)(user, maullido_id, action)

        await self.channel_layer.group_send(
            self.group_name,
            {
                "type": "sendReactionUpdate",
                "maullido_id": maullido_id,
                "reactions": reactions,
            }
        )

    def _processReaction(self, user, maullido_id, action):
        maullido = Maullido.objects.get(pk=maullido_id)

        reaction, created = MaullidoReaction.objects.get_or_create(
            user=user,
            maullido=maullido,
            defaults={"reaction": action}
        )

        if not created:
            if reaction.reaction == action:
                reaction.delete()
            else:
                reaction.reaction = action
                reaction.save()

        return {
            "happys": maullido.happys_count,
            "sads": maullido.sads_count,
            "loves": maullido.loves_count,
            "shockeds": maullido.shockeds_count,
            "angrys": maullido.angrys_count,
        }

    async def sendReactionUpdate(self, event):
        await self.send(text_data=json.dumps({
            "maullido_id": event["maullido_id"],
            "reactions": event["reactions"],
        }))
