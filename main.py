import threading
import DashboardServer
import MoveCursor

p1 = threading.Thread(target=DashboardServer.run_server)
p2 = threading.Thread(target=MoveCursor.run_hand_recognition)
p1.start()
p2.start()
