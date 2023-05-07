# ATT&CK Database

## Overview
MITRE ATT&CK v11のTactics、Techniques並びに、Atomic Red Teamの攻撃コマンドを集約したMaria DBで構築されていたデータベースです。

## Requirements
- Docker 20.10.22

## Usage in Local (Linux, Mac 0S)

### .env.sampleから.envを作成
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

## Usage in Local（Windows）
### .env.sampleから.envを作成
```
copy .env.sample .env
```

###　起動は上記と同様

## phpMyAdminからデータベースを閲覧
```
localhost:3333
```
にアクセスする。

## Table Description

###　ER図
```mermaid
erDiagram
    tactics {
        int id
        string external_id
        string name
        text description
    }
    techniques {
        int id
        string external_id
        string name
        text description
        boolean is_subtechnique
    }
    reasons {
        int id
        int tactic_id
        int technique_id
    }
    commands {
        int id
        text command
        int technique_id
    }

    tactics ||--|{ reasons
    techniques ||--|{ reasons
    techniques ||--o{ commands

```