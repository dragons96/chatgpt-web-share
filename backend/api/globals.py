from api.conf import Config
from utils.data_types import RequestCounter, TimeQueue
_config = Config().get_config()


reverse_proxy_log_file = None
reverse_proxy_process = None
server_log_filename = None

startup_time = None

request_log_counter = RequestCounter(
    time_window=_config.stats.request_counter_time_window,
    interval=_config.stats.request_counts_interval
)
ask_log_queue = TimeQueue(_config.stats.ask_log_time_window)  # 7 days
