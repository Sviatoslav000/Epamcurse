import psutil
import argparse
import time
import json

class System_info:

    def get_info(self):

        u=psutil.cpu_times()
        cpu={"user": u.user, "system": u.system, "idle": u.idle}

        total=len(psutil.pids())
        running, sleeping, stopped, zombie= 0, 0, 0, 0
        for p in psutil.process_iter(['status']):
            if p.info['status'] == psutil.STATUS_SLEEPING:
                sleeping+=1
            elif p.info['status'] == psutil.STATUS_RUNNING:
                running+=1
            elif p.info['status'] == psutil.STATUS_STOPPED:
                stopped+=1
            elif p.info['status'] == psutil.STATUS_ZOMBIE:
                zombie+=1
        tasks={"total": total, "running": running, "sleeping": sleeping, "stopped": stopped, "zombie": zombie}

        km=psutil.virtual_memory()
        ks=psutil.swap_memory()
        kib_mem={"total": km.total, "free": km.free, "used": km.used}
        kib_swap={"total": ks.total, "free": ks.free, "used": ks.used}

        result={"Tasks": tasks,
        "%CPU": cpu,
        "KiB Mem": kib_mem,
        "KiB Swap": kib_swap,
        "Timestamp": int(psutil.boot_time())}

        return result

    def system_info(self):

        parser = argparse.ArgumentParser()
        parser.add_argument("-i", help="Interval between snapshots in seconds", type=int, default=30)
        parser.add_argument("-f", help="Output file name", default="snapshot.json")
        parser.add_argument("-n", help="Quantity of snapshot to output", default=20)

        args = parser.parse_args()

        with open(args.f, "w") as file:
            p="p"

        for i in range (args.n):
            res = self.get_info()
            with open(args.f, "a") as file:
                json.dump(res, file)
            print(res)
            time.sleep(args.i)

def main():
    info = System_info()
    info.system_info()

if __name__=="__main__":
    main()


