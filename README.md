# ATT&CK Database Creation Tools

## ローカルでの機能


### 起動
```
$ docker-compose -f <docker-compose_file> up -d
```

### テーブル作成
```
$ docker-compose -f <docker-compose_file> run operation python seed.py
```

localhostの3306番からアクセスできます。