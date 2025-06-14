import subprocess
import time
import os

def run_adb(cmd):
    try:
        result = subprocess.run(['adb'] + cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        return result.stdout.strip()
    except Exception as e:
        return str(e)

def wait_for_device():
    print("[*] Aguardando dispositivo via USB...")
    while True:
        devices = run_adb(['devices']).splitlines()
        connected = [line.split()[0] for line in devices[1:] if 'device' in line]
        if connected:
            print(f"[+] Dispositivo conectado: {connected[0]}")
            return connected[0]
        time.sleep(2)

def get_device_info():
    print("\n[INFO] Coletando informações do dispositivo...")
    return {
        "Modelo": run_adb(["shell", "getprop", "ro.product.model"]),
        "Fabricante": run_adb(["shell", "getprop", "ro.product.manufacturer"]),
        "Versão Android": run_adb(["shell", "getprop", "ro.build.version.release"]),
        "Serial": run_adb(["get-serialno"])
    }

def list_sms():
    print("\n[SMS] Listando SMS recebidos...")
    return run_adb(["shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "address,body,date"])

def list_calls():
    print("\n[CALLS] Listando chamadas...")
    return run_adb(["shell", "content", "query", "--uri", "content://call_log/calls", "--projection", "number,type,date,duration"])

def list_contacts():
    print("\n[CONTACTS] Listando contatos...")
    return run_adb(["shell", "content", "query", "--uri", "content://contacts/phones/", "--projection", "display_name,number"])

def list_apps():
    print("\n[APPS] Listando apps instalados...")
    return run_adb(["shell", "pm", "list", "packages", "-f"])

def export_to_file(name, content):
    with open(name, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"[+] Dados exportados para {name}")

def shell_loop():
    while True:
        cmd = input("\nshell> ").strip()
        if cmd == "exit":
            break
        elif cmd == "info":
            info = get_device_info()
            for k, v in info.items():
                print(f"{k}: {v}")
        elif cmd == "get_sms":
            sms = list_sms()
            print(sms)
        elif cmd == "get_calls":
            calls = list_calls()
            print(calls)
        elif cmd == "get_contacts":
            contacts = list_contacts()
            print(contacts)
        elif cmd == "get_apps":
            apps = list_apps()
            print(apps)
        elif cmd.startswith("export "):
            parts = cmd.split()
            if len(parts) == 2:
                if parts[1] == "sms":
                    export_to_file("sms.txt", list_sms())
                elif parts[1] == "calls":
                    export_to_file("calls.txt", list_calls())
                elif parts[1] == "contacts":
                    export_to_file("contacts.txt", list_contacts())
                elif parts[1] == "apps":
                    export_to_file("apps.txt", list_apps())
                else:
                    print("Tipo de dado desconhecido para exportação.")
            else:
                print("Uso: export sms|calls|contacts|apps")
        elif cmd.startswith("adb "):
            adb_out = run_adb(cmd.split()[1:])
            print(adb_out)
        else:
            print("Comando não reconhecido. Use 'info', 'get_sms', 'get_calls', 'get_contacts', 'get_apps', 'export <tipo>', 'adb <comando>', ou 'exit'.")

if __name__ == "__main__":
    os.system("clear")
    wait_for_device()
    device_info = get_device_info()
    print("\n[+] Informações do dispositivo:")
    for key, value in device_info.items():
        print(f"{key}: {value}")
    shell_loop()
