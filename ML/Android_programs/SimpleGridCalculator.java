package com.example.gridcalculator;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    private EditText result;
    String currentInput= "";
    String operator = "";
    double firstNumber =0;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        result = findViewById(R.id.editText);
    }
        public void onButtonClick(View view){

            Button btn =(Button) view;
            String buttontext = btn.getText().toString();

            switch (buttontext){
                case "C" :
                    currentInput = "";
                    operator = "";
                    firstNumber = 0;
                    result.setText("");
                    break;
                case "+":
                case "-":
                case "*":
                case "/":
                    operator = buttontext;
                    firstNumber = Double.parseDouble(currentInput);
                    currentInput="";
                    result.setText("");
                    break;
                case "=":
                    double secondNumber;
                    secondNumber = Double.parseDouble(currentInput);
                    double res =0;
                    switch(operator){
                        case "+":res = firstNumber + secondNumber;
                            break;
                        case "-":res = firstNumber - secondNumber;
                            break;
                        case "*":res = firstNumber * secondNumber;
                            break;
                        case "/":res = firstNumber / secondNumber;
                            break;
                    }
                    result.setText(String.valueOf(res));
                    currentInput = String.valueOf(res);
                    break;
                default:
                    currentInput += buttontext;
                    result.setText(currentInput);

            }
    }
}

// Activity XML File

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity">

    <TextView
        android:id="@+id/textView"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Grid Layout Calculator!"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintHorizontal_bias="0.498"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.096" />

    <EditText
        android:id="@+id/editText"
        android:layout_width="246dp"
        android:layout_height="68dp"
        android:layout_marginTop="119dp"
        android:layout_marginBottom="42dp"
        android:hint="Enter numbers"
        app:layout_constraintBottom_toTopOf="@+id/gridLayout"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <GridLayout
        android:id="@+id/gridLayout"
        android:layout_width="348dp"
        android:layout_height="241dp"
        android:layout_marginBottom="269dp"
        android:columnCount="4"
        android:rowCount="5"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/editText">

        <Button
            android:onClick="onButtonClick"
            android:text="1" />

        <Button
            android:onClick="onButtonClick"
            android:text="2" />

        <Button
            android:onClick="onButtonClick"
            android:text="3" />

        <Button
            android:onClick="onButtonClick"
            android:text="4" />

        <Button
            android:onClick="onButtonClick"
            android:text="5" />

        <Button
            android:onClick="onButtonClick"
            android:text="6" />

        <Button
            android:onClick="onButtonClick"
            android:text="7" />

        <Button
            android:onClick="onButtonClick"
            android:text="8" />

        <Button
            android:onClick="onButtonClick"
            android:text="9" />

        <Button
            android:onClick="onButtonClick"
            android:text="0" />

        <Button
            android:onClick="onButtonClick"
            android:text="C" />

        <Button
            android:onClick="onButtonClick"
            android:text="+" />

        <Button
            android:onClick="onButtonClick"
            android:text="-" />

        <Button
            android:onClick="onButtonClick"
            android:text="*" />

        <Button
            android:onClick="onButtonClick"
            android:text="/" />

        <Button
            android:onClick="onButtonClick"
            android:text="=" />

    </GridLayout>


</androidx.constraintlayout.widget.ConstraintLayout>
