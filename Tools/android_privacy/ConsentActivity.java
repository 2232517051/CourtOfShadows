package org.renpy.android;

import android.app.Activity;
import android.content.Intent;
import android.content.SharedPreferences;
import android.graphics.Color;
import android.os.Bundle;
import android.text.method.LinkMovementMethod;
import android.view.Gravity;
import android.view.View;
import android.widget.Button;
import android.widget.LinearLayout;
import android.widget.ScrollView;
import android.widget.TextView;

public final class ConsentActivity extends Activity {
    private static final String PREFS_NAME = "privacy_consent";
    private static final String AGREED_KEY = "agreed_v1";
    private static final int GOLD = Color.rgb(212, 169, 66);
    private static final int BODY = Color.rgb(210, 202, 188);

    @Override
    protected void onCreate(Bundle state) {
        super.onCreate(state);

        SharedPreferences preferences = getSharedPreferences(PREFS_NAME, MODE_PRIVATE);
        if (preferences.getBoolean(AGREED_KEY, false)) {
            launchGame();
            return;
        }

        showConsent(preferences);
    }

    private TextView text(String value, float size, int color) {
        TextView view = new TextView(this);
        view.setText(value);
        view.setTextSize(size);
        view.setTextColor(color);
        view.setLineSpacing(0.0f, 1.25f);
        view.setPadding(0, 8, 0, 8);
        view.setMovementMethod(LinkMovementMethod.getInstance());
        return view;
    }

    private void showConsent(SharedPreferences preferences) {
        LinearLayout root = new LinearLayout(this);
        root.setOrientation(LinearLayout.VERTICAL);
        root.setPadding(48, 28, 48, 28);
        root.setBackgroundColor(Color.rgb(10, 9, 18));

        TextView title = text("用户协议与隐私政策", 25, GOLD);
        title.setGravity(Gravity.CENTER);
        root.addView(title, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT,
                LinearLayout.LayoutParams.WRAP_CONTENT));

        TextView policy = text(
                "欢迎使用《权谋之庭》。请在启动游戏前阅读以下内容：\n\n"
                + "1. 个人信息\n"
                + "本游戏为纯单机游戏，不收集、上传或分享您的个人信息。游戏存档和设置仅保存在本地。\n\n"
                + "2. 设备传感器\n"
                + "您同意后，游戏引擎 SDL 才会初始化，并可能读取设备支持的传感器类型列表，用于输入设备识别和屏幕显示适配。游戏不记录、存储或上传传感器数据。\n\n"
                + "3. 第三方组件\n"
                + "本游戏仅使用 Ren'Py、SDL 和视频播放等引擎组件，未集成广告、统计、推送或社交 SDK。\n\n"
                + "4. 本地存储\n"
                + "游戏仅在应用自身目录保存进度和设置，不申请通讯录、定位、相机、麦克风或外部存储权限。\n\n"
                + "5. 网络\n"
                + "本游戏不需要互联网连接，不会向服务器发送数据。\n\n"
                + "6. 您的选择\n"
                + "点击“同意并继续”后才会启动游戏引擎；点击“不同意并退出”将直接关闭应用。卸载游戏可删除本地数据。\n\n"
                + "联系邮箱：2232517051@qq.com\n"
                + "版本：3.9.2｜更新日期：2026年8月｜开发者：FFire的工作室",
                15,
                BODY);

        ScrollView scroll = new ScrollView(this);
        scroll.addView(policy);
        root.addView(scroll, new LinearLayout.LayoutParams(
                LinearLayout.LayoutParams.MATCH_PARENT, 0, 1.0f));

        LinearLayout buttons = new LinearLayout(this);
        buttons.setOrientation(LinearLayout.HORIZONTAL);
        buttons.setGravity(Gravity.CENTER);
        buttons.setPadding(0, 18, 0, 0);

        Button decline = new Button(this);
        decline.setText("不同意并退出");
        decline.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                finishAffinity();
            }
        });

        Button agree = new Button(this);
        agree.setText("同意并继续");
        agree.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (preferences.edit().putBoolean(AGREED_KEY, true).commit()) {
                    launchGame();
                }
            }
        });

        LinearLayout.LayoutParams buttonParams = new LinearLayout.LayoutParams(0, 56, 1.0f);
        buttonParams.setMargins(8, 0, 8, 0);
        buttons.addView(decline, buttonParams);
        buttons.addView(agree, buttonParams);
        root.addView(buttons);

        setContentView(root);
    }

    private void launchGame() {
        Intent intent = new Intent(this, PythonSDLActivity.class);
        intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK | Intent.FLAG_ACTIVITY_CLEAR_TASK);
        startActivity(intent);
        finish();
    }
}
