import time

class Inviter(DiscordTower):
    # ... (весь предыдущий код)

    def get_voice_timings(self):
        try:
            with open('voice_timings.txt', 'r') as file:
                lines = file.readlines()
                voice_timings = {}
                for line in lines:
                    channel_id, timings = line.strip().split('?')
                    enter_time, exit_time = timings.split(':')
                    voice_timings[channel_id] = {'enter': enter_time, 'exit': exit_time}
                return voice_timings
        except Exception as err:
            logger.error(f"{self.account_index} | Error reading voice timings: {err}")
            return {}

    def manage_voice_channels(self):
        voice_timings = self.get_voice_timings()

        for channel_id, timings in voice_timings.items():
            current_time = time.strftime('%H:%M', time.localtime())
            if current_time == timings['enter']:
                # Подключение к голосовому каналу
                self.join_voice_channel(channel_id)
            elif current_time == timings['exit']:
                # Выход из голосового канала
                self.leave_voice_channel(channel_id)
