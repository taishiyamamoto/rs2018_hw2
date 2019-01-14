# ロボットシステム学課題概要

# 課題２について

## やったこと
* WiringPi-Pythonを使ってLEDをpwmで光らせるノードを作成しました。

* 動画のURL：

## 動作確認
```
$cd catkin_ws && catkin_make /*パッケージのビルドが必要*/
$roslaunch assignment2 led_pwm.launch led_pwm_value:=255 /*0から255の範囲で値を代入することができる。defaultは0*/
$rosparam set /led_pwm_pub/led_value 0 /*launch起動中に値を更新する場合*/
```

## 今後の課題
* このプログラムでは使用するGPIOピンを外部から変更できない。主にgpioピンにアクセスするにはroot権限が必要であるため。 
（このプログラムではGPIO25を使用）
* roslaunchおよびrosparamで数値以外のものを送るとパブリッシャーのノードが死んでしまう。
