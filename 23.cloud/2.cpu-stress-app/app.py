from flask import Flask, request, render_template, jsonify
import subprocess
import psutil
import time
import threading

app = Flask(__name__)

# 전역 상태 관리
current_task = {
    "running": False,
    "start_time": None,
    "duration": None,
    "cpu": None,
    "load": None
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/load")
def load():
    global current_task
    cpu = request.args.get("cpu", default=2, type=int)
    duration = request.args.get("time", default=60, type=int)
    load = request.args.get("load", default=80, type=int)

    if current_task["running"]:
        # 이미 실행 중 → 현재 진행 상태 반환
        elapsed = int(time.time() - current_task["start_time"])
        remaining = max(0, current_task["duration"] - elapsed)
        return render_template(
            "running.html",
            cpu=current_task["cpu"],
            load=current_task["load"],
            start_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_task["start_time"])),
            duration=current_task["duration"],
            remaining=remaining
        )

    # 새로운 작업 시작
    current_task.update({
        "running": True,
        "start_time": time.time(),
        "duration": duration,
        "cpu": cpu,
        "load": load
    })

    def run_stress():
        subprocess.run([
            "stress-ng",
            "--cpu", str(cpu),
            "--cpu-load", str(load),
            "--timeout", str(duration)
        ])
        current_task["running"] = False

    threading.Thread(target=run_stress, daemon=True).start()

    return render_template(
        "running.html",
        cpu=cpu,
        load=load,
        start_time=time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(current_task["start_time"])),
        duration=duration,
        remaining=duration
    )

@app.route("/status")
def status():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    return jsonify({
        "cpu_percent": cpu_percent,
        "memory": {
            "total": mem.total,
            "used": mem.used,
            "percent": mem.percent
        },
        "disk": {
            "total": disk.total,
            "used": disk.used,
            "percent": disk.percent
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
