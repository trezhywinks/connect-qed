## Instale o ADB:
 ```ts
sudo apt install adb
```
## Connect-qed:
```
$ git clone https://github.com/trezhywinks/connect-qed.git
$ cd connect-qed
$ bash ins.sh
$ qed -s --start or $ python3 qed.py
```

## 🧠 Observações técnicas: 

- Para ler SMS, chamadas, contatos, o comando ADB usa o ```content provider```:
```ts
adb shell content query --uri content://sms/inbox
adb shell content query --uri content://call_log/calls
adb shell content query --uri content://contacts/phones/
```

- Pode haver limitações de acesso dependendo da versão do Android e permissões do sistema.
## 🧪 Comandos disponíveis:

``info``	Mostra info do aparelho

``get_sms``	Lista SMS recebidos

``get_calls``	Lista histórico de chamadas

``get_contacts``	Lista contatos

``get_apps``	Lista apps instalados

``export sms``	Salva SMS em ```sms.txt```

``export calls``	Salva chamadas em ```calls.txt```

``export contacts``	Salva contatos em ```contacts.txt```

``export apps``	Salva apps em ```apps.txt```

``adb <comando>``	Executa qualquer comando ADB manual

``exit``	Sai do shell
