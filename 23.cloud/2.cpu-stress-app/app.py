from flask import Flask, request
import subprocess
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    usage = """
    <h2>Stress-ng Test API</h2>
    <p>이 API는 CPU 부하 테스트와 상태 확인을 제공합니다.</p>
    <ul>
        <li><b>/load</b> - CPU 부하 발생<br>
            예: <code>/load?cpu=2&time=60&load=80</code><br>
            - <b>cpu</b>: 사용할 CPU 개수 (기본값=2)<br>
            - <b>time</b>: 실행 시간(초) (기본값=60)<br>
            - <b>load</b>: CPU 부하율 % (기본값=80)
        </li>
        <li><b>/status</b> - 현재 CPU/메모리/디스크 상태 확인</li>
    </ul>
    """
    return usage

@app.route("/load")
def load():
    cpu = request.args.get("cpu", default=2, type=int)
    duration = request.args.get("time", default=60, type=int)
    load = request.args.get("load", default=80, type=int)

    subprocess.Popen([
        "stress-ng",
        "--cpu", str(cpu),
        "--cpu-load", str(load),
        "--timeout", str(duration)
    ])

    return f"Started stress-ng with {cpu} CPU(s), load {load}% for {duration} seconds."

@app.route("/status")
def status():
    cpu_percent = psutil.cpu_percent(interval=1)
    mem = psutil.virtual_memory()
    disk = psutil.disk_usage("/")

    status_info = {
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
    }
    return status_info

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
