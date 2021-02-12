# 概要  
Dockerコンテナ上でDiscordのbotを起動し、VCで音楽ファイルを再生する  
音楽ファイルの再生にはFFmpegを用いるため、対応フォーマットもそれに準ずる  
appディレクトリはプログラムが稼働するコンテナの/root/optディレクトリとしてマウントされる  

---  
# 必要なもの  
DockerおよびDocker-compose  
Discordのbotとそのアクセストークン  
再生する音楽ファイル(ffmpegが対応しているフォーマット)  


# botに必要な権限  
チャンネルの閲覧  
メッセージ送信  
VCへの参加  
VCでの発言  

# 使う前にやること  
app/audio以下に音楽ファイルの設置  
secret.dummy.pyを複製し、secret.pyにリネーム  
secret.pyのアクセストークンを自分のbotのものに変更  

---  

# 使い方  

## Dockerコンテナ
Dockerfileのあるディレクトリで下記の起動コマンドを実行。  
コンテナ起動時にbotの起動まで行われます。  

起動  
```  
$ docker-compose up -d  
```  
停止  
```  
$ docker-compose stop  
```  

## discord上でのbotへのコマンド  

メッセージを送ったユーザーが参加しているVCにbotを参加させる  
```  
!join-bg  
```  

VCでapp/audio/sample.mp3を再生する  
```  
!play-bg sample.mp3
```  

音楽の停止  
```  
!stop-bg  
```  

botをVCから切断  
```  
!quit-bg  
```  

app/audio以下のファイル一覧表示  
```  
!list-bg  
```  
