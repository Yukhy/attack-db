# ATT&CK Database Creation Tools

## 要件 (検証済み環境)
- Docker 20.10.22
- Docker Compose 2.15.1

## ローカルでの起動 (Linux, Mac 0S)
- .env.sampleから.envを作成する。
```
$ cp .env.sample .env
```
- .envに任意の値を入力する。

### 起動
```
$ docker compose -f docker-compose.local.yaml up -d
```
### テーブル作成
```
$ docker compose -f docker-compose.local.yaml run operation python seed.py
```

### データベースへのアクセス
- localhostの3306番からアクセスする。
```
// ホストからのアクセス (別途MySQLクライアントのインストールが必要)
$ mysql -h localhost -P 3306 --protocol=tcp -u <username> -p
// mariadbコンテナからのアクセス
$ docker compose -f docker-compose.local.yaml exec -it mariadb bash

$ mysql -u <username> -p
```

## ローカルでの起動（Windows）
- .env.sampleから.envを作成する。
```
copy .env.sample .env
```
- .envに任意の値を入力する。
起動はおそらくLinux等々と同じ。

## phpMyAdminからデータベースを閲覧
```
localhost:3333
```
にアクセスする。
