package jarkko.courseclod.com.myapplication;

import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;

public class MainActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
    }

    public void shutdown(View v){
        Client mycli = new Client("shutdown");
        mycli.execute();
    }

    public void restart(View v){
        Client mycli2 = new Client("restart");
        mycli2.execute();
    }

    public void music(View v){
        Client mycli3 = new Client("music");
        mycli3.execute();
    }
}
