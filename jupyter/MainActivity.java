package com.zjgsu.cxxu.memowithmindmap;

import android.content.res.Resources;
import android.os.Bundle;
import android.text.Editable;
import android.text.TextWatcher;
import android.view.View;
import android.widget.*;
import androidx.appcompat.app.AppCompatActivity;

/**
 * MainActivity.java
 in the view,you still need to write the logic code,further more,to cooperate with the Presenter,you need do things with presenter,as following:
 * Firstly, This activity implements the MainActivityPresenter.View Interface through which it’s overridden method will be called.
 * Secondly, we have to create the MainActivityPresenter object with view as a constructor.
 * We use this presenter object to listen the user input and update the data as well as view .
 */
public class MainActivity extends AppCompatActivity implements MainActivityPresenter.View {
    /*list the member of the Activity(view)*/
    private MainActivityPresenter presenter;
    private TextView myTextView;
    private ProgressBar progressBar;

    /* implement the methods definded in the Presenter.View inner interface */
    @Override
    public void updateUserInfoTextView(String info) {
        myTextView.setText(info);
    }

    @Override
    public void showProgressBar() {
        progressBar.setVisibility(View.VISIBLE);
    }

    @Override
    public void hideProgressBar() {
        progressBar.setVisibility(View.INVISIBLE);
    }

    /* create the instance of the Presenter object (often in the overridden onCreate() method)*/
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        Toolbar toolbar = findViewById(R.id.toolbar);
        setSupportActionBar(toolbar);
        /* instantiate the Presenter object in the onCreate() method:
        often,we pass this to the Preseter constructor: */
        presenter = new MainActivityPresenter(this);
        /* the presenter no need to deal the view binding work */
        myTextView = findViewById(R.id.myTextView);
        EditText userName = findViewById(R.id.username);
        EditText email = findViewById(R.id.email);
        initProgressBar();

        userName.addTextChangedListener(
                new TextWatcher() {
                    @Override
                    public void beforeTextChanged(CharSequence s, int start, int count, int after) {

                    }

                    @Override
                    public void onTextChanged(CharSequence s, int start, int before, int count) {
                      /* use the presenter instance to listen the  user input and update the data as well as view 
                        you'd know that ,this method want to modify the model's data,the it's time to call
                        presenter to delegate the task with method api the Presenter defined and implemented by us just before in the Activity(View) class */
                        presenter.updateFullName(s.toString());
                    }

                    @Override
                    public void afterTextChanged(Editable s) {
                      /* as for methods like this ,you no need to call presenter to deal with it
                      becasue the operation/behaviour will not trigger the change of the model(instance,the is the user instance) */
                        hideProgressBar();
                    }
                }
        );
      /* the similar listener case with the addTextChangedListener of userName local instance variable  */
        email.addTextChangedListener(new TextWatcher() {
            @Override
            public void beforeTextChanged(CharSequence s, int start, int count, int after) {
            }

            @Override
            public void onTextChanged(CharSequence s, int start, int before, int count) {
                presenter.updateEmail(s.toString());
            }

            @Override
            public void afterTextChanged(Editable s) {
                hideProgressBar();
            }
        });

    }
    /* just for the widget ProgressBar */
    private void initProgressBar() {
        progressBar = new ProgressBar(this, null, android.R.attr.progressBarStyleSmall);
        progressBar.setIndeterminate(true);
        RelativeLayout.LayoutParams params = new RelativeLayout.LayoutParams(
                Resources.getSystem().getDisplayMetrics().widthPixels,
                250
        );
        params.addRule(RelativeLayout.CENTER_IN_PARENT);
        this.addContentView(progressBar, params);
        showProgressBar();
    }
}
