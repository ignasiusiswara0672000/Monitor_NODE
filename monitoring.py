# Source code by Alif Almuqsit
# Keep exploring
# Trial and Error, but Be Carefull

def monitoring():
  import psutil
  from time import sleep
  
  cpu = psutil.cpu_percent()
  memory = psutil.viritual_memory().percent
  
  rx = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_sent
  tx = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_recv
  sleep(1)
  rx_new = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_sent
  tx_new = psutil.net_io_counters(pernic=True)['enp0s3'].bytes_recv
  rx = operasi(rx, rx_new)
  tx = operasi(tx, tx_new)
 
  print('''
              SISTEM MONITORING COMPUTER
                    CPU   : {}%
                    Memori: {}%
                    tx/rx : {} Kbps/{} Kbps

          Untuk menghentikan program tekan Ctrl+C
  '''.format(cpu, memory, tx, rx))

def operasi(old, new):
  new = new - old
  new = (new * 8) / 1000
  new = new
  return new



try:
  monitor()
except:
  print(" \n \t program ini selesai. :)")