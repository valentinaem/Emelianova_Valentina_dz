#  Не используя библиотеки для парсинга, распарсить файл логов web-сервера nginx_logs.txt
# — получить список кортежей вида: (<remote_addr>, <request_type>, <requested_resource>). ('141.138.90.60', 'GET', '/downloads/product_2')
#  Найти IP адрес спамера и количество отправленных им запросов по данным файла логов из предыдущего задания.
# Примечания: спамер — это клиент, отправивший больше всех запросов; код должен работать даже с файлами,
# размер которых превышает объем ОЗУ компьютера.
f = open('nginx_logs.txt', 'r', encoding='utf-8')
all_text = f.read()
all_text = all_text.replace('"', '')
lines = all_text.splitlines()
all_logs = []
for i in lines:
    log = i.split(' ')
    remote_addr = log[0]
    request_type = log[5]
    requested_resource = log[6]
    log = (remote_addr, request_type, requested_resource)
    all_logs.append(log)
print(all_logs)
log_statistic = {}
for i in all_logs:
    count = all_logs.count(i)
    log_statistic[i] = count
max_count = max(log_statistic.values())
max_count = {key:valye for key, valye in log_statistic.items() if valye == max_count}
print(f'IP адрес спамера: {max_count}')