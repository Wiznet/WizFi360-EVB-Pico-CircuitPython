# How to Test Blink Example



## Step 1: Prepare hardware

1. Connect WizFi360-EVB-Pico to desktop or laptop using 5 pin micro USB cable.



## Step 2: Setup Blink Example

To test the Blink example, minor settings shall be done in code.

1. Setup LED blink interval.

Setup the LED blink interval you want to check.

The default value is set to 0.5 seconds(500 milliseconds).

```cpp
    time.sleep(0.5)
```

2. Save the modified Blink example in 'code.py' in 'CIRCUITPY' drive.



## Step 3: Run

1. If the Blink example works normally on WizFi360-EVB-Pico, You can see the green LED built on WizFi360-EVB-Pico blinking at the blink interval you set.
