# ATT&CK Database Creation Tools

## 初期設定
- .env.sampleから.envを作成する
```
$ cp .env.sample .env
```
- .envに任意の値を入力

## 起動
```
$ docker-compose -f <docker-compose_file> up -d
```

## テーブル作成
```
$ docker-compose -f <docker-compose_file> run operation python3 seeds
```