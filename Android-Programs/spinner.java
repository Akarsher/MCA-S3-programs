package com.example.spinner;

import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity extends AppCompatActivity {

    EditText name,age,number;
    Button btn;
    Spinner spin;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main);

        name = findViewById(R.id.name);
        age = findViewById(R.id.age);
        number = findViewById(R.id.mobile);

        btn = findViewById(R.id.button);
        spin = findViewById(R.id.spinner);

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {

                String uname = name.getText().toString();
                String uage = age.getText().toString();
                String mobile = number.getText().toString();
                String course = spin.getSelectedItem().toString();

                if(uname.isEmpty()){
                    name.setError("enter name.");
                    return;
                }
                if(uage.isEmpty()){
                    age.setError("enter age.");
                    return;
                }
                if(mobile.length()<10){
                    number.setError("enter valid mobile number.");
                    return;
                }
                Intent intent = new Intent(MainActivity.this,MainActivity2.class);
                intent.putExtra("name",uname);
                intent.putExtra("age",uage);
                intent.putExtra("number",mobile);
                intent.putExtra("course",course);

                startActivity(intent);
            }
        });
    }
}

//Main activity.xml

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
        android:text="Registration Form"
        android:textStyle="bold"
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintVertical_bias="0.092" />

    <EditText
        android:id="@+id/name"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="27dp"
        android:layout_marginTop="53dp"
        android:hint="Name "
        app:layout_constraintBottom_toTopOf="@+id/age"
        app:layout_constraintStart_toStartOf="@+id/textView"
        app:layout_constraintTop_toBottomOf="@+id/textView" />

    <EditText
        android:id="@+id/age"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginEnd="8dp"
        android:layout_marginBottom="32dp"
        android:hint="Age "
        app:layout_constraintBottom_toTopOf="@+id/mobile"
        app:layout_constraintEnd_toEndOf="@+id/name" />

    <EditText
        android:id="@+id/mobile"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:hint="Mobile no. "
        app:layout_constraintBottom_toBottomOf="parent"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Spinner
        android:id="@+id/spinner"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="45dp"
        android:entries="@array/courses"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/mobile" />

    <Button
        android:id="@+id/button"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginTop="64dp"
        android:text="Register"
        app:layout_constraintEnd_toEndOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toBottomOf="@+id/spinner"
        tools:ignore="UnknownId" />

</androidx.constraintlayout.widget.ConstraintLayout>

// Resource file : array.xml

  <?xml version="1.0" encoding="utf-8"?>
<resources>
    <string-array name="courses">
        <item>MCA</item>
        <item>B-tech</item>
        <item>M-tech</item>
        <item>Diploma</item>
    </string-array>
</resources>

// second activity.java

  package com.example.spinner;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.TextView;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class MainActivity2 extends AppCompatActivity {
    TextView result;
    Button btn;

    @SuppressLint("MissingInflatedId")
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_main2);

        result = findViewById(R.id.result_tab);
        btn = findViewById(R.id.button2);

        String name = getIntent().getStringExtra("name");
        String age = getIntent().getStringExtra("age");
        String mobile = getIntent().getStringExtra("number");
        String course = getIntent().getStringExtra("course");

        result.setText("Student Details:\n"+
                "\nName :"+name+
                "\nAge :"+age+
                "\nMobile no :"+mobile+
                "\nCourse Selected :"+course);
        Toast.makeText(this,"Congratulations \n you are now a "+course+" Student", Toast.LENGTH_SHORT).show();

        btn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = new Intent(MainActivity2.this,MainActivity.class);
                startActivity(intent);

            }
        });

    }
}

// second activity.xml

<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    xmlns:tools="http://schemas.android.com/tools"
    android:id="@+id/main"
    android:layout_width="match_parent"
    android:layout_height="match_parent"
    tools:context=".MainActivity2">

    <TextView
        android:id="@+id/result_tab"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:layout_marginStart="155dp"
        android:layout_marginTop="108dp"
        android:text="TextView"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintTop_toTopOf="parent" />

    <Button
        android:id="@+id/button2"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="Go back"
        tools:layout_editor_absoluteX="160dp"
        tools:layout_editor_absoluteY="331dp"
        tools:ignore="MissingConstraints" />
</androidx.constraintlayout.widget.ConstraintLayout>
